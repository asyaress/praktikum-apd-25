from utils import bersih, loading
import state
from rich.console import Console
from rich.panel import Panel
from prettytable import PrettyTable
import questionary
from questionary import Choice

console = Console()


def hapus_musik():
    bersih()
    console.rule("[bold]HAPUS MUSIK[/]")

    lagu_saya = state.lagu.get(state.pengguna_aktif, [])

    if len(lagu_saya) == 0:
        bersih()
        console.print("\n[yellow]Belum ada musik yang bisa dihapus.[/]")
        console.print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    table = PrettyTable()
    table.field_names = ["No", "Judul", "Artist", "Genre"]
    for i, l in enumerate(lagu_saya, start=1):
        table.add_row([i, l.get("judul", ""), l.get("artis", ""), l.get("genre", "")])
    console.print(table)

    try:
        choices = [
            Choice(
                title=f"{i}. {l['judul']} - {l['artis']} ({l['genre']})", value=i - 1
            )
            for i, l in enumerate(lagu_saya, start=1)
        ]
        indeks = questionary.select(
            "Pilih musik yang mau dihapus:", choices=choices
        ).ask()
        if indeks is None:
            raise KeyboardInterrupt
    except (KeyboardInterrupt, EOFError):
        bersih()
        console.print("\n[yellow]Input dibatalkan.[/]")
        console.print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    terpilih = lagu_saya[indeks]

    try:
        yakin = questionary.confirm(f"Yakin mau hapus '{terpilih['judul']}'?").ask()
        if yakin is None:
            raise KeyboardInterrupt
    except (KeyboardInterrupt, EOFError):
        bersih()
        console.print("\n[yellow]Input dibatalkan.[/]")
        console.print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    if yakin:
        try:
            del lagu_saya[indeks]
        except Exception:
            bersih()
            console.print("\n[bold red]Terjadi kesalahan saat menghapus.[/]")
            console.print("\nBalik ke halaman sebelumnya...")
            loading()
            return

        bersih()
        console.print(Panel.fit("[bold green]Musik berhasil dihapus![/]"))
        console.print("\nLoading...")
        loading()
    else:
        bersih()
        console.print("\n[yellow]Penghapusan dibatalkan.[/]")
        console.print("\nBalik ke halaman sebelumnya...")
        loading()
