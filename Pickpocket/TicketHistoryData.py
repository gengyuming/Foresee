import json
import csv
import io
import re

import requests
import pdfplumber
import pytesseract
from PIL import Image
import bs4

from Core.Request import Request
from Core.DBHandler import mysql_conn
from Core.TicketEnum import TicketType
from Core.ConfigReader import core_config


pytesseract_path = tesseract_cmd = core_config.get('tesseract_orc', 'tesseract_cmd')
pytesseract.pytesseract.tesseract_cmd = pytesseract_path


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

    @staticmethod
    def lotto_pdf_api(draw_number):
        url = 'https://pdf.sporttery.cn/33800/{draw_number}/{draw_number}.pdf'.format(draw_number=draw_number)
        print(url)
        response = requests.get(url)
        content = response.content

        return content

    def lotto_image_api(self, draw_number):
        url = 'https://static.sporttery.cn/cms/upload/20190710/20190710210507857.jpg'
        print(url)
        response = requests.get(url)
        content = response.content.decode('utf-8')

        return content


open_api = OpenApi()


class HistoryData:
    def __init__(self):
        self.default_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

        self.csv_file_path = ''
        self.csv_headers = []

    def set_csv_save_path(self, path):
        self.csv_file_path = path

    def save_csv(self, rows):
        with open(self.csv_file_path, 'w+', newline='') as file:
            csv_writer = csv.DictWriter(file, self.csv_headers)
            csv_writer.writeheader()
            csv_writer.writerows(rows)

    @staticmethod
    def save_db_api_info(rows):
        for row in rows:
            sql = "INSERT INTO `foresee`.`ticket_history`(`draw_number`, `draw_sort_result`, `draw_time`, `ticket_type`) " \
                  "VALUES ('{draw_number}', '{draw_sort_result}', '{draw_time}', {ticket_type});".format(draw_number=row.get('draw_number'),
                                                                                                         draw_sort_result=row.get('draw_sort_result'),
                                                                                                         draw_time=row.get('draw_time'),
                                                                                                         ticket_type=row.get('ticket_type'))
            mysql_conn.execute_sql(sql)

    @staticmethod
    def update_db_source_result(draw_number, draw_source_result):
        sql = 'UPDATE `foresee`.`ticket_history` SET draw_source_result="{draw_source_result}" WHERE draw_number="{draw_number}"'.format(
            draw_source_result=draw_source_result,
            draw_number=draw_number
        )
        mysql_conn.execute_sql(sql)


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

    @staticmethod
    def get_format_api_history_data():
        resp = open_api.lotto_history_api()

        history_list = []
        for value in resp['list']:
            history_list.append(
                {
                    'draw_number': value.get('lotteryDrawNum'),
                    'draw_sort_result': value.get('lotteryDrawResult'),
                    'draw_time': value.get('lotteryDrawTime'),
                    'ticket_type': TicketType.LOTTO
                }
            )

        return history_list

    def add_api_lotto_history_db_data(self):
        """
        数据库插入lotto API接口数据
        :return:
        """
        api_result = self.get_format_api_history_data()
        self.save_db_api_info(api_result)

    def add_db_source_result(self):
        rows = mysql_conn.execute_sql('SELECT * FROM `foresee`.`ticket_history`')
        for row in rows:
            if not row.get('draw_source_result'):
                draw_number = row.get('draw_number')
                draw_source_result = self.get_pdf_source_result(draw_number)
                self.update_db_source_result(draw_number, draw_source_result)

    @staticmethod
    def get_pdf_source_result(draw_number):

        pdf_content = open_api.lotto_pdf_api(draw_number)
        content_io = io.BytesIO(pdf_content)

        with pdfplumber.open(content_io) as pdf:
            page01 = pdf.pages[0]  # 指定页码
            text = page01.extract_text()  # 提取文本
            # print(text)
            source_no = re.search('(?<=本期出球顺序： ).*?(?=\n)', text)
            # print(source_no.group())

        return source_no.group()

    def get_img_source_result(self, draw_number):

        image_content = open_api.lotto_image_api(draw_number)
        image_full = Image.open(image_content)
        # 裁剪截图成验证码图片
        box = (
            300,
            145,
            680,
            180
        )

        image_crop= image_full.crop(box)
        image_crop = image_crop.convert('L')
        # image_crop_prop.save('./test_crop1.png')

        config_str = '--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789'
        prop_result = pytesseract.image_to_string(image_crop, lang='eng', config=config_str).strip()


# if __name__ == '__main__':
#     lotto_his = LottoHistory()
#     lotto_his.init_api_history_data()
