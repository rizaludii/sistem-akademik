# AI Usage Log

Dokumen ini menjelaskan penggunaan AI dalam perancangan desain
UML Sistem Akademik serta revisi manual yang dilakukan untuk
memastikan desain sesuai prinsip OOP dan SOLID.

---

## Prompt 1 – Class Diagram Sistem Akademik
**Prompt:**
"Anda adalah software architect. Buat class diagram UML untuk sistem akademik
dengan User sebagai base class (Mahasiswa, Dosen, Admin, CalonMahasiswa),
serta class Course, Enrollment, Schedule, dan Grade.
Terapkan prinsip SOLID dan tampilkan dalam format Mermaid."

**Hasil AI:**
AI menghasilkan class diagram dasar dengan relasi inheritance dan
asosiasi antar class utama.

**Revisi Manual:**
- Menambahkan class `Schedule` dan `Grade`
- Memisahkan tanggung jawab `Enrollment` dan `Grade`
- Menambahkan method pada setiap class

**Alasan Revisi:**
- Menghindari God Object
- Menerapkan Single Responsibility Principle (SRP)
- Memperjelas relasi composition dan aggregation

---

## Prompt 2 – Validasi Prinsip SOLID
**Prompt:**
"Evaluasi class diagram berikut terhadap prinsip SOLID dan
berikan rekomendasi perbaikan desain."

**Hasil AI:**
AI menemukan potensi pelanggaran SRP pada class Enrollment.

**Revisi Manual:**
- Memindahkan pengelolaan nilai ke class `Grade`

**Alasan Revisi:**
- Memastikan setiap class memiliki satu tanggung jawab utama

---

## Prompt 3 – Use Case Diagram
**Prompt:**
"Buat use case diagram sistem akademik dengan aktor Mahasiswa,
Dosen, Admin Akademik, dan Calon Mahasiswa."

**Hasil AI:**
AI menghasilkan use case dasar tanpa system boundary.

**Revisi Manual:**
- Menambahkan boundary `Sistem Akademik`
- Memperjelas relasi antar use case

**Alasan Revisi:**
- Menyesuaikan dengan standar UML Use Case Diagram

---

## Prompt 4 – Sequence Diagram PMB
**Prompt:**
"Buat sequence diagram proses pendaftaran mahasiswa baru
lengkap dengan validasi data."

**Hasil AI:**
Sequence diagram hanya menampilkan alur sukses.

**Revisi Manual:**
- Menambahkan alternate flow untuk data tidak valid
- Menambahkan Database sebagai participant

**Alasan Revisi:**
- Membuat diagram lebih realistis
- Memenuhi rubrik penilaian

---

## Prompt 5 – Sequence Diagram KRS
**Prompt:**
"Buat sequence diagram validasi KRS dengan pengecekan
prasyarat, batas SKS, dan jadwal bentrok."

**Hasil AI:**
AI belum menampilkan proses notifikasi dan approval dosen.

**Revisi Manual:**
- Menambahkan aktor `Dosen PA`
- Menambahkan notifikasi dan status pending approval

**Alasan Revisi:**
- Sinkron dengan use case dan kebutuhan sistem akademik

---

## Kesimpulan
AI digunakan sebagai alat bantu awal dalam menghasilkan desain UML.
Seluruh hasil AI divalidasi dan direvisi secara manual untuk memastikan
kualitas desain sesuai prinsip OOP, SOLID, dan kebutuhan sistem akademik.
