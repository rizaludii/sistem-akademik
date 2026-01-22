
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.krs import KRS
from app.models.mahasiswa import Mahasiswa

router = APIRouter()

@router.post("/ambil")
def ambil_krs(nim: str, semester: int, db: Session = Depends(get_db)):
    mhs = db.query(Mahasiswa).filter(Mahasiswa.nim == nim).first()
    if not mhs:
        return {"error": "Mahasiswa tidak ditemukan"}
    krs = KRS(mahasiswa_id=mhs.id, semester=semester)
    db.add(krs)
    db.commit()
    return {"message": "KRS berhasil"}
