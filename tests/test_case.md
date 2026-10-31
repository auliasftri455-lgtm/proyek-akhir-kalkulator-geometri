# Pengujian Kalkulator Geometri

Pengujian dilakukan untuk memastikan program dapat menghitung luas dan keliling bangun datar serta menolak input yang tidak valid.

| No. | Pengujian | Input | Hasil yang Diharapkan |
|---|---|---|---|
| 1 | Persegi | Sisi = 5 | Luas = 25, keliling = 20 |
| 2 | Persegi panjang | Panjang = 8, lebar = 4 | Luas = 32, keliling = 24 |
| 3 | Segitiga | Alas = 6, tinggi = 4, sisi = 5, 5, 6 | Luas = 12, keliling = 16 |
| 4 | Lingkaran | Jari-jari = 7 | Luas ≈ 153,94, keliling ≈ 43,98 |
| 5 | Input negatif | Sisi = -5 | Program menampilkan pesan kesalahan |
| 6 | Input nol | Jari-jari = 0 | Program menampilkan pesan kesalahan |
| 7 | Sisi segitiga tidak valid | Sisi = 2, 3, 6 | Program menolak input karena tidak membentuk segitiga |