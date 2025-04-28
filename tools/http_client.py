import requests

from constants.request_method import RequestMethod
from tools.config_util import ConfigUtil
from tools.custom_allure_step_decorator import custom_allure_step


class HttpClient:
    def __init__(self, base_url=None):
        if base_url:
            self.base_url = base_url
        else:
            self.base_url = ConfigUtil.get_base_url()
        print("\r")

    def get(self, path, params=None, **kwargs):
        @custom_allure_step(method=RequestMethod.GET.value, base_url=self.base_url)
        def do_get(api_path, api_params, **api_kwargs):
            return requests.get(f"{self.base_url}{api_path}", params=api_params, **api_kwargs)

        return do_get(path, params, **kwargs)

    def post(self, path, data=None, json=None, **kwargs):
        @custom_allure_step(method=RequestMethod.POST.value, base_url=self.base_url)
        def do_post(api_path, api_params, api_data, api_json, **api_kwargs):
            if api_json is not None:
                return requests.post(f"{self.base_url}{api_path}", json=api_json, **api_kwargs)
            return requests.post(f"{self.base_url}{api_path}", data=api_data, **api_kwargs)

        return do_post(path, None, data, json, **kwargs)

    def put(self, path: str, data=None, **kwargs):
        @custom_allure_step(method=RequestMethod.PUT.value, base_url=self.base_url)
        def do_put(api_path: str, api_params, api_data, api_json, **api_kwargs):
            json_data = kwargs.get("json")
            if json_data is not None or json_data != {}:
                return requests.put(f"{self.base_url}{api_path}", **api_kwargs)
            return requests.put(f"{self.base_url}{api_path}", data=api_data, **api_kwargs)

        return do_put(path, None, data, None, **kwargs)

    def patch(self, path: str, data=None, **kwargs):
        @custom_allure_step(method=RequestMethod.PATCH.value, base_url=self.base_url)
        def do_patch(api_path: str, api_params, api_data, api_json, **api_kwargs):
            json_data = kwargs.get("json")
            if json_data is not None or json_data != {}:
                return requests.patch(f"{self.base_url}{api_path}", **api_kwargs)
            return requests.patch(f"{self.base_url}{api_path}", data=api_data, **api_kwargs)

        return do_patch(path, None, data, None, **kwargs)

    def delete(self, path: str, **kwargs):
        json_data = kwargs.get("json")
        if json_data is not None or json_data != {}:
            kwargs = {key: value for key, value in kwargs.items() if
                      key not in ['data']}

        @custom_allure_step(method=RequestMethod.DELETE.value, base_url=self.base_url)
        def do_delete(api_path: str, api_params, api_data, api_json, **api_kwargs):
            return requests.delete(f"{self.base_url}{api_path}", **api_kwargs)

        return do_delete(path, None, None, None, **kwargs)


if __name__ == "__main__":
    http_client = HttpClient("https://postman-echo.com")
    res = http_client.get("/get", params={"id": 1}, headers={})
    assert (res.status_code == 200)
