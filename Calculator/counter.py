from Core.db_handler import mysql_conn
from Calculator import calculator_config


lotto_stages = {
    'stage1': ('last', '19081')
}


class Counter:
    def __init__(self):
        self.bucket = {}


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


if __name__ == '__main__':
    pass

