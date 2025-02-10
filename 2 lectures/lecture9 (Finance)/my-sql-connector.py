#code example taken from:
#https://dev.mysql.com/doc/connector-python/en/

# This requires setting up a user and password when installing MySQL.

import mysql.connector

try:
    cnx = mysql.connector.connect(user="root",
                                  password="your-password",
                                  host="127.0.0.1",
                                  port="3306",
                                  database='world')
except mysql.connector.Error as err:
  if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

#instantiate a cursor object in order to execute SQL statements:
cursor = cnx.cursor()
query = "select Name,Population from country"
cursor.execute(query)
for name, population in cursor:
    print(name, population)

cursor.close()
cnx.close()
