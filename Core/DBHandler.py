# -*- encoding: utf-8 -*-

import pymysql
import pymongo

from Core.Logger import log


class MysqlDB:
    def __init__(self, config, env):
        section_name = env.upper() + '.' + 'Mysql'
        self.__host__ = config.get(section_name, 'host')
        self.__port__ = int(config.get(section_name, 'port'))
        self.__username__ = config.get(section_name, 'username')
        self.__password__ = config.get(section_name, 'password')
        self.connection = self.create_connection()
        self.cursor = self.connection.cursor()

    def create_connection(self):
        self.connection = pymysql.connect(host=self.__host__,
                                          port=self.__port__,
                                          user=self.__username__,
                                          password=self.__password__,
                                          charset='utf8',
                                          cursorclass=pymysql.cursors.DictCursor)

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

        log('————————数据库执行————————')
        log('Database: {}'.format(database))
        log(sql)
        if database:
            use_database_sql = 'USE {}'.format(database)
            self.cursor.execute(use_database_sql)
        rows = self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.connection.commit()
        log('执行结果数量: {}'.format(rows))
        log('执行结果\n{}'.format(result))
        log('————————数据库执行结束————————')

        return result

    def get_db_thread_id(self):
        return self.connection.thread_id()


class MongoDB:
    def __init__(self, config, env):
        section_name = env.upper() + '.' + 'Mongo'
        self.__connection__ = None
        self.__collections__ = None
        self.__host__ = config.get(section_name, 'host')
        self.__username__ = config.get(section_name, 'username')
        self.__password__ = config.get(section_name, 'password')
        self.__database__ = config.get(section_name, 'database')
        self.__init_connection__()

    def __del__(self):
        if self.__connection__ is not None:
            self.__connection__.close()

    def __init_connection__(self):
        self.__connection__ = pymongo.MongoClient(
            'mongodb://{}:{}@{}'.format(
                self.__username__,
                self.__password__,
                self.__host__
            )
        )

        self.__collections__ = self.__connection__[self.__database__]

    def find_one(self, collection, condition=''):
        log(collection)
        log(condition)
        result = self.__collections__[collection].find_one(condition)

        if result is None:
            return_value = {}
        else:
            return_value = result

        return return_value

    def find(self, collection, condition=None):
        log(collection)
        log(condition)
        if condition is None:
            condition = {}

        return_value = []
        result = self.__collections__[collection].find(condition)

        for document in result:
            return_value.append(document)

        return return_value

    def update(self, collection, condition, value):
        log(collection)
        log(condition)
        log(value)
        return_value = []
        result = self.__collections__[collection].update(
            condition,
            value
        )

        return_value.append(result)

        return return_value
