#class adalah blueprint untuk membuat objek (OBJECT ORIENTED PROGRAM)
class mahasiswa():
    #nama = nama adalah atribut yang menempel pada class
    nama = "nama"

#METHOD ADALAH FUNGSI DIDALAM CLASS
    def belajar(self, kondisi):
        print(self.nama,'sedang belajar', kondisi)
    
    def tidur(self):
        print(self.nama, "tidur di kelas")

#MAIN PROGRAMNYA
#otong adalah instense dan mahasiswa adalah objectnya
otong = mahasiswa()
ucup = mahasiswa()

otong.nama = "otong surotong"
ucup.nama = "ucup babi"


otong.belajar("dengan giat")
ucup.tidur()
otong.tidur()