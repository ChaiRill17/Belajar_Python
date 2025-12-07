# soal enter pin dengan batas percobaan 3x

print('==== Bank Syarirah indonesia ====')
print()

pin = int(input('Masukkan Pin Anda : '))
coba = 1

while pin != 170805 and coba < 3: # batasi 3x percobaan
    pin = int(input('Pin Salah, Masukkan Pin Anda Kembali : '))
    coba += 1

if pin != 170805:
    print('Anda sudah 3x memasukkan pin salah, akun anda diblokir. Silakan hubungi bank.')  

else:
    print('Pin Anda Benar, Selamat Datang di Bank Syarirah indonesia')