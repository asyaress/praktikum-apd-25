angka = [5, 8, 1, 1, 1, 1, 19]

print("mencari angka yang lebih besar dari 10....")

for i in angka:
    print(f"memeriksa angka: {i}")
    if i > 10:
        print(f"{i} lebih besar dari 10")
        break
    else:
        print("tidak ada angka yang lebih besar dari 10")
print("program selesai")
