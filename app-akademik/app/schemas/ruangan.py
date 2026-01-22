from pydantic import BaseModel

class RuanganCreate(BaseModel):
    nama: str
    kapasitas: int
