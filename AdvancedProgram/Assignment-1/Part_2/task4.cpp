#include <iostream>
#include <iomanip>
using namespace std;
    
int main()
{
    string name, dob, home, major, studentID, weight;
    cout << "Please fill out your information below:\n";
    
    cout << "Name: "; getline(cin, name); 
    cout << "Date of birth: "; cin >> dob;
    cout << "Major: "; cin.ignore(); getline(cin, major);
    cout << "Student ID: "; cin >> studentID; 
    cout << "Home address: "; cin.ignore(); getline(cin, home); 
    cout << "Weight (kg): "; cin >> weight;
    system("CLS");
    cout << "\n============================================================\n";
    cout << "\t\tStudent personal information\n" << endl;
    cout << left << setw(20) << "Name: " << name << endl
        << left << setw(20) << "Date of birth: " << dob << endl
        << left << setw(20) << "Major: " << major << endl
        << left << setw(20) <<  "Student ID: " << studentID << endl 
        << left << setw(20) << "Home address: " << home << endl
        << left << setw(20) << "Weight: " << weight << " kg";
    cout << "\n=============================================================\n";
    return 0;
}