
def input_angka(pesan):
    while True:
        try:
            angka = float(input(pesan))

            if angka <= 0:
                print("Angka harus lebih dari 0!")
            else:
                return angka

        except ValueError:
            print("Input harus berupa angka!")
