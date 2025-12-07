# and adalah operator logika yang hasilnya True jika kedua operator bernilai True
umur = 20
memiliki_ktp = True
boleh_masuk = (umur >= 17) and memiliki_ktp
print("Boleh masuk klub?", boleh_masuk)

# or adalah operator logika yang hasilnya True jika salah satu operator bernilai True
memiliki_sim = False
punya_motor = True
boleh_mengemudi = memiliki_sim or punya_motor
print("Boleh mengemudi?", boleh_mengemudi)

# not adalah operator logika yang membalik nilai boolean
lapar = False
tidak_lapar = not lapar
print("Apakah tidak lapar?", tidak_lapar)
