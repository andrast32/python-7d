kursi = []
baris = ["A", "B", "C", "D"]

terisi = 0
kosong = 0
maks_terisi = 0
baris_terpadat = []

for i in range(4):
    data_baris = []
    print(f"\nInput Baris {baris[i]}")

    for j in range(6):

        while True:
            isi = input(f"Kursi {baris[i]}{j+1} (O/X): ").upper()

            if isi == "O" or isi == "X":
                data_baris.append(isi)
                break
            else:
                print("ERROR! Input hanya boleh O atau X")

    kursi.append(data_baris)

print("\n===== DENAH KURSI =====")
print("   1   2   3   4   5   6")

for i in range(len(kursi)):
    print(baris[i], end=" ")

    jumlah_baris = 0

    for j in range(len(kursi[i])):
        print(f"[ {kursi[i][j]} ]", end="")

        if kursi[i][j] == "X":
            terisi += 1
            jumlah_baris += 1
        else:
            kosong += 1

    print()

    if jumlah_baris > maks_terisi:
        maks_terisi = jumlah_baris
        baris_terpadat = [baris[i]]

    elif jumlah_baris == maks_terisi:
        baris_terpadat.append(baris[i])

pendapatan = terisi * 15000

print("\n========================")
print("Kursi Terisi :", terisi, "kursi")
print("Kursi Kosong :", kosong, "kursi")
print("Pendapatan   : Rp", pendapatan)

print("========================")
print("Baris Terpadat :", " & ".join(baris_terpadat),
      f"({maks_terisi} kursi)")