# PROPOSAL PROYEK AKHIR
# KALKULATOR GEOMETRI BERBASIS PYTHON

**Program Menghitung Luas dan Keliling Bangun Datar**

### Identitas Kelompok

| No. | Nama Anggota | NIM |
|---|---|---|
| 1 | Aulia Safitri | 2225250190 |
| 2 | Siti Solehah | 2225250058 |
| 3 | Ayu Syarifatu Zahra | 2225250043 |
| 4 | Zahwa Ajmala Fitriani | 2225250191 |

**Program Studi:** Pendidikan Matematika

**Mata Kuliah:** Algoritma dan Pemrograman

**Universitas:** Universitas Sultan Ageng Tirtayasa

---

## 1. Latar Belakang

Geometri merupakan salah satu materi dalam matematika yang mempelajari bentuk, ukuran, luas, dan keliling suatu bangun. Dalam kehidupan sehari-hari, konsep geometri sering digunakan, misalnya untuk menghitung luas tanah, ukuran ruangan, dan keliling suatu benda.

Namun, dalam proses perhitungan, terkadang masih terdapat kesalahan ketika menggunakan rumus atau melakukan perhitungan secara manual. Oleh karena itu, diperlukan sebuah program sederhana yang dapat membantu mempermudah proses perhitungan geometri.

Berdasarkan hal tersebut, kelompok kami merancang proyek **Kalkulator Geometri Berbasis Python**. Program ini dibuat untuk menghitung luas dan keliling beberapa bangun datar, yaitu persegi, persegi panjang, segitiga, dan lingkaran. Program ini diharapkan dapat membantu pengguna melakukan perhitungan dengan lebih mudah, cepat, dan tepat sekaligus menjadi sarana untuk menerapkan pemrograman Python dalam menyelesaikan permasalahan matematika.

## 2. Pengguna dan Tujuan Proyek

### A. Pengguna

Program Kalkulator Geometri ditujukan untuk:
1. Mahasiswa atau pelajar yang sedang mempelajari materi geometri.
2. Pengguna yang ingin menghitung luas dan keliling bangun datar.
3. Siapa saja yang membutuhkan alat bantu perhitungan geometri sederhana.

### B. Tujuan

Tujuan pembuatan program ini adalah:
1. Mempermudah pengguna dalam menghitung luas dan keliling bangun datar.
2. Mengurangi kesalahan dalam perhitungan manual.
3. Menerapkan konsep matematika ke dalam pemrograman Python.
4. Melatih penggunaan fungsi, percabangan, perulangan, dan validasi input dalam Python.

## 3. Ruang Lingkup Proyek

Program Kalkulator Geometri Berbasis Python memiliki ruang lingkup sebagai berikut:

1. Program dijalankan melalui terminal atau console menggunakan bahasa pemrograman Python.
2. Program menyediakan pilihan empat bangun datar, yaitu persegi, persegi panjang, segitiga, dan lingkaran.
3. Program dapat menghitung luas dan keliling dari setiap bangun datar yang dipilih.
4. Pengguna memasukkan ukuran sesuai dengan bangun datar yang dipilih.
5. Program menampilkan hasil perhitungan berdasarkan rumus matematika yang sesuai.
6. Program melakukan validasi input agar nilai ukuran tidak boleh nol atau negatif.
7. Program menyediakan pilihan untuk melakukan perhitungan kembali atau mengakhiri program.

Program ini hanya berfokus pada perhitungan bangun datar dan tidak mencakup bangun ruang maupun tampilan grafis (GUI).

## 4. Kebutuhan Proyek

### A. Kebutuhan Fungsional

Kebutuhan fungsional merupakan fitur atau fungsi yang harus tersedia dalam program. Adapun kebutuhan fungsional Kalkulator Geometri adalah:

1. Program menampilkan menu pilihan bangun datar.
2. Program menerima input berupa ukuran bangun datar dari pengguna.
3. Program dapat menghitung luas dan keliling persegi.
4. Program dapat menghitung luas dan keliling persegi panjang.
5. Program dapat menghitung luas dan keliling segitiga.
6. Program dapat menghitung luas dan keliling lingkaran.
7. Program menampilkan hasil perhitungan sesuai pilihan pengguna.
8. Program menyediakan pilihan untuk mengulang perhitungan atau keluar dari program.

### B. Kebutuhan Nonfungsional

Kebutuhan nonfungsional merupakan ketentuan mengenai kualitas dan cara kerja program. Kebutuhan nonfungsional program ini adalah:

1. Program dibuat menggunakan bahasa pemrograman Python.
2. Program dapat dijalankan melalui terminal atau console di Visual Studio Code.
3. Program memiliki tampilan menu yang sederhana dan mudah dipahami.
4. Program menggunakan rumus matematika yang tepat.
5. Program dapat memberikan pesan kesalahan apabila pengguna memasukkan nilai yang tidak valid.
6. Program dapat dijalankan dengan baik tanpa memerlukan koneksi internet.

## 5. IPO (Input, Process, Output)

