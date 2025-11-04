import os
import time

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
