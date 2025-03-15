from Cpu import Cpu
from Ram import Ram
from Harddrive import Harddrive
from Komputer import Komputer
from Server import Server

cpu = Cpu(8, 3.4, "Intel", "Core i7")
ram1 = Ram(16, "DDR5", "Corsair", "Vengeance", 3.2)
ram2 = Ram(8, "DDR4", "Kingston", "HyperX", 2.8)
ram3 = Ram(32, "DDR5", "G.Skill", "Trident Z", 3.6)

harddrive = Harddrive(1024, "SSD", "Samsung", "Evo")

komputer = Komputer("PC Abdul", cpu, [ram1, ram2, ram3], harddrive)
komputer.add_ram(Ram(16, "DDR5", "Kingston", "FURY", 3.0))

print("=== Informasi Komputer (Hierarchical Inheritance) ===")
print(f"Nama      : {komputer.get_nama()}")
print(f"CPU       : {komputer.get_cpu().get_merk()} {komputer.get_cpu().get_nama()}"
      f" ({komputer.get_cpu().get_jumlah_core()} Core, {komputer.get_cpu().get_kecepatan_ghz()} GHz)")

print("\nDaftar RAM dalam Komputer:")
for ram in komputer.get_ram_list():
    print("------------------------------------")
    print(f"Merk      : {ram.get_merk()}")
    print(f"Nama      : {ram.get_nama()}")
    print(f"Kapasitas : {ram.get_kapasitas_gb()} GB")
    print(f"Tipe DDR  : {ram.get_ddr()}")
    print(f"OC Speed  : {ram.get_max_speed_ghz()} GHz")

print(f"\nHarddrive : {komputer.get_harddrive().get_tipe_drive()} {komputer.get_harddrive().get_merk()}"
      f" {komputer.get_harddrive().get_nama()} ({komputer.get_harddrive().get_kapasitas_gb()} GB)")

server = Server(4, 16, 3.8, 8, "NVIDIA", "AMD", "Ryzen 9")
print("\n=== Informasi Server (Hybrid Inheritance) ===")
print(f"Server menggunakan CPU {server.get_merk()} {server.get_nama()}"
      f" ({server.get_jumlah_core()} Core, {server.get_kecepatan_ghz()} GHz)")
print(f"Server menggunakan GPU {server.get_merk()} {server.get_nama()}"
      f" ({server.get_vram_gb()} GB VRAM, {server.get_chipset()} Chipset)")
print(f"Server memiliki {server.get_jumlah_rack()} rack")