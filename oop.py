#ACCCESS MODIFIER
# __ -> buat private access modifier
# _ -> buat protected
#  -> jika tidak ada tanda berarti public

#inner class
class Player:
    #ATRIBUT (default atribut dalam bentuk public)
    nama = input("masukan nama player : ").upper() #atribut dalam bentuk public
    tinggi = float(input("masukan tinggi player : ")) #atribut dalam bentuk public
    __salary = 1_000_000 #atribut sudah dalam bentuk private
    
    #METHOD
    #cara mengekonvert atribut private ke public
    #self untuk memanggil atribut
    def get_name(self):
        return self.nama
    def get_salary(self):
        return self.__salary
#inner class

#outerclass
player = Player()
# player.nama bisa dipanggil di luar inner class karena bersifat public
player.salary = 3_000_000 #variable salary yang dibuat di luar inner class.
# player.__salary (tidak bisa di akses karna bersifat private)
#tapi karena sudah di return dalam atribut (self) maka kita mengakses dengan cara
#memanggil get_salary()
print('#####EXECUTED#####')
print(f"ini adalah default salary dari ({player.get_name()}) yang sudah di convert kedalam method self {player.get_salary()}")
print(f"ini adalah tinggi dari player ({player.nama}) tanpa di return kedalam method self {player.tinggi}")
print(f"ini adalah salary dari variable player.salary ({player.nama}) yang tidak ada di inner class {player.salary}")
