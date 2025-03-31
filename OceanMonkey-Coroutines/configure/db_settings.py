"""
@author: Nigo
@desc:
"""


class DatabaseType:
    MYSQL = 0
    REDIS = 1
    MONGODB = 2


DB_CONFIG = {
    DatabaseType.MYSQL: {
        "host": "localhost",
        "user": "root",
        "passwd": "123456",
        "db": "crawler"
    }
}

