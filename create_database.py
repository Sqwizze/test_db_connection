import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to my db
connection = psycopg2.connect(user="postgres", password="postgres")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# Create database
cursor = connection.cursor()
sql_create_database = cursor.execute('create database things_2')
# Close connection
cursor.close()
connection.close()
