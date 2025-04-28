import functools
import allure

from tools.logger import Logger
import json as json_tool


def custom_allure_step(**kw):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            method = kw["method"]
            base_url = kw["base_url"]
            path = args[0]
            params = args[1]
            data = args[2] if len(args) > 2 else None
            json = args[3] if len(args) > 3 else None
            json = json if json is not None else (kwargs.get("json") if kwargs.get("json") else None)
            headers = kwargs.get("headers")
            arguments = {key: value for key, value in kwargs.items() if
                         key not in ['headers', 'json']}
            if arguments.get("params"):
                params = arguments.get("params")

            url = f"{base_url}{path}"

            if params is not None and params != {}:
                query_string = '&'.join(f"{key}={value}" for key, value in params.items())
                url = f"{url}?{query_string}"
            Logger().info(f"[{method}]", url)

            with allure.step(f"{method} {url}"):
                # headers
                if headers is not None and headers != {}:
                    Logger().info(f"[Headers]", json_tool.dumps(headers, indent=2))
                    allure.attach(json_tool.dumps(headers, indent=2), name="Request Headers",
                                  attachment_type=allure.attachment_type.JSON)
                # send json request body
                if json is not None and json != {}:
                    Logger().info(f"[Json Request Body]", json_tool.dumps(json, indent=2))
                    allure.attach(json_tool.dumps(json, indent=2), name="Json Request Body",
                                  attachment_type=allure.attachment_type.JSON)
                # send text request body
                if (json is None or json == {}) and data is not None and data != "":
                    Logger().info(f"[Text Request Body]", data)
                    allure.attach(data, name="Text Request Body",
                                  attachment_type=allure.attachment_type.TEXT)

                # other arguments
                arguments = {key: value for key, value in arguments.items() if
                             key not in ['params']}
                if arguments is not None and arguments != {}:
                    Logger().info(f"[Arguments]", json_tool.dumps(arguments, indent=2))
                    allure.attach(json_tool.dumps(arguments, indent=2), name="Arguments",
                                  attachment_type=allure.attachment_type.JSON)

                response = func(*args, **kwargs)

                try:
                    # json response body
                    data = response.json()
                    Logger().info(f"[JSON Response Body]", json_tool.dumps(data, indent=2))
                    allure.attach(json_tool.dumps(data, indent=2), name="Response",
                                  attachment_type=allure.attachment_type.JSON)
                except ValueError:
                    # text response body
                    # set right encoding
                    response.encoding = response.apparent_encoding
                    data = response.text
                    Logger().info(f"[Text Response Body]", data)
                    allure.attach(data, name="Response", attachment_type=allure.attachment_type.TEXT)
            return response

        return wrapper

    return decorator


if __name__ == "__main__":
    pass
