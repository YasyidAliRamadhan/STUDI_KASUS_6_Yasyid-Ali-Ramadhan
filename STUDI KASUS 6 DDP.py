import json

while True:
    print("\n=== SISTEM MANAJEMEN INVENTARIS ===")
    print("1. Tampilkan Data Barang")
    print("2. Tambah Data Barang")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        file = open("SC DAN MP DDP/SC 6.json", "r")
        data_barang = json.load(file)
        file.close()

        print("\n=== DATA BARANG ===")

        for barang in data_barang:
            print("KODE :", barang["kode"])
            print("NAMA BARANG :", barang["nama"])
            print("STOK :", barang["stok"])
            print("HARGA :", barang["harga"])
            print("------------------------")

    elif pilihan == "2":
        file = open("SC DAN MP DDP/SC 6.json", "r")
        data_barang = json.load(file)
        file    .close()
        kode = input("Masukkan kode barang: ")
        nama = input("Masukkan nama barang: ")
        stok = input("Masukkan stok barang: ")
        harga = input("Masukkan harga barang: ")



        barang_baru = {
            "kode": kode,
            "nama": nama,
            "stok": stok,
            "harga": harga
        }

        data_barang.append(barang_baru)

        file = open("SC DAN MP DDP/SC 6.json", "w")
        json.dump(data_barang, file, indent=4)
        file.close()

        print("\nData barang berhasil ditambahkan.")

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")