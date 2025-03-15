#pragma once
#include <iostream>
#include <string>
#include "Komponen.cpp"

using namespace std;

class GPU : virtual public Komponen
{
private:
    int vramGB;
    string chipset;

public:
    GPU() {}

    GPU(int vramGB, string chipset, string merk, string nama) : Komponen(merk, nama)
    {
        this->vramGB = vramGB;
        this->chipset = chipset;
    }

    void setVramGB(int vramGB) { this->vramGB = vramGB; }
    void setChipset(string chipset) { this->chipset = chipset; }

    int getVramGB() { return vramGB; }
    string getChipset() { return chipset; }

    virtual ~GPU() {}
};
