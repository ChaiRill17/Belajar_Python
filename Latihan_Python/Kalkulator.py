# kalkulator sederhana

angka1 = int(input('Masukkan angka: '))
operator = input('Pilih Operator (+, -, *, /): ')
angka2 = int(input('Masukkan angka: '))


if operator == '+':
    print(angka1 + angka2)
elif operator == '-':
    print(angka1 - angka2)
elif operator == '*':
    print(angka1 * angka2)
elif operator == '/':
    if angka1 == 0 or angka2 == 0:
        print('Error! Tidak bisa membagi dengan nol')
    else:
        print(angka1 / angka2)

print('Hasil kalkulator selesai')