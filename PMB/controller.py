from database import connect_db

def daftar_mahasiswa(nama, prodi):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS pendaftar (id INTEGER PRIMARY KEY AUTOINCREMENT, nama TEXT, prodi TEXT, status TEXT)"
    )
    cursor.execute(
        "INSERT INTO pendaftar (nama, prodi, status) VALUES (?, ?, ?)",
        (nama, prodi, "Menunggu")
    )
    conn.commit()
    conn.close()
    print("Pendaftaran berhasil")