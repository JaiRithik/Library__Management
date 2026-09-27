from utilies import borrow_book, return_book 
import os 
def books(member_id): 
    while True: 
        print("\n===== Borrow/Return System ======\n") 
        print("1. Borrow a Book") 
        print("2. Return a Book") 
        print("3. Logout") 
        print("\n=================================") 
        choice = input("Enter your choice (1-3): ").strip( )         
        if choice == "1": 
                os.system('cls') 
                borrow_book(member_id)             
        elif choice=="2": 
                os.system('cls') 
                return_book(member_id)                 
        elif choice == "3": 
                    print("Logging out...") 
                    os.system('cls')     
                    break 
        else: 
                print("Invalid choice. Please enter 1, 2, or 3.") 
                continue
