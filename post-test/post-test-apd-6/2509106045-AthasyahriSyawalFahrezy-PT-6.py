import os
import time

akun = {"pares": "045"}  # DICT MENYIMPAN DATA LOGIN DAN REGISTER

lagu = {
    "pares": [{"judul": "Bohemian Rhapsody", "artis": "Queen", "genre": "Rock"}]
}  # DICT SIMPAN DATA MUSIK

genre = {
    1: "Pop",
    2: "Rock",
    3: "Jazz",
    4: "Hip-Hop",
    5: "Electronic",
    6: "Classical",
    7: "R&B",
    8: "Country",
}  # DICT MENYIMPAN GENRE

pengguna_aktif = ""

os.system("cls" if os.name == "nt" else "clear")
print("=" * 60)
print("SELAMAT DATANG DI MANAJEMEN MUSIK PERSONALMU LET'S PLAY MUSIC")
print("=" * 60)

sudah_masuk = False

# MENU AWAL START
while sudah_masuk == False:
    print("\n--- MENU AWAL ---")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilih = input("\nPilih menu (1-3): ")

    # LOGIN START
    if pilih == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" + "=" * 60)
        print("LOGIN")
        print("=" * 60)

        nama = input("Username: ")
        sandi = input("Password: ")

        dapatakun = False

        if nama in akun and akun[nama] == sandi:
            dapatakun = True
            pengguna_aktif = nama

        if dapatakun == True:
            sudah_masuk = True
            os.system("cls" if os.name == "nt" else "clear")
            print("\nKamu berhasil masuk, WELCOME BROO", pengguna_aktif)
            print("\nMemuat halaman dalam...")
            hitung = 3
            while hitung > 0:
                print(hitung, "...")
                time.sleep(1)
                hitung = hitung - 1
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("\nUsername atau password salah, coba inget-inget dulu!!")
            print("\nKembali dalam...")
            hitung = 3
            while hitung > 0:
                print(hitung, "...")
                time.sleep(1)
                hitung = hitung - 1
            os.system("cls" if os.name == "nt" else "clear")
    # LOGIN END

    # REGISTER START
    elif pilih == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" + "=" * 60)
        print("REGISTER AKUN BARU")
        print("=" * 60)

        nama_baru = input("Username baru: ")

        if nama_baru == "":
            os.system("cls" if os.name == "nt" else "clear")
            print("\nUsername tidak boleh kosong!")
            print("\nBalik ke halaman sebelumnya...")
            hitung = 3
            while hitung > 0:
                print(hitung, "...")
                time.sleep(1)
                hitung = hitung - 1
            os.system("cls" if os.name == "nt" else "clear")
        else:
            if nama_baru in akun:
                os.system("cls" if os.name == "nt" else "clear")
                print("\nUsername sudah digunakan! Pilih username lain.")
                print("\nBalik ke halaman sebelumnya...")
                hitung = 3
                while hitung > 0:
                    print(hitung, "...")
                    time.sleep(1)
                    hitung = hitung - 1
                os.system("cls" if os.name == "nt" else "clear")
            else:
                sandi_baru = input("Password baru: ")

                if sandi_baru == "":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("\nPassword tidak boleh kosong!")
                    print("\nBalik ke halaman sebelumnya...")
                    hitung = 3
                    while hitung > 0:
                        print(hitung, "...")
                        time.sleep(1)
                        hitung = hitung - 1
                    os.system("cls" if os.name == "nt" else "clear")
                else:
                    akun[nama_baru] = sandi_baru
                    os.system("cls" if os.name == "nt" else "clear")
                    print("\nRegister berhasil! Silakan login.")
                    print("\nBalik ke halaman sebelumnya...")
                    hitung = 3
                    while hitung > 0:
                        print(hitung, "...")
                        time.sleep(1)
                        hitung = hitung - 1
                    os.system("cls" if os.name == "nt" else "clear")
        # REGISTER END

    # LOGOUT START
    elif pilih == "3":
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" + "=" * 60)
        print("Terima kasih! See you next time!")
        print("=" * 60)
        exit()
    # LOGOUT END

    # ERROR HANDLING
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("\nPilihan tidak valid!")
        print("\nBalik ke halaman sebelumnya...")
        hitung = 3
        while hitung > 0:
            print(hitung, "...")
            time.sleep(1)
            hitung = hitung - 1
        os.system("cls" if os.name == "nt" else "clear")
# MENU AWAL END

