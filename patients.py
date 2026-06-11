#                CLI  PATIENT MANAGER


import sqlite3

def get_connection():
    conn=sqlite3.connect("emergency.db")  #creates a database .conn is the connection object between py and db. A LINE.
    return conn 

def create_table():
    conn=get_connection()
    cursor=conn.cursor()  # cursor object that actually sends and receives SQL.  HOW YOU TAK=LK THROUGH THE LINE.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        city TEXT,
        condition TEXT
    )
""")
    # print("Table Created successfully")

    conn.commit()
    conn.close()

def add_patient(name,age,city,condition):
    conn=get_connection()
    cursor=conn.cursor()
    if condition in("critical","moderate","stable"):

        cursor.execute("INSERT INTO patients (name,age,city,condition) Values (?,?,?,?)",(name,age,city,condition))
        conn.commit()
        conn.close()

    else: 
        raise ValueError("Condition is invalid .")


def get_all_patients():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select * from  patients")
    rows=cursor.fetchall()
    for row in rows:
        id,name,age,city,condition=row
        print(f"id: {id}    |   name: {name}   |   age: {age}  |   city: {city}    |   condition: {condition}")

    conn.close()

def delete_patients_table():
    conn=get_connection()
    cursor=conn.cursor()
    # cursor.execute("truncate table patients")
    cursor.execute("delete from patients")  # delete the whole damn table .
    
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='patients'")  # resets the autoincrement to 1 again. 
    print("The table got deleted successfully.")
    conn.commit()
    conn.close()

def search_patient(name):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select * from patients where name = (?)",(name,))
    patient_detail=cursor.fetchone()
    if patient_detail is None:
        print("Patient not found.")
    else:

        id,name,age,city,condition=patient_detail
        print(f"id: {id}    |   name: {name}   |   age: {age}  |   city: {city}    |   condition: {condition}")

    conn.close()

def update_condition(name,new_condition):
    if new_condition not in("critical","moderate","stable"):
        raise ValueError("Invalid Condition .")
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE name = ?", (name,))
    if cursor.fetchone() is None:
        conn.close()
        raise ValueError(f"Patient {name} not found.")
    cursor.execute("update patients set condition=(?) where name=(?)",(new_condition,name))
    print(f"Updated the condition for {name}")


    conn.commit()
    conn.close()

def delete_patient_record(name):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("delete from patients where name =(?)",(name,))
    print(f"Deleted the patient record for {name}") 

    conn.commit()
    conn.close()

def main():
    create_table()

    while True:
        print("\n--- Patient Tracker ---")
        print("1. Add patient")
        print("2. Search patient by name ")
        print("3. Update patient condition")
        print("4. Delete patient")
        print("5. Show all patients")
        print("6. Exit")
       
        
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            city = input("City: ")
            condition = input("Condition: ")
            try:
                add_patient(name,age,city,condition)
            
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            name = input("Name: ")
            search_patient(name)
           
        elif choice == "3":
            name = input("Name: ")
            condition = input("Condition: ")
            update_condition(name,condition)
           
        elif choice == "4":
            name = input("Name: ")
            delete_patient_record(name)
          
           
        elif choice == "5":
            get_all_patients()
            
          
        elif choice == "6":
           
            print("Exiting !")
            break

        else:
            print("Invalid Choice !")

main()
        

# delete_patients_table()
