import string
import secrets
import hashlib

class User:
   
    def inputUser(self):
        self.id = input("\nmasukan ID atau User Name anda : ")
        self.telpNumber = int(input("masukan nomor hp anda : "))
        choice = input("apakah anda ingin membuat password sendiri (y/n)? ")
        if  choice.lower() == "y":
                plain_password = input("Masukan password anda : ")
                self.password = self.encrypt_password(plain_password)
        else :
                generated = self.generate_password()
                print("\npassword berhasil di generate, ")
                print("password acak anda adalah : ", generated)
                
                self.password = self.encrypt_password(generated)
        
    def generate_password(self, length= 8):
        # import string, secrets
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(characters) for _ in range(length))
    
    def encrypt_password(self,plain_password):
        #gunakan sha256 untuk hashing
        return hashlib.sha256(plain_password.encode()).hexdigest()
    
    def userInfo(self):
        return f"\nID : {self.id}\nNomor HP : {self.telpNumber}\nPassword : {self.password} \n"

user = User()

print("\n###### USER INPUT #####\n")
user.inputUser()

print("\n###### INFO USER #####\n")
print(user.userInfo())
print("DEMI KEAMANAN AKUN ANDA, PASSWORD ANDA BERHASIL KAMI ENKRIPSI!\n")