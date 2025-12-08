# Program tebak angka acak
import random
print('== TEBAK ANGKA ACAK ==')
print('Saya sudah memilih sebuah angka antara 1 sampai 10')
print()
angka_acak = random.randint(1, 10)
kesempatan = 5

tebakan = int(input('Msukkan tebakan anda (1-10): '))
while tebakan != angka_acak and kesempatan > 1: # != tidak sama dengan dan > lebih besar dari
     tebakan = int(input('Salah! Coba lagi: '))
     kesempatan -= 1 # mengurangi kesempatan

     if tebakan < 1 or tebakan > 10: # or mengecek apakah tebakan kurang dari 1 atau lebih dari 10
        print('Diluar batas! Masukkan angka antara 1 sampai 10')
     elif tebakan < angka_acak:
        print('Tebakan anda terlalu kecil!')
     elif tebakan > angka_acak:
        print('Tebakan anda terlalu besar!')
# ini adalah kondisi akhir while
# masuk baris baru atau keluar dari loop
if tebakan == angka_acak:
      print('Selamat! Tebakan anda benar!')
else:
      print('Kesempatan anda sudah habis!')
      print('Angka yang saya pilih adalah', angka_acak)
    