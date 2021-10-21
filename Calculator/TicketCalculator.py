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
        results = {}
        if result_type == 'sort':
            for row in rows:
                results[row.get('draw_number')] = row.get('draw_sort_result')
        if result_type == 'source':
            for row in rows:
                if row.get('draw_source_result'):
                    results[row.get('draw_number')] = row.get('draw_source_result')

        return results


lc = LottoCalculator()





