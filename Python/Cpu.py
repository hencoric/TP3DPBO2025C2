from Komponen import Komponen

class Cpu(Komponen):
    def __init__(self, jumlah_core=0, kecepatan_ghz=0.0, merk="", nama=""):
        super().__init__(merk, nama)
        self._jumlah_core = jumlah_core
        self._kecepatan_ghz = kecepatan_ghz

    def set_jumlah_core(self, jumlah_core):
        self._jumlah_core = jumlah_core

    def set_kecepatan_ghz(self, kecepatan_ghz):
        self._kecepatan_ghz = kecepatan_ghz

    def get_jumlah_core(self):
        return self._jumlah_core

    def get_kecepatan_ghz(self):
        return self._kecepatan_ghz