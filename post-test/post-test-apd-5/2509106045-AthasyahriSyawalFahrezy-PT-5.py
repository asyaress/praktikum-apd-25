import os
import time

akun = [["pares", "045"]] # LIST MENYIMPAN DATA LOGIN DAN REGISTER

lagu = [["pares", "Bohemian Rhapsody", "Queen", "Rock"]] # LIST SIMPAN DATA MUSIK

genre = ["Pop", "Rock", "Jazz", "Hip-Hop", "Electronic", "Classical", "R&B", "Country"] # LIST MENYIMPAN GENRE

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
        i = 0

        while i < len(akun):
            if akun[i][0] == nama:
                if akun[i][1] == sandi:
                    dapatakun = True
                    pengguna_aktif = akun[i][0]
                    break
            i = i + 1

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
            ada = False
            i = 0
            while i < len(akun):
                if akun[i][0] == nama_baru:
                    ada = True
                    break
                i = i + 1
            if ada == True:
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
                    akun.append([nama_baru, sandi_baru])
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

        lagu_saya = []

        i = 0
        while i < len(lagu):
            if lagu[i][0] == pengguna_aktif:
                lagu_saya.append(lagu[i])
            i = i + 1

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
                    print("Judul  :", l[1])
                    print("Artist :", l[2])
                    print("Genre  :", l[3])
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
                    if kata_kunci.lower() in l[1].lower():
                        hasil.append(l)

                if len(hasil) == 0:
                    print("\nTidak ada musik dengan judul tersebut.")
                else:
                    no = 1
                    for l in hasil:
                        print("\nMusik", no)
                        print("-" * 40)
                        print("Judul  :", l[1])
                        print("Artist :", l[2])
                        print("Genre  :", l[3])
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
                    if kata_kunci.lower() in l[2].lower():
                        hasil.append(l)

                if len(hasil) == 0:
                    print("\nTidak ada musik dari artist tersebut.")
                else:
                    no = 1
                    for l in hasil:
                        print("\nMusik", no)
                        print("-" * 40)
                        print("Judul  :", l[1])
                        print("Artist :", l[2])
                        print("Genre  :", l[3])
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
                    if kata_kunci.lower() in l[3].lower():
                        hasil.append(l)

                if len(hasil) == 0:
                    print("\nTidak ada musik dengan genre tersebut.")
                else:
                    no = 1
                    for l in hasil:
                        print("\nMusik", no)
                        print("-" * 40)
                        print("Judul  :", l[1])
                        print("Artist :", l[2])
                        print("Genre  :", l[3])
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
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 60)
        print("TAMBAH MUSIK BARU")
        print("=" * 60)

        judul = input("\nJudul Lagu     : ")

        # ERROR HANDLING (Judul lagu yang di inputkan kosong)
        if judul == "":
            os.system("cls" if os.name == "nt" else "clear")
            print("\nJudul lagu tidak boleh kosong!")
            print("\nBalik ke halaman sebelumnya...")
            hitung = 3
            while hitung > 0:
                print(hitung, "...")
                time.sleep(1)
                hitung = hitung - 1
        else:
            artis = input("Nama Artist    : ")

            # ERROR HANDLING (Artis lagu yang di inputkan kosong)
            if artis == "":
                os.system("cls" if os.name == "nt" else "clear")
                print("\nNama artist tidak boleh kosong!")
                print("\nBalik ke halaman sebelumnya...")
                hitung = 3
                while hitung > 0:
                    print(hitung, "...")
                    time.sleep(1)
                    hitung = hitung - 1
            else:
                print("\nPilih Genre:")
                i = 0
                while i < len(genre):
                    print(str(i + 1) + ".", genre[i])
                    i = i + 1

                pilih_genre = input("\nPilih nomor genre: ")

                # ERROR HANDLING (Genre lagu yang di inputkan selain angka)
                if pilih_genre.isdigit() == False:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("\nInput harus berupa angka!")
                    print("\nBalik ke halaman sebelumnya...")
                    hitung = 3
                    while hitung > 0:
                        print(hitung, "...")
                        time.sleep(1)
                        hitung = hitung - 1
                else:
                    indeks = int(pilih_genre) - 1

                    # ERROR HANDLING (Genre lagu yang di inputkan tidak sesuai nomor genre yang tersedia)
                    if indeks < 0 or indeks >= len(genre):
                        os.system("cls" if os.name == "nt" else "clear")
                        print("\nNomor tidak valid!")
                        print("\nBalik ke halaman sebelumnya...")
                        hitung = 3
                        while hitung > 0:
                            print(hitung, "...")
                            time.sleep(1)
                            hitung = hitung - 1
                    else:
                        genre_dipilih = genre[indeks]
                        lagu.append([pengguna_aktif, judul, artis, genre_dipilih])
                        os.system("cls" if os.name == "nt" else "clear")
                        print("\nMusik berhasil ditambahkan!")
                        print("\nLoading...")
                        hitung = 3
                        while hitung > 0:
                            print(hitung, "...")
                            time.sleep(1)
                            hitung = hitung - 1
    # TAMBAH MUSIK END

    # EDIT MUSIK START
    elif menu == "3":
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 60)
        print("EDIT MUSIK")
        print("=" * 60)

        lagu_saya = []

        i = 0
        while i < len(lagu):
            if lagu[i][0] == pengguna_aktif:
                lagu_saya.append(lagu[i])
            i = i + 1

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
                print(no, ".", l[1], "-", l[2])
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
                    indeks_asli = 0

                    i = 0
                    while i < len(lagu):
                        if lagu[i] == terpilih:
                            indeks_asli = i
                            break
                        i = i + 1

                    print(
                        "\nMasukkan data baru (tekan Enter jika tidak ingin mengubah):"
                    )

                    judul_baru = input("Judul Lagu [" + lagu[indeks_asli][1] + "]: ")
                    if judul_baru != "":
                        lagu[indeks_asli][1] = judul_baru

                    artis_baru = input("Nama Artist [" + lagu[indeks_asli][2] + "]: ")
                    if artis_baru != "":
                        lagu[indeks_asli][2] = artis_baru

                    print("\nPilih Genre Baru:")
                    i = 0
                    while i < len(genre):
                        print(str(i + 1) + ".", genre[i])
                        i = i + 1
                    print("Genre sekarang:", lagu[indeks_asli][3])

                    genre_baru = input(
                        "Pilih nomor genre (atau Enter untuk tidak ubah): "
                    )

                    if genre_baru != "":
                        if genre_baru.isdigit() == False:
                            print("\nInput harus berupa angka! Genre tidak diubah.")
                        else:
                            indeks_genre = int(genre_baru) - 1

                            if indeks_genre < 0 or indeks_genre >= len(genre):
                                print("\nNomor tidak valid! Genre tidak diubah.")
                            else:
                                lagu[indeks_asli][3] = genre[indeks_genre]

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

        lagu_saya = []

        i = 0
        while i < len(lagu):
            if lagu[i][0] == pengguna_aktif:
                lagu_saya.append(lagu[i])
            i = i + 1

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
                print(no, ".", l[1], "-", l[2])
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
                        "Yakin mau hapus '" + terpilih[1] + "'? (ya/tidak): "
                    )

                    if konfirmasi == "ya" or konfirmasi == "Ya" or konfirmasi == "YA":
                        lagu.remove(terpilih)
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
