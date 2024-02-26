angka1 = (input("Masukkan bilangan pertama: "))
angka2 = (input("Masukkan bilangan kedua: "))
angka3 = (input("Masukkan bilangan ketiga: "))
try:
    a = int(angka1)
    b = int(angka2)
    c = int(angka3)
    if a > b and a > c:
        print("Terbesar: ", a)
    elif b > a and b > c:
        print("Terbesar: ", b)
    elif c > a and c > b:
        print("Terbesar: ", c)
except:
    print("Format yang anda masukkan harus dalam bentuk angka!")