from Core.DBHandler import mysql_conn
from Calculator import calculator_config


lotto_stages = {
    'stage1': ('last', '19081')
}


class LottoCalculator:
    def __init__(self):
        config_factors = calculator_config.options('Lotto')

        self.factors = {}
        for factor in config_factors:
            self.factors[factor] = calculator_config.get('Lotto', factor)

    @staticmethod
    def get_results(result_type='source'):
        sql = 'SELECT * FROM ticket_history'
        rows = mysql_conn.execute_sql(sql)
        results = []
        if result_type == 'sort':
            for row in rows:
                results.append(row)
        if result_type == 'source':
            for row in rows:
                if row.get('draw_source_result'):
                    results.append(row)

        return results

    def calculate_date_factor(self, draw_number, data_list):
        """
        计算日期因素
        :param draw_number: 期号
        :param data_list: 历史数据
        :return:
        """
        for data in data_list:
            current_date = data['draw_time'].replace('-', '')
            print(current_date)




if __name__ == '__main__':
    lc = LottoCalculator()
    res = lc.get_results()






