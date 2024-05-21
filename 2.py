# a. Import the appropriate connector in # Statement 1.
import mysql.connector

# b. Pass the required parameters for connector() in # Statement 2.
mydb = mysql.connector.connect(
    host="localhost",    # Assuming your database is on the local machine
    user="root",
    passwd="Eren_Jeager1",
    database="testdatabase"
)

cur = mydb.cursor()

while True:
    d = input("Enter employee id = ")
    n = input("Enter employee name = ")
    s = int(input("Enter salary = "))

#   c. Write SQL command to insert the record at # Statement 3.
    sql = "INSERT INTO Employee (Emp_Id, EName, Salary) VALUES (%s, %s, %s)"
    
#   d. Write the command to execute the values stored in row variable at # Statement 4.
    values = (d, n, s)
    cur.execute(sql, values)
    
    mydb.commit()  # You need to commit the changes to the database

    print("Record inserted successfully..")

    c = input("Do you want to enter more records? (Y/N) = ")
    if c.upper() == 'N':
        break

cur.close()
mydb.close()


