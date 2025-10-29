from .utils import get_installed_packages, install_packages, uninstall_packages

class PackageManager:
    def __init__(self):
        self.refresh()

    def refresh(self):
        self.packages = get_installed_packages()

    def install(self, pkgs):
        if pkgs:
            install_packages(pkgs)
            self.refresh()

    def uninstall(self, pkgs):
        if pkgs:
            uninstall_packages(pkgs)
            self.refresh()