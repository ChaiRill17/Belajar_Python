# Game tebak-tebakan sederhana

angka_rahasia = 17
kesempatan = 1
print("Selamat datang di permainan tebak-tebakan!")
print('Saya telah memilih sebuah angka antara 1 hingga 20')
print('Bisakah Anda menebaknya? Anda memiliki 5 kesempatan.')
Tebak = int(input('Masukkan tebakan Anda: '))

while Tebak != angka_rahasia and kesempatan < 6:
    Tebak = int(input('Tebakan salah, coba lagi: '))
    kesempatan += 1
if Tebak == angka_rahasia:
    print(f'Selamat! Anda menebak dengan benar dalam {kesempatan} kesempatan.')
elif Tebak > 20:
    print('Tebakan Anda di luar jangkauan! Silakan coba lagi nanti.')
else:
    print('Maaf, Anda telah kehabisan kesempatan. Angka yang benar adalah 17.')
    
   