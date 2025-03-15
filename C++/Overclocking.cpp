#pragma once
#include <iostream>
using namespace std;

class Overclocking
{
private:
    float maxSpeedGHz;

public:
    Overclocking() {}

    Overclocking(float maxSpeedGHz)
    {
        this->maxSpeedGHz = maxSpeedGHz;
    }

    void setMaxSpeedGHz(float maxSpeedGHz)
    {
        this->maxSpeedGHz = maxSpeedGHz;
    }

    float getMaxSpeedGHz()
    {
        return maxSpeedGHz;
    }

    ~Overclocking() {}
};
