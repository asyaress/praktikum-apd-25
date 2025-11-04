from utils import bersih, loading, cek_input_kosong
import state
from dashboard import dashboard


def pilihan1_login():
    bersih()
    print("\n" + "=" * 60)
    print("LOGIN")
    print("=" * 60)

    nama = cek_input_kosong("Username: ")
    sandi = cek_input_kosong("Password: ")

    dapatakun = False

    if nama in state.akun and state.akun[nama] == sandi:
        dapatakun = True
        state.pengguna_aktif = nama

    if dapatakun is True:
        state.sudah_masuk = True
        bersih()
        print("\nKamu berhasil masuk, WELCOME BROO", state.pengguna_aktif)
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

    if nama_baru in state.akun:
        bersih()
        print("\nUsername sudah digunakan! Pilih username lain.")
        print("\nBalik ke halaman sebelumnya...")
        loading()
        bersih()
        return

    sandi_baru = cek_input_kosong("Password baru: ")

    state.akun[nama_baru] = sandi_baru
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
