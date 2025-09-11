from sqlalchemy import Column, String, Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    surname = Column(String)
    country = Column(String)
    contact_number = Column(String)
    mobile_number = Column(String, nullable=True)
    password_hash = Column(String)
    marketing_opt_in = Column(Boolean, default=False)