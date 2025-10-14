# matakuliah = ["APD", "Kalkulus", "Orsikom"]

# matakuliah = []

# membaca list
# print(matakuliah[1:3])

# print(matakuliah[-1])

# print(matakuliah[1])

# matakuliah.insert("Bahasa Inggris", 1, "Pendidikan Pancasia")

# print(matakuliah)

# praktikum = ["Mahasiswa", 20, True, 45.10, ["APD", 25]]

# print(praktikum[4][0])

# update list

# list awal
# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]

# print(studyclub)

# Kita akan mengganti elemen di indeks ke-2, yakni "Multimedia"
# studyclub[2] = "AI"

# print(studyclub)

# list awal
# matakuliah = ["PTI", "APD", "Kalkulus", "Diskrit"]
# menghapus elemen pada indeks ke-2, yakni "Kalkulus"
# del matakuliah[2]
# matakuliah.remove('PTI')
# print(matakuliah)
# Menghapus & mengambil elemen 'Kalkulus' pada indeks ke-2
# hapus = matakuliah.pop(2)
# print(hapus)
# print(matakuliah)

# list = [1, 2, 3]

# print (sum(list)/len(list))

kelas = [
    ["Ridho", "Lian", "Nabil"],
    ["Daffa", "Dante", "Santoso"],
    ["Pernanda", "Riyadi", "Ahnaf"],
]

for i in kelas:
    for j in i:
        print(j)