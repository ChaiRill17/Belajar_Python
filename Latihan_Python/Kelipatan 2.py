# Program cek kelipatan dari sebuah angka

for angka in range(1, 101):
    if angka % 2 == 0 and angka % 10 == 0:
         print('Genap Bel')
    elif angka % 2 == 0:
        print('Genap')
    elif angka % 10 == 0:
        print('Bel')
    else:
        print(angka)