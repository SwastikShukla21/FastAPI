# from database import Base
# from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text


# class Post(Base):
#     __tablename__ = "posts"

#     id = Column(Integer,primary_key=True,nullable=False)
#     title = Column(String,nullable=False)
#     content = Column(String,nullable=False)
#     published = Column(Boolean, server_default='TRUE')
#     created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

from databases import Database
import sqlalchemy

DATABASE_URL = "postgresql://postgres:root@localhost/postgres"

database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
