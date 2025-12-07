# soal enter pin

print('==== Bank Syarirah indonesia ====')
print()

pin = int(input('Masukkan Pin Anda : '))
while pin != 170805:
    pin = int(input('Pin Salah, Masukkan Pin Anda Kembali : '))

print('Pin Anda Benar, Selamat Datang di Bank Syarirah indonesia')