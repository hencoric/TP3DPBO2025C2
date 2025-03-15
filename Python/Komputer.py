from Cpu import Cpu
from Harddrive import Harddrive
from Ram import Ram

class Komputer:
    def __init__(self, nama="", cpu=None, ram_list=None, harddrive=None):
        self._nama = nama
        self._cpu = cpu if cpu else Cpu()
        self._ram_list = ram_list if ram_list else []
        self._harddrive = harddrive if harddrive else Harddrive()

    def set_nama(self, nama):
        self._nama = nama

    def set_cpu(self, cpu):
        self._cpu = cpu

    def set_ram(self, ram_list):
        self._ram_list = ram_list

    def set_harddrive(self, harddrive):
        self._harddrive = harddrive

    def add_ram(self, ram):
        self._ram_list.append(ram)

    def get_nama(self):
        return self._nama

    def get_cpu(self):
        return self._cpu

    def get_ram_list(self):
        return self._ram_list

    def get_harddrive(self):
        return self._harddrive