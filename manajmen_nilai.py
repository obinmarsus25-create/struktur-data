# Inisialisasi data awal (bisa kosong atau diisi contoh)
data_mahasiswa = [
    ["ahmad", 85],
    ["Budi", 78],
    ["Citra", 90]
]

def tampilkan_menu():
    print("\n====================================")
    print(" APLIKASI MANAJEMEN NILAI MAHASISWA")
    print("====================================")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Urutkan Data Berdasarkan Nilai")
    print("7. Hitung Rata-rata Nilai")
    print("8. Keluar")
    print("====================================")

def tampilkan_data():
    if not data_mahasiswa:
        print("\nData masih kosong.")
    else:
        print("\n--- Daftar Nilai Mahasiswa ---")
        print(f"{'No':<5} {'Nama':<20} {'Nilai':<10}")
        print("-" * 35)
        for i, mhs in enumerate(data_mahasiswa):
            print(f"{i+1:<5} {mhs[0]:<20} {mhs[1]:<10}")

def tambah_data():
    nama = input("\nMasukkan Nama Mahasiswa: ")
    try:
        nilai = int(input("Masukkan Nilai Mahasiswa (0-100): "))
        if 0 <= nilai <= 100:
            data_mahasiswa.append([nama, nilai])
            print(f" Data {nama} berhasil ditambahkan!")
        else:
            print(" Nilai harus antara 0 sampai 100.")
    except ValueError:
        print(" Input nilai harus berupa angka.")

def ubah_data():
    tampilkan_data()
    if not data_mahasiswa:
        return
    
    try:
        index = int(input("\nPilih nomor data yang ingin diubah: ")) - 1
        if 0 <= index < len(data_mahasiswa):
            nama_baru = input(f"Ubah Nama ({data_mahasiswa[index][0]}) menjadi: ")
            nilai_baru = int(input(f"Ubah Nilai ({data_mahasiswa[index][1]}) menjadi: "))
            
            if 0 <= nilai_baru <= 100:
                data_mahasiswa[index] = [nama_baru, nilai_baru]
                print(" Data berhasil diubah!")
            else:
                print(" Nilai harus antara 0 sampai 100.")
        else:
            print(" Nomor data tidak valid.")
    except ValueError:
        print(" Input harus berupa angka.")

def hapus_data():
    tampilkan_data()
    if not data_mahasiswa:
        return

    try:
        index = int(input("\nPilih nomor data yang ingin dihapus: ")) - 1
        if 0 <= index < len(data_mahasiswa):
            konfirmasi = input(f"Yakin ingin menghapus {data_mahasiswa[index][0]}? (y/n): ").lower()
            if konfirmasi == 'y':
                removed = data_mahasiswa.pop(index)
                print(f" Data {removed[0]} berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
        else:
            print(" Nomor data tidak valid.")
    except ValueError:
        print(" Input harus berupa angka.")

def cari_data():
    kata_kunci = input("\nMasukkan nama mahasiswa yang dicari: ").lower()
    ditemukan = False
    print(f"\n--- Hasil Pencarian '{kata_kunci}' ---")
    for mhs in data_mahasiswa:
        if kata_kunci in mhs[0].lower():
            print(f"Nama: {mhs[0]}, Nilai: {mhs[1]}")
            ditemukan = True
    
    if not ditemukan:
        print("Data tidak ditemukan.")

def urutkan_data():
    # Mengurutkan berdasarkan nilai (index 1), reverse=True untuk tertinggi ke terendah
    data_mahasiswa.sort(key=lambda x: x[1], reverse=True)
    print("\n Data berhasil diurutkan berdasarkan nilai tertinggi.")
    tampilkan_data()

def hitung_rata_rata():
    if not data_mahasiswa:
        print("\nData kosong, tidak bisa menghitung rata-rata.")
        return
    
    total_nilai = sum(mhs[1] for mhs in data_mahasiswa)
    rata_rata = total_nilai / len(data_mahasiswa)
    print(f"\nRata-rata nilai seluruh mahasiswa: {rata_rata:.2f}")

# --- PROGRAM UTAMA ---
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu 1-8: ")

    if pilihan == '1':
        tampilkan_data()
    elif pilihan == '2':
        tambah_data()
    elif pilihan == '3':
        ubah_data()
    elif pilihan == '4':
        hapus_data()
    elif pilihan == '5':
        cari_data()
    elif pilihan == '6':
        urutkan_data()
    elif pilihan == '7':
        hitung_rata_rata()
    elif pilihan == '8':
        print("\n  Terima kasih telah menggunakan aplikasi. Sampai jumpa!")
        break
    else:
        print("\n Pilihan tidak valid. Silakan pilih 1-8.")
    
    input("\nTekan Enter untuk melanjutkan...")