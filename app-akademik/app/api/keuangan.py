from fastapi import APIRouter

router = APIRouter()

# Tagihan SPP
@router.get("/spp/{nim}")
def cek_tagihan(nim: str):
    return {
        "nim": nim,
        "tagihan": 3500000,
        "status": "BELUM LUNAS"
    }

# Pembayaran SPP
@router.post("/spp/bayar")
def bayar_spp(
    nim: str,
    jumlah: int
):
    return {
        "nim": nim,
        "jumlah": jumlah,
        "status": "LUNAS"
    }
