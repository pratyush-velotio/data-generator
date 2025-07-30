import sqlite3
from typing import List, Dict
from beautifultable import BeautifulTable

class DBHandler:
    def __init__(self, db_path: str = "data_handler/file_metadata.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_metadata_table()
        self.create_generated_data_table()

    def create_metadata_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS metadata (
                file_id TEXT PRIMARY KEY,
                file_type TEXT,
                file_path TEXT,
                generated_at TEXT
            );
        ''')
        self.conn.commit()

    def create_generated_data_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS generated_data (
                user_id VARCHAR2,
                full_name VARCHAR2,
                product_name VARCHAR2,
                category VARCHAR2,
                Price FLOAT,
                address VARCHAR2,
                available BOOLEAN DEFAULT 1,
                created_at VARCHAR2
            );
        ''')
        self.conn.commit()

    def insert_metadata(self, file_id: str, file_type: str, file_path: str, generated_at: str):
        self.conn.execute(
            "INSERT INTO metadata (file_id, file_type, file_path, generated_at) VALUES (?, ?, ?, ?)",
            (file_id, file_type, file_path, generated_at)
        )
        self.conn.commit()

    def insert_generated_data(self, records: List[Dict]):
        for record in records:
            self.conn.execute("""
                INSERT OR IGNORE INTO generated_data (
                    user_id, full_name, product_name, category,
                    Price, address, available, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                record.get("user_id"),
                record.get("full_name"),
                record.get("product_name"),
                record.get("category"),
                record.get("Price"),
                str(record.get("address")),
                record.get("available"),
                record.get("created_at")
            ))
        self.conn.commit()
        
    def get_metadata(self):
        cursor = self.conn.execute(
            "SELECT * FROM metadata ")
        return cursor.fetchone()
    
    def print_metadata(self):
        data = self.get_metadata()
        table = BeautifulTable()
        table.columns.header = ["File ID", "File Type", "File Path", "Generated At"]
        if data:
            table.rows.append(data)
        else:
            table.rows.append(["No metadata found"])
        
        print(table)
    
    def get_tabledata(self):
        cursor = self.conn.execute(
            "SELECT * FROM generated_data")
        return cursor.fetchall()
    
    def print_generated_data(db_handler):
        data = db_handler.get_tabledata()
        table = BeautifulTable()
        table.columns.header = [
            "user_id", "full_name", "product_name", "category",
            "Price", "address", "available", "created_at"
        ]
        for row in data:
            table.rows.append(row)
        
        print(table)
        
    

    def close(self):
        self.conn.close()

    
