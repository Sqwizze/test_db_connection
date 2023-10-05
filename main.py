from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, insert
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to my db
# connection = psycopg2.connect(user="postgres", password="postgres")
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#
# cursor = connection.cursor()
# sql_create_database = cursor.execute('create database things_2')
#
# cursor.close()
# connection.close()

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/things_2", echo=True,
                       pool_size=6, max_overflow=10)
engine.connect()
print(engine)

# Metadata - содержит всю информацию о БД и таблицах
metadata = MetaData()
# Создаем таблицы и колонки

users = Table('users', metadata,
              Column('id', Integer(), primary_key=True),
              Column('username', String(15)),
              Column('email', String(50))
              )

posts = Table('posts', metadata,
              Column('user_id', ForeignKey('users.id')),
              Column('description', String(15))
              )

# Вывод таблиц
# for _tables in metadata.tables:
#     print(metadata.tables[_tables])

# Вывод колонок
# print(posts.columns)
# print(users.columns)

# Создаем в БД таблицы и колонки
metadata.create_all(engine)

# Insert параметров в ячейки таблицы users
ins_users = insert(users).values(
    username='TEST',
    email='test@mail.com'
)

ins_posts = insert(posts).values(
    description='test_desc'
)

# Вывод наших созданных параметров
# print(ins.compile().params)

_connect = engine.connect()
result = _connect.execute(ins_users)
print(result.rowcount)
result = _connect.execute(ins_posts)

# Select
s_1 = users.select()
s_2 = posts.select()

result = _connect.execute(s_1)
print(result.fetchall())
result = _connect.execute(s_2)
print(result.fetchall())
