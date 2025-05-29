import functools
import allure

from tools.logger import Logger
import json as json_tool


def allure_step(func=None, *, step_name=None):
    # common allure step
    if func is None:
        return lambda f: allure_step(f, step_name=step_name)

    log_step_name = step_name if step_name else f"{func.__qualname__}"

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        args_str = f"({', '.join(repr(arg) for arg in args)})" if args else "()"
        step_info = f"{log_step_name}, args: {args_str}"
        if kwargs:
            kwargs_str = ', '.join(f"{key}={repr(value)}" for key, value in kwargs.items())
            step_info += f", kwargs: ({kwargs_str})"

        Logger().info(step_info)

        with allure.step(step_info):
            return func(self, *args, **kwargs)

    return wrapper


def api_allure_step(func=None, **kw):
    # customized allure step for api
    if func is None:
        return lambda f: api_allure_step(f, **kw)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        method = kw["method"]
        base_url = kw["base_url"]
        path, params, data, json = args[0], args[1], args[2] if len(args) > 2 else None, args[3] if len(
            args) > 3 else None
        json = json or kwargs.get("json")
        headers = kwargs.get("headers")
        arguments = {key: value for key, value in kwargs.items() if key not in ['headers', 'json']}
        params = arguments.get("params", params)
        arguments = {key: value for key, value in arguments.items() if key not in ["params"]}

        url = f"{base_url}{path}"
        if params:
            query_string = '&'.join(f"{key}={value}" for key, value in params.items())
            url = f"{url}?{query_string}"

        Logger().info(f"[{method}]", url)

        with allure.step(f"{method} {url}"):
            _log_and_attach("Request Headers", headers)
            _log_and_attach("JSON Request Body", json, is_json=True)
            _log_and_attach("Text Request Body", data, is_text=True)
            _log_and_attach("Arguments", arguments)

            response = func(*args, **kwargs)
            _log_response(response)

        return response

    return wrapper


def _log_and_attach(name, data, is_json=False, is_text=False):
    """Log and attach data to allure."""
    if not data:
        return
    if is_json:
        Logger().info(f"[{name}]", json_tool.dumps(data, indent=2))
        allure.attach(json_tool.dumps(data, indent=2), name=name, attachment_type=allure.attachment_type.JSON)
        return
    if is_text:
        Logger().info(f"[{name}]", data)
        allure.attach(data, name=name, attachment_type=allure.attachment_type.TEXT)
        return
    Logger().info(f"[{name}]", json_tool.dumps(data, indent=2))
    allure.attach(json_tool.dumps(data, indent=2), name=name, attachment_type=allure.attachment_type.JSON)


def _log_response(response):
    """Log the response body."""
    try:
        data = response.json()
        Logger().info("[JSON Response Body]", json_tool.dumps(data, indent=2))
        allure.attach(json_tool.dumps(data, indent=2), name="Response", attachment_type=allure.attachment_type.JSON)
    except ValueError:
        response.encoding = response.apparent_encoding
        data = response.text
        Logger().info("[Text Response Body]", data)
        allure.attach(data, name="Response", attachment_type=allure.attachment_type.TEXT)


if __name__ == "__main__":
    pass
