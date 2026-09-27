import mysql.connector 
import os 
from dotenv import load_dotenv 

load_dotenv() 

DB_HOST = os.getenv("DB_HOST", "localhost") 
DB_USER = os.getenv("DB_USER", "root") 
DB_PASSWORD = os.getenv("DB_PASSWORD") 
DB_NAME = os.getenv("DB_NAME", "library_management") 

def connect_db( ): 
    return mysql.connector.connect( 
    host=DB_HOST, 
    user=DB_USER, 
    password=DB_PASSWORD, 
    database=DB_NAME 
) 
def db_setup( ): 
    try: 
        conn = mysql.connector.connect( 
        host=DB_HOST, 
        user=DB_USER, 
        password=DB_PASSWORD) 
        cursor = conn.cursor( ) 
        cursor.execute("SHOW DATABASES LIKE 'library_management'") 
        exists = cursor.fetchone( ) 
        if not exists: 
            print("Setting up database for the first time...") 
            with open("schema.sql", "r") as f: 
                sql_commands = f.read( ) 
            for command in sql_commands.split(';'): 
                cmd = command.strip( ) 
                if cmd: 
                    cursor.execute(cmd) 
            conn.commit( ) 
            print("Database initialized successfully.\n") 
            input("Press Enter to Initalize the Library Management System...") 
            os.system('cls') 
    except Exception as e: 
        print(f" Database initialization failed: {e}") 
    conn.close( )
