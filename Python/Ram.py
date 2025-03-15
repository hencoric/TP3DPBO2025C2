from Komponen import Komponen
from Overclocking import Overclocking

class Ram(Komponen, Overclocking):
    def __init__(self, kapasitas_gb=0, ddr="", merk="", nama="", max_speed_ghz=0.0):
        Komponen.__init__(self, merk, nama)
        Overclocking.__init__(self, max_speed_ghz)
        self._kapasitas_gb = kapasitas_gb
        self._ddr = ddr

    def set_kapasitas_gb(self, kapasitas_gb):
        self._kapasitas_gb = kapasitas_gb

    def set_ddr(self, ddr):
        self._ddr = ddr

    def get_kapasitas_gb(self):
        return self._kapasitas_gb

    def get_ddr(self):
        return self._ddr
