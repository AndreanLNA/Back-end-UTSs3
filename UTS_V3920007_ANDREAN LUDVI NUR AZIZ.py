import numpy as np
import string
import random
import pyperclip

HURUF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# pada def main terdapat pesan enkripsi,pesan deskripsi, kunci dan mode
def main():
    pesanEnkripsi = "SUCCESSISNOTFINALFAILUREISNOTFATALITISTHECOURAGETOCONTINUETHATCOUNTS"
    pesanDekripsi = "EUFKYFEIVVIGRIQIFSMIOCLRUSQWKSMTDTCGUSWPYPAUUIARFOFCHGUNXMNUMTFCOAFS"
    kunci = 'MADIUN'
    mode1 = 'enkripsi'
    mode2 = 'dekripsi'

    if mode1 == 'enkripsi' and mode2 == 'dekripsi':
        ubah1 = enkripsiPesan(kunci, pesanEnkripsi)
        ubah2 = dekripsiPesan(kunci, pesanDekripsi)

    print("Vigenere Cipher")
    print("")
    print('Kunci yang saya gunakan adalah : ' + kunci)
    print("")
    print('Plaintext : ' + pesanEnkripsi)
    print('%snya yaitu : ' % (mode1.title()) + ubah1)
    print("")
    print('Ciphertext (dari hasil dekripsi Affine Chipher dibawah): ' + pesanDekripsi)
    print('%snya yaitu : ' % (mode2.title()) + ubah2)

    pyperclip.copy(ubah1 + ubah2)
    print()


# def enkripsiPesan merupakan kode untuk melakukan enkripsi pesan
def enkripsiPesan(kunci, pesan):
    return ubahPesan(kunci, pesan, 'enkripsi')


# def dekripsiPesan merupakan kode untuk melakukan dekripsi pesan
def dekripsiPesan(kunci, pesan):
    return ubahPesan(kunci, pesan, 'dekripsi')


def ubahPesan(kunci, pesan, mode):
    ubah = []
    # Digunakan untuk menyimpan pesan enkripsi dan pesan dekripsi

    kunciIndex = 0
    kunci = kunci.upper()

    for symbol in pesan:
        # akan dilakukan pada seluruh karakter dalam pesan
        nomor = HURUF.find(symbol.upper())
        if nomor != -1:  # -1 berarti symbol.upper() tidak ditemukan didalam HURUF
            if mode == 'enkripsi':
                nomor += HURUF.find(kunci[kunciIndex])  # tambahkan jika dienkripsi
            elif mode == 'dekripsi':
                nomor -= HURUF.find(kunci[kunciIndex])  # kurangi jika melakukan dekripsi

            nomor %= len(HURUF)

            # tambahkan pada hasil symbol enkrip/dekrip yang sudah diubahkan
            if symbol.isupper():
                ubah.append(HURUF[nomor])
            elif symbol.islower():
                ubah.append(HURUF[nomor].lower())

            kunciIndex += 1
            # ubah kunci yang akan dipakai selanjutnya
            if kunciIndex == len(kunci):
                kunciIndex = 0

        else:
            # symbol tidak berada pada HURUF, maka tambahkan hal tersebut dan ubahkan
            ubah.append(symbol)

    return ''.join(ubah)


# jika program sudah berjalan dengan benar maka akan memanggil fungsi main
if __name__ == '__main__':
    main()


#Affine Cipher

# Enkripsi
# Tentukan variabel

def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m


# def affine_encrypt adalah fungsi Enkripsi untuk membuat chiphertext
def affine_encrypt(text, key):
    '''
    C = (a*P + b) % 26
    '''
    return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26)
                        + ord('A')) for t in text.upper().replace(' ', '')])


# def affine_decrypt agar Dekripsi dapat kembali ke plaintext
def affine_decrypt(cipher, key):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1]))
                         % 26) + ord('A')) for c in cipher])



def main():
    # memasukkan/membuat text dan key
    text = 'EUFKYFEIVVIGRIQIFSMIOCLRUSQWKSMTDTCGUSWPYPAUUIARFOFCHGUNXMNUMTFCOAFS'  # Pesan yang akan di enkripsi
    key = [3, 5]

    print("Affine Cipher")
    print("")
    print('Kunci yang saya gunakan adalah : {}'.format(key))
    print("")
    print('Plaintext dari hasil enkripsi sebelumnya: {}'.format(text))

    # mengeluarkan/menampilkan enkripsi
    affine_encrypted_text = affine_encrypt(text, key)

    print('Hasil Enkripsi: {}'.format(affine_encrypted_text))
    print("")

    # mengeluarkan/menampilkan dekripsi
    print('Ciphertext : RNUJZURDQQDBXEDBDUHPDVLRZNHBTSHPKOKLXNHTYZYFNNDFEUVUTAXNSWPSNPKUTVFUH')
    print('Hasil deskripsi: {}'.format
          (affine_decrypt(affine_encrypted_text, key)))


if __name__ == '__main__':
    main()
