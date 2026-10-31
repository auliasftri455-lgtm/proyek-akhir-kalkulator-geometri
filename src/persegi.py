
def hitung_persegi():
    print("\n=== PERHITUNGAN PERSEGI ===")

    try:
        sisi = float(input("Masukkan panjang sisi: "))

        if sisi <= 0:
            print("Sisi harus lebih dari 0!")
            return

        luas = sisi * sisi
        keliling = 4 * sisi

        print("Luas persegi:", luas)
        print("Keliling persegi:", keliling)

    except ValueError:
        print("Input harus berupa angka!")
