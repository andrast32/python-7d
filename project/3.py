jumlah = int(input("Masukkan jumlah siswa: "))

nama = []
mat = []
ipa = []
bindo = []
ips = []
kehadiran = []

for i in range(jumlah):

    print(f"\nData Siswa ke-{i+1}")

    nama_siswa = input("Nama siswa : ")
    nilai_mat = int(input("Nilai Matematika : "))
    nilai_ipa = int(input("Nilai IPA : "))
    nilai_bindo = int(input("Nilai Bahasa Indonesia : "))
    nilai_ips = int(input("Nilai IPS : "))
    hadir = int(input("Kehadiran (%) : "))

    nama.append(nama_siswa)
    mat.append(nilai_mat)
    ipa.append(nilai_ipa)
    bindo.append(nilai_bindo)
    ips.append(nilai_ips)
    kehadiran.append(hadir)

naik = 0
tidak_naik = 0

nilai_tertinggi = 0
nilai_terendah = 100

nama_tertinggi = ""
nama_terendah = ""

total_rata_kelas = 0

print("\n====================================")
print("          LAPORAN KELAS 8B")
print("====================================")

for i in range(len(nama)):

    rata = (mat[i] + ipa[i] + bindo[i] + ips[i]) / 4

    total_rata_kelas += rata

    if rata >= 70 and kehadiran[i] >= 80:
        status = "NAIK KELAS"
        naik += 1
    else:
        status = "TIDAK NAIK"
        tidak_naik += 1

    if rata > nilai_tertinggi:
        nilai_tertinggi = rata
        nama_tertinggi = nama[i]

    if rata < nilai_terendah:
        nilai_terendah = rata
        nama_terendah = nama[i]

    print(f"\nSiswa : {nama[i]}")
    print(f"Mat : {mat[i]} | IPA : {ipa[i]}")
    print(f"B.Ind : {bindo[i]} | IPS : {ips[i]}")
    print(f"Rata-rata : {rata:.2f}")
    print(f"Kehadiran : {kehadiran[i]}%")
    print(f"Status : {status}")

rata_kelas = total_rata_kelas / jumlah

print("\n====================================")
print("REKAP KELAS")
print("====================================")
print("Naik Kelas :", naik, "siswa")
print("Tidak Naik :", tidak_naik, "siswa")
print(f"Nilai Tertinggi : {nilai_tertinggi:.2f} ({nama_tertinggi})")
print(f"Nilai Terendah : {nilai_terendah:.2f} ({nama_terendah})")
print(f"Rata-rata Kelas : {rata_kelas:.2f}")
print("====================================")