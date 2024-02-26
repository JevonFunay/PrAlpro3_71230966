input_user = (input("Masukkan suatu bilangan: "))
try:
    bilangan = int(input_user)
    if bilangan == 0:
        print("Nol")

    elif bilangan > 0:
        print("Positif")

    elif bilangan < 0:
        print("Negatif")
except:
    print("Format yang anda masukkan harus dalam bentuk angka!")