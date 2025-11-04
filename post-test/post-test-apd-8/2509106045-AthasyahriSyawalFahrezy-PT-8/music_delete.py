from utils import bersih, loading
import state


def hapus_musik():
    bersih()
    print("=" * 60)
    print("HAPUS MUSIK")
    print("=" * 60)

    lagu_saya = state.lagu.get(state.pengguna_aktif, [])

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
