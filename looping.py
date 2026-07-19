for i in range(1,11):
    print("ulang sebanyak 10 kali")

# for -> kata kunci untuk memulai perulangan
# variabel -> penampung nilai yang berubah setiap kali loop berjalan (dalam contoh ini nama variabelnya i)
# in range(...) -> menentukan rentang angka yang akan di pakai

# studi kasus track workout routine
pushup_per_set = 10
total_pushup = 0

print("Start workout session")

for set_number in range (1, 6) :
    total_pushup = total_pushup + pushup_per_set
    print("set")