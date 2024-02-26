# Februari = 29
# Jan, Mar, May, July, Austus, Oktober, Desember = 31
# April, Juni, September, November = 30

input_user = (input("Masukkan Bulan = "))
try:
    bulan = int(input_user)
    if bulan == 2:
        print("Jumlah Hari = 29")
    elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
        print("Jumlah Hari =30")
    elif bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
        print("Jumlah Hari = 31")
    else:
        print("Format Salah")
except:
    print("Format yang anda masukkan harus dalam bentuk angka!")
