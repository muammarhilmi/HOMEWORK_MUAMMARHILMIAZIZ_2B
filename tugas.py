import modul as tugas
while True:
    tugas.menu()
    pilihan = input('Masukan Pilihan [1-7] : ')
    if pilihan == '1':
        tugas.new()
    elif pilihan == '2':
        tugas.edit()
    elif pilihan == '3':
        tugas.delete()
    elif pilihan == '4':
        tugas.search()
    elif pilihan == '5':
        tugas.tampilan()
    elif pilihan == '6':
        tugas.jumlah()
    elif pilihan == '7':
        print('''
=====Program Terhenti=====
              ''')
        exit()
    else:
        print('''
PILIHAN TIDAK VALID, HARAP MASUKAN PILIHAN YANG BENAR
              ''')
    