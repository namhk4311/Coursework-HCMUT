#include <iostream>
#include <iomanip>
using namespace std;

int capacity = 1;

void add(string *&name, double *&score, int &size, const string &newname, const double &newscore) {
    if (size == capacity) {
        capacity = 2 * capacity;
        string *tmp1 = new string[capacity];
        double *tmp2 = new double[capacity];
        for (int i = 0; i < size; i++) {
            tmp1[i] = name[i];
            tmp2[i] = score[i];
        }
        delete [] name;
        delete [] score;
        name = tmp1;
        score = tmp2;
    }
    name[size] = newname;
    score[size] = newscore;
    size++;
    cout << "\n[" << newname << "] " << "has been added on the list!\n";
}

void display(string *name, double *score, const int &size) {
    cout << left << setw(10) << "No." << left << setw(33) << "    Name " << "Student score" << endl;
    for (int i = 0; i < 58; i++) cout << "-";
    cout << endl;
    for (int i = 0; i < size; i++) {
        cout << left << setw(10) << i + 1 << left << setw(38) << name[i] << score[i] << "\n";
    }
}

void displaymaxscore(string *name, double *score, const int &size) {
    int k = 1;
    double maxscore = -1;
    for (int i = 0; i < size; i++) {
        if (maxscore < score[i]) maxscore = score[i];
    }
    cout << left << setw(10) << "No." << left << setw(33) << "    Name " << "Student score" << endl;
    for (int i = 0; i < 58; i++) cout << "-";
    cout << endl;
    for (int i = 0; i < size; i++) {
        if (score[i] == maxscore)
            cout << left << setw(10) << k++ << left << setw(38) << name[i] << score[i] << "\n";
    }
}

int main()
{

    string *name = new string[capacity];
    double *score = new double[capacity];
    int size = 0;

    cout << "-------------------------------------------------\n";
    cout << "\t\t" << "STUDENT MANAGEMENT\n";

    while (1) {
    back:
        cout << "Option:\n";
        cout << "1. Add new student\n"
            << "2. Display the student list\n"
            << "3. Display the student(s) having the best score on the list\n"
            << "4. Exit\n";
        cout << "Enter a number: "; string x; getline(cin, x);
        string inp;
        double inp2;
        cout << endl;
        if (x == "1") {
            tryagain1_1:
            cout << "Enter the student's name: "; getline(cin, inp);
            if (inp == "") {
                cout << "Error! Please try Again" << endl;
                goto tryagain1_1;
            }
            tryagain1_2:
            cout << "Enter the student's score: "; cin >> inp2;
            cin.ignore();
            if (inp2 < 0) {
                cout << "Error! Please Try Again" << endl;
                goto tryagain1_2;
            }
            add(name, score, size, inp, inp2);
        }
        else if (x == "2") {
            if (!size) {
                cout << "No students available on the list!\n";
            }
            else {
                cout << "=================================================\n";
                cout << "\t\t" << "Student name list\n\n";
                display(name, score, size);
                cout << "\n=================================================\n\n";
            }
        }
        else if (x == "3") {
            if (!size) {
                cout << "No students available on the list!\n";
            }
            else {
                cout << "=================================================\n";
                cout << "\t" << "   Student's best score list\n\n";
                displaymaxscore(name, score, size);
                cout << "\n=================================================\n\n";
            }
        }
        else if (x == "4") break;
        else {
            cout << "\nError! Please try again!\n";
            cout << "*****************************************\n";
            goto back;
        }
        cout << "*****************************************\n";
    }

    delete [] name;
    delete [] score;
    return 0;
}
