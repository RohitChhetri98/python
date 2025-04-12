# DATABASE CRUD OPERATIONS

import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="school")
db = con.cursor()

def menu():
    print("DATABASE CRUD OPERATIONS")
    print("MENU: \n 1. Insert Student \n 2. Display Students \n 3. Search Student by Class \n 4. Search Student by Name \n 5. Delete Student \n 6. Update Student \n 0. Exit")
    ch = int(input("Enter choice: "))
    return ch

def insert_student(name, cls, sec, sex):
    sql = "insert into students values (DEFAULT, %s, %s, %s, %s)"
    params = (name, cls, sec, sex)
    db.execute(sql, params)
    con.commit
    print(db.rowcount," record(s) inserted with roll id: ", db.lastrowid)

def print_students(students):
    print(len(students)," student(s) found.")
    headers = ['ID', 'NAME', 'CLASS', 'SEX']
    print(f"{headers[0]:<5} |{headers[1]:<20} |{headers[2]:<10} |{headers[3]:<8}")
    print("-"*50)
    for x in students:
        if(x[4].lower()=="m"):
            sex = "Male"
        else:
            sex = "Female"
        print(f"{x[0]:<5} |{x[1].title():<20} |{x[2]:<2} {x[3].upper():<7} |{sex:<8}")

def get_students():
    sql = "select * from students"
    db.execute(sql)
    students = db.fetchall()
    print("Displaying all students")
    print_students(students)

def get_class_students(cls):
    sql = "select * from students where class=%s"
    params = (cls,)
    db.execute(sql, params)
    students = db.fetchall()
    print("Displaying all students in class ",cls)
    print_students(students)

def search_student(name):
    sql = "select * from students where name like %s"
    params = (f"%{name}%",)
    db.execute(sql, params)
    students = db.fetchall()
    print("Displaying all students that match: ")
    print_students(students)

def search_roll(roll):
    sql = "select * from students where id=%s"
    params = (roll,)
    db.execute(sql, params)
    students = db.fetchall()
    if(db.rowcount>0):
        print("Student Details: ")
        print_students(students)
    else:
        print("Student not found.")

def delete_student(roll):
    search_roll(roll)
    sql = "delete from students where id=%s"
    params = (roll,)
    db.execute(sql, params)
    con.commit()
    print(db.rowcount, " record(s) affected.")

def update_student(roll, name, cls, sec, sex):
    search_roll(roll)
    sql = "update students set name=%s, class=%s, sec=%s, sex=%s where id=%s"
    params = (name, cls, sec, sex, roll,)
    db.execute(sql, params)
    con.commit()
    print(db.rowcount, " record(s) affected.")
    search_roll(roll)

def driver_program():
    while(True):
        ch = menu()
        if(ch==1):
            name = input("Enter name: ")
            cls = input("Enter class: ")
            sec = input("Enter section: ")
            sex = input("Enter sex: ")
            insert_student(name, cls, sec, sex)
        elif(ch==2):
            get_students()
        elif(ch==3):
            cls = input("Enter class: ")
            get_class_students(cls)
        elif(ch==4):
            name = input("Enter name: ")
            search_student(name)
        elif(ch==5):
            roll = input("Enter roll number to delete: ")
            sure = input("Are you sure you want to delete? (Y/N) : ")
            if(sure.lower()=="y"):
                delete_student(roll)
            else:
                print("Operation cancelled.")
        elif(ch==6):
            roll = input("Enter roll number to update: ")
            sure = input("Are you sure you want to update? (Y/N) : ")
            if(sure.lower()=="y"):
                name = input("Enter name: ")
                cls = input("Enter class: ")
                sec = input("Enter section: ")
                sex = input("Enter sex: ")
                update_student(roll, name, cls, sec, sex)
            else:
                print("Operation cancelled.")
        elif(ch==0):
            break
        else:
            print("Wrong choice.")
        ch = input("Enter any key to continue...")
        

driver_program()
con.commit()
        
