import sqlite3

##connect to sqlite
connection=sqlite3.connect("student.db")

# Creating a cursor object using the  
# cursor() method 
cursor = connection.cursor() 
  
# Creating table 
table ="""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), 
SECTION VARCHAR(255));"""
cursor.execute(table) 
  
# Queries to INSERT records. 
cursor.execute('''INSERT INTO STUDENT VALUES ('Sakshi', 'Data Science', 'A')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Nithya', 'Data Science', 'B')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Soumya', 'Devops', 'C')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Taran', 'Data Science', 'C')''') 
  
# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 
  
# Commit your changes in the database     
connection.commit() 
  
# Closing the connection 
connection.close()