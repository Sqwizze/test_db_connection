from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/postgres", echo=True, pool_size=6)
engine.connect()

print(engine)
