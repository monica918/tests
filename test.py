import responses
import requests
import unittest

# 假设有一个函数fetch_data来请求数据
def fetch_data(url):
    response = requests.get(url)
    return response.json()

class TestFetchData(unittest.TestCase):

    @responses.activate
    def test_fetch_data(self):
        url = 'http://example.com/api/data'
        expected_response = {"key": "value"}

        # 使用responses.add来添加mock响应
        responses.add(responses.GET, url,
                      json=expected_response, status=200)

        result = fetch_data(url)

        # 验证返回结果
        self.assertEqual(result, expected_response)
        # 验证requests.get是否被正确调用
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url, url)

if __name__ == '__main__':
    unittest.main()
