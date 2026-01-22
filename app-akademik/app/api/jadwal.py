
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.jadwal import Jadwal
from app.schemas.jadwal import JadwalCreate
from app.services.conflict_detector import detect_schedule_conflict
from fastapi import Body

router = APIRouter()

@router.post("/tambah")
def tambah_jadwal(
    jadwal: JadwalCreate,
    db: Session = Depends(get_db)
):
    obj = Jadwal(**jadwal.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)

    konflik = detect_schedule_conflict(db.query(Jadwal).all())

@router.get("/")
def list_jadwal(db: Session = Depends(get_db)):
    return db.query(Jadwal).all()


@router.delete("/{jadwal_id}")
def hapus_jadwal(jadwal_id: int, db: Session = Depends(get_db)):
    jadwal = db.query(Jadwal).get(jadwal_id)
    if not jadwal:
        return {"error": "Jadwal tidak ditemukan"}

    db.delete(jadwal)
    db.commit()
    return {"message": "Jadwal dihapus"}

    return {
        "message": "Jadwal berhasil ditambahkan",
        "jadwal_id": obj.id,
        "conflicts": konflik
    }