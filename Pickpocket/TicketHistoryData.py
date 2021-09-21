import json
import csv
import io
import re

import requests
import pdfplumber

from Core.Request import Request
from Core.DBHandler import mysql_conn


# double_color_ball_history_url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=30&isVerify=1&pageNo=1'
# lotto_api_history_url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry'


class HistoryData:
    def __init__(self):
        self.default_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

        self.csv_file_path = ''
        self.csv_headers = []

    def set_csv_save_path(self, path):
        self.csv_file_path = path

    def save_csv(self, headers, rows):
        with open(self.csv_file_path, 'w+', newline='') as file:
            csv_writer = csv.DictWriter(file, self.csv_headers)
            csv_writer.writeheader()
            csv_writer.writerows(rows)


class OpenApi:
    def __init__(self):
        self.default_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        }

    def lotto_history_api(self):
        url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry'

        pre_payload = {
            'gameNo': 85,
            'provinceId': 0,
            'pageSize': 30,
            'isVerify': 1,
            'pageNo': 1
        }

        pre_response = requests.get(url=url,
                                    headers=self.default_headers,
                                    params=pre_payload)

        pre_response_obj = json.loads(pre_response.content)

        if pre_response.status_code == 200 and pre_response_obj['success']:
            total = pre_response_obj['value']['total']
        else:
            raise Exception('Request Error')

        payload = {
            'gameNo': 85,
            'provinceId': 0,
            'pageSize': total + 1,
            'isVerify': 1,
            'pageNo': 1
        }
        print(payload)

        response = requests.get(url=url,
                                headers=self.default_headers,
                                params=payload)

        response_obj = json.loads(response.content)

        if response.status_code == 200 and response_obj['success']:
            return response_obj['value']
        else:
            raise Exception('Request Error')


open_api = OpenApi()


class LottoHistory(HistoryData):
    def __init__(self):
        super().__init__()
        self.csv_file_path = r'D:\workspace\myGitHub\Foresee\SourceData\LottoHistoryData.csv'
        self.csv_headers = ['lotteryDrawNum', 'lotteryDrawResult', 'lotteryDrawTime']
        self.csv_header_cn = {'lotteryDrawNum': '期号',
                              'lotteryDrawResult': '开奖结果',
                              'lotteryDrawTime': '开奖日期'}

    def sort_data(self, data_list):
        pass

    def init_api_history_data(self):
        resp = open_api.lotto_history_api()
        for value in resp['list']:
            print(value)

        # history_list = []
        # for index in range(1, pages + 1):
        #     payload = {
        #         'gameNo': 85,
        #         'provinceId': 0,
        #         'pageSize': 30,
        #         'isVerify': 1,
        #         'pageNo': index
        #     }
        #     response = requests.get(url=url,
        #                             headers=self.default_headers,
        #                             json=payload)
        #
        #     response_content = response.content.decode('utf-8')
        #     response_obj = json.loads(response_content)
        #     data_list = response_obj['value']['list']
        #     for data in data_list:
        #         current_data = {'lotteryDrawNum': data['lotteryDrawNum'],
        #                         'lotteryDrawResult': data['lotteryDrawResult'],
        #                         'lotteryDrawTime': data['lotteryDrawTime']}
        #         history_list.append(current_data)
        #
        # with open(self.csv_file_path, 'w+', newline='') as file:
        #     csv_writer = csv.DictWriter(file, self.csv_headers)
        #     csv_writer.writeheader()
        #     csv_writer.writerows(history_list)

    def update_api_history_data(self):
        url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry'
        payload = {
            'gameNo': 85,
            'provinceId': 0,
            'pageSize': 3000,
            'isVerify': 1,
            'pageNo': 1
        }

        response = requests.get(url=url,
                                headers=self.default_headers,
                                json=payload)

        response_content = response.content.decode('utf-8')
        response_obj = json.loads(response_content)

        if response_obj['success']:
            pages = response_obj['value']['pages']
        else:
            raise Exception('Request Error')

        with open(self.csv_file_path, 'r+', encoding='utf-8') as read_csv_file:
            csv_reader = csv.DictReader(read_csv_file)
            last_lotto_draw_num = next(csv_reader)['lotteryDrawNum']

        update_list = []
        is_end = False
        for index in range(1, pages + 1):
            payload = {
                'gameNo': 85,
                'provinceId': 0,
                'pageSize': 30,
                'isVerify': 1,
                'pageNo': index
            }
            response = requests.get(url=url,
                                    headers=self.default_headers,
                                    json=payload)

            response_content = response.content.decode('utf-8')
            response_obj = json.loads(response_content)
            data_list = response_obj['value']['list']
            for data in data_list:
                if data['lotteryDrawNum'] == last_lotto_draw_num:
                    is_end = True
                    break
                current_data = {'lotteryDrawNum': data['lotteryDrawNum'],
                                'lotteryDrawResult': data['lotteryDrawResult'],
                                'lotteryDrawTime': data['lotteryDrawTime']}
                update_list.append(current_data)

            if is_end:
                break

        with open(self.csv_file_path, 'w+', newline='') as write_csv_file:
            csv_writer = csv.DictReader

    def init_pdf_history_data(self):
        lottery_draw_num_list = []
        response_content = self.get_response_content()
        response_obj = json.loads(response_content)
        if response_obj['success']:
            pages = response_obj['value']['pages']
        else:
            raise Exception('Request Error')

        for index in range(1, pages + 1):
            self.body = {
                'gameNo': 85,
                'provinceId': 0,
                'pageSize': 30,
                'isVerify': 1,
                'pageNo': index
            }
            response_content = self.get_response_content()
            response_obj = json.loads(response_content)
            data_list = response_obj['value']['list']
            for data in data_list:
                current_data = {'lotteryDrawNum': data['lotteryDrawNum'],
                                'lotteryDrawResult': data['lotteryDrawResult'],
                                'lotteryDrawTime': data['lotteryDrawTime']}
        # lotteryDrawNum =
        pdf_url = 'https://pdf.sporttery.cn/33800/{lotteryDrawNum}/{lotteryDrawNum}.pdf'

        source_no = self.get_pdf_source_no(pdf_url)

    @staticmethod
    def get_pdf_source_no(url):
        response = requests.get(url)
        content = response.content
        content_io = io.BytesIO(content)

        with pdfplumber.open(content_io) as pdf:
            page01 = pdf.pages[0]  # 指定页码
            text = page01.extract_text()  # 提取文本
            # print(text)
            source_no = re.search('(?<=本期出球顺序： ).*?(?=\n)', text)
            print(source_no.group())

        return source_no.group()

    def test(self):
        pass


if __name__ == '__main__':
    lotto_his = LottoHistory()
    lotto_his.init_api_history_data()
