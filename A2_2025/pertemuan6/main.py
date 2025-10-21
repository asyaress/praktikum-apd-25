# Membuat set
# buah = {"apel", "jeruk", "mangga", "apel"}
# buah = ([“apel”, “jeruk”, “mangga”, “apel”])
# for i in buah:
#     print(i, end="")

# angka = [1, 1, 2, 3, 4, 4, 4]
# angkaset = set(angka)

# print(angkaset)

# Dict Start

# Daftar_buku = {
#     "Buku1": "Bumi Manusia",
#     "Buku2": "Laut Bercerita"
#     }

# print(Daftar_buku["Buku1"])
# print(Daftar_buku)

Biodata = {
    "Nama": "Ananda Daffa Harahap",
    "NIM": 2409106050,
    "KRS": ["Pemrograman Web", "Struktur Data", "Basis Data"],
    "Mahasiswa_Aktif": True,
    "Social Media": {"Instagram": "daffahrhap"},
}

# for i, j in Biodata.items():
#     print(i)
#     print(j)

# print(f"nama saya adalah {Biodata['Nama']}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get('Nama')}")
# print(Biodata.get('Nama1'))

# Film = {
#     "Avenger Endgame": "Action",
#     "Sherlock Holmes": "Mystery",
#     "The Conjuring": "Horror",
# }

# print(Film)

# Film["Zombieland"] = "Comedy"

# Film.update({"The Conjuring": "Comedy"})
# # Setelah Ditambah
# print(Film)

# data = {"Nama": "Daffa", "Umur": 19, "Jurusan": "Informatika"}
# Sebelum Dihapus
# print(data)
# del data["Nama"]

# print(data)
# memanggil data yang telah dihapus
# print(data.get("Nama"))


# data = {"Nama": "Daffa", "Umur": 19, "Jurusan": "Informatika"}
# # Sebelum Dihapus
# print(data)
# cache = data.pop("Nama")
# # Setelah dihapus
# print(data)
# # memanggil data yang telah dihapus pada dictionary
# print(data.get("Nama"))
# # memanggil data yang telah dihapus pada variabel cache
# print(cache)


# data = {"Nama": "Daffa", "Umur": 19, "Jurusan": "Informatika"}
# # Sebelum Dihapus
# print(data)
# data.clear()
# # Setelah dihapus
# print(data)


# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me", ["tes", "halo"], "Memories"],
#     "Paramore": [
#         "Misery Business",
#         "Ain't It Fun",
#         ["All We Know Is Falling", ["Here We Go Again", "My Heart"]],
#         "This Is Why",
#     ],
# }

# print(Musik["Paramore"][2][1][0])

# a = {10, 11, 12}
# b = {11, 13, 14}
# c = a | b

# print(c)

# Nilai = {"Matematika": 80, "B. Indonesia": 90, "B. Inggris": 81}
# # sebelum Setdefault
# print(Nilai)
# print("")
# # menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# # setelah menggunakan setdefault
# print(Nilai)

Musik = {
    "The Chainsmoker": ["All we Know", "The Paris"],
    "Alan Walker": ["Alone", "Lily"],
    "Neffex": ["Best of Me", "Memories"],
}
for i, j in Musik.items():
    print(f"Musik milik {i} adalah : ")
    for song in j:
        print(song)
    print("")
