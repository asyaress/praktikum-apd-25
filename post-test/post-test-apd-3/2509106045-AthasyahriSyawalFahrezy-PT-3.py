print("="*40)
print("    SISTEM RENTAL MOBIL")
print("="*40)

print("\n--- INPUT DATA CUSTOMER ---")

# input usia dan validasinya
usia_input = input("Masukkan usia Anda: ")
if usia_input.isdigit(): #isdigit untuk cek apakah isi dari string nya adalah digit (angka) 
    usia = int(usia_input)
    if usia < 21:
        print("\n--- HASIL VERIFIKASI ---")
        print("❌ TOLAK: Usia tidak mencukupi")
        print("   Usia minimal 21 tahun untuk rental mobil")
        print("\n" + "="*40)
        print("    Terima kasih telah menggunakan")
        print("       sistem rental mobil kami!")
        print("="*40)
        exit()
else:
    print("❌ INPUT TIDAK VALID: Masukkan angka untuk usia")
    print("\n" + "="*40)
    print("    Terima kasih telah menggunakan")
    print("       sistem rental mobil kami!")
    print("="*40)
    exit()

# Validasi input SIM
sim = input("Apakah Anda memiliki SIM A? (ya/tidak): ").lower()
if sim == "ya":
    pass  # lanjut ke input berikutnya
elif sim == "tidak":
    print("\n--- HASIL VERIFIKASI ---")
    print("❌ TOLAK: Tidak memiliki SIM A")
    print("   SIM A diperlukan untuk menyewa mobil")
    print("\n" + "="*40)
    print("    Terima kasih telah menggunakan")
    print("       sistem rental mobil kami!")
    print("="*40)
    exit()
else:
    print("❌ INPUT TIDAK VALID: Ketik 'ya' atau 'tidak' saja")
    print("\n" + "="*40)
    print("    Terima kasih telah menggunakan")
    print("       sistem rental mobil kami!")
    print("="*40)
    exit()

# Validasi input deposit
deposit_input = input("Masukkan jumlah deposit (Rp): ")
if deposit_input.isdigit(): #isdigit untuk cek apakah isi dari string nya adalah digit (angka) 
    deposit = int(deposit_input)
    if deposit < 500000:
        print("\n--- HASIL VERIFIKASI ---")
        print("❌ TOLAK: Deposit tidak cukup")
        print(f"   Deposit minimal Rp 500.000, Anda hanya menyetor Rp {deposit:,}")
        print("\n" + "="*40)
        print("    Terima kasih telah menggunakan")
        print("       sistem rental mobil kami!")
        print("="*40)
        exit()
else:
    print("❌ INPUT TIDAK VALID: Masukkan angka untuk deposit")
    print("\n" + "="*40)
    print("    Terima kasih telah menggunakan")
    print("       sistem rental mobil kami!")
    print("="*40)
    exit()

# Validasi input pengalaman
pengalaman_input = input("Berapa tahun pengalaman mengemudi Anda: ")
if pengalaman_input.isdigit(): #isdigit untuk cek apakah isi dari string nya adalah digit (angka) 
    pengalaman = int(pengalaman_input)
else:
    print("❌ INPUT TIDAK VALID: Masukkan angka untuk pengalaman mengemudi")
    print("\n" + "="*40)
    print("    Terima kasih telah menggunakan")
    print("       sistem rental mobil kami!")
    print("="*40)
    exit()

print("\n--- HASIL VERIFIKASI ---")
if pengalaman < 4:
    print("✅ SETUJUI UNTUK MOBIL STANDAR SAJA")
    print("   Pengalaman mengemudi Anda kurang dari 4 tahun")
    print("   Mobil premium memerlukan pengalaman minimal 4 tahun")
else:
    print("✅ SETUJUI UNTUK SEMUA JENIS MOBIL")
    print("   Selamat! Anda memenuhi semua persyaratan")
    print("   Anda bisa menyewa mobil standar maupun premium")

print("\n" + "="*40)
print("    Terima kasih telah menggunakan")
print("       sistem rental mobil kami!")
print("="*40)