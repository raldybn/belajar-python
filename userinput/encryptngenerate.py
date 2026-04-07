import string
import secrets
import hashlib

class User:
   
    def inputUser(self):
        self.id = input("\nmasukan ID atau User Name anda : ")
        self.telpNumber = int(input("masukan nomor hp anda : "))
        choice = input("apakah anda ingin membuat password sendiri (y/n)? ")
        if  choice.lower() == "y":
                user_input_password = input("Masukan password anda : ")
                self.password = self.encrypt_password(user_input_password)
                print("\nPASSWORD ANDA BERHASIL KAMI ENKRIPSI!\n")
        else :
                generated = self.generate_password()
                print("\nPASSWORD ANDA BERHASIL KAMI GENERATE!\n")
                print("password acak anda adalah : ", generated)
                
                print("\nPASSWORD ANDA BERHASIL KAMI GENERATE LALU DI ENKRIPSI!\n")
                self.password = self.encrypt_password(generated)
        
    def generate_password(self, length= 8):
        # import string, secrets
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(characters) for _ in range(length))
    
    def encrypt_password(self,user_input_password):
        #gunakan sha256 untuk hashing
        return hashlib.sha256(user_input_password.encode()).hexdigest()
    
    def userInfo(self):
        return f"\nID : {self.id}\nNomor HP : {self.telpNumber}\nPassword : {self.password}"

user = User()

print("\n###### USER INPUT #####")
user.inputUser()

print("###### INFO USER #####")

print(user.userInfo())
print("\n")
