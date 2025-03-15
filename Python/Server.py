from Cpu import Cpu
from GPU import GPU

class Server(Cpu, GPU):
    def __init__(self, jumlah_rack=0, jumlah_core=0, kecepatan_ghz=0.0, vram_gb=0, chipset="", merk="", nama=""):
        Cpu.__init__(self, jumlah_core, kecepatan_ghz, merk, nama)
        GPU.__init__(self, vram_gb, chipset, merk, nama)
        self._jumlah_rack = jumlah_rack

    def set_jumlah_rack(self, jumlah_rack):
        self._jumlah_rack = jumlah_rack

    def get_jumlah_rack(self):
        return self._jumlah_rack