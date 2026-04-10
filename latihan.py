print("#### INPUT NAMA MURID ####")
class Murid:
    def __init__(self):
        self.namaMurid = input("NAMA MURID : \n").upper()
        self.kelas = input("KELAS : \n").upper()
        self.namaPemeriksa = input("NAMA PEMERIKSA : \n")
        self.mataPelajaran = input("MATA PELAJARAN : \n")
        self.jawabanBenar = True
        self.jawabanSalah = False
    
    def info_murid(self):
        print(f"\nNAMA MURID : {self.namaMurid}\nKELAS : {self.kelas}\n")
        
    def jawaban_murid(self):
        self.soal_pertama = input("MASUKAN SOAL : \n")
        self.jawaban = bool(input("JAWABAN : \n"))
        if self.soal_pertama == self.jawaban:
            print('JAWABAN ANDA BENAR')
        else:
            print("JAWABAN ANDA SALAH")
      
murid = Murid()

print("\n#### DATA MURID ####\n")
murid.info_murid()
print("\n#### KOREKSI ####\n")
murid.jawaban_murid()
