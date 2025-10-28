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

def bersih():
    os.system("cls" if os.name == "nt" else "clear")

def loading():
    hitung = 3
    while hitung > 0:
        print(hitung, "...")
        time.sleep(1)
        hitung -= 1

def input_angka(prompt):
    try:
        angka = int(input(prompt))
    except ValueError:
        print("input yang kamu masukkan bukan angka, harus angka broo!!")
        return None
    else:
        print(f"Angka yang kamu input : {angka}")
        return angka
    finally:
        print("Kelar dah")

def cek_input_kosong(pesan):
    while True:
        try:
            nilai = input(pesan).strip()
        except:
            print("\nInput dibatalkan. Silakan coba lagi.")
            continue
        if nilai == "":
            print("Input tidak boleh kosong. Coba lagi.")
        else:
            return nilai

print("=" * 60)
print("SELAMAT DATANG DI MANAJEMEN MUSIK PERSONALMU LET'S PLAY MUSIC")
print("=" * 60)

sudah_masuk = False


# MENU AWAL START
def pilihan1_login():
    global pengguna_aktif, sudah_masuk
    bersih()
    print("\n" + "=" * 60)
    print("LOGIN")
    print("=" * 60)

    nama = cek_input_kosong("Username: ")
    sandi = cek_input_kosong("Password: ")

    dapatakun = False

    if nama in akun and akun[nama] == sandi:
        dapatakun = True
        pengguna_aktif = nama

    if dapatakun is True:
        sudah_masuk = True
        bersih()
        print("\nKamu berhasil masuk, WELCOME BROO", pengguna_aktif)
        print("\nMemuat halaman dalam...")
        loading()
        dashboard()

    else:
        bersih()
        print("\nUsername atau password salah, coba inget-inget dulu!!")
        print("\nKembali dalam...")
        loading()
        bersih()

def pilihan2_register():
    bersih()
    print("\n" + "=" * 60)
    print("REGISTER AKUN BARU")
    print("=" * 60)

    nama_baru = cek_input_kosong("Username baru: ")

    if nama_baru in akun:
        bersih()
        print("\nUsername sudah digunakan! Pilih username lain.")
        print("\nBalik ke halaman sebelumnya...")
        loading()
        bersih()
        return

    sandi_baru = cek_input_kosong("Password baru: ")

    akun[nama_baru] = sandi_baru
    bersih()
    print("\nRegister berhasil! Silakan login.")
    print("\nBalik ke halaman sebelumnya...")
    loading()
    bersih()

def pilihan3_keluar():
    bersih()
    print("\n" + "=" * 60)
    print("Makasih ya! Gue bakal kangen lo!")
    print("=" * 60)
    exit()

def menuawal():
    global sudah_masuk
    while sudah_masuk is False:
        print("\n--- MENU AWAL ---")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")

        pilih = input_angka("\nPilih menu (1-3): ")

        if pilih is None:
            print("\nBalik ke halaman sebelumnya...")
            loading()
            bersih()
            continue

        if pilih == 1:
            pilihan1_login()
        elif pilih == 2:
            pilihan2_register()
        elif pilih == 3:
            pilihan3_keluar()
        else:
            bersih()
            print("\nPilihan tidak valid!")
            print("\nBalik ke halaman sebelumnya...")
            loading()
            bersih()
# MENU AWAL END


# DASHBOARD START
def cetak_lagu_rekursif(daftar, i=0):
    if i == len(daftar):
        return
    l = daftar[i]
    print(f"\nMusik {i+1}")
    print("-" * 40)
    print("Judul  :", l.get("judul", ""))
    print("Artist :", l.get("artis", ""))
    print("Genre  :", l.get("genre", ""))
    cetak_lagu_rekursif(daftar, i + 1)

