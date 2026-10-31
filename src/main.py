
from persegi import hitung_persegi
from persegi_panjang import hitung_persegi_panjang
from segitiga import hitung_segitiga
from lingkaran import hitung_lingkaran


def tampilkan_menu():
    print("\n=== KALKULATOR GEOMETRI ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Keluar")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            hitung_persegi()
        elif pilihan == "2":
            hitung_persegi_panjang()
        elif pilihan == "3":
            hitung_segitiga()
        elif pilihan == "4":
            hitung_lingkaran()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-5.")


if __name__ == "__main__":
    main()
