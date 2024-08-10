#include <iostream>
#include <math.h>
using namespace std;
    
int main()
{
    int n;
    cout << "Enter a number: "; cin >> n;
    cout << "---------------------\nResult:\n";
    cout << "abs(" << n << ") = " << abs(n) << "\n"
         << "sin(" << n << ") = " << sin(n) << "\n"
         << "cos(" << n << ") = " << cos(n) << "\n"
         << "tan(" << n << ") = " << tan(n) << "\n"
         << "log(" << n << ") = " << log(n) << "\n"
         << "log10(" << n << ") = " << log10(n) << "\n"
         << "sqrt(" << n << ") = " << sqrt(n) << "\n"
         << "exp(" << n << ") = " << exp(n);  
    return 0;
}