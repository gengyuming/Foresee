from Core.DBHandler import mysql_conn


lotto_stages = {
    'stage1': ('last', '19081')
}


class LottoCalculator:
    def __init__(self):
        self.factors_multiple = {
            'time': 1,
            'offset': 1,
            'unknown': 1
        }

    def set_factors(self, **kwargs):
        for factor, multiple in kwargs.items():
            if factor in self.factors_multiple.keys():
                self.factors_multiple[factor] = multiple

    @staticmethod
    def calculate_offset(result_type='source'):
        sql = 'SELECT * FROM ticket_history'
        rows = mysql_conn.execute_sql(sql)
        offset = {}
        if result_type == 'sort':
            for row in rows:
                offset[row.get('draw_number')] = row.get('draw_sort_result')
        if result_type == 'source':
            for row in rows:
                if row.get('draw_source_result'):
                    offset[row.get('draw_number')] = row.get('draw_source_result')

        return offset




