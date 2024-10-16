#Python API Automation Frameworks
#Create a Fresh Project at Pycharm
Tech stack
-Python 3.12
-Request -HTTP Requests
-Pytest - Testing Framework
-Reporting - Allure Report, PyTest HTML reports
-Test Data -CSV, EXCEL, JSON, Faker
-Advance API Testcase - Jsonschema
-Parallel execution - x distribute (xdist)

#How to install the below mentioned packages?

pip install requests pytest pytest-html faker allure-pytest jsonschema python-dotenv pandas

#How to run testcases Parallelly?

pip install pytest-xdist

How to run a basic testcase?

pytest test_first.py --alluredir=allure_result -v -s