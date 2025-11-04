from utils import bersih, loading
import state

from music_read import lihat_cari_musik
from music_create import tambah_musik
from music_update import edit_musik
from music_delete import hapus_musik

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
        print("User:", state.pengguna_aktif)
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
