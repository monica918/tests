1。python的responses库/apifox/charles 都可以mock响应数据，原理都是拦截请求，修改请求内容、模拟响应数据。
2。
requests：用于实际发送 HTTP 请求。
responses 库是专门设计用于模拟 HTTP 请求和响应的库，提供了丰富的功能和选项来模拟各种 HTTP 请求和响应的情况。
mock 库是 Python 标准库中的一部分，用于模拟对象和行为，不仅可以用于模拟 HTTP 请求和响应，还可以模拟任何 Python 对象和函数的行为。
推荐使用responses 库，满足需求，简单好上手
3。
import responses
import requests
import unittest

# 假设有一个函数 fetch_data 来请求数据
def fetch_data(url, params):
    response = requests.get(url, params=params)
    return response.json()

class TestFetchDataWithParams(unittest.TestCase):

    @responses.activate
    def test_fetch_data_with_params(self):
        url = 'http://example.com/api/data'
        params = {'name': 'zs'}
        expected_response = {"key": "value"}

        # 使用 responses.add 来添加 mock 响应
        responses.add(
            responses.GET, 
            url, 
            match_querystring=True,
            json=expected_response, 
            status=200, 
            
        )

        # 调用 fetch_data 函数
        result = fetch_data(url, params)

        # 验证返回结果
        self.assertEqual(result, expected_response)

        # 验证 requests.get 是否被正确调用
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url, f"{url}?name=zs")

if __name__ == '__main__':
    unittest.main()

使用 @responses.activate 装饰器激活 responses 库的 mock 功能。装饰器确保在测试函数执行期间，所有的 HTTP 请求都会被 responses 拦截。
添加 mock 响应：使用 responses.add 方法添加预定义的 HTTP 响应。该函数允许你指定请求的方法、URL、响应的数据、状态码等。
