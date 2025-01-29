import sqlite3
import config

def open_existing_election(file_path):
    print(f"Opening existing election file: {file_path}")
    try:
        #Connect to the existing SQLite database
        connection=sqlite3.connect(file_path)
        cursor=connection.cursor()
        config.file_path=file_path
        
    except sqlite3.Error as ex:
        print(f"Error opening file: {ex}")


