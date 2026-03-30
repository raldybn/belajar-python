#OPERASI KOMMPERASI
#setiap hasil dari operasi komparasi adalah boolean
# >,<,>=,<=,==,!=, is, is not

a  = 4
b = 2
# LEBIH BESAR DARI >
print("LEBIH BESAR DARI")
hasil = a > b
print(a,'>', 3, '=', hasil)

hasil = b > 3
print(b, '>', 3, '=', hasil)

# KURANG DARI <
print("\nKURANG DARI")
hasil = a < b
print(a,'<', 3, '=', hasil)

hasil = b < 3
print(b, '<', 3, '=', hasil)

# LEBIH BESAR DARI SAMA DENGAN >=
print("\nLEBIH BESAR SAMA DENGAN")
hasil = a >= b
print(a,'>=', 3, '=', hasil)

hasil = b >= 3
print(b, '>=', 3, '=', hasil)

# KURANG DARI SAMA DENGAN <=
print("\nKURANG SAMA DENGAN")
hasil = a <= b
print(a,'<=', 3, '=', hasil)

hasil = b <= 3
print(b, '<=', 3, '=', hasil)

# TIDAK SAMA DENGAN
print("\nTIDAK SAMA DENGAN")
hasil = a != 4
print(a,'!=', 4, '=', hasil)

hasil = b != 3
print(b, '!=', 3, '=', hasil)

# SAMA DENGAN
print("\nSAMA DENGAN")
hasil = a == 4
print(a,'==', 4, '=', hasil)

hasil = b == 3
print(b, '==', 3, '=', hasil)

# IS SEBAGAI KOMPARASI OBJECT
print('\nIS SEBAGAI KOMPARASI OBJECT')
x = 5 #ini adalah  assignment membuat object
y = 5

# id =', hex(id(x))) CARA MELIHAT LOKASI MEMORY 

print('nilai x= ', x, ', id =', hex(id(x)))
print('nilai y= ', y, ', id =', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

# IS NOT SEBAGAI KOMPARASI OBJECT
print('\nIS NOT SEBAGAI KOMPARASI OBJECT')
x = 5 #ini adalah  assignment membuat object
y = 6

# id =', hex(id(x))) CARA MELIHAT LOKASI MEMORY 

print('nilai x= ', x, ', id =', hex(id(x)))
print('nilai y= ', y, ', id =', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)