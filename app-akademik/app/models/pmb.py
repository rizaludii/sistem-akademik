
from sqlalchemy import Column, Integer, String
from app.database import Base

class PMB(Base):
    __tablename__ = "pmb"
    id = Column(Integer, primary_key=True)
    nama = Column(String)
    prodi = Column(String)
    status = Column(String, default="MENUNGGU")
