import psycopg2
#establishing the connection
con = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="8389",
    host="localhost",
    port="5432"
)
#Creating a cursor object using the cursor() method
cursor = con.cursor()
# Create table
cursor.execute("Create table Employee (id int primary key, name varchar(20), salary int);")
# Insert data into table(static data)
cursor.execute("Insert into Employee (id, name, salary) values (1, 'John', 50000);")
print("Static Data inserted successfully")
cursor.execute("Insert into Employee (id, name, salary) values (2, 'Jane', 60000);")
print("Static Data inserted successfully")
# Commit your changes in the database
con.commit()
#closing the connection
con.close()
