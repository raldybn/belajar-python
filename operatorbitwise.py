#operator bitwise

a = 9
b = 5

#BITWISE OR (|)
c = a | b
print(c)
print("\n ===== OR ===== \n")
print('nilai : ', a,', binary : ', format(a,"08b"))
print('nilai : ', b,', binary : ', format(b,"08b"))
print('------------------------------ (|)')
print('nilai : ', c,', binary : ', format(c,"08b"))
print(sep=("-"))

#BITWISE AND (&)
c = a & b
print(c)
print("\n ===== AND ===== \n")
print('nilai : ', a,', binary : ', format(a,"08b"))
print('nilai : ', b,', binary : ', format(b,"08b"))
print('------------------------------ (&)')
print('nilai : ', c,', binary : ', format(c,"08b"))
print(sep=("-"))


#BITWISE XOR (^)
c = a ^ b
print(c)
print("\n ===== XOR ===== \n")
print('nilai : ', a,', binary : ', format(a,"08b"))
print('nilai : ', b,', binary : ', format(b,"08b"))
print('------------------------------ (^)')
print('nilai : ', c,', binary : ', format(c,"08b"))
print(sep=("-"))


#BITWISE NOT(~)
c = ~a
print("\n ===== NOT ===== \n")
print('nilai : ',a,', binary : ', format(a,"08b"))
print('------------------------------ (~)')
print('nilai : ',c,', binary : ', format(c,"08b"))
print(sep=("-"))
print('------------------------------ (^)')
d = 0b0000001001
e = 0b11111111111
print('nilai : ',e^d,', binary : ',format(e^d, '08b'))

#SHIFTING

#SHIFT RIGHT (>>)
c = a >> 1
print("\n ===== SHIFT RIGHT (>>) ===== \n")
print('nilai : ',a,', binary : ', format(a,"08b"))
print('------------------------------ (>>)')
print('nilai : ',c,', binary : ', format(c,"08b"))
print(sep=("-"))

#SHIFT LEFT (<<)
c = a << 1
print("\n ===== SHIFT LEFT (<<) ===== \n")
print('nilai : ',a,', binary : ', format(a,"08b"))
print('------------------------------ (<<)')
print('nilai : ',c,', binary : ', format(c,"08b"))
print(sep=("-"))

