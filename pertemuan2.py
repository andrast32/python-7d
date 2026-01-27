berat = float(input("masukan berat badan anda = "))
tinggi = float(input("masukan tinggi badan anda = (m) "))

print("berat badan anda ", berat)
print("tinggi badan anda ", tinggi)

bmi = berat / (tinggi ** 2)

print ("bmi anda", round(bmi , 2))

if bmi < 18.5 :
      print ("ANDA KURUS")

elif bmi < 25 :
      print ("berat badan anda ideal")

elif bmi < 30 :
      print ("berat badan anda gemuk")

else :
      print ("ANDA OBESITAS")