from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/postgres", echo=True, pool_size=6)
engine.connect()
# print(engine)

metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer(), primary_key=True),
              Column('username', String(15)),
              Column('email', String(50))
              )

posts = Table('posts', metadata,
              Column('user_id', ForeignKey('users.id'), primary_key=True),
              Column('description', String(150))
              )

for _tables in metadata.tables:
    print(metadata.tables[_tables])

print(posts.columns)
print(users.columns)