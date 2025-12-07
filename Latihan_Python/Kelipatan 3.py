# Program membuat kelipatan 

for hari in range(1, 31):
    if hari % 2 == 0 and hari % 7 == 0:
        print('Selasa Minggu')
    elif hari % 2 == 0:
        print('Selasa')
    elif hari % 7 == 0:
        print('Minggu')
    else:
        print(hari)
    