def tambah_ubah_nilai_mahasiswa(nilai_mahasiswa):
    # Meminta input nama mahasiswa
    nama = input("Masukkan nama mahasiswa: ")

    # Meminta input nilai mahasiswa
    nilai_str = input("Masukkan nilai mahasiswa (pisahkan dengan koma): ")
    nilai = tuple(map(int, nilai_str.split(',')))

    # Jika pengguna memasukkan lebih dari tiga nilai, berikan peringatan
    if len(nilai) > 3:
        print("Peringatan: Anda memasukkan lebih dari tiga nilai. Nilai tidak bisa diproses.")
        return

    # Menambahkan atau mengubah nilai mahasiswa
    nilai_mahasiswa[nama] = nilai

def hitung_nilai_mahasiswa(nilai_mahasiswa):
    # Membuat dictionary untuk menyimpan nilai akhir
    nilai_akhir = {}

    # Iterasi melalui dictionary nilai_mahasiswa
    for nama, nilai in nilai_mahasiswa.items():
        # Menghitung rata-rata nilai
        rata_rata = sum(nilai) / len(nilai)
        # Menambahkan nilai rata-rata ke dictionary nilai_akhir
        nilai_akhir[nama] = rata_rata

    return nilai_akhir

def tampilkan_nilai_mahasiswa(nilai_mahasiswa):
    # Menghitung dan mencetak nilai akhir
    nilai_akhir = hitung_nilai_mahasiswa(nilai_mahasiswa)
    
    for nama, rata_rata in nilai_akhir.items():
        print(f"Nama: {nama}, Nilai: {nilai_mahasiswa[nama]}, Rata-rata: {rata_rata}")

# Membuat dictionary dengan nama mahasiswa sebagai kunci dan tuple nilai sebagai nilai
nilai_mahasiswa = {
    "Budi": (85, 90, 78),
    "Ani": (92, 88, 84),
    "Sari": (75, 80, 88)
}

while True:
    # Meminta input pilihan pengguna
    pilihan = input("Apakah Anda ingin melihat rekap data nilai atau memasukkan data baru? (rekap/data): ")

    if pilihan.lower() == 'rekap':
        tampilkan_nilai_mahasiswa(nilai_mahasiswa)
    elif pilihan.lower() == 'data':
        tambah_ubah_nilai_mahasiswa(nilai_mahasiswa)

    # Meminta input apakah ingin melanjutkan atau tidak
    lanjut = input("Apakah Anda ingin melanjutkan? (ya/tidak): ")
    if lanjut.lower() != 'ya':
        break
