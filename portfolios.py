import sqlite3
import config

def view_portfolios():
    try:
        connection=sqlite3.connect(config.file_path)
        cursor=connection.cursor()
        #Fetch and display the polling station files
        cursor.execute("SELECT * FROM portfolios")
        portfolios=cursor.fetchall()
        if portfolios:
            print("=== Registered Portfolios ===")
            for portfolio in portfolios:
                print(f"ID: {portfolio[0]} | Category: {portfolio[1]} | Portfolio: {portfolio[3]}")
            print()
        else:
         print("No Registered Portfolio found")
        connection.close()
    except sqlite3.Error as e:
        print(f"Error loading the data: {e}")
        

def add_new_portfolio(category,portfolio_name):
    try:
        connection=sqlite3.connect(config.file_path)
        cursor=connection.cursor()
        cursor.execute("SELECT EXISTS (SELECT 1 FROM portfolios WHERE category=? AND portfolio_name=?)",(category,portfolio_name))
        result=cursor.fetchone()[0]
        if result:
            print(f"{portfolio_name} under the {category} already exists!")
        else:
            #First, Get the portfolio ID
            cursor.execute("SELECT count(*) FROM portfolios WHERE Category=?",(category))
            portfolio_id=cursor.fetchone()[0]
            #Add the new polling station
            cursor.execute("INSERT INTO portfolios(category,portfolio_name,portfolio_id) VALUES (?,?,?)",(category,portfolio_name,portfolio_id))
            connection.commit()
       
        
    except sqlite3.Error as ex:
        print(f"Could not save the data: {ex}")
    finally:
         connection.close()
        
        