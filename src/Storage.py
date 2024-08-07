import csv
import os
import sqlite3
import contants
from logger import logger

class Storage():
    def __init__(self, test_mode=False) -> None:
        self.fieldnames = ['Name', 'Age', 'City']
        if test_mode:
            self.db = "/Users/rileysatanek/Desktop/Tax App/src/database/prod.db"
        else:
            self.db = "/Users/rileysatanek/Desktop/Tax App/src/database/test.db"
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
            self.cursor.execute(query, data)
        else:
            self.cursor.execute(query)

        self.conn.commit()

    def fetch_record(self, query):
        self.execute_sql(query)

        column_names = [description[0] for description in self.cursor.description]
        rows = self.cursor.fetchone()
        self.create_dict_from_res(column_names, rows)

    def write_record(self, query, data, table_name):
        logger.info(f"Executing query: {query} with values {data}")
        # table_name = self.extract_table_names(query, "FROM")
        if not self.check_table_exist(table_name):
            create_table_query = contants.CREATE_TABLES[table_name]
            logger.info(f"Creating table: {table_name} with query \n {create_table_query}")
            self.execute_sql(create_table_query)
            logger.info("Table created")

        self.execute_sql(query, data)



    def create_dict_from_res(self, first, second):
        return dict(zip(list(first), list(second)))


    def close_connection(self):
        # if self.conn
        pass

    def check_table_exist(self, table_name) -> bool:
        self.execute_sql(contants.CHECK_TABLE_EXISTS.format(table_name=table_name))
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
