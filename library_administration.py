from db_config import connect_db 
from utilies import add_book, remove_book, borrow_book, return_book 
import os 

ADMIN_ACCESS_CODE = os.getenv("ADMIN_ACCESS_CODE") 

def admin_menu( ): 
    print("Enter Admin Access Password to Proceed...") 
    admin_code = input('').strip( ) 
    if not ADMIN_ACCESS_CODE or admin_code != ADMIN_ACCESS_CODE: 
        print("\nAdmin Access DENIED") 
        input("Press Enter to return to the main menu...") 
        os.system('cls') 
        return 
    os.system('cls') 
    print("Welcome to the Library Administration System!") 
    while True: 
        print("\n=========== Admin Access ===========\n") 
        print("1. Admin Login") 
        print("2. Admin Sign Up") 
 
        print("3. Exit") 
        print("\n====================================\n") 
        choice = input("Enter choice: ").strip( ) 
        if choice == '1': 
            os.system('cls') 
            admin_login( ) 
        elif choice == '2': 
            os.system('cls') 
            admin_signup( ) 
        elif choice == '3': 
            os.system('cls') 
            break 
        else: 
            print("Invalid choice. Try again.") 
            input("Press Enter to continue...") 
            os.system('cls') 
        os.system('cls') 
def admin_signup( ): 
    from db_config import connect_db 
    from datetime import date 
    conn = connect_db( ) 
    cursor = conn.cursor( ) 
    while True: 
        print("\n=========== Admin Sign Up ===========\n") 
        print("Please enter the following details to create an admin account.") 
        admin_user = input("Enter username: ").strip( ) 
        if not admin_user : 
            print("Error: Username is required.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue  
        if len(admin_user) < 5: 
            print("Error: Username must be at least 5 characters long.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue 
        break      
    while True: 
        admin_pwd = input("Enter password: ").strip( ) 
        if not admin_pwd: 
            print("Error: Password is required.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue 
 
        if len(admin_pwd) < 8: 
            print("Error: Password must be at least 8 characters long.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue 
        admin_confirm_pwd = input("Confirm password: ").strip( ) 
        if admin_pwd != admin_confirm_pwd: 
            print("Error: Passwords do not match.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue 
        break 
    try: 
        cursor.execute(""" 
            INSERT INTO administration (username, password, created_on) 
            VALUES (%s, %s, %s) 
        """, (admin_user, admin_pwd, date.today( ))) 
        conn.commit( ) 
    except: 
        print(" Error: That username may already exist.") 
        input("Press Enter to continue...") 
        os.system('cls') 
    conn.close( ) 
    print("\n=================================\n") 
    input("Press Enter to return to the admin menu...") 
    os.system('cls') 
    print(f"Administrator {admin_user} Sign Up Successful!") 
def admin_login( ):  
    conn = connect_db( ) 
    cursor = conn.cursor( ) 
    while True: 
        print("\n============ Admin Login ============") 
        print("Please enter your admin credentials to access the library administration system.\n") 
        admin_user = input("Admin Username: ").strip( ) 
        admin_pwd = input("Admin Password: ").strip( ) 
        try: 
            cursor.execute("""SELECT * FROM administration  
            WHERE username = %s AND password = %s""",(admin_user, admin_pwd)) 
        except: 
            input("Invalid admin credentials. Press Enter to try again...") 
            os.system('cls') 
            continue 
        result = cursor.fetchone( )      
 
        if result: 
            os.system('cls') 
            print(f"\nWelcome, Administrator {admin_user}!") 
            admin_panel(admin_user, admin_pwd) 
            conn.close( ) 
            print("\n=================================") 
            break 
        else: 
            print("Invalid admin credentials.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue 
    conn.close( ) 
def admin_panel(user,pwd): 
    conn=connect_db( ) 
    cursor=conn.cursor( ) 
    while True: 
        print("\n========= Admin Panel ===========\n") 
        print("1. Add a Book") 
        print("2. Remove a Book") 
        print("3. Borrow a Book") 
        print("4. Return a Book") 
        print("5. Back to Main Menu") 
        print("\n=================================\n") 
        choice = input("Enter your choice: ").strip( ) 
        try: 
            if choice == '1': 
                os.system('cls') 
                add_book( )    
            elif choice == '2': 
                os.system('cls') 
                remove_book( ) 
            elif choice == '3': 
                os.system('cls') 
                member_username = input("Enter Member Username to borrow for: ").strip( ) 
                cursor.execute("SELECT id FROM members WHERE username = %s", (member_username,)) 
                member = cursor.fetchone( ) 
                if member: 
                    borrow_book(member[0]) 
                else: 
                    print("Member not found.") 
                    input("Press Enter to return...") 
 
            elif choice == '4': 
                os.system('cls') 
                member_username = input("Enter Member Username to return for: ").strip( ) 
                cursor.execute("SELECT id FROM members WHERE username = %s", (member_username,)) 
                member = cursor.fetchone( ) 
                if member: 
                    return_book(member[0]) 
                else: 
                    print("Member not found.") 
                    input("Press Enter to return...") 
            elif choice == '5': 
                return 
        except Exception as e: 
            print(f"An error occurred: {e}") 
            input("Press Enter to continue...") 
            continue
