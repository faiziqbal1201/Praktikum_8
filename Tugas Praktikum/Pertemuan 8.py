class DataMahasiswa:
    def __init__(self):
        self.data = {}

    def tambah(self, nama, nilai):
        self.data[nama] = nilai
        print(f"Data {nama} berhasil ditambahkan dengan nilai : {nilai}.")

    def tampilkan(self):
        if not self.data:
            print("Belum ada data mahasiswa.")
        else:
            print("Daftar Nilai Mahasiswa:")
            for nama, nilai in self.data.items():
                print(f"{nama}: {nilai}")

    def hapus(self, nama):
        if nama in self.data:
            del self.data[nama]
            print(f"Data {nama} berhasil dihapus.")
        else:
            print(f"Data {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        if nama in self.data:
            self.data[nama] = nilai_baru
            print(f"Data {nama} berhasil diubah dengan nilai {nilai_baru}.")
        else:
            print(f"Data {nama} tidak ditemukan.")

# Contoh penggunaan
data_mahasiswa = DataMahasiswa()

data_mahasiswa.tambah("Muhammad", 90)
data_mahasiswa.tambah("Faiz Iqbal", 85)
data_mahasiswa.tambah("Dio Alfa", 78)
data_mahasiswa.tampilkan()
data_mahasiswa.hapus("Muhammad")
data_mahasiswa.tampilkan()
data_mahasiswa.ubah("Faiz Iqbal", 95)
data_mahasiswa.tampilkan()