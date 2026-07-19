target = 350000

tabungan = [30000, 45000, 20000, 50000, 60000, 55000, 40000, 55000]

total = 0

print("Target Tabungan: Rp", target)
print("============================")

for i in range(len(tabungan)):
    total = total + tabungan[i]

    print(f"Minggu {i+1}: Nabung Rp {tabungan[i]} -> Total: Rp {total}")

    if total >= target:
        print("============================")
        print(f"Target TERCAPAI di minggu ke-{i+1}!")

        sisa = total - target
        print(f"Sisa uang : Rp {sisa}")
        break

if total < target:
    print("============================")
    print("Target belum tercapai")