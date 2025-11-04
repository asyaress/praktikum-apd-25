from utils import bersih, loading
import state

def edit_musik():
    bersih()
    print("=" * 60)
    print("EDIT MUSIK")
    print("=" * 60)

    lagu_saya = state.lagu.get(state.pengguna_aktif, [])

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
        while i <= len(state.genre):
            print(str(i) + ".", state.genre[i])
            i += 1
        print("Genre sekarang:", terpilih["genre"])

        genre_baru = input("Pilih nomor genre (atau Enter untuk tidak ubah): ")

        if genre_baru != "":
            try:
                indeks_genre = int(genre_baru)
            except ValueError:
                print("\nInput harus berupa angka! Genre tidak diubah.")
            else:
                if 1 <= indeks_genre <= len(state.genre):
                    terpilih["genre"] = state.genre[indeks_genre]
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
