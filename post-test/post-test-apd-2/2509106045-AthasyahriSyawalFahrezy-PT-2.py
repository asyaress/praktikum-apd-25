# Program Input Menu Coffee Shop
print("=" * 55)
print("         PROGRAM INPUT MENU COFFEE SHOP")
print("=" * 55)

print("\nSilahkan masukkan data menu coffee shop:")
print("-" * 45)

# Input yang menggunakan tipe data string
nama_menu = input("Nama Menu           : ")
deskripsi_menu = input("Deskripsi Menu      : ")

# Input yang menggunakan tipe data integer
kode_menu = int(input("Kode Menu           : "))
stok_tersedia = int(input("Stok Tersedia       : "))

# Input yang menggunakan tipe data float untuk harga
harga_modal = float(input("Harga Modal (Rp)    : "))
harga_jual = float(input("Harga Jual (Rp)     : "))

# Input yang menggunakan tipe data boolean
print("\nPertanyaan (jawab dengan y/n):")
input_menu_unggulan = input("Apakah menu unggulan? (y/n): ").lower()
menu_unggulan = input_menu_unggulan == "y"  # Konversi ke boolean

input_tersedia = input("Apakah menu tersedia hari ini? (y/n): ").lower()
menu_tersedia = input_tersedia == "y"  # Konversi ke boolean

# Busines logic
keuntungan_per_item = harga_jual - harga_modal
persentase_keuntungan = (keuntungan_per_item / harga_modal) * 100
total_nilai_stok = stok_tersedia * harga_modal
potensi_pendapatan = stok_tersedia * harga_jual
total_keuntungan_maksimal = stok_tersedia * keuntungan_per_item

# Print hasil dari semua input
print("\n" + "=" * 55)
print("              DETAIL MENU COFFEE SHOP")
print("=" * 55)

print(f"Kode Menu           : {kode_menu}")
print(f"Nama Menu           : {nama_menu}")
print(f"Deskripsi           : {deskripsi_menu}")

print("\n--- INFORMASI HARGA ---")
print(f"Harga Modal         : Rp {harga_modal:,.2f}")
print(f"Harga Jual          : Rp {harga_jual:,.2f}")
print(f"Keuntungan per Item : Rp {keuntungan_per_item:,.2f}")
print(f"Margin Keuntungan   : {persentase_keuntungan:.1f}%")

print("\n--- INFORMASI STOK ---")
print(f"Stok Tersedia       : {stok_tersedia} Gelas")
print(f"Total Nilai Stok    : Rp {total_nilai_stok:,.2f}")
print(f"Potensi Pendapatan  : Rp {potensi_pendapatan:,.2f}")
print(f"Total Keuntungan Max: Rp {total_keuntungan_maksimal:,.2f}")

print("\n--- STATUS MENU ---")
print(f"Menu Unggulan       : {menu_unggulan} (boolean)")
print(f"Tersedia Hari Ini   : {menu_tersedia} (boolean)")

print("=" * 55)
print("        Data menu berhasil diinput dan dianalisis!")
print("=" * 55)