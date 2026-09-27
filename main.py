from users import login, signup 
from library_administration import admin_menu 
from db_config import db_setup 
import os 
def main( ): 
    db_setup( ) 
    while True: 
        try: 
            print("\n=== Library Management System ===") 
            print("\n1. Login") 
            print("2. Sign Up") 
            print("3. Library Administration System") 
            print("4. Exit") 
            print("\n=================================") 
            choice = input("\nSelect an option (1-4): ").strip( ) 
            if choice == '1': 
                os.system('cls') 
                login( ) 
            elif choice == '2': 
                os.system('cls') 
                signup( ) 
            elif choice == '3': 
                os.system('cls') 
                admin_menu( ) 
            elif choice == '4': 
                os.system('cls') 
                print("Goodbye!") 
                break 
            else: 
                print("Invalid choice. Try again.") 
                input("Press Enter to continue...") 
                os.system('cls') 
                continue 
        except: 
            os.system('cls') 
            continue   
main( )
