#include <iostream>
using namespace std;
    
int main()
{
    double n; 
    int s;
    cout << "Please enter the amount of money (VND): "; cin >> n;
    cout << "Please select the currency to convert ([1] for AUD, [2] for USD): "; cin >> s;
    cout << fixed << n << " VND(s) = ";
    if (s == 1) cout << fixed << n / 16000 << "AUD(s)";
    else cout << fixed << n / 24000 << "USD(s)";
    return 0;
}