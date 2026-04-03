class Nasabah :
    def __init__ (self):
        self.nama = input('MASUKAN NAMA NASABAH : ').upper()
        self.namaBank = input('MASUKAN NAMA BANK : ').upper()
        self.noRek = int(input('MASUKAN NOMOR REKENING : '))
        self.alamat = input('MASUKAN ALAMAT ANDA : ').upper()
        self.saldo = 0 #DEFAULT SALDO
        
    def info_nasabah(self):
        print("\n###### INFO NASABAH ######\n")
        return(f"NAMA NASABAH : {self.nama}\nNAMA BANK : {self.namaBank}\nMASUKAN NOMOR REKENING NASABAH : {self.noRek}\nMASUKAN ALAMAT NASABAH : {self.alamat}")

    def saldoAwal(self):
        self.saldo = int(input("MASUKAN SALDO ANDA : "))
        return(f"\nSALDO ANDA ADALAH : {self.saldo}\n")
    
    def menabung(self):
        self.nasabahChoice = input("APAKAH ANDA INGIN MENABUNG? (Y/N)" ).upper()
        if self.nasabahChoice == "Y":
            jumlahUangDitabung = int(input("\nMASUKAN JUMLAH UANG YANG INGIN DITABUNG : \n"))
            print("SALDO ANDA ADALAH :", self.saldo + jumlahUangDitabung) 
        elif self.nasabahChoice == "N":
            print("TERIMAKASIH\n")
        else:
            print("MAAF JAWABAN TIDAK TERSEDIA\n")
    
    def withdraw(self):
        self.nasabahChoice = input("APAKAH ANDA INGIN MENARIK UANG? (Y/N) ").upper()
        
        if self.nasabahChoice == "Y":
            jumlahUangDitarik = int(input("MASUKAN JUMLAH UANG YANG INGIN DITARIK : \n"))
            print("SALDO ANDA ADALAH : ", self.saldo + jumlahUangDitarik)
        elif self.nasabahChoice == "N":
            print("TERIMAKASIH")
        else :
            print("MAAF JAWABAN ANDA TIDAK TERSEDIA")
        
        
nasabah = Nasabah()
print(nasabah.info_nasabah())
print("\n############\n")
print(nasabah.saldoAwal())
nasabah.menabung()
nasabah.withdraw()