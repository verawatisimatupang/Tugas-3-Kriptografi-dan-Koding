# Implementasi Program Tanda-tangan Digital dengan Menggunakan Algoritma RSA dan Fungsi hash SHA-3
#  Menu pembangkitan tanda-tangan digital (signing)
from hashlib import sha3_224

# Menghitung nilai hash dari pesan M
def Hash(message):
    hash = sha3_224(message.encode("latin-1")).hexdigest()
    hashed = int(hash, 16)
    return hashed

# Mengenkripsi h dengan kunci privatnya (SK) menggunakan persamaan enkripsi RSA, hasilnya adalah signature S:
def enkrip(message,PK, n):
    hashed = Hash(message)
    S = (hashed**PK) % n
    return S

# dekripsi terhadap tanda-tangan S dengan kuncipublik si pengirim (PK) menggunakan persamaan dekripsi RSA:
def dekrip(message, PK, n, S):
    hashed = Hash(message)%n
    h= (S**PK)%n
    if int(h) == int(hashed):
        return True
    else:
        return False
