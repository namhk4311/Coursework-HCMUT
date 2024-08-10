#include <iostream>
using namespace std;
    
int main()
{
    int a, b;
    char c;
    cout << "Please enter the 1st number: "; cin >> a;
    cout << "Please enter the 2nd number: "; cin >> b;
    cout << "Please enter the operator you want to calculate (+,-,*,/): "; cin >> c;
    cout << "Result: ";
    if (c == '+') cout << a + b;
    else if (c == '-') cout << a - b;
    else if (c == '*') cout << a * b;
    else if (c == '/') {
        if (b == 0) cout << "Error\n";
        else cout << (float)a / b;
    }
    return 0;
}