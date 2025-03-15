#pragma once
#include "Komponen.cpp"
#include "Overclocking.cpp"

class Ram : public Komponen, public Overclocking
{
private:
    int kapasitasGB;
    string ddr;

public:
    Ram() {}

    Ram(int kapasitasGB, string ddr, string merk, string nama, float maxSpeedGHz)
        : Komponen(merk, nama), Overclocking(maxSpeedGHz)
    {
        this->kapasitasGB = kapasitasGB;
        this->ddr = ddr;
    }

    void setKapasitasGB(int kapasitasGB)
    {
        this->kapasitasGB = kapasitasGB;
    }

    void setDdr(string ddr)
    {
        this->ddr = ddr;
    }

    int getKapasitasGB()
    {
        return kapasitasGB;
    }

    string getDdr()
    {
        return ddr;
    }

    ~Ram() {}
};
