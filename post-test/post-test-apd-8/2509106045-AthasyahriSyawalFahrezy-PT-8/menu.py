from utils import bersih, loading, input_angka
import state
from auth import pilihan1_login, pilihan2_register, pilihan3_keluar

def menuawal():
    while state.sudah_masuk is False:
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
