input1 = (input("Masukkan Sisi 1 = "))
input2 = (input("Masukkan Sisi 2 = "))
input3 = (input("Masukkan Sisi 3 = "))

try: 
    sisi1 = int(input1)
    sisi2 = int(input2)
    sisi3 = int(input3)

    if sisi1 == sisi2 == sisi3:
        print("3 Sisi Sama")
    elif sisi1 == sisi2 or sisi2 == sisi3 or sisi1 == sisi3:
        print("2 Sisi Sama")
    else:
        print("Tidak ada sisi yang sama")
except:
    print("Format yang anda masukkan harus dalam bentuk angka!")