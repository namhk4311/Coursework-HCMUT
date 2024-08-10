#include <iostream>
#include <iomanip>
using namespace std;
    
int main()
{
    double us;
    cout << "Please enter the amount of money in US Dollar: "; cin >> us;
    cout << "Result:\n" ;
    cout << fixed << us << " USD = " << us * 24000 << " VND";  
    return 0;
}