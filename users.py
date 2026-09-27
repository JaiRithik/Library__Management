from db_config import connect_db 
from datetime import date 
from book import books 
import os 
def signup( ): 
    print("\n============ Sign up ============\n") 
    while True: 
        user = input("Enter username: ").strip( ) 
        if not user : 
            print("Error: Username is required.") 
            input("Press Enter to continue...") 
            os.system('cls') 
 
            continue  
        if len(user) < 5: 
            print("Error: Username must be at least 5 characters long.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue 
        break 
    while True: 
        pwd = input("Enter password: ").strip( ) 
        if not pwd: 
            print("Error: Password is required.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue 
        if len(pwd) < 8: 
            print("Error: Password must be at least 8 characters long.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue 
        break 
    confirm_pwd = input("Confirm password: ").strip( ) 
    if pwd != confirm_pwd: 
        print("Error: Passwords do not match.") 
        input("Press Enter to return...") 
        os.system('cls') 
        return 
    while True: 
        full_name = input("Enter your full name: ").strip( ) 
        if not full_name : 
            print("Error: Full Name is required.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue 
        if len(full_name) < 5: 
            print("Error: Full Name must be at least 5 characters long.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue 
        break 
    while True: 
        email = input("Enter your email: ").strip( ) 
        if not email : 
            print("Error: Email is required.") 
            input("Press Enter to continue...") 
 
            os.system('cls') 
            continue 
        if not (email.endswith("@gmail.com") or email.endswith("@outlook.com")): 
            print("Error: Use a Gmail account or Outlook account to sign up.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue 
        break 
    while True: 
        phone = input("Enter your phone number: ").strip( ) 
        if not phone : 
            print("Error: Phone Number is required.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue 
        if not(phone.isdigit( )) or len(phone)!=10: 
            print("Error: Enter a valid phone Number") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue 
        break 
    while True: 
        address = input("Enter your address: ").strip( ) 
        if not address : 
            print("Error: Address is required.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue 
        break 
    conn = connect_db( ) 
    cursor = conn.cursor( ) 
    try: 
        cursor.execute("INSERT INTO members (username, password, full_name, email, phone, address, joined_date) VALUES (%s, %s, %s, %s, %s, %s, %s)", (user, pwd, full_name, email, phone, address , date.today( ))) 
        conn.commit( ) 
        print("\n=================================") 
        os.system('cls') 
        print("Sign Up Success: Account created.") 
    except : 
        print("Error: Could not create account. Try a different username.") 
        input("Press Enter to return...") 
        os.system('cls') 
        return 
 
    conn.close( ) 
def login( ): 
    print("\n============= Login =============\n") 
    user = input("Enter username: ").strip( ) 
    pwd = input("Enter password: ").strip( ) 
    if not user or not pwd: 
        print("Error: Both fields are required.") 
        input("Press Enter to return...") 
        os.system('cls') 
        return 
    conn = connect_db( ) 
    cursor = conn.cursor( ) 
    cursor.execute("SELECT * FROM members WHERE username=%s AND password=%s", (user, pwd)) 
    result = cursor.fetchone( ) 
    conn.close( ) 
    print("\n=================================") 
    os.system('cls') 
    if result: 
        print(f"\nLogin Success: Welcome, {user}!") 
        books(result[0])  
    else: 
        print("Login Failed: Invalid username or password.") 
        input("Press Enter to return...") 
        os.system('cls') 
        return
