# Sistem Informasi Akademik

## 📌 Deskripsi
Sistem Informasi Akademik Terpadu adalah aplikasi berbasis web yang dibangun menggunakan **FastAPI** dan **SQLAlchemy** untuk mengelola proses akademik perguruan tinggi secara terintegrasi.  
Sistem ini mencakup modul inti akademik serta beberapa modul pendukung yang disiapkan dalam bentuk skeleton agar dapat dikembangkan lebih lanjut.

Aplikasi ini dikembangkan sebagai **tugas UAS**, dengan fokus pada **arsitektur sistem, integrasi modul, dan penerapan konsep-konsep penting** seperti:
- Modular system
- Conflict detection algorithm
- Observer (Publisher–Subscriber) pattern
- REST API

---

## 🧩 Modul dalam Sistem

### 1️⃣ Modul PMB (Penerimaan Mahasiswa Baru)
- Pendaftaran calon mahasiswa
- Verifikasi dan penerimaan PMB
- Generate NIM otomatis
- Data PMB terintegrasi ke data Mahasiswa

### 2️⃣ Modul KRS
- Pengambilan KRS oleh mahasiswa
- Relasi mahasiswa dengan mata kuliah
- Terintegrasi dengan modul Jadwal

### 3️⃣ Modul Jadwal & Ruangan
- Manajemen jadwal perkuliahan
- Manajemen data ruangan dan kapasitas
- **Conflict Detection Algorithm**:
  - Bentrok ruangan
  - Bentrok dosen
  - Bentrok waktu
- **Observer Pattern**:
  - Notifikasi otomatis ke mahasiswa dan dosen saat jadwal berubah

### 4️⃣ Modul Nilai & Transkrip (Skeleton)
- Input nilai mahasiswa
- Menampilkan transkrip dan IPK (simulasi)

### 5️⃣ Modul Keuangan (SPP) (Skeleton)
- Cek tagihan SPP
- Pembayaran SPP (simulasi)

### 6️⃣ Modul Presensi QR Code (Skeleton)
- Generate QR Code presensi berdasarkan jadwal
- Presensi mahasiswa (simulasi scan QR)

---

## 🏗️ Arsitektur Sistem

- **Backend**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **API Style**: RESTful API
- **Documentation**: Swagger UI (`/docs`)
- **Design Pattern**:
  - Observer / Publisher–Subscriber
  - Modular architecture

Semua modul berjalan dalam **satu aplikasi** dan **satu database terpusat**.

---

## 📂 Struktur Folder