# DASHBOARD START
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 60)
    print("User:", pengguna_aktif)
    print("=" * 60)

    print("\n--- WELCOME TO DASHBOARD ---")
    print("1. Lihat/Cari musik?")
    print("2. Tambah musik baru")
    print("3. Edit musik")
    print("4. Hapus musik")
    print("5. Logout")

    menu = input("\nMasukkan pilihan (1-5): ")

    # LIHAT/CARI MUSIK START
    if menu == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 60)
        print("LIHAT/CARI MUSIK")
        print("=" * 60)

        print("\n--- PILIHAN PENCARIAN ---")
        print("1. Lihat semua musik")
        print("2. Cari berdasarkan judul")
        print("3. Cari berdasarkan artist")
        print("4. Cari berdasarkan genre")

        pilih_cari = input("\nPilih jenis pencarian (1-4): ")

        lagu_saya = lagu.get(pengguna_aktif, [])

        # ERROR HANDLING (JIKA BELUM ADA DATA MUSIK)
        if len(lagu_saya) == 0:
            os.system("cls" if os.name == "nt" else "clear")
            print("\nBelum ada musik yang tersimpan.")
            print("\nBalik ke halaman sebelumnya...")
            hitung = 3
            while hitung > 0:
                print(hitung, "...")
                time.sleep(1)
                hitung = hitung - 1

        else:
            # TAMPIL SEMUA MUSIK START
            if pilih_cari == "1":
                os.system("cls" if os.name == "nt" else "clear")
                print("=" * 60)
                print("SEMUA MUSIK")
                print("=" * 60)
                no = 1
                for l in lagu_saya:
                    print("\nMusik", no)
                    print("-" * 40)
                    print("Judul  :", l["judul"])
                    print("Artist :", l["artis"])
                    print("Genre  :", l["genre"])
                    no = no + 1

                input("\nTekan Enter untuk kembali...")
            # TAMPIL SEMUA MUSIK END

            # SEARCH MUSIK BY KEYWORD JUDUL START
            elif pilih_cari == "2":
                kata_kunci = input("\nMasukkan keyword judul: ")

                os.system("cls" if os.name == "nt" else "clear")
                print("=" * 60)
                print("HASIL PENCARIAN JUDUL")
                print("=" * 60)

                hasil = []
                for l in lagu_saya:
                    if kata_kunci.lower() in l["judul"].lower():
                        hasil.append(l)

                if len(hasil) == 0:
                    print("\nTidak ada musik dengan judul tersebut.")
                else:
                    no = 1
                    for l in hasil:
                        print("\nMusik", no)
                        print("-" * 40)
                        print("Judul  :", l["judul"])
                        print("Artist :", l["artis"])
                        print("Genre  :", l["genre"])
                        no = no + 1

                input("\nTekan Enter untuk kembali...")
            # SEARCH MUSIK BY KEYWORD JUDUL END

            # SEARCH MUSIK BY KEYWORD ARTIS START
            elif pilih_cari == "3":
                kata_kunci = input("\nMasukkan keyword artist: ")

                os.system("cls" if os.name == "nt" else "clear")
                print("=" * 60)
                print("HASIL PENCARIAN ARTIST")
                print("=" * 60)

                hasil = []
                for l in lagu_saya:
                    if kata_kunci.lower() in l["artis"].lower():
                        hasil.append(l)

                if len(hasil) == 0:
                    print("\nTidak ada musik dari artist tersebut.")
                else:
                    no = 1
                    for l in hasil:
                        print("\nMusik", no)
                        print("-" * 40)
                        print("Judul  :", l["judul"])
                        print("Artist :", l["artis"])
                        print("Genre  :", l["genre"])
                        no = no + 1

                input("\nTekan Enter untuk kembali...")
            # SEARCH MUSIK BY KEYWORD ARTIS END

            # SEARCH MUSIK BY KEYWORD GENRE START
            elif pilih_cari == "4":
                kata_kunci = input("\nMasukkan keyword genre: ")

                os.system("cls" if os.name == "nt" else "clear")
                print("=" * 60)
                print("HASIL PENCARIAN GENRE")
                print("=" * 60)

                hasil = []
                for l in lagu_saya:
                    if kata_kunci.lower() in l["genre"].lower():
                        hasil.append(l)

                if len(hasil) == 0:
                    print("\nTidak ada musik dengan genre tersebut.")
                else:
                    no = 1
                    for l in hasil:
                        print("\nMusik", no)
                        print("-" * 40)
                        print("Judul  :", l["judul"])
                        print("Artist :", l["artis"])
                        print("Genre  :", l["genre"])
                        no = no + 1

                input("\nTekan Enter untuk kembali...")
            # SEARCH MUSIK BY KEYWORD GENRE END

            # ERROR HANDLING (Pilihan selain 1-4)
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print("\nPilihan tidak valid!")
                print("\nBalik ke halaman sebelumnya...")
                hitung = 3
                while hitung > 0:
                    print(hitung, "...")
                    time.sleep(1)
                    hitung = hitung - 1
    # LIHAT/CARI MUSIK END

    # TAMBAH MUSIK START 
    elif menu == "2":
        while True:
            print("\n=== TAMBAH MUSIK BARU ===")

            judul = input("Judul Lagu : ").strip()
            if not judul:
                os.system("cls" if os.name == "nt" else "clear")
                print("Judul tidak boleh kosong.\n")
                continue
            if judul.isdigit():
                os.system("cls" if os.name == "nt" else "clear")
                print("Judul tidak boleh hanya angka.\n")
                continue

            artis = input("Nama Artist: ").strip()
            if not artis:
                os.system("cls" if os.name == "nt" else "clear")
                print("Artist tidak boleh kosong.\n")
                continue
            if artis.isdigit():
                os.system("cls" if os.name == "nt" else "clear")
                print("Artist tidak boleh hanya angka.\n")
                continue

            print("\nPilih Genre:")
            for i in range(1, len(genre) + 1):
                print(f"{i}. {genre[i]}")
            pilih_genre = input("Nomor genre: ").strip()

            if not pilih_genre.isdigit():
                print("masukkan angka.\n")
                continue

            indeks = int(pilih_genre)
            if indeks < 1 or indeks > len(genre):
                print("nomor genre tidak valid.\n")
                continue

            genre_dipilih = genre[indeks]

            if pengguna_aktif not in lagu:
                lagu[pengguna_aktif] = []
            lagu[pengguna_aktif].append(
                {"judul": judul, "artis": artis, "genre": genre_dipilih}
            )

            print("\nMusik berhasil ditambahkan!\n")

            lagi = input("Tambah musik lagi? (y/n): ").strip().lower()
            if lagi != "y":
                break
    # TAMBAH MUSIK END

    # EDIT MUSIK START
    elif menu == "3":
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 60)
        print("EDIT MUSIK")
        print("=" * 60)

        lagu_saya = lagu.get(pengguna_aktif, [])

        # ERROR HANDLING (tidak ada data musik, takda yang bisa di edit)
        if len(lagu_saya) == 0:
            os.system("cls" if os.name == "nt" else "clear")
            print("\nBelum ada musik yang bisa diedit.")
            print("\nBalik ke halaman sebelumnya...")
            hitung = 3
            while hitung > 0:
                print(hitung, "...")
                time.sleep(1)
                hitung = hitung - 1
        else:
            print("\nDaftar Musik:")
            no = 1
            for l in lagu_saya:
                print(no, ".", l["judul"], "-", l["artis"])
                no = no + 1

            pilih_edit = input("\nPilih nomor musik yang mau diedit: ")

            if pilih_edit.isdigit() == False:
                os.system("cls" if os.name == "nt" else "clear")
                print("\nInput harus berupa angka!")
                print("\nBalik ke halaman sebelumnya...")
                hitung = 3
                while hitung > 0:
                    print(hitung, "...")
                    time.sleep(1)
                    hitung = hitung - 1
            else:
                indeks = int(pilih_edit) - 1

                if indeks < 0 or indeks >= len(lagu_saya):
                    os.system("cls" if os.name == "nt" else "clear")
                    print("\nNomor tidak valid!")
                    print("\nBalik ke halaman sebelumnya...")
                    hitung = 3
                    while hitung > 0:
                        print(hitung, "...")
                        time.sleep(1)
                        hitung = hitung - 1
                else:
                    terpilih = lagu_saya[indeks]

                    print(
                        "\nMasukkan data baru (tekan Enter jika tidak ingin mengubah):"
                    )

                    judul_baru = input("Judul Lagu [" + terpilih["judul"] + "]: ")
                    if judul_baru != "":
                        terpilih["judul"] = judul_baru

                    artis_baru = input("Nama Artist [" + terpilih["artis"] + "]: ")
                    if artis_baru != "":
                        terpilih["artis"] = artis_baru

                    print("\nPilih Genre Baru:")
                    i = 1
                    while i <= len(genre):
                        print(str(i) + ".", genre[i])
                        i = i + 1
                    print("Genre sekarang:", terpilih["genre"])

                    genre_baru = input(
                        "Pilih nomor genre (atau Enter untuk tidak ubah): "
                    )

                    if genre_baru != "":
                        if genre_baru.isdigit() == False:
                            print("\nInput harus berupa angka! Genre tidak diubah.")
                        else:
                            indeks_genre = int(genre_baru)

                            if indeks_genre < 1 or indeks_genre > len(genre):
                                print("\nNomor tidak valid! Genre tidak diubah.")
                            else:
                                terpilih["genre"] = genre[indeks_genre]

                    os.system("cls" if os.name == "nt" else "clear")
                    print("\nMusik berhasil diedit!")
                    print("\nLoading...")
                    hitung = 3
                    while hitung > 0:
                        print(hitung, "...")
                        time.sleep(1)
                        hitung = hitung - 1
    # EDIT MUSIK END

    # HAPUS MUSIK START
    elif menu == "4":
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 60)
        print("HAPUS MUSIK")
        print("=" * 60)

        lagu_saya = lagu.get(pengguna_aktif, [])

        if len(lagu_saya) == 0:
            os.system("cls" if os.name == "nt" else "clear")
            print("\nBelum ada musik yang bisa dihapus.")
            print("\nBalik ke halaman sebelumnya...")
            hitung = 3
            while hitung > 0:
                print(hitung, "...")
                time.sleep(1)
                hitung = hitung - 1
        else:
            print("\nDaftar Musik:")
            no = 1
            for l in lagu_saya:
                print(no, ".", l["judul"], "-", l["artis"])
                no = no + 1

            pilih_hapus = input("\nPilih nomor musik yang mau dihapus: ")

            if pilih_hapus.isdigit() == False:
                os.system("cls" if os.name == "nt" else "clear")
                print("\nInput harus berupa angka!")
                print("\nBalik ke halaman sebelumnya...")
                hitung = 3
                while hitung > 0:
                    print(hitung, "...")
                    time.sleep(1)
                    hitung = hitung - 1
            else:
                indeks = int(pilih_hapus) - 1

                if indeks < 0 or indeks >= len(lagu_saya):
                    os.system("cls" if os.name == "nt" else "clear")
                    print("\nNomor tidak valid!")
                    print("\nBalik ke halaman sebelumnya...")
                    hitung = 3
                    while hitung > 0:
                        print(hitung, "...")
                        time.sleep(1)
                        hitung = hitung - 1
                else:
                    terpilih = lagu_saya[indeks]
                    konfirmasi = input(
                        "Yakin mau hapus '" + terpilih["judul"] + "'? (ya/tidak): "
                    )

                    if konfirmasi == "ya" or konfirmasi == "Ya" or konfirmasi == "YA":
                        del lagu_saya[indeks]
                        os.system("cls" if os.name == "nt" else "clear")
                        print("\nMusik berhasil dihapus!")
                        print("\nLoading...")
                        hitung = 3
                        while hitung > 0:
                            print(hitung, "...")
                            time.sleep(1)
                            hitung = hitung - 1
                    else:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("\nPenghapusan dibatalkan.")
                        print("\nBalik ke halaman sebelumnya...")
                        hitung = 3
                        while hitung > 0:
                            print(hitung, "...")
                            time.sleep(1)
                            hitung = hitung - 1
    # HAPUS MUSIK END

    # LOGOUT START
    elif menu == "5":
        konfirmasi = input("\nYakin mau logout? (ya/tidak): ")

        if konfirmasi == "ya" or konfirmasi == "Ya" or konfirmasi == "YA":
            os.system("cls" if os.name == "nt" else "clear")
            print("\nLogout berhasil!")
            print("\n" + "=" * 60)
            print("Terima kasih sudah menggunakan Manajemen Musik Personal!")
            print("Sampai jumpa lagi!")
            print("=" * 60)
            break
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("\nLogout dibatalkan.")
            print("\nBalik ke halaman sebelumnya...")
            hitung = 3
            while hitung > 0:
                print(hitung, "...")
                time.sleep(1)
                hitung = hitung - 1
    # LOGOUT END

    # ERROR HANDLING (Jika pilihan yang dipilih tidak valid)
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("\nPilihan tidak valid!")
        print("\nBalik ke halaman sebelumnya...")
        hitung = 3
        while hitung > 0:
            print(hitung, "...")
            time.sleep(1)
            hitung = hitung - 1
# DASHBOARD END
