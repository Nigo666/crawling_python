"""
@author: Nigo
@desc:
"""
from dal import database
from utils import utils
import pandas as pd


def load_sh_futures_2_db(db_conn, data, excel_file_path=None):
    df = pd.DataFrame(data=data)
    df.to_excel(excel_file_path, index=False) if excel_file_path else None
    table = "sh_futures"
    columns = database.get_db_columns(db_conn, table)
    sql = utils.build_sql(columns, table)
    database.load_data_2_database(db_conn, sql, df.values.tolist())


def load_shares_2_db(db_conn, data, excel_file_path=None):
    df = pd.DataFrame(data=data)
    df.to_excel(excel_file_path, index=False) if excel_file_path else None


def load_drugs_2_db(db_conn, data, excel_file_path=None):
    df = pd.DataFrame(data=data)
    df.to_excel(excel_file_path, index=False) if excel_file_path else None
    table = "drugs"
    columns = database.get_db_columns(db_conn, table)
    sql = utils.build_sql(columns, table)
    database.load_data_2_database(db_conn, sql, df.values.tolist())
