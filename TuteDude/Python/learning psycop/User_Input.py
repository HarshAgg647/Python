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
cursor.execute("Create table IF NOT EXISTS Employee (id int primary key, name varchar(20), salary int);")
# Extracting data from table
print("The data in the table is:")
cursor.execute("SELECT * FROM Employee;")
row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()
# Commit your changes in the database
con.commit()
#closing the connection
con.close()