from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Jadwal(Base):
    __tablename__ = "jadwal"

    id = Column(Integer, primary_key=True)
    mata_kuliah = Column(String)
    hari = Column(String)
    jam_mulai = Column(String)
    jam_selesai = Column(String)
    dosen = Column(String)
    ruangan_id = Column(Integer, ForeignKey("ruangan.id"))
