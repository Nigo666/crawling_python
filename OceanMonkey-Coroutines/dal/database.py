"""
@author: Nigo
@desc:
"""

from configure import db_settings
import pymysql


def build_db_conn(db_type=db_settings.DatabaseType.MYSQL):
    db_conn = None
    if db_type == db_settings.DatabaseType.MYSQL:
        db_config = db_settings.DB_CONFIG[db_type]
        db_conn = pymysql.connect(
            host=db_config["host"],
            user=db_config["user"],
            passwd=db_config["passwd"],
            db=db_config["db"]
        )
    return db_conn


def load_data_2_database(db_conn, sql, data, db_type=db_settings.DatabaseType.MYSQL):
    if db_type == db_settings.DatabaseType.MYSQL:
        cursor = db_conn.cursor()
        cursor.executemany(sql, data)
        db_conn.commit()


def get_db_columns(db_conn, table, exclude_fields=None):
    sql = f"show columns from {table}"
    cursor = db_conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    columns = [result[0] for result in results]
    exclude_fields = exclude_fields or ["id", "ct"]
    if exclude_fields:
        for field in exclude_fields:
            columns.remove(field) if field in columns else None
    return columns
