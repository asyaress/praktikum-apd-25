total_harga = float(input("Masukkan total belanja:      "))

if total_harga >= 100000 and total_harga <= 1000000:
    harga_akhir = total_harga - (total_harga * 0.20)
    print("Total hargamu" , harga_akhir)
elif total_harga >= 50000 and total_harga <100000:
    harga_akhir = total_harga - (total_harga * 0.10)
    print("Total hargamu" , harga_akhir)
else:
    print("Harganya", total_harga , "maaf kamu tidak dapat diskon")
  