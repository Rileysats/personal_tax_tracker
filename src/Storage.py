import csv
import os
import sqlite3
import constants
from logger import logger
from helpers import ensure_directory_exists
from pathlib import Path


class Storage():
    def __init__(self, test_mode=False) -> None:
        self.fieldnames = ['Name', 'Age', 'City']
        repo_root = Path(__file__).parent.parent
        ensure_directory_exists(repo_root / "database")
        if test_mode:
            # self.db = "/Users/rileysatanek/Desktop/Tax App/src/database/prod.db"
            self.db = repo_root / "database/test.db"
        else:
            self.db = repo_root / "database/prod.db"
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()

    # def load_data(self):
    #     with open(self.path, 'r', newline='') as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         data = [row for row in reader]

    #     for row in data:
    #         print(row)

    # # can use decorator, just fieldnames are changing
    # def write_data(self, data):
    #     with open(self.path, 'a', newline='') as csvfile:
    
    #         writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
    #         if not self.file_exist(self.path):
    #             writer.writeheader()
    #         writer.writerows(data)

    # def file_exist(self, file_path) -> bool:
    #     return os.path.isfile(file_path)

    def execute_sql(self, query, data=None):
        if data:
            logger.info(f"Executing query: {query} with values {data}")

            self.cursor.execute(query, data)
        else:
            logger.info(f"Executing query: {query}")

            self.cursor.execute(query)

        self.conn.commit()

    def fetch_record(self, query):
        self.execute_sql(query)

        row = self.cursor.fetchone()
        self.create_dict_from_res(row)

    def fetch_all_records(self, table_name: str):
        self.execute_sql(constants.SELECT_ALL.format(table_name))

        rows = self.cursor.fetchall()
        self.create_dict_from_res(rows)


    def fetch_records_filter(self, table_name: str, filters: str):
        self.execute_sql(constants.SELECT_ALL_FILTER.format(table_name=table_name, filters=filters))

        rows = self.cursor.fetchall()
        self.create_dict_from_res(rows)


    def write_record(self, query, data, table_name):
        # table_name = self.extract_table_names(query, "FROM")
        if not self.check_table_exist(table_name):
            create_table_query = constants.CREATE_TABLES[table_name]
            logger.info(f"Creating table: {table_name} with query \n {create_table_query}")
            self.execute_sql(create_table_query)
            logger.info("Table created")

        self.execute_sql(query, data)



    def create_dict_from_res(self, results):
        column_names = [description[0] for description in self.cursor.description]
        return dict(zip(list(column_names), list(results)))


    def close_connection(self):
        # if self.conn
        pass

    def check_table_exist(self, table_name) -> bool:
        self.execute_sql(constants.CHECK_TABLE_EXISTS.format(table_name=table_name))
        if self.cursor.fetchone() is None:
            return False
        return True
    
    # TODO: below func
    # def extract_table_names(self, pattern, text):
    #     import re
    #     # Use a regular expression to capture text after the pattern
    #     match = re.search(rf'{pattern}(.*)', text)
    #     if match:
    #         print(match.group(1).strip())  # Extract the part after the pattern
    #     return None  # Pattern not found