def lihat_cari_musik():
    bersih()
    print("=" * 60)
    print("LIHAT/CARI MUSIK")
    print("=" * 60)

    print("\n--- PILIHAN PENCARIAN ---")
    print("1. Lihat semua musik")
    print("2. Cari berdasarkan judul")
    print("3. Cari berdasarkan artist")
    print("4. Cari berdasarkan genre")

    try:
        pilih_cari = int(input("\nPilih jenis pencarian (1-4): "))
    except ValueError:
        bersih()
        print("\nInput harus angka 1-4.")
        print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    lagu_saya = lagu.get(pengguna_aktif, [])

    if not lagu_saya:
        bersih()
        print("\nBelum ada musik yang tersimpan.")
        print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    if pilih_cari == 1:
        bersih()
        print("=" * 60)
        print("SEMUA MUSIK")
        print("=" * 60)
        cetak_lagu_rekursif(lagu_saya)
        input("\nTekan Enter untuk kembali...")

    elif pilih_cari in (2, 3, 4):
        field_map = {2: "judul", 3: "artis", 4: "genre"}
        field = field_map[pilih_cari]

        try:
            kata_kunci = input(f"\nMasukkan keyword {field}: ").strip()
            if not kata_kunci:
                raise ValueError("Keyword tidak boleh kosong.")
        except ValueError as e:
            bersih()
            print(f"\n{e}")
            print("\nBalik ke halaman sebelumnya...")
            loading()
            return

        bersih()
        print("=" * 60)
        print(f"HASIL PENCARIAN {field.upper()}")
        print("=" * 60)

        hasil = [l for l in lagu_saya if kata_kunci.lower() in l[field].lower()]

        if not hasil:
            print("\nTidak ada musik yang cocok.")
        else:
            cetak_lagu_rekursif(hasil)

        input("\nTekan Enter untuk kembali...")

    else:
        bersih()
        print("\nPilihan tidak valid!")
        print("\nBalik ke halaman sebelumnya...")
        loading()

def tambah_musik():
    while True:
        try:
            print("\n=== TAMBAH MUSIK BARU ===")

            judul = input("Judul Lagu : ").strip()
            if not judul:
                bersih()
                print("Judul tidak boleh kosong.\n")
                continue
            if judul.isdigit():
                bersih()
                print("Judul tidak boleh hanya angka.\n")
                continue

            artis = input("Nama Artist: ").strip()
            if not artis:
                bersih()
                print("Artist tidak boleh kosong.\n")
                continue
            if artis.isdigit():
                bersih()
                print("Artist tidak boleh hanya angka.\n")
                continue

            print("\nPilih Genre:")
            for i in range(1, len(genre) + 1):
                print(f"{i}. {genre[i]}")
            pilih_genre = input("Nomor genre: ").strip()

            try:
                indeks = int(pilih_genre)
            except ValueError:
                print("masukkan angka.\n")
                continue

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

        except (KeyboardInterrupt, EOFError):
            bersih()
            print("\nInput dibatalkan.")
            print("\nBalik ke halaman sebelumnya...")
            loading()
            break

def edit_musik():
    bersih()
    print("=" * 60)
    print("EDIT MUSIK")
    print("=" * 60)

    lagu_saya = lagu.get(pengguna_aktif, [])

    if len(lagu_saya) == 0:
        bersih()
        print("\nBelum ada musik yang bisa diedit.")
        print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    print("\nDaftar Musik:")
    no = 1
    for l in lagu_saya:
        print(no, ".", l["judul"], "-", l["artis"])
        no += 1

    try:
        pilih_edit = input("\nPilih nomor musik yang mau diedit: ")
    except (KeyboardInterrupt, EOFError):
        bersih()
        print("\nInput dibatalkan.")
        print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    try:
        indeks = int(pilih_edit) - 1
    except ValueError:
        bersih()
        print("\nInput harus berupa angka!")
        print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    if indeks < 0 or indeks >= len(lagu_saya):
        bersih()
        print("\nNomor tidak valid!")
        print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    terpilih = lagu_saya[indeks]

    try:
        print("\nMasukkan data baru (tekan Enter jika tidak ingin mengubah):")
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
            i += 1
        print("Genre sekarang:", terpilih["genre"])

        genre_baru = input("Pilih nomor genre (atau Enter untuk tidak ubah): ")

        if genre_baru != "":
            try:
                indeks_genre = int(genre_baru)
            except ValueError:
                print("\nInput harus berupa angka! Genre tidak diubah.")
            else:
                if 1 <= indeks_genre <= len(genre):
                    terpilih["genre"] = genre[indeks_genre]
                else:
                    print("\nNomor tidak valid! Genre tidak diubah.")

    except (KeyboardInterrupt, EOFError):
        bersih()
        print("\nInput dibatalkan. Tidak ada perubahan yang disimpan.")
        print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    bersih()
    print("\nMusik berhasil diedit!")
    print("\nLoading...")
    loading()

