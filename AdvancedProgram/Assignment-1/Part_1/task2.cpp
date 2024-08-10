#include <iostream>
using namespace std;
    
int main()
{
    cout << "Enter 2 numbers: \n"; 
    int a, b;
    cout << "a = "; cin >> a;
    cout << "b = "; cin >> b;
    cout << "Summation: " << a + b 
        << "\nSubtraction: " << a - b
        << "\nDivision: ";
        if (b == 0) cout << "Error";
        else cout << a / b;
    cout << "\nModulus: ";
        if (b == 0) cout << "Error";
        else cout << a % b;
    cout << "\nMultiplication: " << a * b;
    return 0;
}