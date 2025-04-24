kontak={"Randi":"089564872901",
        "Ridwan":"087134502887",
        "Rasya":"085634775210"
        }



def tampilkan_kontak():
    if not kontak:
        print("\nDaftar kontak kosong.")
        
    else:
        print("\n Inilah Daftar kontak yang telah terdaftar semua:")
        for i,(nama, nomor)in enumerate(kontak.items(),):
            print(f"{i}.{nama} {nomor}")
        
#program menyimpan Data kontak

while True:
    print("\nMenu pilihan yang tersedia:")
    print("1. Tambah kontak")
    print("2. Hapus kontak")
    print("3. Cari kontak")
    print("4. Lihat semua kontak")
    print("5. Keluar")

    pilihan = input("silahkan pilih menu (1-5): ")

    if pilihan == '1':
        nama = input("Nama Kontak: ")
        nomor = input("Nomor Telepon: ")
        kontak[nama] = nomor
        print("selamat kontak anda berhasil ditambahkan.")

    elif pilihan == '2':
        nama = input("Nama kontak yang ingin anda hapus:")
        if nama in kontak:
            del kontak[nama]
            print("kontak berhasil dihapus.")
        else:
            ("kontak tidak dapat ditemukan.")

    elif pilihan == '3':
        nama = input("Nama kontak yang ingin anda cari: ")
        if nama in kontak:
            print(f"{nama}: {kontak[nama]} ")
        else:
            print("Kontak yang anda cari tidak di temukan .")


    elif pilihan == '4':
         tampilkan_kontak()
    elif pilihan =='5':
        print("Terima kasih , program kami telah selesai.")


    else:
        print("pilihan tidak sesuai/tidak terdaftar, mohon coba lagi.")
        break
        
