#include <iostream>
#include <iomanip>
using namespace std;
    
int main()
{
    double a[4][4];
    int sum = 0;
    cout << "Please enter the elements of 4x4 matrix:\n";
    for (int i = 0; i < 4; i++) {
        for  (int j = 0; j < 4; j++) {
            cout << "matrix[" << i << "]" << "[" << j << "] = ";
            cin >> a[i][j];
            sum += a[i][j];
        }
    }
    int row[4], col[4], diagonal1 = 0, diagonal2 = 0;
    row[0] = row[1] = row[2] = row[3] = 0;
    col[0] = col[1] = col[2] = col[3] = 0;
    for (int i = 0, j = 0; i < 4, j < 4; i++, j++) {
        diagonal1 += a[i][j];
    }
    for (int i = 0, j = 3 - i; i < 4; i++, j = 3 - i) {
        diagonal2 += a[i][j];
    }
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) row[i] += a[i][j];
    }

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) col[i] += a[j][i];
    }

    cout << endl;
    cout << "Matrix:\n";


    for (int i = 0; i < 45; i++) cout << "-";
    cout << endl;
    for (int i = 0; i < 4; i++) {
        cout << "|";
        cout << left << setw(10) << a[0][i]; 
    }
    cout << "|\n";

    for (int i = 0; i < 45; i++) cout << "-";
    cout << endl;
    for (int i = 0; i < 4; i++) {
        cout << "|";
        cout << left << setw(10) << a[1][i]; 
    }
    cout << "|\n";

    for (int i = 0; i < 45; i++) cout << "-";
    cout << endl;
    for (int i = 0; i < 4; i++) {
        cout << "|";
        cout << left << setw(10) << a[2][i]; 
    }
    cout << "|\n";

    for (int i = 0; i < 45; i++) cout << "-";
    cout << endl;
    for (int i = 0; i < 4; i++) {
        cout << "|";
        cout << left << setw(10) << a[3][i]; 
    }
    cout << "|\n";

    for (int i = 0; i < 45; i++) cout << "-";
    cout << endl << endl;
    
    cout << "The sum of all elements in the matrix: " << sum << endl;
    cout << endl;

    cout << "The sum of elements in the 1st row: " << row[0] << endl
        << "The sum of elements in the 2nd row: " << row[1] << endl
        << "The sum of elements in the 3rd row: " << row[2] << endl
        << "The sum of elements in the 4th row: " << row[3] << endl;

    cout << endl;

    cout << "The sum of elements in the 1st column: " << col[0] << endl
        << "The sum of elements in the 2nd column: " << col[1] << endl
        << "The sum of elements in the 3rd column: " << col[2] << endl
        << "The sum of elements in the 4th column: " << col[3] << endl;

    cout << endl;

    cout << "The sum of elements in the 1st diagonal: " << diagonal1 << endl
        << "The sum of elements in the 2nd diagonal: " << diagonal2 << endl;
    return 0;
}