# SOAL PERTAMA
# #cek bilangan positif dan genap
# Buat program yang meminta input bilangan bulat, lalu:

# Tampilkan "Bilangan positif dan genap" jika bilangan lebih dari 0 dan habis dibagi 2.
# Tampilkan "Tidak memenuhi syarat" jika tidak

print("\nSOAL PERTAMA\n")
userInput = int(input("masukan angka : "))

angka = userInput
#jika angka lebih dari 0 dan habis dibagi 2
if angka > 0 and angka % 2 == 0:
    print("Bilangan positif dan genap")
else:
    print("angka tidak memenuhi syarat")

# SOAL 2 – Cek Usia untuk SIM
# Buat program yang meminta input usia, lalu:

# Jika usia ≥ 17 dan ≤ 65, tampilkan "Boleh membuat SIM".
# Jika tidak, tampilkan "Tidak boleh membuat SIM".

print("\nSOAL KEDUA\n")
usia = int(input("berapa usia anda : "))

if usia >= 17 and usia <= 62:
    print("ANDA BISA MENGURUS SIM")
else:
    print("MAAF USIA ANDA TIDAK MASUK KRITERIA")

# SOAL 3 – Login Sederhana
# Buat program yang meminta username dan password:

# Username benar jika "admin", password benar jika 1234.
# Jika keduanya benar, tampilkan "Login berhasil".
# Jika salah satu salah, tampilkan "Login gagal".

print("\nSOAL KETIGA\n")
try : 
    userName = input("masukan username anda : ".lower())
    password = int(input("masukan password anda : "))

    if userName == "admin" and password == 1234:
        print("anda berhasil login")
    else :
        print("login gagal")
except :
    print("password harus berupa angka")