import os
import time
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from .manager import PackageManager

class PackageManagerUI:
    def __init__(self):
        self.console = Console()
        self.pm = PackageManager()
        os.system("title pypacm Package Manager")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_table(self, columns=3):
        pkgs = self.pm.packages
        table = Table(title=f"\n[green]Installed Python Packages: ({len(pkgs)})[/green]")

        for _ in range(columns):
            table.add_column("Package", style="cyan", no_wrap=True)
            table.add_column("Version", style="magenta")

        rows = [pkgs[i:i + columns] for i in range(0, len(pkgs), columns)]
        for row in rows:
            flat = []
            for name, version in row:
                flat.extend([name, version])
            while len(flat) < columns * 2:
                flat.extend(["", ""])
            table.add_row(*flat)

        self.console.print(table)

    def run(self):
        while True:
            self.clear_screen()
            self.show_table()

            self.console.print("\nOptions: [blue](I)nstall[/blue] | [red](U)ninstall[/red] | [yellow](R)efresh[/yellow] | [green](A)bout[/green] | (Q)uit")
            choice = Prompt.ask("Choose an action", choices=["i", "u", "r", "a", "q"]).lower()

            if choice == "i":
                pkgs = Prompt.ask("Enter package name(s) to install").split()
                if pkgs:
                    self.pm.install(pkgs)
                    self.console.print(f"[green]Successfully installed: {', '.join(pkgs)}![/green]")
                    time.sleep(3)
                    self.clear_screen()
                    self.show_table()

            elif choice == "u":
                pkgs = Prompt.ask("Enter package name(s) to uninstall").split()
                if pkgs and Confirm.ask(f"Are you sure you want to uninstall: [red]{', '.join(pkgs)}[/red]?"):
                    self.pm.uninstall(pkgs)
                    self.console.print(f"[green]Successfully uninstalled: {', '.join(pkgs)}![/green]")
                    time.sleep(3)
                    self.clear_screen()
                    self.show_table()

            elif choice == "r":
                self.pm.refresh()
                self.clear_screen()
                self.show_table()

            elif choice == "a":
                self.console.print("\nMade with love by ethanmal30! | [red]26/10/25[/red] | ver [green]1.0[/green]")
                time.sleep(3)

            elif choice == "q":
                break