IPO merupakan gambaran mengenai masukan (input), proses pengolahan data (process), dan hasil yang ditampilkan (output) dalam program.

| Bangun Datar | Input | Process | Output |
|---|---|---|---|
| Persegi | Panjang sisi | Luas = sisi × sisi; Keliling = 4 × sisi | Hasil luas dan keliling persegi |
| Persegi Panjang | Panjang dan lebar | Luas = panjang × lebar; Keliling = 2 × (panjang + lebar) | Hasil luas dan keliling persegi panjang |
| Segitiga | Alas, tinggi, dan tiga sisi | Luas = ½ × alas × tinggi; Keliling = sisi 1 + sisi 2 + sisi 3 | Hasil luas dan keliling segitiga |
| Lingkaran | Jari-jari | Luas = π × r × r; Keliling = 2 × π × r | Hasil luas dan keliling lingkaran |

Sebelum melakukan perhitungan, program akan memeriksa apakah nilai input valid. Jika nilai yang dimasukkan tidak sesuai, program akan menampilkan pesan kesalahan.

## 6. Algoritma dan Pseudocode

### A. Algoritma Program

Langkah-langkah kerja program Kalkulator Geometri adalah:

1. Mulai program.
2. Tampilkan menu pilihan bangun datar.
3. Pengguna memilih bangun datar yang ingin dihitung.
4. Program meminta pengguna memasukkan ukuran sesuai bangun datar yang dipilih.
5. Program memeriksa apakah input bernilai positif dan valid.
6. Jika input valid, program menghitung luas dan keliling menggunakan rumus yang sesuai.
7. Program menampilkan hasil perhitungan.
8. Program menanyakan apakah pengguna ingin melakukan perhitungan kembali.
9. Jika pengguna memilih ya, program kembali ke menu utama.
10. Jika pengguna memilih tidak, program selesai.

### B. Pseudocode

```text
MULAI

ULANGI
    Tampilkan menu bangun datar
    Masukkan pilihan pengguna

    JIKA pilihan = persegi
        Masukkan sisi
        Periksa sisi harus positif
        Hitung luas dan keliling

    JIKA pilihan = persegi panjang
        Masukkan panjang dan lebar
        Periksa panjang dan lebar harus positif
        Hitung luas dan keliling

    JIKA pilihan = segitiga
        Masukkan alas, tinggi, dan tiga sisi
        Periksa semua ukuran harus positif
        Periksa jumlah dua sisi harus lebih besar
        dari sisi lainnya
        Hitung luas dan keliling

    JIKA pilihan = lingkaran
        Masukkan jari-jari
        Periksa jari-jari harus positif
        Hitung luas dan keliling

    Tampilkan hasil perhitungan
    Tanyakan apakah ingin menghitung kembali

SAMPAI pengguna memilih tidak

SELESAI
```

## 7. Struktur Program dan Pembagian Modul

Program akan disusun dalam beberapa file agar setiap bagian memiliki fungsi masing-masing. Struktur folder proyek direncanakan sebagai berikut:

```text
proyek-akhir-kalkulator-geometri/
│
├── README.md
├── proposal.md
├── .gitignore
│
├── src/
│   ├── main.py
│   ├── persegi.py
│   ├── persegi_panjang.py
│   ├── segitiga.py
│   ├── lingkaran.py
│   └── utilitas.py
│
└── tests/
    └── test_case.md
```

### Penjelasan File

1. **main.py**: Menjalankan program utama dan menampilkan menu pilihan.
2. **persegi.py**: Berisi fungsi untuk menghitung luas dan keliling persegi.
3. **persegi_panjang.py**: Berisi fungsi untuk menghitung luas dan keliling persegi panjang.
4. **segitiga.py**: Berisi fungsi untuk menghitung luas dan keliling segitiga.
5. **lingkaran.py**: Berisi fungsi untuk menghitung luas dan keliling lingkaran.
6. **utilitas.py**: Berisi fungsi pendukung, seperti validasi input.
7. **test_case.md**: Berisi daftar skenario pengujian program.
8. **README.md**: Berisi informasi dan petunjuk penggunaan proyek.
9. **proposal.md**: Berisi rancangan proyek akhir.
10. **.gitignore**: Berisi daftar file atau folder yang tidak perlu dimasukkan ke GitHub.

## 8. Struktur Data yang Digunakan

Dalam pembuatan program Kalkulator Geometri, terdapat beberapa jenis tipe data yang digunakan, yaitu:

1. **Integer (int)**  
   Digunakan untuk menyimpan pilihan menu yang dimasukkan oleh pengguna.

2. **Float**  
   Digunakan untuk menyimpan ukuran bangun datar, seperti sisi, panjang, lebar, alas, tinggi, jari-jari, serta hasil perhitungan luas dan keliling.

3. **String (str)**  
   Digunakan untuk menyimpan data berupa teks, seperti pilihan menu dan jawaban pengguna ketika ditanya apakah ingin melakukan perhitungan kembali.

