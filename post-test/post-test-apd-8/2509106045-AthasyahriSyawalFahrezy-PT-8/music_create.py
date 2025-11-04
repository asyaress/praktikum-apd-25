from utils import bersih, loading
import state
from rich.console import Console
from rich.panel import Panel
import questionary

console = Console()


def tambah_musik():
    while True:
        try:
            console.print("\n=== [bold]TAMBAH MUSIK BARU[/] ===")

            judul = input("Judul Lagu : ").strip()
            if not judul:
                bersih()
                console.print("[yellow]Judul tidak boleh kosong.[/]\n")
                continue
            if judul.isdigit():
                bersih()
                console.print("[yellow]Judul tidak boleh hanya angka.[/]\n")
                continue

            artis = input("Nama Artist: ").strip()
            if not artis:
                bersih()
                console.print("[yellow]Artist tidak boleh kosong.[/]\n")
                continue
            if artis.isdigit():
                bersih()
                console.print("[yellow]Artist tidak boleh hanya angka.[/]\n")
                continue

            choices = [f"{i}. {state.genre[i]}" for i in range(1, len(state.genre) + 1)]
            selected = questionary.select("Pilih Genre:", choices=choices).ask()
            if selected is None:
                raise KeyboardInterrupt
            genre_dipilih = selected.split(". ", 1)[1] 

            if state.pengguna_aktif not in state.lagu:
                state.lagu[state.pengguna_aktif] = []
            state.lagu[state.pengguna_aktif].append(
                {"judul": judul, "artis": artis, "genre": genre_dipilih}
            )

            console.print(Panel.fit("[bold green]Musik berhasil ditambahkan![/]"))

            lagi = questionary.confirm("Tambah musik lagi?").ask()
            if not lagi:
                break

        except (KeyboardInterrupt, EOFError):
            bersih()
            console.print("\n[yellow]Input dibatalkan.[/]")
            console.print("\nBalik ke halaman sebelumnya...")
            loading()
            break
