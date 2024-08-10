#include <iostream>
using namespace std;
    
int main()
{
    int sum = 0;
    for (int i = 0; i < 10; i++) {
        cout << "Please enter the " << i + 1;
        if (i == 0) cout << "st ";
        else if (i == 1) cout << "nd ";
        else if (i == 2) cout << "rd ";
        else cout << "th ";
        cout << "student's score: ";
        int x;
        cin >> x;
        sum += x;
    }
    cout << "======================================\nThe average score of 10 students: " << (float)sum / 10;
    return 0;
}