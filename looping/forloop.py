#perulangan (loop)
 #for kondisi :
 #  aksi
 
 #ini dengan list
print("loop dengan menggunakan list")
angka2_list = [0 ,1 ,2 ,3 , 4] 
print("angka2_list = [0 ,1 ,2 ,3 , 4] ")
print(angka2_list)
 
for i in angka2_list:
   print(f" i sekarang -> {i}")

print("AKHIRI PROGRAM 1\n") 

print("loop dengan menggunakan range")

#ini dengan range
print("angka2_range = range(5)")
angka2_range = range(5)
for i in angka2_range:
  print(f" i sekarang -> {i}")

print("AKHIRI PROGRAM 2\n") 

print("perhatikan perbedaan pada value\n")
#ini dengan range yang ke 2
print("angka2_range2 = range(1,5)")
print("posisi 1 tidak boleh lebih dari 5")
angka2_range2 = range(1,5) # posisi 1 tidak boleh lebih dari 5



for i in angka2_range2:
   print(f" i sekarang -> {i}")

print("AKHIRI PROGRAM 3\n") 

# LOOP MENGGUNAKAN STRING

data_str = "nama saya raldy"

for huruf in data_str:
  print(huruf)
  
print("akhir dari program 4")