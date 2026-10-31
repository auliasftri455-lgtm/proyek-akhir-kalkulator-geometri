
def hitung_segitiga():
    print("\n=== PERHITUNGAN SEGITIGA ===")

    try:
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        sisi1 = float(input("Masukkan sisi pertama: "))
        sisi2 = float(input("Masukkan sisi kedua: "))
        sisi3 = float(input("Masukkan sisi ketiga: "))

        if alas <= 0 or tinggi <= 0 or sisi1 <= 0 or sisi2 <= 0 or sisi3 <= 0:
            print("Semua ukuran harus lebih dari 0!")
            return

        if (sisi1 + sisi2 <= sisi3 or
            sisi1 + sisi3 <= sisi2 or
            sisi2 + sisi3 <= sisi1):
            print("Ukuran sisi tidak membentuk segitiga!")
            return

        luas = 0.5 * alas * tinggi
        keliling = sisi1 + sisi2 + sisi3

        print("Luas segitiga:", luas)
        print("Keliling segitiga:", keliling)

    except ValueError:
        print("Input harus berupa angka!")
