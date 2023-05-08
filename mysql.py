import pymysql

class Database:
    """数据库操作类"""

    def __init__(self, host, user, password, database, charset="utf8"):
        self.db = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset
        )
        self.cursor = self.db.cursor()

    def execute(self, sql, params=None, fetchall=False):
        """执行SQL语句"""
        self.cursor.execute(sql, params)
        if fetchall:
            results = self.cursor.fetchall()
            return results
        else:
            self.db.commit()

    def close(self):
        """关闭数据库连接"""
        self.db.close()
