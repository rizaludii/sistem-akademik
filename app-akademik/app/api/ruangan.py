from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.ruangan import Ruangan
from app.schemas.ruangan import RuanganCreate

router = APIRouter()

@router.post("/")
def tambah_ruangan(data: RuanganCreate, db: Session = Depends(get_db)):
    r = Ruangan(**data.dict())
    db.add(r)
    db.commit()
    db.refresh(r)
    return r

@router.get("/")
def list_ruangan(db: Session = Depends(get_db)):
    return db.query(Ruangan).all()

@router.delete("/{ruangan_id}")
def hapus_ruangan(ruangan_id: int, db: Session = Depends(get_db)):
    r = db.query(Ruangan).get(ruangan_id)
    if not r:
        return {"error": "Ruangan tidak ditemukan"}
    db.delete(r)
    db.commit()
    return {"message": "Ruangan dihapus"}
