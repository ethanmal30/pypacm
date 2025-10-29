import subprocess
import sys
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn

def get_installed_packages():
    import importlib.metadata
    return sorted(
        [(dist.metadata["Name"], dist.version) for dist in importlib.metadata.distributions()],
        key=lambda x: x[0].lower()
    )

def run_pip_with_progress(command, pkg_name, action):
    with Progress(TextColumn(f"{action} {pkg_name}"), BarColumn(), TimeElapsedColumn()) as progress:
        task = progress.add_task("pip_task", total=100)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)

        for line in process.stdout:
            line = line.strip()
            progress.update(task, advance=1)
        process.wait()
        progress.update(task, completed=100)

def install_packages(packages):
    for pkg in packages:
        run_pip_with_progress([sys.executable, "-m", "pip", "install", pkg, "-q"], pkg, "[green]Installing[/green]")

def uninstall_packages(packages):
    for pkg in packages:
        run_pip_with_progress([sys.executable, "-m", "pip", "uninstall", "-y", pkg, "-q"], pkg, "[green]Uninstalling[/green]")