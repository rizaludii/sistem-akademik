
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.pmb import PMB
from app.models.mahasiswa import Mahasiswa
import random

router = APIRouter()

def generate_nim():
    return "2026" + str(random.randint(1000,9999))

@router.post("/daftar")
def daftar_pmb(nama: str, prodi: str, db: Session = Depends(get_db)):
    pmb = PMB(nama=nama, prodi=prodi)
    db.add(pmb)
    db.commit()
    return {"message": "Pendaftaran PMB berhasil"}

@router.post("/terima/{pmb_id}")
def terima_pmb(pmb_id: int, db: Session = Depends(get_db)):
    pmb = db.query(PMB).get(pmb_id)
    pmb.status = "DITERIMA"
    mhs = Mahasiswa(nim=generate_nim(), nama=pmb.nama, prodi=pmb.prodi)
    db.add(mhs)
    db.commit()
    return {"message": "PMB diterima", "nim": mhs.nim}
