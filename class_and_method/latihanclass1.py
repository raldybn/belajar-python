class Siswa:
    def __init__(self):
        self.nama = input("MASUKAN NAMA SISWA : ").upper()
        self.kelas = input("KELAS : ").upper()
        self.jurusan = input("JURUSAN : ").upper()
        
    def info_siswa(self):
        print(f"NAMA SISWA : {self.nama}\nKELAS : {self.kelas}\nJURUSAN : {self.jurusan}")
    
class Koreksi :
    def __init__(self):
        self.maPel  = input("MATA PELAJARAN : ").upper()
        self.nilai = float(input("MASUKAN NILAI SISWA :"))
    
    def nilai_dari_guru(self):
        if self.nilai >= 6.5 :
            print("SISWA LULUS")
        elif self.nilai < 6.5 :
            print("SISWA TIDAK LULUS, SISWA HARUS IKUT REMEDIAL")
        else:
            print("MASUKAN NILAI SISWA DENGAN BENAR")

siswa = Siswa()
koreksi = Koreksi()
print("\n#### INFO SISWA ####\n")
siswa.info_siswa()
print("\n#### GURU MENGKOREKRSI ####\n")
koreksi.nilai_dari_guru()