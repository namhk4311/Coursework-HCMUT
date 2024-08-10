#include <iostream>
using namespace std;
    
int main()
{
    double radius, height;
    cout << "Enter radius of the cylinder: "; cin >> radius;
    cout << "Enter height of the cylinder: "; cin >> height;
    cout << "------------------------------\n";
    cout << "Result:\n";
    cout << fixed << "The volume of the cylinder is " << 3.14159265 * radius * radius * height << endl;
    return 0;
}