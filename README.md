
# Praktikum_8
# Nilai Mahasiswa Class

## Overview
The `NilaiMahasiswa` class is a simple Python class designed to manage and manipulate student data, specifically their names and corresponding grades. The class provides functionality to add, display, update, and delete student records.

## Let's discuss each method

### `__init__(self)`
- Ini adalah metode konstruktor yang akan dipanggil saat objek kelas dibuat.
- Membuat atribut `data` yang akan digunakan untuk menyimpan data mahasiswa dalam bentuk kamus (`dictionary`).

### `tambah(self, nama, nilai)`
- Metode ini digunakan untuk menambahkan data mahasiswa baru atau memperbarui nilai mahasiswa yang sudah ada.
- Menambahkan nama mahasiswa sebagai kunci dan nilai sebagai nilainya ke dalam kamus `data`.

### `tampilkan(self)`
- Metode ini digunakan untuk menampilkan daftar nilai mahasiswa.
- Memeriksa apakah kamus `data` kosong atau tidak. Jika kosong, mencetak pesan bahwa belum ada data. Jika tidak kosong, mencetak daftar nama dan nilai mahasiswa.

### `hapus(self, nama)`
- Metode ini digunakan untuk menghapus `data mahasiswa` berdasarkan nama.
- Memeriksa apakah nama mahasiswa ada dalam kamus `data`. Jika ada, menghapus entri tersebut; jika tidak, mencetak pesan bahwa data tidak ditemukan.

### `ubah(self, nama, nilai_baru)`
- Metode ini digunakan untuk mengubah nilai mahasiswa berdasarkan nama.
- Memeriksa apakah nama mahasiswa ada dalam kamus `data`. Jika ada, mengubah nilai dengan nilai baru yang diberikan; jika tidak, mencetak pesan bahwa data tidak ditemukan.

## `Contoh Penggunaan`

```python
# Membuat objek data_mahasiswa dari kelas DataMahasiswa
data_mahasiswa = DataMahasiswa()

# Menambahkan beberapa data mahasiswa menggunakan metode tambah, tampilkan, hapus, ubah
data_mahasiswa.tambah("Muhammad", 90)
data_mahasiswa.tambah("Faiz Iqbal", 85)
data_mahasiswa.tambah("Dio Alfa", 78)

data_mahasiswa.tampilkan()
data_mahasiswa.hapus("Muhammad")
data_mahasiswa.tampilkan()
data_mahasiswa.ubah("Faiz Iqbal", 95)

# Menampilkan daftar nilai mahasiswa setelah perubahan dengan hapus dan ubah 
data_mahasiswa.tampilkan()
```
