import sqlite3

conn = sqlite3.connect("database/company.db")

cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Employee(
               EmployeeID INTEGER PRIMARY KEY,
               Name TEXT,
               Department TEXT,
               Salary INTEGER)""")

employees = [
    (1,"Ram","IT",50000),
    (2,"Ravi","HR",70000),
    (3,"John","IT",60000),
    (4,"Sindhu","Data Science",80000),
    (5,"Priya","Finance",65000),
    (6,"Kiran","IT",75000),
    (7,"Anjali","HR",68000),
    (8,"Arjun","Finance",72000),
    (9,"Vikram","IT",90000),
    (10,"Sneha","Data Science",95000),
    (11,"Rahul","Finance",62000),
    (12,"Divya","HR",71000),
    (13,"Suresh","IT",85000),
    (14,"Pooja","Data Science",88000),
    (15,"Manoj","Finance",67000),
    (16,"Keerthi","HR",73000),
    (17,"Naveen","IT",81000),
    (18,"Akhil","Data Science",92000),
    (19,"Bhavana","Finance",70000),
    (20,"Teja","HR",76000)
]

cursor.executemany(
    "INSERT OR REPLACE INTO Employee Values(?,?,?,?)"
    ,employees)

conn.commit()

print('Data Inserted Successfully')


conn.close()
