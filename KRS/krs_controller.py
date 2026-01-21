from database import connect_db

def isi_krs(nim, kode_mk):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS krs (id INTEGER PRIMARY KEY AUTOINCREMENT, nim TEXT, kode_mk TEXT)"
    )
    cursor.execute(
        "INSERT INTO krs (nim, kode_mk) VALUES (?, ?)",
        (nim, kode_mk)
    )
    conn.commit()
    conn.close()
    print("KRS berhasil disimpan")