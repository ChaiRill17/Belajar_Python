# Program untuk menampilkan kelipatan dari sebuah angka

for angka in range(1, 51):
    if angka % 4 == 0 and angka % 6 == 0:
        print('Empat Enam')
    elif angka % 4 == 0:
        print('Empat')
    elif angka % 6 == 0:
        print('Enam')
    else:
        print(angka)