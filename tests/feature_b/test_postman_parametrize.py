import pytest
import allure
from constants.severity import Severity
from tools.config_util import ConfigUtil
from tools.http_client import HttpClient
from tools.jsonpath_util import JSONPathUtil


@allure.feature("Feature: Login")
class TestPostmanDemo:
    def setup_class(self):
        self.http_client = HttpClient(base_url=ConfigUtil.get_base_url())

    def teardown_class(self):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    @pytest.mark.P0
    @allure.severity(Severity.BLOCKER.value)
    @allure.title("Postman: demo get, data driven")
    @allure.description("Postman: demo get, data driven")
    @allure.testcase("https://www.baidu.com")
    @pytest.mark.parametrize("request_id, expected_response_id", [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    ])
    # @pytest.mark.skip
    def test_get_parametrize(self, request_id, expected_response_id):
        res = self.http_client.get("/get", params={"id": request_id}, headers={"JSESSIONID": "abcd123"})

        status_code = res.status_code
        assert status_code == 200, f"status code is {status_code}, not 200"

        jsonpath_util = JSONPathUtil(res.json())
        id_in_response = jsonpath_util.get_value("args.id")
        assert id_in_response == str(
            expected_response_id), f"actual id: {id_in_response}, expected id: {expected_response_id}"
