#pragma once
#include <iostream>
#include <string>
#include "Cpu.cpp"
#include "GPU.cpp"

using namespace std;

class Server : public Cpu, public GPU
{
private:
    int jumlahRack;

public:
    Server() {}

    Server(int jumlahRack, int jumlahCore, float kecepatanGHz, int vramGB, string chipset, string merk, string nama)
        : Komponen(merk, nama), Cpu(jumlahCore, kecepatanGHz, merk, nama), GPU(vramGB, chipset, merk, nama)
    {
        this->jumlahRack = jumlahRack;
    }

    void setJumlahRack(int jumlahRack)
    {
        this->jumlahRack = jumlahRack;
    }

    int getJumlahRack()
    {
        return jumlahRack;
    }

    ~Server() {}
};
