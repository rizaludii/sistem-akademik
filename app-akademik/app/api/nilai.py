from fastapi import APIRouter
from typing import List

router = APIRouter()

# Input nilai oleh dosen
@router.post("/nilai")
def input_nilai(
    nim: str,
    mata_kuliah: str,
    nilai: str
):
    return {
        "message": "Nilai berhasil disimpan",
        "nim": nim,
        "mata_kuliah": mata_kuliah,
        "nilai": nilai
    }

# Lihat transkrip mahasiswa
@router.get("/transkrip/{nim}")
def lihat_transkrip(nim: str):
    return {
        "nim": nim,
        "ipk": 3.75,
        "detail": [
            {
                "mata_kuliah": "Kalkulus",
                "nilai": "A"
            },
            {
                "mata_kuliah": "Algoritma",
                "nilai": "A-"
            }
        ]
    }
