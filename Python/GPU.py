from Komponen import Komponen

class GPU(Komponen):
    def __init__(self, vram_gb=0, chipset="", merk="", nama=""):
        super().__init__(merk, nama)
        self._vram_gb = vram_gb
        self._chipset = chipset

    def set_vram_gb(self, vram_gb):
        self._vram_gb = vram_gb

    def set_chipset(self, chipset):
        self._chipset = chipset

    def get_vram_gb(self):
        return self._vram_gb

    def get_chipset(self):
        return self._chipset