#include <iostream>
#include <string>
#include <iomanip>
using namespace std;
    
int capacity;

class Student {
    private:
        double score;
        string name;
    public:
        Student(string name, double score) : name(name), score(score) {}
        const string& getname() {return name;}
        const double& getscore() {return score;}
        ~Student() {};
};

void add(Student **&stu, int &size, const string &name, const double &score) {
    if (size == capacity) {
        capacity *= 2;
        Student **tmp = new Student*[capacity];
        for (int i = 0; i < size; i++) {
            tmp[i] = stu[i];
            stu[i] = nullptr;
        }
        delete [] stu;
        stu = tmp;
    }
    stu[size++] = new Student(name, score);
    cout << "\n[" << name << "] " << "has been added on the list!\n";
}

void display(Student **stu, const int& size) {
    cout << left << setw(10) << "No." << left << setw(33) << "    Name " << "Student score" << endl; 
    for (int i = 0; i < 58; i++) cout << "-";
    cout << endl;
    for (int i = 0; i < size; i++) {
        cout << left << setw(10) << i + 1 << left << setw(38) << stu[i]->getname() << stu[i]->getscore() << "\n"; 
    }
}

void displaymaxscore(Student **stu, const int& size) {
    double maxscore = -1;
    for (int i = 0; i < size; i++) {
        maxscore = (maxscore < stu[i]->getscore()) ? stu[i]->getscore() : maxscore;
    }
    cout << left << setw(10) << "No." << left << setw(33) << "    Name " << "Student score" << endl; 
    for (int i = 0; i < 58; i++) cout << "-";
    cout << endl;
    int idx = 1;
    for (int i = 0; i < size; i++) {
        if (stu[i]->getscore() == maxscore)
            cout << left << setw(10) << idx++ << left << setw(38) << stu[i]->getname() << stu[i]->getscore() << "\n"; 
    }
}

void remove(Student **&stu, int& size, const string &name) {
    int idx[size];
    int cnt = 0;
    Student **tmp;
    for (int i = 0; i < size; i++) {
        if (stu[i]->getname() == name) {
            cnt++;
        }
    }
    if (cnt == 0) {
        cout << "[" << name << "] is not available on the list!\n"; 
    }
    else {
        int new_size = size - cnt;
        tmp = new Student*[capacity];
        int cnt_tmp = 0;
        for (int i = 0; i < size; i++) {
            if (stu[i]->getname() != name) {
                tmp[cnt_tmp++] = stu[i];
                stu[i] = nullptr;
            }
            else {
                delete stu[i];
                stu[i] = nullptr;
            }
        }
        delete [] stu;
        stu = tmp;
        size = new_size;
        cout << "[" << name << "] has been removed on the list!\n"; 
    }
}

int main()
{
    capacity = 3;
    int size = 0;
    Student **list = new Student*[capacity];
    
    cout << "-------------------------------------------------\n";
    cout << "\t\t" << "STUDENT MANAGEMENT\n";

    while (1) {
        back:
        cout << "Option:\n";
        cout << "1. Add new student\n"
            << "2. Display the student list\n"
            << "3. Display the student(s) having the best score on the list\n"
            << "4. Remove student(s) on the list\n"
            << "5. Exit\n";
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
            add(list, size, inp, inp2);
        }
        else if (x == "2") {
            if (!size) {
                cout << "No student available on the list!\n";
            }
            else {
                cout << "=================================================\n";
                cout << "\t\t" << "Student name list\n\n";
                display(list, size);
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
                displaymaxscore(list, size);
                cout << "\n=================================================\n\n";
            }
        }
        else if (x == "4") {
            tryagain4:
            cout << "Enter the student's name: "; getline(cin, inp);
            if (inp == "") {
                cout << "Error! Please try again!\n";
                goto tryagain4;
            }
            cout << endl;
            remove(list, size, inp);
        }
        else if (x == "5") break;
        else {
            cout << "\nError! Please try again!\n";
            cout << "*****************************************\n";
            goto back;
        }
        cout << "*****************************************\n";
    }

    for (int i = 0; i < size; i++) {
        delete list[i];
    }
    delete [] list;
    return 0;
}