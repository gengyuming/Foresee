# -*- encoding: utf-8 -*-

import pymysql
import traceback

from Core.Logger import log
from Core.ConfigReader import ConfigReader


config_path = './Core/config.ini'


class MysqlDB:
    def __init__(self, config):
        self.__config_section__ = 'Mysql'
        self.__host__ = config.get(self.__config_section__, 'host')
        self.__port__ = int(config.get(self.__config_section__, 'port'))
        self.__username__ = config.get(self.__config_section__, 'username')
        self.__password__ = config.get(self.__config_section__, 'password')
        self.__database__ = config.get(self.__config_section__, 'database')
        self.connection = self.create_connection()
        self.cursor = self.connection.cursor()

    def create_connection(self):
        self.connection = pymysql.connect(host=self.__host__,
                                          port=self.__port__,
                                          user=self.__username__,
                                          password=self.__password__,
                                          charset='utf8',
                                          cursorclass=pymysql.cursors.DictCursor)

        if self.__database__:
            self.connection.select_db(self.__database__)

        return self.connection

    def close_cursor(self):
        """
        关闭游标
        """
        if self.cursor:
            self.cursor.close()
        self.cursor = None

    def close_connection(self):
        """
        关闭连接
        """
        if self.cursor:
            self.close_cursor()

        self.connection.close()

    def execute_sql(self, sql, database=None):
        # 激活连接
        self.connection.ping()

        log_list = [
            '————————数据库执行————————',
            'Database: {}'.format(database),
            'SQL:\n{}'.format(sql)
        ]

        if database:
            use_database_sql = 'USE {}'.format(database)
            self.cursor.execute(use_database_sql)
        rows = self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.connection.commit()
        log_list.append('执行结果数量: {}'.format(rows))
        log_list.append('执行结果\n{}'.format(result))
        log_list.append('————————数据库执行结束————————')

        log_content = '\n'.join(log_list)
        log(log_content)

        return result

    def get_db_thread_id(self):
        return self.connection.thread_id()


__conf__ = ConfigReader.load_config(config_path)
mysql_conn = MysqlDB(__conf__)


