from utils import bersih, loading
import state
from rich.console import Console
from rich.panel import Panel
import questionary
from prettytable import PrettyTable

console = Console()


def edit_musik():
    bersih()
    console.rule("[bold]EDIT MUSIK[/]")

    lagu_saya = state.lagu.get(state.pengguna_aktif, [])

    if len(lagu_saya) == 0:
        bersih()
        console.print("\n[yellow]Belum ada musik yang bisa diedit.[/]")
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
            f"{i}. {l['judul']} - {l['artis']} ({l['genre']})"
            for i, l in enumerate(lagu_saya, start=1)
        ]
        selected = questionary.select(
            "Pilih musik yang mau diedit:", choices=choices
        ).ask()
        if selected is None:
            raise KeyboardInterrupt
        indeks = int(selected.split(". ", 1)[0]) - 1
    except (ValueError, KeyboardInterrupt, EOFError):
        bersih()
        console.print("\n[yellow]Input dibatalkan.[/]")
        console.print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    terpilih = lagu_saya[indeks]

    try:
        console.print("\nMasukkan data baru (Enter untuk mempertahankan nilai):")

        judul_baru = questionary.text(
            f"Judul Lagu [{terpilih['judul']}]:", default=terpilih["judul"]
        ).ask()
        if judul_baru is None:
            raise KeyboardInterrupt
        if judul_baru.strip() == "":
            judul_baru = terpilih["judul"]

        artis_baru = questionary.text(
            f"Nama Artist [{terpilih['artis']}]:", default=terpilih["artis"]
        ).ask()
        if artis_baru is None:
            raise KeyboardInterrupt
        if artis_baru.strip() == "":
            artis_baru = terpilih["artis"]

        # Pilih genre baru (opsi pertama: tidak ubah)
        genre_choices = [f"Tidak ubah (tetap: {terpilih['genre']})"] + [
            f"{i}. {state.genre[i]}" for i in range(1, len(state.genre) + 1)
        ]
        gsel = questionary.select("Pilih Genre Baru:", choices=genre_choices).ask()
        if gsel is None:
            raise KeyboardInterrupt

        if gsel.startswith("Tidak ubah"):
            genre_baru = terpilih["genre"]
        else:
            try:
                indeks_genre = int(gsel.split(". ", 1)[0])
                if 1 <= indeks_genre <= len(state.genre):
                    genre_baru = state.genre[indeks_genre]
                else:
                    console.print("\n[yellow]Nomor tidak valid! Genre tidak diubah.[/]")
                    genre_baru = terpilih["genre"]
            except Exception:
                console.print(
                    "\n[yellow]Input genre tidak valid! Genre tidak diubah.[/]"
                )
                genre_baru = terpilih["genre"]

        # Simpan perubahan
        terpilih["judul"] = judul_baru
        terpilih["artis"] = artis_baru
        terpilih["genre"] = genre_baru

    except (KeyboardInterrupt, EOFError):
        bersih()
        console.print(
            "\n[yellow]Input dibatalkan. Tidak ada perubahan yang disimpan.[/]"
        )
        console.print("\nBalik ke halaman sebelumnya...")
        loading()
        return

    bersih()
    console.print(Panel.fit("[bold green]Musik berhasil diedit![/]"))
    console.print("\nLoading...")
    loading()
