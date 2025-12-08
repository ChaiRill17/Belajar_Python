# Progrram daftar makanan menggunakan list
makanan = ['Nasi Goreng', 'Mie Ayam', 'Telur Dadar', 'Mie Kari', 'Cumi Kuah']

print(f'Daftar Makanan: {makanan}')
print(f'Pesan makanan: {makanan[0]} dan {makanan[3]} dan {makanan[-1]}')

makanan [1] = 'Bakso'  # mengubah nilai pada list
print(f'Daftar Makanan terbaru: {makanan}')

makanan.append('Sate Ayam') # menambahkan nilai pada list
makanan.insert(0, 'Ayam Geprek') # menambahkan nilai pada list di posisi tertentu
print(f'Daftar Makanan terbaru: {makanan}')

makanan.remove('Ayam Geprek') # menghapus nilai pada list
del makanan[4] # menghapus nilai pada list berdasarkan index
print(f'Daftar Makanan terbaru: {makanan}')