
import math


def hitung_lingkaran():
    print("\n=== PERHITUNGAN LINGKARAN ===")

    try:
        jari_jari = float(input("Masukkan jari-jari: "))

        if jari_jari <= 0:
            print("Jari-jari harus lebih dari 0!")
            return

        luas = math.pi * jari_jari ** 2
        keliling = 2 * math.pi * jari_jari

        print("Luas lingkaran:", luas)
        print("Keliling lingkaran:", keliling)

    except ValueError:
        print("Input harus berupa angka!")
