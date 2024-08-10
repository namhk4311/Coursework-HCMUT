#include <iostream>
#include <string>
#include <iomanip>
using namespace std;
    
int capacity = 1000;

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



class University {
    private:
        string uniname;
        Student **list;
        int listsize;
    public:
        University(string name) : uniname(name) {
            list = new Student*[capacity];
            listsize = 0;
        }
        const int& getlistsize() const {
            return listsize;
        }
        void add(const string &name, const double &score) {
            if (listsize == capacity) {
                capacity *= 2;
                Student **tmp = new Student*[capacity];
                for (int i = 0; i < listsize; i++) {
                    tmp[i] = list[i];
                    list[i] = nullptr;
                }
                delete [] list;
                list = tmp;
            }
            list[listsize++] = new Student(name, score);
            cout << "\n[" << name << "] " << "has been added on the list!\n";
        }
        void display() {
            cout << left << setw(10) << "No." << left << setw(33) << "    Name " << "Student score" << endl; 
            for (int i = 0; i < 58; i++) cout << "-";
            cout << endl;
            for (int i = 0; i < listsize; i++) {
                cout << left << setw(10) << i + 1 << left << setw(38) << list[i]->getname() << list[i]->getscore() << "\n"; 
            }
        }
        void displaymaxscore() {
            int idx_max = -1;
            double maxscore = -1;
            for (int i = 0; i < listsize; i++) {
                maxscore = (maxscore < list[i]->getscore()) ? list[i]->getscore() : maxscore;
            }
            cout << left << setw(10) << "No." << left << setw(33) << "    Name " << "Student score" << endl; 
            for (int i = 0; i < 58; i++) cout << "-";
            cout << endl;
            int idx = 1;
            for (int i = 0; i < listsize; i++) {
                if (list[i]->getscore() == maxscore)
                    cout << left << setw(10) << idx++ << left << setw(38) << list[i]->getname() << list[i]->getscore() << "\n"; 
            }
        }
        void remove(const string &name) {
            int cnt = 0;
            Student **tmp;
            for (int i = 0; i < listsize; i++) {
                if (list[i]->getname() == name) {
                    cnt++;
                }
            }
            if (cnt == 0) {
                cout << "[" << name << "] is not available on the list!\n"; 
            }
            else {
                int new_size = listsize - cnt;
                tmp = new Student*[capacity];
                int cnt_tmp = 0;
                for (int i = 0; i < listsize; i++) {
                    if (list[i]->getname() != name) {
                        tmp[cnt_tmp++] = list[i];
                        list[i] = nullptr;
                    }
                    else {
                        delete list[i];
                        list[i] = nullptr;
                    }
                }
                delete [] list;
                list = tmp;
                listsize = new_size;
                cout << "[" << name << "] has been removed on the list!\n"; 
            }
        }
        ~University() {
            for (int i = 0; i < listsize; i++) {
                delete list[i];
            }
            delete [] list;
            listsize = 0;
        }
};    

int main()
{
    cout << "-------------------------------------------------\n";
    cout << "\t\t" << "STUDENT MANAGEMENT\n";
    string nameUni;
    cout << "\nUniversity name: "; getline(cin, nameUni);
    cout << "\n";
    University *uni = new University(nameUni);
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
            uni->add(inp, inp2);
        }
        else if (x == "2") {
            if (!uni->getlistsize()) {
                cout << "No student available on the list!\n";
            }
            else {
                cout << "=================================================\n";
                cout << "\t\t" << "Student name list\n\n";
                uni->display();
                cout << "\n=================================================\n\n";
            }
        }
        else if (x == "3") {
            if (!uni->getlistsize()) {
                cout << "No student available on the list!\n";
            }
            else {
                cout << "\n=================================================\n";
                cout << "\t" << "   Student's best score list\n\n";
                uni->displaymaxscore();
                cout << "\n=================================================\n\n";
            }
        }
        else if (x == "4") {
            cout << "Enter the student's name: "; getline(cin, inp);
            cout << endl;
            uni->remove(inp);
        }
        else if (x == "5") break;
        else {
            cout << "\nError! Please try again!\n";
            cout << "*****************************************\n";
            goto back;
        }
        cout << "*****************************************\n";
    }
    delete uni;
}