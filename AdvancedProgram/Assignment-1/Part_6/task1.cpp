#include <iostream>
using namespace std;
    
float sumTripple(float a, float b, float c) {
    return a + b + c;
}

float mulTripple(float a, float b, float c) {
    return a * b * c;
}

float aveTripple(float a, float b, float c) {
    return (a + b + c) / 3;
}

int main()
{
    while (1) {
        float a, b, c;
        cout << "Enter a: ";
        cin >> a; if (a == -1) break;
        cout << "Enter b: ";
        cin >> b; if (b == -1) break;
        cout << "Enter c: ";
        cin >> c; if (c == -1) break;
        cout << "==========================\nResult:\n";
        cout << "The sum of a, b, c: " << sumTripple(a, b, c) << endl;
        cout << "The multiplication of a, b, c: " << mulTripple(a, b, c) << endl;
        cout << "The average of a, b, c: " << aveTripple(a, b, c) << endl;
        cout << "==========================\n";
    }
    return 0;
}