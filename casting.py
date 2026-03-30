#INTEGER

print('====INTEGER====')
data_int = 9
print('data =', data_int, ',type =', type(data_int))

#cara mengcasting(mengubah type data)

data_float = float(data_int)
print('data=', data_float, ',type =', type(data_float))

data_str = str(data_int)
print('data=', data_int, ',type =', type(data_str))

data_bool = bool(data_int) #nilai akan menjadi false jika nilai= 0
print('data =', data_bool, 'type = ', type(data_bool))

#FLOAT
print('====FLOAT====')
data_float = 3.4
print('data =', data_float, ',type =', type(data_float))

#cara mengcasting(mengubah type data)
data_int = int(data_float)
print('data =', data_int, ',type =', type(data_int))

data_str = str(data_float)
print('data =', data_str, ',type =', type(data_str))

data_bool = bool(data_float) #nilai akan menjadi false jika nilai= 0
print('data =', data_bool, 'type = ', type(data_bool))


#STRING
print('====STRING====')
data_str = "RALDY"
print('data =', data_str, ',type =', type(data_str))

#cara mengcasting(mengubah type data)
#data_int = int(data_str) #akan error karena string tidak bisa diubah ke integer
data_int = int(data_str)
print('data =', data_int, ',type =', type(data_int))

data_float = float(data_str)
print('data =', data_float, ',type =', type(data_float))

data_bool = bool(data_str) #nilai akan menjadi false jika nilai= 0
print('data =', data_bool, ',type = ', type(data_bool))