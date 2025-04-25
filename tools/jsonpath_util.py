import json
from jsonpath_ng import parse
from typing import Any, Dict, List, Optional


class JSONPathUtil:
    def __init__(self, json_data):
        """初始化 JSONPathReader，加载 JSON 数据"""
        if isinstance(json_data, str):
            self.data: Dict[str, Any] = self.load_json(json_data)
        elif isinstance(json_data, dict):
            self.data: Dict[str, Any] = json_data
        else:
            raise ValueError("json_data must be a JSON string or a dictionary.")

    @staticmethod
    def load_json(json_data: str) -> Dict[str, Any]:
        """加载 JSON 数据并返回字典"""
        try:
            return json.loads(json_data)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON data") from e

    def get_value(self, jsonpath_expr: str) -> Optional[List[Any]]:
        """根据 JSONPath 表达式获取值"""
        jsonpath_expr = parse(f"$.{jsonpath_expr}")
        matches = jsonpath_expr.find(self.data)
        result = [match.value for match in matches] if matches else None
        if len(result) == 1:
            return result[0]
        return result


# 示例用法
if __name__ == "__main__":
    json_string = '''
    {
        "store": {
            "book": [
                {"category": "reference", "author": "Nigel Rees", "title": "Sayings of the Century", "price": 8.95},
                {"category": "fiction", "author": "Evelyn Waugh", "title": "Sword of Honour", "price": 12.99},
                {"category": "fiction", "author": "Herman Melville", "title": "Moby Dick", "isbn": "0-553-21311-3", "price": 8.99},
                {"category": "fiction", "author": "J. R. R. Tolkien", "title": "The Lord of the Rings", "isbn": "0-395-19395-8", "price": 22.99}
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
    authors = jsonpath_util.get_value("$.store.book[*].author")
    print("Authors:", authors)

    # 获取所有书籍的价格
    prices = jsonpath_util.get_value("$.store.book[*].price")
    print("Prices:", prices)
