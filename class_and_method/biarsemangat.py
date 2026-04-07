nama = input("KAMU SIAPA?? ").upper()
clear = "\n" * 8
print(clear)
def user_test(user):
    baik = "baik"
    buruk = "buruk"
    if user == baik:
        print(f"AKU SENANG DENGERNYA, SEMOGA {nama} MASIH SEMANGAT NGODING YAA !! :D")
    elif user == buruk:
        print(f"SEMOGA KAMU SEGERA MEMBAIK DAN SEMANGAT LAGI YA {nama}, OHIYAA... JANGAN LUPA JAGA KESEHATAN DAN TETAP TERUS NGODING YAAA!! :D")
    else:
        print(f"MAAF YA {nama} KAMU TIDAK MENJAWAB DENGAN BENAR, AKU HARAP KAMU BAIK2 AJA... SEMANGATT BUAT NGODINGNYAA :D")

# print(f"SELAMAT DATANG {nama}, SEMOGA KAMU SEMANGAT BUAT BELAJAR CODING DAN JANGAN LUPA JAGA KESEHATAN YA!! :D")
user_test(input(f"HALLO {nama}!!, BAGAIMANA KABAR KAMU SEKARANG??? : "))  
print(clear)
print("####PROGRAM BERAKHIR####")
print(  )