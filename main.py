import os
import config
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import sqlite3

#Import modules for new and existing election
from new_election import NewElection
from existing_election import open_existing_election
from polling_station import add_new_polling_station,view_polling_stations,deletePollingStation
from portfolios import view_portfolios,add_new_portfolio



def main():
    print("")
    print("=== Phewcliq Election System ===")
    print("""
    1. Create New Election
    2. Open Existing Election
    3. Exit
    """)

    choice=input("Enter your choice (1/2/3):")

    if choice=="1":
        #Call the New Election Class
        NewElection().start()
        perform_action()
        
    elif choice=="2":
        root=Tk()
        #Let user choose an existing election file
        root.withdraw() #Hide the Tkinter's root window
        file_path=askopenfilename(
            title="Open Existing Election File",
            filetypes=[("SQLite Database","*.db"),("All Files","*.*")]
        )
        if file_path:
            open_existing_election(file_path)
            perform_action()
        else:
            print("No file selected. Returing to main menu")

    elif choice=="3":
        print("Exiting program")
    else:
        print("Invalid choice. Please try again.")
        main()


def perform_action():
      #Open the existing file menu
    while True:
        print("=== Main Menus ===")
        print("""
              1. Polling Stations
              2. Portfolios
              3. Aspirants
              4. Codes
              5. Settings 
              6. Exit    
              """)
        menu_selected=input("Enter your choice ( 1/2/3/4/5/6): ")
        if menu_selected=="6":
            print("Exiting Program")
            break
        
        elif menu_selected=="1":
            while True:
                print("""
                === Polling Station Menu ===
                1. View Registered Stations
                2. Create New Station
                3. Back to Main Menu
                """)
                ps_choice=input("Enter your choice (1/2/3): ")
                if ps_choice=="3":
                    break #Go back to Main menu
                elif ps_choice=="1":
                    #display the registered stations
                    view_polling_stations()
                    
                elif ps_choice=="2":
                    add_new_polling_station()
                    while True:
                        print("""
                        === Polling Station Menu ===
                        1. Delete Polling Station
                        2. Create New Station
                        3. Back to Main Menu
                        """)
                        response=input("Enter your choice (1/2/3)")
                        if response=="3":
                            break
                        elif response=="2":
                            add_new_polling_station()
                        elif response=="1":
                            deletePollingStation()
                            
        elif menu_selected=="2":
            while True:
                #Retrieve or add or delete portfolio
                print("""
                    Choose to View, Add, or delete Portfolios
                    ____________________________________________
                    1. View registered portfolio
                    2. Add New Portfolio
                    3. Back to Main Menu
                    """)
                portfolio_action=input("Enter your choice (1/2/3) ")
                if portfolio_action=="3":
                    break
                
                elif portfolio_action=="1":
                    view_portfolios()
                                        
                elif portfolio_action=="2":
                    #Add new portfolio
                    user_portfolios=input("""Read this information carefully
                    1. If this portfolio will be voted for by every voter, the category you must enter
                    is 'General'.
                    2. If you have specific or special portfolios for special delegates, you must type
                    the special delegate's group. An example is (Gold House -> for voters from Gold house)
                    
                    3. Enter the Category and the Portfolio, separated by comma: 
                    4. To enter more than one portfolio, separate each new portfolio with colon (:) 
                     """)
                    
                    multipleportfolios=[portfolios.strip() for portfolios in user_portfolios.split(':')]
                    for singleportfolio in multipleportfolios:
                        result=[portfolio.strip() for portfolio in singleportfolio.split(',')]
                        if len(result)!=2: #Ensure the user input has two parts
                            print(f"Invalid input format: '{singleportfolio}'. Skipping...")
                        continue
                    add_new_portfolio(result[0],result[1])
                    view_portfolios #Display the portfolio(s) added
        elif menu_selected=="5":
            print("""
                Enter the settings in the format below (separated by comma):
                Name of Instution,Name for the Election,Year of Election,Number of Voters,EC Password,Phone Number
                """)
            user_input=input()
            sort_input=[item.strip() for item in user_input.split(",")]
            print(sort_input)
            for item in sort_input:
                settings(item[0],item[1],item[2],item[3],item[4],item[5])
            
            
            
def settings(Institution_name,Election_name,Election_year,Number_voters,EC_password,Phone_number):
    try:
        connection=sqlite3.connect(config.file_path)
        cursor=connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM settings")
        result=cursor.fetchone()[0]
        if result=="1":
            print("Setting's data already exists. You can not overwrite")
        else:
            cursor.execute("INSERT INTO settings(Institution_name,Election_name,Election_year,Number_voters,EC_password,Phone_number) VALUES(?,?,?,?,?,?)",(Institution_name,Election_name,Election_year,Number_voters,EC_password,Phone_number))                
            print()
            print("Settings saved successfully!")
    except sqlite3.Error as ex:
        print(f"Eror occured: {ex}")
    finally:
       connection.close()
       
       
if __name__=="__main__":
    main()