def hapus_musik():
    bersih()
    print("=" * 60)
    print("HAPUS MUSIK")
    print("=" * 60)

    lagu_saya = lagu.get(pengguna_aktif, [])

    if len(lagu_saya) == 0:
        bersih()
        print("\nBelum ada musik yang bisa dihapus.")
        print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    print("\nDaftar Musik:")
    no = 1
    for l in lagu_saya:
        print(no, ".", l["judul"], "-", l["artis"])
        no += 1

    try:
        pilih_hapus = input("\nPilih nomor musik yang mau dihapus: ")
    except (KeyboardInterrupt, EOFError):
        bersih()
        print("\nInput dibatalkan.")
        print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    try:
        indeks = int(pilih_hapus) - 1
    except ValueError:
        bersih()
        print("\nInput harus berupa angka!")
        print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    if indeks < 0 or indeks >= len(lagu_saya):
        bersih()
        print("\nNomor tidak valid!")
        print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    terpilih = lagu_saya[indeks]

    try:
        konfirmasi = input(
            f"Yakin mau hapus '{terpilih['judul']}'? (ya/tidak): "
        ).strip()
    except (KeyboardInterrupt, EOFError):
        bersih()
        print("\nInput dibatalkan.")
        print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    if konfirmasi.lower() == "ya":
        try:
            del lagu_saya[indeks]
        except Exception:
            bersih()
            print("\nTerjadi kesalahan saat menghapus.")
            print("\nBalik ke halaman sebelumnya...")
            loading()
            return

        bersih()
        print("\nMusik berhasil dihapus!")
        print("\nLoading...")
        loading()
    else:
        bersih()
        print("\nPenghapusan dibatalkan.")
        print("\nBalik ke halaman sebelumnya...")
        loading()

def logout_dashboard():
    try:
        konfirmasi = input("\nYakin mau logout? (ya/tidak): ").strip().lower()
    except (KeyboardInterrupt, EOFError):
        bersih()
        print("\nInput dibatalkan.")
        print("\nBalik ke halaman sebelumnya...")
        loading()
        return False

    if konfirmasi in ("ya", "y"):
        bersih()
        print("\nLogout berhasil!")
        print("\n" + "=" * 60)
        print("Terima kasih sudah menggunakan Manajemen Musik Personal!")
        print("Sampai jumpa lagi!")
        print("=" * 60)
        return True
    elif konfirmasi in ("tidak", "t", "no", "n"):
        bersih()
        print("\nLogout dibatalkan.")
        print("\nBalik ke halaman sebelumnya...")
        loading()
        return False
    else:
        bersih()
        print("\nInput tidak valid! Gunakan 'ya' atau 'tidak'.")
        print("\nBalik ke halaman sebelumnya...")
        loading()
        return False

def dashboard():
    while True:
        bersih()
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

        if menu == "1":
            lihat_cari_musik()
        elif menu == "2":
            tambah_musik()
        elif menu == "3":
            edit_musik()
        elif menu == "4":
            hapus_musik()
        elif menu == "5":
            if logout_dashboard():
                break
        else:
            bersih()
            print("\nPilihan tidak valid!")
            print("\nBalik ke halaman sebelumnya...")
            loading()
# DASHBOARD END

if __name__ == "__main__":
    menuawal()
