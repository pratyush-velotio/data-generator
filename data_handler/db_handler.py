import sqlite3
from typing import List, Dict

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
                user_id Text,
                full_name TEXT,
                product_name TEXT,
                category TEXT,
                Price float,
                address TEXT,
                available BOOLEAN DEFAULT 1,
                created_at TEXT
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
                    Price, available, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                record.get("user_id"),
                record.get("full_name"),
                record.get("product_name"),
                record.get("category"),
                record.get("Price"),
                record.get("address"),
                record.get("available"),
                record.get("created_at")
            ))
            break
        self.conn.commit()
        
    def get_metadata(self, file_id):
        cursor = self.conn.execute(
            "SELECT * FROM metadata WHERE file_id = ?",
            (file_id,))
        return cursor.fetchone()
    
    def get_tabledata(self):
        cursor = self.conn.execute(
            "SELECT * FROM generated_data")
        return cursor.fetchall()
        
    

    def close(self):
        self.conn.close()

    
