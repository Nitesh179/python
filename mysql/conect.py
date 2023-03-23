import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Tout@52'
)

mycurser=mydb.cursor()
mycurser.execute('use pythondb')
# mycurser.execute('desc Persons')
# mycurser.execute('''CREATE TABLE Persons (
#     PersonID int,
#     LastName varchar(255),
#     FirstName varchar(255),
#     Address varchar(255),
#     City varchar(255)
# );''')

# mydb.commit()

print(mycurser.fetchall())