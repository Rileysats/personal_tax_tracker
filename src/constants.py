INSERT_INTO_ASSETS = """
                    INSERT INTO assets (Date, Description, Ticker, Value, Type, Currency) VALUES (?, ?, ?, ?, ?, ?)
                    """

INSERT_INTO_DEDUCTIONS = """
                        INSERT INTO deductions (Type, Description, Value) VALUES (?, ?, ?)
                        """

CHECK_TABLE_EXISTS = """
                    SELECT name FROM sqlite_master WHERE type = 'table' AND name = '{table_name}'
                    """ 

CREATE_TABLES = { 
                "assets": 
                """
                    CREATE TABLE IF NOT EXISTS assets (
                        ID INTEGER PRIMARY KEY,
                        Date DATE,
                        Type TEXT,
                        Description TEXT,
                        Ticker TEXT,
                        Value FLOAT,
                        Currency TEXT
                    )
                """,
                "deductions": 
                """
                    CREATE TABLE IF NOT EXISTS deductions (
                        ID INTEGER PRIMARY KEY,
                        Type TEXT,
                        Description TEXT,
                        Value FLOAT
                    )
                """
                }
