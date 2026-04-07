#fungsi sederhana
print("####FUNGSI SEDERHANA####")
def tambah(a, b):
    return a + b  # Mengembalikan hasil penjumlahan
hasil = tambah(5, 3)  # Nilai 8 dikembalikan dan disimpan di 'hasil'
print(hasil)  # Output: 8

# Fungsi dengan satu parameter
print("####FUNGSI DENGAN SATU PARAMETER####")
def sapa(nama):
    print(f"Halo, {nama}!")
sapa("Budi")
sapa("Siti")

#   fungsi dengan beberapa parameter
print("####FUNGSI DENGAN BEBERAPA PARAMETER####")

def hitung_luas_persegi_panjang(panjang, lebar):
    """Menghitung luas persegi panjang."""
    if panjang <= 0 or lebar <= 0:
        return "Panjang dan lebar harus lebih dari 0"
    return panjang * lebar
# Contoh pemanggilan
print(hitung_luas_persegi_panjang(5, 3))   # 15
print(hitung_luas_persegi_panjang(0, 4))   # Validasi error

#FUNGSI DENGAN PARAMETER DEFAULT
print("####FUNGSI DENGAN PARAMETER DEFAULT####")
def sapa_dengan_default(nama="Pengunjung"):
    print(f"Halo, {nama}, bagaimana kabarmu hari ini? masihkah kamu semangat belajar coding :D ??")
sapa_dengan_default()       # Menggunakan default
sapa_dengan_default(input("isi nama anda:  ")) # Menggunakan nilai yang diberikan