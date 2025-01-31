import yaml

from src.consts import CONFIG_DIR
from src.data.project_info import ProjectInfo


def load_config_data(env):
    config_file_path = CONFIG_DIR / f"{env}.yaml"
    with open(config_file_path, "r") as file:
        config_data = yaml.safe_load(file)

        for k, v in config_data.items():
            setattr(ProjectInfo, k, v)

    return config_data
