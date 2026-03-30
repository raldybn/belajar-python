#OPERASI LOGIKA ATAU BOOLEAN

#not, or, and ,xor

#NOT
print('\n=====NOT====')
a = False
c = not a
print('data a = ', a)
print('----------NOT')
print('data c = ', c)

#OR (jika salah satu true, maka hasilnya adalah true)
print('\n=====OR====')
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)

#AND (jika dua buah nilai true hasilnya true)
print('\n=====AND====')
a = False
b = False
c = a and b
print(a, 'and', b, '=', c)
a = False
b = True
c = a and b
print(a, 'and', b, '=', c)
a = True
b = False
c = a and b
print(a, 'and', b, '=', c)
a = True
b = True
c = a and b
print(a, 'and', b, '=', c)

#XOR (akan true jika true hanya terdapat pada salah 1, sisanya false)
print('\n===== XOR (^)====')
a = False
b = False
c = a ^ b
print(a, 'xor', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'xor', b, '=', c)
a = True
b = False
c = a ^ b
print(a, 'xor', b, '=', c)
a = True
b = True
c = a ^ b
print(a, 'xor', b, '=', c)