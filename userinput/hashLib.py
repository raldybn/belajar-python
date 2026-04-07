import hashlib

# Data yang akan di-hash
data = "Belajar Python".encode()

# Menggunakan SHA256
hash_value = hashlib.sha256(data).hexdigest()
print("SHA256:", hash_value)