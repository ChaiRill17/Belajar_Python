# list adalah tipe data yang dapat menyimpan beberapa nilai dalam satu variabel
buah = ['apel', 'jeruk', 'mangga']
print('Buah favorit saya adalah:', buah [0]) 

buah [1] = 'pisang' # mengubah nilai pada list
print('Buah favorit saya adalah:', buah [1])

buah.append('semangka') # menambahkan nilai pada list
print('Buah favorit saya adalah:', buah [3])

buah.insert(1, 'kiwi')  # menambahkan nilai pada list di posisi tertentu
print('Buah favorit saya adalah:', buah)

buah.remove('mangga')   # menghapus nilai pada list
print('Buah favorit saya adalah:', buah)

buah.pop(1) # menghapus nilai pada list berdasarkan index 
print('Buah favorit saya adalah:', buah)

del buah[0]              # menghapus nilai pada list berdasarkan index
print('Buah favorit saya adalah:', buah)

print('Jumlah buah favorit saya adalah:', len(buah))  # menghitung jumlah nilai pada list