
from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base

class KRS(Base):
    __tablename__ = "krs"
    id = Column(Integer, primary_key=True)
    mahasiswa_id = Column(Integer, ForeignKey("mahasiswa.id"))
    semester = Column(Integer)
