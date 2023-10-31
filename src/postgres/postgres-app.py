import sqlalchemy
from models import Base

print("Migrate database")
engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:root@localhost:5432/postgres")
# Generate Code first table
print("Drop all table")
Base.metadata.drop_all(engine)

print("create all tables")
Base.metadata.create_all(engine)