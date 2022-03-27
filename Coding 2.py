barang = ['Baju', 'Celana', 'Tas', 'Buku', 'Lemari']

while True :
  print("""pilih salah satu perintah berikut :
  a. menambahkan
  b. menghapus
  c. mengedit
  d. menampilkan
  e. mencari barang
  f. mencari index""")
  perintah = input("masukkan perintah di atas : ")
  
  if perintah == 'a':
    tambah = input("masukkan barang : ")
    barang.append(tambah)
  elif perintah =='b':
    hapus = int(input("masukkan index yang akan dihapus : "))
    del barang[hapus]
  elif perintah == 'c':
    ubah = int(input("masukkan index yang akan diubah : "))
    barang[ubah] = input("masukkan barang baru : ")
  elif perintah == 'd':
    print(barang)
  elif perintah == 'e':
    cari = input("masukkan barang yang dicari : ")
    if cari in barang:
      print("barang ditemukan")
    else: 
      print("barang tidak ditemukan")
  elif perintah == 'f':
      cari = input("masukkkan item yang ingin dicari indeksnya : ")
      if cari in barang:
        print(barang.index(cari))
      else :
        print("barang tidak ditemukan")
  else:
     break

print("selesai")