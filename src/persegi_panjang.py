
def hitung_persegi_panjang():
    print("\n=== PERHITUNGAN PERSEGI PANJANG ===")

    try:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))

        if panjang <= 0 or lebar <= 0:
            print("Panjang dan lebar harus lebih dari 0!")
            return

        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)

        print("Luas persegi panjang:", luas)
        print("Keliling persegi panjang:", keliling)

    except ValueError:
        print("Input harus berupa angka!")
