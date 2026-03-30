#USER INPUT (sudah pasti type data yang keluar adalah string)
data = input("MASUKAN DATA : ")
print("data anda adalah = ", data, ", type = ", type(data))

#JIKA TYPE DATA INPUT INGIN DIGANTI DAN DISESUAIKAN MAKA HARUS DICASTING TERLEBIH DAHULU

#casting input integer
data_int = int(input(("masukan angka = ")))
print("angka anda adalah =", data_int, "type =", type(data_int))

#casting input float
data_float = float(input(("masukan angka = ")))
print("angka anda adalah =", data_float, "type =", type(data_float))

#casting input bool
#CASTING INPUT BOOLEAN HARUS DIUBAH TERLEBIH DAHULU KE INT LALU KE BOOLEAN, 
#JIKA TIDAK MAKA NILAI YANG KELUAR AKAN TETAP TRUE
data_bool = bool(int(input(("masukan biner = "))))
print("biner anda adalah =", data_bool, "type =", type(data_bool))