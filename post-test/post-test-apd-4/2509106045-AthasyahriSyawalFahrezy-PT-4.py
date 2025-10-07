import os

username = "pares"
password = "045"
percobaan = 0

while percobaan < 5:
    print("Login dulu broo")
    masukusername = input("Username:    ")
    masukpassword = input("Password:    ")

    if (
        masukusername.lower() == username
        and masukpassword
        == password  # pakai func bawaan python lower() smeua inputan jadi lower jadi biarpun input PARES tetap akan bisa login (Menangangi case-sensitive)
    ):
        print("Login berhasil!")
        break  # keluar dari loop login next ke loop pt sebelumnya (pt-3)
    else:
        percobaan = percobaan + 1
        print(
            "Username/Password mu salah, coba lagi. Sisa percobaan:", 5 - percobaan
        )  # print berapa kali sudah dicoba

if percobaan == 5:
    # bersihkan terminal saat percobaan habis (poin tambah ya banggg)
    os.system("cls" if os.name == "nt" else "clear")
    print("Batas percobaan habis. Program selesai.")  # percobaan dah abis


else:  # lanjut ke posttest sebelumnya (pt-3)
    while True:
        print("\n" + "=" * 40)
        print("SISTEM RENTAL MOBIL")
        print("=" * 40)
        print("1. Proses verifikasi rental")
        print("0. Berhenti")
        pilihan = input("\nPilih menu [0/1]: ")

        if pilihan == "1":
            print("\n--- INPUT DATA CUSTOMER ---")

            # input usia dan validasinya
            usia_input = input("Masukkan usia Anda: ")
            if (
                usia_input.isdigit()
            ):  # isdigit untuk cek apakah isi dari string nya adalah digit (angka)

                usia = int(usia_input)
                if usia < 21:
                    print("\n--- HASIL VERIFIKASI ---")
                    print("TOLAK: Usia tidak mencukupi")
                    print("   Usia minimal 21 tahun untuk rental mobil")
                    print("\n" + "=" * 40)
                    print("    Terima kasih telah menggunakan")
                    print("       sistem rental mobil kami!")
                    print("=" * 40)
                    continue  # beri continue agar saat ditolak ia kembali ke pilih menu
            else:
                print("INPUT TIDAK VALID: Masukkan angka untuk usia")
                print("\n" + "=" * 40)
                print("    Terima kasih telah menggunakan")
                print("       sistem rental mobil kami!")
                print("=" * 40)
                continue  # beri continue agar saat ditolak ia kembali ke pilih menu

            # Validasi input SIM
            sim = input("Apakah Anda memiliki SIM A? (ya/tidak): ").lower()
            if sim == "ya":
                pass  # lanjut ke input berikutnya
            elif sim == "tidak":
                print("\n--- HASIL VERIFIKASI ---")
                print("TOLAK: Tidak memiliki SIM A")
                print("   SIM A diperlukan untuk menyewa mobil")
                print("\n" + "=" * 40)
                print("    Terima kasih telah menggunakan")
                print("       sistem rental mobil kami!")
                print("=" * 40)
                continue  # beri continue agar saat ditolak ia kembali ke pilih menu
            else:
                print("INPUT TIDAK VALID: Ketik 'ya' atau 'tidak' saja")
                print("\n" + "=" * 40)
                print("    Terima kasih telah menggunakan")
                print("       sistem rental mobil kami!")
                print("=" * 40)
                continue  # beri continue agar saat ditolak ia kembali ke pilih menu

            # Validasi input deposit
            deposit_input = input("Masukkan jumlah deposit (Rp): ")
            if (
                deposit_input.isdigit()
            ):  # isdigit untuk cek apakah isi dari string nya adalah digit (angka)
                deposit = int(deposit_input)
                if deposit < 500000:
                    print("\n--- HASIL VERIFIKASI ---")
                    print("TOLAK: Deposit tidak cukup")
                    print(
                        f"   Deposit minimal Rp 500.000, Anda hanya menyetor Rp {deposit:,}"
                    )
                    print("\n" + "=" * 40)
                    print("    Terima kasih telah menggunakan")
                    print("       sistem rental mobil kami!")
                    print("=" * 40)
                    continue  # beri continue agar saat ditolak ia kembali ke pilih menu
            else:
                print("INPUT TIDAK VALID: Masukkan angka untuk deposit")
                print("\n" + "=" * 40)
                print("    Terima kasih telah menggunakan")
                print("       sistem rental mobil kami!")
                print("=" * 40)
                continue  # beri continue agar saat ditolak ia kembali ke pilih menu

            # Validasi input pengalaman
            pengalaman_input = input("Berapa tahun pengalaman mengemudi Anda: ")
            if (
                pengalaman_input.isdigit()
            ):  # isdigit untuk cek apakah isi dari string nya adalah digit (angka)
                pengalaman = int(pengalaman_input)
            else:
                print("INPUT TIDAK VALID: Masukkan angka untuk pengalaman mengemudi")
                print("\n" + "=" * 40)
                print("    Terima kasih telah menggunakan")
                print("       sistem rental mobil kami!")
                print("=" * 40)
                continue  # beri continue agar saat ditolak ia kembali ke pilih menu

            print("\n--- HASIL VERIFIKASI ---")
            if pengalaman < 4:
                print("SETUJUI UNTUK MOBIL STANDAR SAJA")
                print("Pengalaman mengemudi Anda kurang dari 4 tahun")
                print("Mobil premium memerlukan pengalaman minimal 4 tahun")
            else:
                print("SETUJUI UNTUK SEMUA JENIS MOBIL")
                print("Selamat! Anda memenuhi semua persyaratan")
                print("Anda bisa menyewa mobil standar maupun premium")

        elif pilihan == "0":
            # bersihkan terminal saat berhenti (poin tambah)
            os.system("cls" if os.name == "nt" else "clear")
            print("\n" + "=" * 40)
            print("    Terima kasih telah menggunakan")
            print("       sistem rental mobil kami!")
            print("=" * 40)
            print("Program selesai. Sampai jumpa!")
            break  # keluar dari loop menu

        else:
            print("\nPilihan tidak valid.")
            input("Enter untuk kembali ke menu...")
            continue  # beri continue agar kembali ke pilih menu