4. **Boolean (bool)**  
   Digunakan untuk menyimpan kondisi benar atau salah, misalnya untuk menentukan apakah input yang dimasukkan valid.

Penggunaan tipe data tersebut disesuaikan dengan kebutuhan program agar proses pengolahan data dapat berjalan dengan baik.

## 9. Rencana Pengujian Program

Pengujian dilakukan untuk memastikan setiap fitur program dapat berjalan sesuai dengan tujuan. Berikut adalah beberapa skenario pengujian yang direncanakan:

| No. | Skenario Pengujian | Input | Hasil yang Diharapkan |
|---|---|---|---|
| 1 | Menghitung persegi | Sisi = 5 | Luas = 25 dan keliling = 20 |
| 2 | Menghitung persegi panjang | Panjang = 8, lebar = 4 | Luas = 32 dan keliling = 24 |
| 3 | Menghitung segitiga | Alas = 6, tinggi = 4, sisi = 5, 5, 6 | Luas = 12 dan keliling = 16 |
| 4 | Menghitung lingkaran | Jari-jari = 7 | Luas = 154 dan keliling = 44 (menggunakan π = 22/7) |
| 5 | Memasukkan nilai negatif | Sisi = -5 | Program menampilkan pesan kesalahan |
| 6 | Memasukkan nilai nol | Jari-jari = 0 | Program menampilkan pesan kesalahan |
| 7 | Memasukkan sisi segitiga tidak valid | Sisi = 2, 3, 6 | Program menolak input karena tidak memenuhi syarat segitiga |

Pengujian dilakukan dengan membandingkan hasil yang ditampilkan program dengan hasil perhitungan berdasarkan rumus matematika. Program dinyatakan berjalan sesuai harapan apabila menghasilkan perhitungan yang benar dan dapat menolak input yang tidak valid.

## 10. Pembagian Tugas Anggota Kelompok

Pembagian tugas dilakukan agar setiap anggota kelompok memiliki tanggung jawab masing-masing dalam proses perancangan dan pembuatan program.

| No. | Nama Anggota | NIM | Tugas dan Tanggung Jawab |
|---|---|---|---|
| 1 | Aulia Safitri | 2225250190 | Mengkoordinasikan pengerjaan proyek, menyusun program utama, dan menggabungkan seluruh bagian program. |
| 2 | Siti Solehah | 2225250058 | Membuat fungsi perhitungan luas dan keliling persegi serta persegi panjang. |
| 3 | Ayu Syarifatu Zahra | 2225250043 | Membuat fungsi perhitungan luas dan keliling segitiga serta lingkaran. |
| 4 | Zahwa Ajmala Fitriani | 2225250191 | Membuat validasi input dan membantu melakukan pengujian program. |

Setiap anggota kelompok bertanggung jawab menyelesaikan tugas yang telah diberikan serta bekerja sama dalam proses pengembangan dan penyempurnaan program.

## 11. Jadwal Pelaksanaan Proyek

Pelaksanaan proyek direncanakan dalam beberapa tahap sesuai dengan jadwal perkuliahan Algoritma dan Pemrograman.

| Pertemuan | Kegiatan | Target yang Dicapai |
|---|---|---|
| Pertemuan 14 | Perancangan proyek dan penyusunan proposal | Proposal proyek selesai dan struktur program direncanakan. |
| Pertemuan 15 | Implementasi program menggunakan Python | Seluruh fitur program selesai dibuat dan dilakukan pengujian. |
| Pertemuan 16 | Penyempurnaan dan presentasi proyek | Program siap digunakan dan hasil proyek dipresentasikan. |

Jadwal tersebut menjadi pedoman bagi seluruh anggota kelompok agar proyek dapat diselesaikan sesuai dengan waktu yang telah ditentukan.

## 12. Repository GitHub

Proyek Kalkulator Geometri Berbasis Python akan disimpan dan dikembangkan menggunakan GitHub sebagai tempat penyimpanan kode program dan dokumentasi proyek.

Repository GitHub kelompok:

**Nama Repository:** `proyek-akhir-kalkulator-geometri`

**Link Repository:** https://github.com/auliasftri455-lgtm/proyek-akhir-kalkulator-geometri.git

Repository ini digunakan oleh seluruh anggota kelompok untuk menyimpan, mengelola, dan memperbarui hasil pengerjaan proyek.

## 13. Penutup

Berdasarkan rancangan yang telah dibuat, proyek Kalkulator Geometri Berbasis Python diharapkan dapat menjadi program sederhana yang membantu pengguna menghitung luas dan keliling bangun datar dengan lebih mudah dan tepat.

Melalui proyek ini, kelompok kami juga dapat menerapkan materi Algoritma dan Pemrograman, khususnya penggunaan variabel, tipe data, fungsi, percabangan, perulangan, dan validasi input.

Kami berharap proyek ini dapat diselesaikan dengan baik melalui kerja sama seluruh anggota kelompok serta memberikan manfaat bagi pengguna dalam mempelajari dan memahami konsep geometri.