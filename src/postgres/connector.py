import sqlalchemy
from sqlalchemy.orm import Session


# TODO: Update with config file
engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:root@localhost:5432/postgres")

session = Session(engine, autoflush=False)
