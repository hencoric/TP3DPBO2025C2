#include <bits/stdc++.h>
#include "Cpu.cpp"
#include "Ram.cpp"
#include "Harddrive.cpp"
#include "Komputer.cpp"
#include "Server.cpp"

using namespace std;

int main()
{
     ios::sync_with_stdio(0);
     cin.tie(0);
     Cpu cpu(8, 3.4, "Intel", "Core i7");
     Ram ram1(16, "DDR5", "Corsair", "Vengeance", 3.2);
     Ram ram2(8, "DDR4", "Kingston", "HyperX", 2.8);
     Ram ram3(32, "DDR5", "G.Skill", "Trident Z", 3.6);

     Harddrive harddrive(1024, "SSD", "Samsung", "Evo");

     Komputer komputer("PC Abdul", cpu, {ram1, ram2, ram3}, harddrive);
     komputer.addRam(Ram(16, "DDR5", "Kingston", "FURY", 3.0));

     cout << "=== Informasi Komputer (Hierarchical Inheritance) ===" << endl;
     cout << "Nama      : " << komputer.getNama() << endl;
     cout << "CPU       : " << komputer.getCpu().getMerk() << " " << komputer.getCpu().getNama()
          << " (" << komputer.getCpu().getJumlahCore() << " Core, " << komputer.getCpu().getKecepatanGHz() << " GHz)" << endl;

     cout << "\nDaftar RAM dalam Komputer:" << endl;
     for (Ram &ram : komputer.getRamList())
     {
          cout << "------------------------------------" << endl;
          cout << "Merk      : " << ram.getMerk() << endl;
          cout << "Nama      : " << ram.getNama() << endl;
          cout << "Kapasitas : " << ram.getKapasitasGB() << " GB" << endl;
          cout << "Tipe DDR  : " << ram.getDdr() << endl;
          cout << "OC Speed  : " << ram.getMaxSpeedGHz() << " GHz" << endl;
     }

     cout << "\nHarddrive : " << komputer.getHarddrive().getTipeDrive() << " " << komputer.getHarddrive().getMerk()
          << " " << komputer.getHarddrive().getNama() << " (" << komputer.getHarddrive().getKapasitasGB() << " GB)" << endl;

     Server server(4, 16, 3.8, 8, "NVIDIA", "AMD", "Ryzen 9");
     cout << "\n=== Informasi Server (Hybrid Inheritance) ===" << endl;
     cout << "Server menggunakan CPU " << server.getMerk() << " " << server.getNama()
          << " (" << server.getJumlahCore() << " Core, " << server.getKecepatanGHz() << " GHz)" << endl;
     cout << "Server menggunakan GPU " << server.getMerk() << " " << server.getNama()
          << " (" << server.getVramGB() << " GB VRAM, " << server.getChipset() << " Chipset)" << endl;
     cout << "Server memiliki " << server.getJumlahRack() << " rack" << endl;

     return 0;
}
