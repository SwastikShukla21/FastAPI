# # from sqlalchemy import create_engine
# # from sqlalchemy.ext.declarative import declarative_base
# # from sqlalchemy.orm import sessionmaker

# # SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:root@localhost/postgres'

# # engine = create_engine(SQLALCHEMY_DATABASE_URL)

# # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Base = declarative_base()

# # def get_db():
# #     db = SessionLocal()
# #     print("DB Connection Opened")
# #     try:
# #         yield db
# #     finally:
# #         db.close()

# from database import Database,Base
# import sqlalchemy

# DATABASE_URL = "postgresql://postgres:root@localhost/postgres"

# database = Database(DATABASE_URL)
# metadata = sqlalchemy.MetaData()

# users = sqlalchemy.Table(
#     "users",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("name", sqlalchemy.String),
#     sqlalchemy.Column("email", sqlalchemy.String, unique=True),
# )

# engine = sqlalchemy.create_engine(DATABASE_URL)
# metadata.create_all(engine)
