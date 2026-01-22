from sqlalchemy import Column, Integer, String
from app.database import Base

class Ruangan(Base):
    __tablename__ = "ruangan"

    id = Column(Integer, primary_key=True)
    nama = Column(String, unique=True)
    kapasitas = Column(Integer)