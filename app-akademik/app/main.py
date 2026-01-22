from fastapi import FastAPI
from app.database import Base, engine

# 🔴 WAJIB: import semua model
from app.models.mahasiswa import Mahasiswa
from app.models.pmb import PMB
from app.models.krs import KRS
from app.models.ruangan import Ruangan
from app.models.jadwal import Jadwal
from app.api import ruangan
from app.api import nilai, keuangan, presensi


# router
from app.api import pmb, krs, jadwal

app = FastAPI(title="Sistem Akademik")

app.include_router(pmb.router, prefix="/pmb", tags=["PMB"])
app.include_router(krs.router, prefix="/krs", tags=["KRS"])
app.include_router(jadwal.router, prefix="/jadwal", tags=["Jadwal & Ruangan"])
app.include_router(ruangan.router, prefix="/ruangan", tags=["Ruangan"])
app.include_router(nilai.router, prefix="/akademik", tags=["Nilai & Transkrip"])
app.include_router(keuangan.router, prefix="/keuangan", tags=["Keuangan"])
app.include_router(presensi.router, prefix="/presensi", tags=["Presensi QR"])

# 🔴 create_all PALING BAWAH
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "Sistem Akademik Berjalan"}
