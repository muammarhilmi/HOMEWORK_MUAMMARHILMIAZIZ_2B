def menu():
    print('Selamat datang di program manajemen stok barang!')
    print('''pilihan:
          1. Tambah Data Barang
          2. Edit Data
          3. Hapus Data Barang
          4. Cari Data
          5. Tampilkan Data Barang
          6. Tampilkan Jumlah Data
          7. Keluar''')
    
    
barang = []

def new():
    nama = str(input('Masukan Nama Barang : ').title())
    stok = int(input('Masukan Jumlah Stok Barang : '))
    barang_baru = {'Nama barang':nama,'Stok':stok}
    barang.append(barang_baru)
    print('--- DATA BERHASIL DITAMBAHKAN ---')

def edit():
    ganti = int(input('Edit Data Indeks ke : '))
    nama = str(input('Masukkan Nama Barang : ').title())
    jumlah = int(input('Masukkan Jumlah Stok Barang : '))
    barang[ganti] = {'Nama barang':nama,'Stok':jumlah}
    print('--- DATA BERHASIL DIUBAH ---')

def delete():
    hapus = int(input('Hapus Data Index Ke : '))
    del barang[hapus]
    print('--- DATA BERHASIL DIHAPUS ---')

def tampilan():
    print('======= TOKO ELEKTRONIK =======')
    if len(barang) == 0:
        print('--- DATA BARANG KOSONG ---')
    else:
        for a in barang:
            print('-',a['Nama barang'],':',a['Stok'])

def search():
    cari = str(input('Cari Nama Barang : ').title())
    print('======= Hasil Pencarian =======')
    for item in barang:
        if cari in item['Nama barang']:
            nama_terformat = ''.join(item['Nama barang'])
            print(f"{nama_terformat}, Stok : {item['Stok']}")

def jumlah():
    if len(barang) == 0:
        print('--- DATA BARANG KOSONG ---')
    else:
        print('Jumlah data tersimpan : ',len(barang),'barang')