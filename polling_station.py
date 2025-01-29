import sqlite3
import config

def view_polling_stations():
    try:
        connection=sqlite3.connect(config.file_path)
        cursor=connection.cursor()
        #Fetch and display the polling station files
        cursor.execute("SELECT * FROM centers")
        polling_stations=cursor.fetchall()
        if polling_stations:
            print("=== Registered Polling Stations ===")
            for stations in polling_stations:
                print(f"ID: {stations[0]} | Polling Station: {stations[1]}")
        else:
         print("No Registered Polling station found")
        
    except sqlite3.Error as e:
        print(f"Error loading the data: {e}")
    finally:
        connection.close()
        
        
def add_new_polling_station():
    try:
        connection=sqlite3.connect(config.file_path)
        cursor=connection.cursor()
        count = 0
        polling_station=input("Enter the polling stations, separated by comma: ")
        polling_stations=[station.strip() for station in polling_station.split(',')]
        for item in polling_stations:
            cursor.execute("SELECT EXISTS (SELECT 1 FROM centers WHERE center=?)",(item,))
            result=cursor.fetchone()[0]
            if result:
                print(f"{polling_station} already exists!")
            else:
                if len(item)>2: #Two character's can make a word
                    #Add the new polling station
                    cursor.execute("INSERT INTO centers(center) VALUES (?)",(item,))
                    connection.commit()
                    count+=1
        
        print(f"{count} new polling stations added successfully!")
    except sqlite3.Error as ex:
            print(f"Could not save the data: {ex}")
    finally:
        connection.close()
            
   
def deletePollingStation(id):
    try:
        connection=sqlite3.connect(config.file_path)
        cursor=connection.cursor()
        cursor.execute("DELETE FROM centers WHERE ID=?",(id))
        connection.commit()
        connection.close()  
    except sqlite3.Error as ex:
        print(f"An error occured {ex}")
        