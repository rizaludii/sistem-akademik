from pydantic import BaseModel

class JadwalCreate(BaseModel):
    mata_kuliah: str
    hari: str
    jam_mulai: str
    jam_selesai: str
    dosen: str
    ruangan_id: int
