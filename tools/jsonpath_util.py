import json

from jsonpath_ng import parse
from typing import Any, Dict, List, Optional


class JSONPathUtil:
    def __init__(self, json_data):
        """初始化 JSONPathReader，加载 JSON 数据"""
        if isinstance(json_data, str):
            self.data: Dict[str, Any] = self.load_json(json_data)
            return
        if isinstance(json_data, dict):
            self.data: Dict[str, Any] = json_data
            return
        raise ValueError("json_data must be a JSON string or a dictionary.")

    @staticmethod
    def load_json(json_data: str) -> Dict[str, Any]:
        """加载 JSON 数据并返回字典"""
        try:
            return json.loads(json_data)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON data") from e

    def save_json(self, file_path):
        """保存 JSON 数据到指定文件"""
        with open(file_path, 'w') as file:
            json.dump(self.data, file, indent=2)
            file.close()

    def get_value(self, jsonpath_expr: str) -> Optional[List[Any]]:
        """根据 JSONPath 表达式获取值"""
        jsonpath_expr = parse(f"$.{jsonpath_expr}")
        matches = jsonpath_expr.find(self.data)
        result = [match.value for match in matches] if matches else None
        if len(result) == 1:
            return result[0]
        return result

    def update_value(self, jsonpath_expr: str, value: any):
        """根据 JSONPath 表达式修改其对应值"""
        jsonpath_expr = parse(f"$.{jsonpath_expr}")
        matches = jsonpath_expr.find(self.data)
        for match in matches:
            match.context.value[str(match.path)] = value

    def remove(self, jsonpath_expr: str):
        """根据 JSONPath 表达式删除内容"""
        jsonpath_expr = parse(f"$.{jsonpath_expr}")
        matches = jsonpath_expr.find(self.data)
        for match in matches:
            parent = match.context.value
            parent.remove(match.value)


# 示例用法
if __name__ == "__main__":
    json_string = '''
    {
        "store": {
            "book": [
                {"category": "reference", "author": "Nigel Rees", "title": "Sayings of the Century", "price": 8.95},
                {"category": "fiction", "author": "Evelyn Waugh", "title": "Sword of Honour", "price": 12.99},
                {"category": "fiction", "author": "Herman", "title": "Moby Dick", "isbn": "0-553", "price": 8.99},
                {"category": "fiction", "author": "Tolkien", "title": "The Lord...", "isbn": "0-395", "price": 22.99}
            ],
            "bicycle": {
                "color": "red",
                "price": 19.95
            }
        }
    }
    '''

    jsonpath_util = JSONPathUtil(json_string)

    # 使用 JSONPath 表达式获取书籍的作者
    authors = jsonpath_util.get_value("store.book[*].author")
    print("Authors:", authors)

    # 获取所有书籍的价格
    prices = jsonpath_util.get_value("store.book[*].price")
    print("Prices:", prices)

    # 修改值
    jsonpath_util.update_value("store.book[*].price", 100)
    prices = jsonpath_util.get_value("store.book[*].price")
    print("Prices:", prices)

    jsonpath_util.update_value("store.book[0].price", 666)
    prices = jsonpath_util.get_value("store.book[*].price")
    print("Prices:", prices)

    # 删除内容
    jsonpath_util.remove("store.book[0]")
    print(jsonpath_util.data)
