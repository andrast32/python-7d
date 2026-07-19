tinggi = int (input("Masukan nilai = "))
for i in range (1, tinggi + 1):
    print(" " * (tinggi - i), end = "")
    print ("*" * (2 * i - 1))