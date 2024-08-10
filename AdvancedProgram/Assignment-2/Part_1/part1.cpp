#include <iostream>
#include <string>
using namespace std;

const int Max = 1000;

void add(string *arr, int &size, string name) {
    if (size == Max) {
        cout << "Full capacity\n";
        return;
    }
    else {
        arr[size++] = name;
        cout << "\n[" << name << "]" << " has been added on the list!\n";
    }
}

void display(string *arr, int size) {
    for (int i = 0; i < size; i++) cout << i + 1 << ". " << arr[i] << endl;
}

void remove(string *arr, int &size, string name) {
    int cnt = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] == name) {
            cnt++;
        }
    }
    if (cnt == 0 || size == 0) {
        cout << "\n[" << name << "]" << " is not available on the list\n";
    }
    else {
        string tmp[Max];
        int cnt_size = 0;
        for (int i = 0; i < size; i++) {
            if (arr[i] != name) {
                tmp[cnt_size++] = arr[i];
            }
            else {
                arr[i] = "";
            }
        }
        for (int i = 0; i < size - cnt; i++) {
            arr[i] = tmp[i];
        }
        size -= cnt;
        cout << "\n[" << name << "]" << " has been removed on the list\n";
    }
}

int main()
{
    string name[Max];
    int size = 0;
    cout << "-------------------------------------------------\n";
    cout << "\t\t" << "STUDENT MANAGEMENT\n";
    while (1) {
back:
        cout << "Option:\n";
        cout << "1. Add new student\n"
            << "2. Display the student list\n"
            << "3. Remove a student on the list\n"
            << "4. Exit\n";
        cout << "Enter a number: "; string x; getline(cin, x);
        string inp;
        cout << endl;
        if (x == "1") {
            cout << "Enter the student's name: "; getline(cin, inp);
            add(name, size, inp);
        }
        else if (x == "2") {
            cout << "=================================================\n";
            cout << "\t\t" << "Student name list\n";
            display(name, size);
            cout << "=================================================\n\n";
        }
        else if (x == "3") {
            tryagain3:
            cout << "Enter the student's name: "; getline(cin, inp);
            if (inp == "") {
                cout << "Error! Please try again" << endl;
                goto tryagain3;
            }
            remove(name, size, inp);
        }
        else if (x == "4") break;
        else {
            cout << "Error! Please try again!\n";
            cout << "*****************************************\n";
            goto back;
        }
        cout << "*****************************************\n";
    }
    return 0;
}
