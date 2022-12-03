from Core.db_handler import mysql_conn
from Calculator import calculator_config
from Core.logger import log


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
    def get_results(result_type='source', draw_number=None, draw_time=None, limit=None):
        sql = 'SELECT * FROM ticket_history'
        if draw_number or draw_time:
            sql += ' WHERE'
            if draw_number:
                sql += ' draw_number BETWEEN "%s" AND "%s"' % (min(draw_number), max(draw_number))
            if draw_time:
                sql += ' draw_time BETWEEN "%s" AND "%s"' % (min(draw_time), max(draw_time))
        if limit:
            sql += ' LIMIT %s' % limit

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

    def calculate_result_rate(self, results):
        """
        计算日期因素
        :param results: 历史数据
        :return:
        """
        bucket = {}
        rate = {}
        total = 0
        for r in results:
            dsr = r.get('draw_sort_result')
            dsr_list = dsr.split(' ')
            for d in dsr_list:
                if d not in bucket.keys():
                    bucket[d] = 1
                else:
                    bucket[d] += 1
                total += 1

        bks = sorted(bucket.keys())

        for k in bks:
            v = bucket.get(k)
            ra = round(v/total, 2)
            rate[k] = (v, ra)

        return rate


if __name__ == '__main__':
    lc = LottoCalculator()
    res = lc.get_results()
    # res = lc.get_results(draw_time=['2022-11-4', '2022-12-4'])
    log(res)
    rate = lc.calculate_result_rate(res)
    log(rate)
    for r in rate.items():
        log(r)









