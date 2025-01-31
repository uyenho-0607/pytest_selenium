import json
import os

import allure

from src.consts import ROOTDIR
from src.data.logs import MsgLog
from src.data.project_info import DriverList
from src.utils.logging_util import logger


def capture_screenshot(driver, name="screenshot"):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )


def log_step_to_allure():
    test_steps = []
    _msg_logs = MsgLog.step_logs

    # Find index step in list
    # get description from index
    steps_index = [
        index for index, value in enumerate(_msg_logs)
        if ("step" or "steps" or "Should see") in value.lower()
    ]

    for i in range(len(steps_index)):
        if i == (len(steps_index) - 1):
            test_steps.append(_msg_logs[steps_index[i]:])
            break
        test_steps.append(_msg_logs[steps_index[i]: steps_index[i + 1]])

    # Log test to allure reports
    for steps in test_steps:
        step = steps.pop(0)

        with allure.step(step):
            for verify in steps:
                with allure.step(verify):
                    pass

    del _msg_logs[:]


def custom_allure_report(allure_dir):
    allure_dir = ROOTDIR / allure_dir
    allure_result_files = [f for f in os.listdir(allure_dir) if f.endswith("result.json")]

    # sort result files based on created time
    files = [os.path.join(allure_dir, f) for f in allure_result_files]
    files.sort(key=lambda x: os.path.getmtime(x))

    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

                # failed_attachments = [
                #     item for item in data.get("attachments", []) if item["name"] == "screenshot"
                # ]

                failed_attachments = list(
                    filter(lambda x: x["name"] == "screenshot", data.get("attachments", []))
                )

                # broken_attachments = [
                #     item for item in data.get("attachments", []) if item["name"] == "broken"
                # ]

                # custom failed verify steps
                if data["status"] == "failed":

                    failed_logs = MsgLog.all_failed_logs

                    for item in data["steps"]:
                        for verify_step in item.get("steps", []):
                            for failed_step, msg_detail in MsgLog.all_failed_logs:

                                if verify_step["name"].lower() == failed_step.lower():

                                    verify_step["status"] = "failed"
                                    item["status"] = "failed"
                                    verify_step.update(statusDetails=dict(message=msg_detail))

                                    failed_logs.pop(0)

                                    if failed_attachments:
                                        verify_step["attachments"] = failed_attachments[:len(DriverList.web_driver)]
                                        del failed_attachments[:len(DriverList.web_driver)]

                                    break

                # custom broken step
                if MsgLog.is_broken:
                    data["status"] = "broken"
                    last_step = data["steps"][-1]
                    last_step["status"] = "broken"
                    last_step["attachments"] = list(
                        filter(lambda x: x["name"] == "broken", data.get("attachments", []))
                    )

                data["attachments"] = []
                statusDetails = data.get("statusDetails", {})
                "trace" not in str(data) or statusDetails.pop("trace")

                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=4)  # Write with indentation for readability

        except Exception as e:
            logger.error(f"Error processing file {os.path.basename(file_path)}: {e}")
