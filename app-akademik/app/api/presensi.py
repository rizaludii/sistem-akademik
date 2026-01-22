from fastapi import APIRouter

router = APIRouter()

# Generate QR Code (simulasi)
@router.get("/qr/{jadwal_id}")
def generate_qr(jadwal_id: int):
    return {
        "jadwal_id": jadwal_id,
        "qr_code": f"QR-JADWAL-{jadwal_id}"
    }

# Presensi mahasiswa
@router.post("/hadir")
def presensi_hadir(
    nim: str,
    jadwal_id: int
):
    return {
        "nim": nim,
        "jadwal_id": jadwal_id,
        "status": "HADIR"
    }
