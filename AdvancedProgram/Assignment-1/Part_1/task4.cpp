#include <iostream>
using namespace std;
    
int main()
{
    int x, y;
    cout << "Enter the percentage x: "; cin >> x;
    cout << "Enter the number y: "; cin >> y;
    cout << x << "% of " << y << " is " << x / (double)100 * y << endl;
    return 0;
}