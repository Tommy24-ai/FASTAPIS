from sqlalchemy import create_engine,String
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

Database_url="sqlite:///mydatabase.db"

engine=create_engine(Database_url,echo=True)

class Base(DeclarativeBase):
    pass
class user(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(50))
    email:Mapped[str]=mapped_column(String(50),unique=True)
print("Creating database and tables...")
Base.metadata.create_all(engine)
print("Database and tables created successfully!")


