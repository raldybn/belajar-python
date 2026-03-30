#IF & ELSE STATEMENT
nama = input("siapa nama anda : ")
 
#PROGRAM SEBELUMNYA
#kondisi : aksi
#PROGRAM SELANJUTNYA

#1. program if inline
# if nama == "raldy" : print("kamu adalah raldy")
# print(f"terimakasihh {nama}")

#2. Program if indentation

# if nama == "raldy" : 
#     print("kamu ganteng abies") #identation adalah jarak di belakang print
#     print("kamu juga keren bgt")
# print(f"Terimakasih {nama}")

# else statment
if nama == "otong":
    print("hai otong keren!")
elif nama == "raldy":
    print("kamu ganteng max")
else:
    print(f"maaf ya {nama}, kamu bukan yg kami mau")    
print("####PROGRAM KE DUA####")
number = int(input("SILAHKAN MASUKAN ANGKA : "))

if number < 0:
    print("bilangan akan menjadi negatif. ", type(number))
elif number == 0:
    print("bilangan anda 0, ", type(number))
elif number > 0: 
    print("selamat bilangan anda positif, ", type(number))
else:
    print("maaf data tidak terdefinisi, ", type(number))
    
# test = int(input("Enter a test: "))
# result = "Positive" if test > 0 else "Not positive"
# print(result, type(result))

print("####AKHIR DARI PROGRAM KEDUA####")
print(f"Terimakasih {nama}")