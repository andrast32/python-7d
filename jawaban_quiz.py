umur = int(input("masukkan umurmu:"))

if umur < 12 and umur >= 0:
   print("anak anak")
elif umur >= 13 and umur <= 17:
   print ("remaja")
elif umur >= 18 and umur <= 59:
   print ("dewasa")
elif umur >= 60:
   print ("lansia")
else:
   print("Umur tidak valid")