# # # # # def perkenalan():
# # # # #     print(f"Halo aku {nama}")

# # # # # def kali():
# # # # #     x = 5 * 5
# # # # #     print(x)

# # # # # nama = "Ridho"

# # # # # print(f"Nama : {nama}")
# # # # # perkenalan()

# # # # # def persegi(p, l):
# # # # #     luas = p * l
# # # # #     print(luas)

# # # # # panjang = int(input("Masukkan panjangnya:   "))
# # # # # lebar = int(input("Masukkan lebarnya:   "))

# # # # # persegi(panjang, lebar)

# # # # def segitiga(alas, tinggi):
# # # #     luas = 0.5 * alas * tinggi
# # # #     return luas

# # # # alas = int(input("Masukkan alas:   "))
# # # # tinggi = int(input("Masukkan tinggi:   "))

# # # # print(segitiga(alas, tinggi))

# # # # membuat variabel global
# # # Nama = "Hambali"

# # # Mata_Kuliah = "Algoritma dan Pemrograman Dasar"

# # # # membuat variabel lokal
# # # def info():
# # #     Nama = "Informatika"
# # #     Mata_Kuliah = "Logika Informatika"

# # # # mengakses variabel lokal
# # # print("Prodi:", Nama)
# # # print("Mata Kuliah:", Mata_Kuliah)

# # # # mengakses variabel global
# # # print("Prodi:", Nama)
# # # print("Mata Kuliah:", Mata_Kuliah)

# # # # memanggil fungsi info
# # # info()

# # def faktorial(n):
# # # Basis (Base Case): Kondisi berhenti
# #     if n == 1 or n == 0:
# #         return 1
# #     # Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri
# #     else:
# #         return n * faktorial(n - 1)
# # # Memanggil fungsi
# # hasil = faktorial(5)
# # print(f"Hasil dari 5! adalah: {hasil}")

# film = []

# def show_data():
#     if len(film) <= 0:
#         print("Belum Ada data")
#     else:
#         print("ID | Judul Film")
#         for indeks in range(len(film)):
#             print(indeks, "|", film[indeks])

# # Fungsi untuk menambah data
# def insert_data():
#     film_baru = input("Judul Film: ")
#     film.append(film_baru)
#     print("Film berhasil ditambahkan!")


# # Fungsi untuk mengedit data
# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         film[indeks] = judul_baru
#         print("Film berhasil diupdate!")


# # Fungsi untuk menghapus data
# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         film.remove(film[indeks])
#         print("Film berhasil dihapus!")


# # fungsi untuk menampilkan menu
# def show_menu():
#     print("\n")
#     print("----------- MENU---------- ")
#     print("[1] Show Data")
#     print("[2] Insert Data")
#     print("[3] Edit Data")
#     print("[4] Delete Data")
#     print("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print("\n")

#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print("Salah pilih!")


# if __name__ == "__main__":
#     while True:
#         show_menu()

try:
    password = input("Password yang diinginkan : ")
    if len(password) < 8:
        raise ValueError("Password Minimal Memiliki 8 karakter")
    elif not password.isdigit():
        raise ValueError("Password harus pakai angka")
except ValueError as e:
    print(e)

try:
    barang 
    if len(password) < 8:
        raise ValueError("Password Minimal Memiliki 8 karakter")
    elif not password.isdigit():
        raise ValueError("Password harus pakai angka")
except ValueError as e:
    print(e)

    
