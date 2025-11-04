from utils import bersih, loading
import state

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
            for i in range(1, len(state.genre) + 1):
                print(f"{i}. {state.genre[i]}")
            pilih_genre = input("Nomor genre: ").strip()

            try:
                indeks = int(pilih_genre)
            except ValueError:
                print("masukkan angka.\n")
                continue

            if indeks < 1 or indeks > len(state.genre):
                print("nomor genre tidak valid.\n")
                continue

            genre_dipilih = state.genre[indeks]

            if state.pengguna_aktif not in state.lagu:
                state.lagu[state.pengguna_aktif] = []
            state.lagu[state.pengguna_aktif].append(
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
