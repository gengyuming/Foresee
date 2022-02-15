import json

import requests

from Core.core_exception import MethodException


class Request:

    def send_request(self, method, url, headers, body, files=None):
        """
        发送请求
        :param method: 请求方法
        :param url: 请求地址
        :param headers: 请求头
        :param body: 请求实体
        :param files: 文件
        :return: 响应
        """
        if method.upper() == 'GET':
            response = self.get_request(url, headers, body)
        elif method.upper() == 'POST':
            response = self.post_request(url, headers, body, files=files)
        elif method.upper() == 'PUT':
            response = self.put_request(url, headers, body)
        elif method.upper() == 'DELETE':
            response = self.delete_request(url, headers, body)
        else:
            raise MethodException(method)

        print(response.elapsed.total_seconds())

        return response

    @staticmethod
    def get_request(url, headers, body):
        """
        GET 请求方法
        :return:
        """
        response = requests.get(url=url,
                                headers=headers,
                                params=body)

        response.content.decode('utf-8')

        return response

    @staticmethod
    def post_request(url, headers, body, files=None):
        """
        POST 请求方法
        :return:
        """
        if 'Content-Type' in headers.keys() and headers['Content-Type'] == 'application/json':
            body = json.dumps(body).encode('utf-8')

        response = requests.post(url=url,
                                 headers=headers,
                                 params=body,
                                 files=files)

        response.content.decode('utf-8')

        return response

    @staticmethod
    def put_request(url, headers, body):
        """
        PUT 请求方法
        :return:
        """
        response = requests.put(url=url,
                                headers=headers,
                                params=body)

        response.content.decode('utf-8')

        return response

    @staticmethod
    def delete_request(url, headers, body):
        """
        DELETE 请求方法
        :return:
        """
        response = requests.delete(url=url,
                                   headers=headers,
                                   params=body)

        response.content.decode('utf-8')

        return response

