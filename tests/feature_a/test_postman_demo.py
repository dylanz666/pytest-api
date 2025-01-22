import pytest
import allure
from constants.severity import Severity
from entity.user import User
from tools.config_util import ConfigUtil
from tools.http_client import HttpClient


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
    @allure.title("Postman: demo get")
    @allure.description("Postman: demo get")
    @allure.testcase("https://www.baidu.com")
    # @pytest.mark.skip
    def test_get(self):
        res = self.http_client.get("/get", params={"id": 1}, headers={"JSESSIONID": "abcd123"})
        assert (res.status_code == 200)

    @pytest.mark.P1
    @allure.severity(Severity.CRITICAL.value)
    @allure.title("Postman: demo post")
    @allure.description("Postman: demo post")
    @allure.testcase("https://www.baidu.com")
    # @pytest.mark.skip
    def test_post(self):
        request_body: User = User(id=1234, first_name="dylan", last_name="zzz")
        res = self.http_client.post("/post", params={"id": 1}, headers={"JSESSIONID": "abcd123"}, data="abcd",
                                    json=request_body.to_dict())
        assert (res.status_code == 200)

    @pytest.mark.P2
    @allure.severity(Severity.NORMAL.value)
    @allure.title("Postman: demo put")
    @allure.description("Postman: demo put")
    @allure.testcase("https://www.baidu.com")
    # @pytest.mark.skip
    def test_put(self):
        request_body: User = User(id=1234, first_name="dylan", last_name="zzz")
        res = self.http_client.put("/put", params={"id": 1}, headers={"JSESSIONID": "abcd123"}, data="abcd",
                                   json=request_body.to_dict())
        assert (res.status_code == 200)

    @pytest.mark.P3
    @allure.severity(Severity.MINOR.value)
    @allure.title("Postman: demo patch")
    @allure.description("Postman: demo patch")
    @allure.testcase("https://www.baidu.com")
    # @pytest.mark.skip
    def test_patch(self):
        request_body: User = User(id=1234, first_name="dylan", last_name="zzz")
        res = self.http_client.patch("/patch", params={"id": 1}, headers={"JSESSIONID": "abcd123"}, data="abcd",
                                     json=request_body.to_dict())
        assert (res.status_code == 200)

    @pytest.mark.sanity
    @allure.severity(Severity.TRIVIAL.value)
    @allure.title("Postman: demo delete")
    @allure.description("Postman: demo delete")
    @allure.testcase("https://www.baidu.com")
    # @pytest.mark.skip
    def test_delete(self):
        request_body: User = User(id=1234, first_name="dylan", last_name="zzz")
        res = self.http_client.delete("/delete", params={"id": 1}, headers={"JSESSIONID": "abcd123"}, data="abcd",
                                      json=request_body.to_dict())
        assert (res.status_code == 200)
