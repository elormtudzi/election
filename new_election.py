import sqlite3
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
import config

class NewElection:
          
    def start(self):
        print("=== Create New Election ==")
        root=Tk()
        root.withdraw() #Hide TKinter's root window
        config.file_path=asksaveasfilename(
            title="Save New Election File",
            defaultextension=".db",
            filetypes=[("sqlite Database","*.db"),("All Files","*.*")]
        )
        if config.file_path:
            create_database
        else:
            print("No election file created!")
            
        
def create_database():
        #create sqlite database for the new election
        connection=sqlite3.connect(config.file_path)
        cursor=connection.cursor()
        
        #Create the tables for the election
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS aspirants(ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                       portfolio_id INTEGER NOT NULL, portfolio TEXT NOT NULL,
                       position INTGER, category  TEXT,Aspirant TEXT, image BLOB,
                       vote_gain INTEGER DEFAULT 0, yes_vote INTEGER DEFAULT 0,
                       no_vote INTEGER DEFAULT 0)
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS centers(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        center TEXT NOT NULL,election_status TEXT)
        """)
        cursor.execute("""
       CREATE TABLE IF NOT EXISTS codes(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,center	TEXT,
                       Code TEXT UNIQUE,VoteStatus TEXT DEFAULT '0',
                       CurrentForm	TEXT)
        """)
        cursor.execute("""
       CREATE TABLE IF NOT EXISTS portfolios(ID	INTEGER PRIMARY KEY AUTOINCREMENT,Category TEXT DEFAULT 'General',
                       portfolio_id	TEXT,Portfolio_name	TEXT)
        """)
        cursor.execute("""
      CREATE TABLE IF NOT EXISTS settings(IDNumber INTEGER NOT NULL UNIQUE PRIMARY KEY,
                       Institution_name TEXT,Election_name	TEXT,
                       Election_year	TEXT,Number_voters	INTEGER DEFAULT 10,
                        Status	INTEGER NOT NULL DEFAULT 0,EC_password TEXT,
                       Phone_number TEXT,passcode TEXT)
        """)
        cursor.execute("""
     CREATE TABLE IF NOT EXISTS skippedVotes(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                       portfolio_id INTEGER NOT NULL,portfolio TEXT, Category TEXT, 
                       Center TEXT,Vote_gain INTEGER DEFAULT 0)
        """)
        connection.commit
        connection.close

        print(f"New Election file created at '{config.file_path}' successfully!")
