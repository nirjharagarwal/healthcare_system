import sqlite3
import os

db_path = "mydatabase.db"

def create_db():
    if not os.path.exists(db_path): 

        # Connect to the SQLite database
        # If 'mydatabase.db' does not exist, it will be created in the current directory.
        conn = sqlite3.connect('mydatabase.db')

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Create a new table named 'users' if it doesn't exist
        # The 'IF NOT EXISTS' clause ensures that the table is created only if it does not already exist.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                patient_name TEXT NOT NULL,
                insured_name TEXT,
                claim_no TEXT,
                address_line1 TEXT,
                address_line2 TEXT,
                employer_name TEXT,
                policy_number TEXT,
                notice_date DATE,
                provider_name TEXT,
                provider_number TEXT,
                payment_amount TEXT,
                service_desc TEXT
            )
        ''')

        # Commit the changes to the database
        conn.commit()

        # Close the connection to the database
        conn.close()

        print("Database and table created successfully (if they didn't exist already)!")

def insert_record(a,b,c,d,e,f,g,h,i,j,k,l):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (patient_name, insured_name, claim_no, address_line1, address_line2,employer_name, policy_number, notice_date, provider_name, provider_number, payment_amount, service_desc)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (a,b,c,d,e,f,g,h,i,j,k,l))

    conn.commit()
    conn.close()
    print("Data inserted successfully!")

def show_alldata():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Execute a SELECT statement
    cursor.execute('SELECT * FROM users')

    # Fetch all results from the executed query
    rows = cursor.fetchall()

    # Print the fetched data
    for row in rows:
        print(row)

    # Close the connection
    conn.close()