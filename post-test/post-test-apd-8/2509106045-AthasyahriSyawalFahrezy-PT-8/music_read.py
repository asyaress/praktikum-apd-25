from utils import bersih, loading
import state

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

    lagu_saya = state.lagu.get(state.pengguna_aktif, [])

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
