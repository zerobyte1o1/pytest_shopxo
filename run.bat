
pytest test_case --clean-alluredir --alluredir=./report/allure_raw

::allure generate ./report/allure_raw -o ./report --clean

allure serve report/allure_raw