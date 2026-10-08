# STUDI_KASUS_6_Yasyid Ali Ramadhan

NAMA: Yasyid Ali Ramadhan

NIM: 2609116072

KELAS: B

**PENJELASAN PROGRAM SISTEM MANAJEMEN INVENTARIS BARANG**

**1. PENJELASAN FILE JSON**

File .json digunakan sebagai tempat penyimpanan data inventaris barang. format JSON dapat digunakan untuk menyimpan dan membaca data, serta mendukung struktur data seperti array dan object

contoh program: 

<img width="291" height="283" alt="image" src="https://github.com/user-attachments/assets/9878437b-0a1a-4687-85bb-fce6d7f2ce1e" />

**2. PENJELASAN PROGRAM PY**

**A. IMPORT JSON**

<img width="238" height="34" alt="image" src="https://github.com/user-attachments/assets/cda06a2e-5359-41c4-af8b-4831efe8b07b" />

Program ini digunakan untuk mengaktifkan modul json pada python. Modul ini digunakan untuk membaca data dari file JSON dan menyimpan data kembali ke file JSON.

**B. PERULANGAN PROGRAM**

<img width="190" height="34" alt="image" src="https://github.com/user-attachments/assets/61d6280c-7058-4918-8329-03c0ac1c9882" />

Program ini digunakan agar program terus berjalan dan menu terus ditampilkan. Progran akan berhenti ketika pengguna memilih menu 3. keluar.

**C. MENU PROGRAM**

<img width="503" height="85" alt="image" src="https://github.com/user-attachments/assets/91e9bf9a-7ff1-438f-a5c4-208ccfb424ce" />

Program ini digunakan untuk menampilkan 3 pilihan menu kepada pengguna.

contoh ouput:

<img width="297" height="77" alt="image" src="https://github.com/user-attachments/assets/ff87806d-ae0b-493d-9726-b154b1adfff6" />

ketika program berhasil dijalankan maka akan menampilkan menu yang ingin dipilih oleh pengguna.

**D. MENAMPILKAN DATA BARANG**

<img width="425" height="88" alt="image" src="https://github.com/user-attachments/assets/2f099149-ee54-4162-bb92-726f0e97f6bf" />

Jika pengguna memilih nomor 1, program akan membuka file JSON dengan mode "r" atau read untuk membaca data.

<img width="313" height="34" alt="image" src="https://github.com/user-attachments/assets/17ef2c3c-e539-4f49-a54d-24c9bb70e11d" />

digunakan untuk mengambil data yang terdapat di dalam file JSON dan menyimpannya ke dalam variabel data.

Setelah selesai membaca, file ditutup dengan:

<img width="143" height="34" alt="image" src="https://github.com/user-attachments/assets/75dcfac9-39f2-41e3-95d1-c8f22af9d582" />

Kemudian data ditampilkan menggunakan perulangan:

<img width="525" height="126" alt="image" src="https://github.com/user-attachments/assets/447cf456-0248-4ea1-96d1-2e5de1403cd9" />

Perulangan for digunakan untuk menampilkan setiap barang yang terdapat di dalam data JSON.

Ini adalah output jika program nomor 1 berhasil dijalankan.

contoh output:

<img width="398" height="300" alt="image" src="https://github.com/user-attachments/assets/91093869-c499-47b3-8680-257031ba5e18" />


**E. MENAMBAHKAN DATA BARANG**

Jika pengguna memilih menu 2, program kembali membaca data yang sudah ada di file JSON.

contoh program:

<img width="475" height="77" alt="image" src="https://github.com/user-attachments/assets/ee0b3ece-f773-406e-93ff-e72d9f705329" />

kemudian program ini pengguna akan diminta menginput data barang seperti kode, nama, stok, harga.

contoh program:

<img width="487" height="87" alt="image" src="https://github.com/user-attachments/assets/f41fc839-33ce-4772-ae44-ca9d81dc3774" />

Data tersebut kemudian dibuat menjadi sebuah object/dictionary:

<img width="223" height="134" alt="image" src="https://github.com/user-attachments/assets/6d5a6c13-1c71-4961-bd09-b4c1877e8935" />

Setelah itu, barang baru ditambahkan ke data menggunakan:

<img width="311" height="35" alt="image" src="https://github.com/user-attachments/assets/571f2486-653f-45c1-aa18-399cc37b62ee" />

append digunakan untuk menambahkan data barang baru ke dalam list.

saat program berhasil dijalankan pengguna akan diminta memasuki data barang seperti kode, nama, stok, harga. Dan akan muncul keterangan "Data barang berhasil ditambahkan"

contoh output:

<img width="371" height="200" alt="image" src="https://github.com/user-attachments/assets/b246d30d-9958-4ea8-a70b-b5e8710655b4" />

**F. MENYIMPAN DATA KE FILE JSON**

<img width="419" height="69" alt="image" src="https://github.com/user-attachments/assets/f5b55072-3192-4d82-811b-ea975325196c" />

Mode "w" digunakan untuk membuka file dalam proses penulisan. json.dump digunakan untuk menyimpan data ke dalam file JSON.

Dengan cara ini, data barang yang baru ditambahkan tetap tersimpan di file sehingga tidak hilang ketika program ditutup dan dijalankan kembali.

Saat program berhasil dijalankan maka data barang akan otomatis tertambah di file python maupun JSON

contoh output py:

<img width="447" height="391" alt="image" src="https://github.com/user-attachments/assets/c9705cc1-9f5f-4f86-b57d-b410fb59df56" />

contoh output JSON:

<img width="445" height="408" alt="image" src="https://github.com/user-attachments/assets/bf18cc4f-8afd-474c-b966-1f67d2650b73" />

**G. Keluar dari Program**

<img width="495" height="72" alt="image" src="https://github.com/user-attachments/assets/575f3355-93c7-4e5a-aae8-e9d30356e3d5" />

Jika pengguna memilih menu 3, program menampilkan pesan bahwa program selesai. Perintah break digunakan untuk menghentikan perulangan while.

<img width="646" height="79" alt="image" src="https://github.com/user-attachments/assets/25a05555-e065-43f2-b008-5b4da95aa618" />

Program ini digunakan ketika pengguna memasukin menu yang tidak ada di pilihan, maka akan muncul keterangan "Pilihan tidak valid. Silakan pilih menu yang tersedia."




