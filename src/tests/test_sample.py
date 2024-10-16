import pytest
import allure


@allure.title("A Sample TestCase!")
@pytest.mark.smoke
def test_sample_tc1():
    print("A sample testcase is checking!")
    assert True == True