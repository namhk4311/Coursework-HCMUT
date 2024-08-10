#include <iostream>
using namespace std;
    
int main()
{
    int a; 
    cout << "Please enter your age: "; cin >> a;
    cout << "Your ticket price: ";
    if (a < 5) cout << "free\n";
    else if (5 <= a && a <= 10) cout << "$10\n";
    else if (11 <= a && a <= 16) cout << "$20\n";
    else if (a > 16) cout << "$25\n";
    cout << "--------------------------\n";
    cout << "Price information\n"
        << "Under 5 years old: free\n"
        << "5 - 10 years old: $10\n"
        << "11 - 16 years old: $20\n"
        << "Over 16 years old: $25\n"
        << "--------------------------\n";    
    return 0;
}