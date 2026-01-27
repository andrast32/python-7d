# contoh operasi perbandingan
a = 12
b = 32

# 1. sama dengan
print(a == b) # False, karena 12 tidak sama dengan 32

# 2 tidak sama dengan
print(a != b) # True, Karena 12 memang tidak sama dengan 32

# 3 lebih kecil
print(a < b) # True, karena 12 lebih kecil dari 32 

# 4 lebih besar
print(a > b) # False, karena 12 tidak lebih besar dari 32

# 5 lebih besar atau sama dengan
print(a >= 12) # True, karena 12 sama dengan 12 (variabel)

# 6 lebih kecil atau sama dengan
print(b <= 32) # True, karena 32 sama dengan 32 (variabel)

# contoh penggunaan operator aritmatika
# 1 AND (True jika semua kondisinya benar)

umur = 20 #kita atur umur 20
punya_ktp = True #kita atur punya ktpnya

if umur >= 17 and punya_ktp: #jika umur lebih dari 17 tahun (perbandingan diambil dari variabel) dan punya ktp maka boleh masuk
    print("boleh masuk")
else : # jika tidak ga boleh masuk
    print("tidak boleh masuk")

#outputnya (boleh masuk) karena umur lebih dari 17 dan punya ktp

# 2 OR (True jika salah satu kondisi true)
hari = "Minggu" #variabel hari

if hari == "Sabtu" or hari =="Minggu" : #kondisi disini sesuai dengan nilai Variabel yang kita atur di variabel hari
    print("Hari libur")
else: 
    print("Hari kerja")

#outputnya (hari libur) karena hari Minggu menjadi salah satu nilai true 

# 3 NOT (Membalik nilai boolean)
hujan = False #kita mengatur hujan menjadi false (tidak hujan)
if not hujan:
    print("anda bisa keluar rumah") 
else :
    print("anda tidak boleh keluar rumah")

# outputnya (anda bisa keluar rumah) karena not membalikkan nilai false menjadi nilai true

nilai = 77
if nilai >= 85 and nilai <= 100:
    print("Predikat A")
elif nilai >= 65 and nilai <= 84:
    print("Predikat B")
elif nilai >= 45 and nilai <= 64:
    print("Predikat C")
elif nilai > 100:
    print("Predikat Anda Luar Biasa")
else:
    print("Predikat Anda Kurang mumpuni")

#outputnya jadi Predikat B, kenapa? karena 77 memenuhi kondisi nilai lebih dari sama dengan 65 dan lebih kecil sama dengan 85

#lalu jika nilai = 125 maka hasilnya jadi Predikat anda Luar Biasa, kenapa? karena 125 lebih besar dari 100

