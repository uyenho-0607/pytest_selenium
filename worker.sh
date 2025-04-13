#!/bin/bash

#pytest tests/web/login/test_login.py --browser=firefox & pytest tests/web/login/test_login.py --browser=chrome
pytest tests/test_init_driver.py --platform=ios --alluredir=a & pytest tests/test_init_driver.py --platform=mac --alluredir=b
