from utils import bersih, loading
import state
from rich.console import Console
from rich.panel import Panel
from prettytable import PrettyTable
import questionary
from questionary import Choice

console = Console()


def _print_table(daftar):
    table = PrettyTable()
    table.field_names = ["No", "Judul", "Artist", "Genre"]
    for i, l in enumerate(daftar, start=1):
        table.add_row([i, l.get("judul", ""), l.get("artis", ""), l.get("genre", "")])
    console.print(table)

def cetak_lagu_rekursif(daftar, i=0):
    _print_table(daftar)


def lihat_cari_musik():
    bersih()
    console.rule("[bold]LIHAT/CARI MUSIK[/]")

    pilih_cari = questionary.select(
        "Pilih jenis pencarian:",
        choices=[
            Choice("Lihat semua musik", 1),
            Choice("Cari berdasarkan judul", 2),
            Choice("Cari berdasarkan artist", 3),
            Choice("Cari berdasarkan genre", 4),
        ],
    ).ask()

    if pilih_cari is None:
        bersih()
        console.print("\n[yellow]Aksi dibatalkan.[/]")
        console.print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    lagu_saya = state.lagu.get(state.pengguna_aktif, [])

    if not lagu_saya:
        bersih()
        console.print("\n[yellow]Belum ada musik yang tersimpan.[/]")
        console.print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    if pilih_cari == 1:
        bersih()
        console.rule("[bold]SEMUA MUSIK[/]")
        _print_table(lagu_saya)
        input("\nTekan Enter untuk kembali...")

    elif pilih_cari in (2, 3, 4):
        field_map = {2: "judul", 3: "artis", 4: "genre"}
        field = field_map[pilih_cari]

        while True:
            kata_kunci = questionary.text(f"Masukkan keyword {field}:").ask()
            if kata_kunci is None:
                bersih()
                console.print("\n[yellow]Input dibatalkan.[/]")
                console.print("\nBalik ke halaman sebelumnya...")
                loading()
                return
            kata_kunci = kata_kunci.strip()
            if kata_kunci:
                break
            console.print("[yellow]Keyword tidak boleh kosong.[/]")

        bersih()
        console.rule(f"[bold]HASIL PENCARIAN {field.upper()}[/]")

        hasil = [l for l in lagu_saya if kata_kunci.lower() in l[field].lower()]

        if not hasil:
            console.print("\n[yellow]Tidak ada musik yang cocok.[/]")
        else:
            _print_table(hasil)

        input("\nTekan Enter untuk kembali...")

    else:
        bersih()
        console.print(Panel.fit("[bold red]Pilihan tidak valid![/]"))
        console.print("\nBalik ke halaman sebelumnya...")
        loading()
