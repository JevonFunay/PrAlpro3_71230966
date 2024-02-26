input_user = (input("Masukkan suhu tubuh: "))
try:
    suhu = int(input_user)
    if suhu >= 38 and suhu < 40:
        print("Anda demam")
    elif suhu == 40:
        print("Anda Tidak Mungkin Hidup")
    else:
        print("Anda tidak demam")
except:
    print("Format yang anda masukkan harus dalam bentuk angka!")