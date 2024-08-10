#include <iostream>
#include <iomanip>
using namespace std;
    
int main()
{
    cout << "-----------------------------------------\n";
    cout << "|" << setw(32) << "Personal information" << setw(9) << "|\n";
    cout << "|" << setw(8) << "Name:" << setw(20) << "Ho Khanh Nam" << setw(13) << "|\n";
    cout << "|" << setw(8) << "DoB: " << setw(18) << "11/03/2004" << setw(15) << "|\n";
    cout << "|" << setw(9) << "Class:" << setw(15) << "CC22KHM1" << setw(17) << "|\n";
    cout << "|" << setw(14) << "Student ID:" << setw(9) << "2252500" << setw(18) << "|\n";
    cout << "|" << setw(11) << "Falcuty:" << setw(21) << "Computer Science" << setw(9) << "|\n";
    cout << "-----------------------------------------\n";
    return 0;
}