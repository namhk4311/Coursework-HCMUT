#include <iostream>
#include <string>
#include <iomanip>
#include <cstdlib>
#include <ctime>
using namespace std;


int capacity = 1000;
    
class Course {
    protected:
        string Course_name;
    public:
        Course(string _name) : Course_name(_name) {}
        virtual const string& getCourseName() = 0;
        virtual void setNameCourse(const string& name) = 0;
        virtual ~Course() {}        
};

class UniCourse : public Course {
    private:
        int assmt[3];
        int test[2];
        int exam;
    public:
        UniCourse(string name = "unknown") : Course(name) {
            assmt[0] = assmt[1] = assmt[2] = 0;
            test[0] = test[1] = 0;
            exam = 0;
        }
        const string& getCourseName() override {
            return Course_name;
        }

        void setScoreAssmt(int assmt1, int assmt2, int assmt3) {
            assmt[0] = assmt1;
            assmt[1] = assmt2;
            assmt[2] = assmt3;
        }
        void setNameCourse(const string& name) override {
            this->Course_name = name;
        }
        int getA1() {return assmt[0];}
        int getA2() {return assmt[1];}
        int getA3() {return assmt[2];}
        int getT1() {return test[0];}
        int getT2() {return test[1];}
        int getE() {return exam;}
        void setScoreTest(int test1, int test2) {
            test[0] = test1;
            test[1] = test2;
        }
        void setScoreExam(int exam) {
            this->exam = exam;  
        }
        double getFinalCourseScore() {
            return (assmt[0] + assmt[1] + assmt[2] + test[0] + test[1] + exam) / 6;
        }
        ~UniCourse() {}
};

class CollegeCourse : public Course {
    private:
        int assmt;
        int test;
        int exam;
    public:
        CollegeCourse(string name = "unknown") : Course(name) {
            assmt = test = exam = 0;
        }
        const string& getCourseName() override {
            return Course_name;
        }
        void setNameCourse(const string& name) override {
            this->Course_name = name;
        }
        void setScoreAssmt(int assmt) {
            this->assmt = assmt;
        }
        int getA() {return assmt;}
        int getT() {return test;}
        int getE() {return exam;}
        void setScoreTest(int test) {
            this->test = test;
        }
        void setScoreExam(int exam) {
            this->exam = exam;  
        }
        double getFinalCourseScore() {
            return (assmt + test + exam) / 3;
        }
        ~CollegeCourse() {}
};

class Semester {
    protected:
        int sem_num;
    public:
        Semester(int num, string *course_name) : sem_num(num) {}
        virtual void removeAllCourse() = 0;
        virtual const int& getSemNum() = 0;
        virtual void displayCourseScore() = 0; 
        virtual double getAverageCourseScoreInASemester() = 0;
        virtual ~Semester() {}
};

class UniSemester : public Semester {
    private:
        UniCourse *course[4];
        //bool course_update[4]; 
        int count;
    public:
        UniSemester(int num, string *course_name) : Semester(num, course_name) {
            count = 0;
            for (int i = 0; i < 4; i++) {
                course[i] = new UniCourse(course_name[i]);
            }
        }
        const int& getSemNum() override {
            return sem_num;
        }
        UniCourse *getCourse(int idx) {
            return course[idx];
        }
        void removeAllCourse() override {
            for (int i = 0; i < 4; i++) {
                if (course[i]) {
                    delete course[i];
                }
            }
        }
        double getAverageCourseScoreInASemester() {
            double result = 0;
            for (int i = 0; i < 4; i++) {
                result += course[i]->getFinalCourseScore();
            }
            return result / 4;
        }
        void displayCourseScore() override {
            cout << left << setw(15) << "     Course" << left << setw(5) << "|" << left << setw(10) << "Assmt 1" << left << setw(5) << "|" << left << setw(10) << "Assmt 2" << left << setw(5) << "|" << left << setw(10) << "Assmt 3" << left << setw(5) << "|" << left << setw(10) << "Test 1" << left << setw(5) << "|" << left << setw(10) << "Test 2" << left << setw(5) << "|" << left << setw(10) << "Exam" << left << setw(5) << "|" << "Final score" << endl;  
            for (int i = 0; i < 121; i++) cout << "-";
            cout << endl;
            for (int i = 0; i < 4; i++) {
            cout << left << setw(15) << course[i]->getCourseName() << left << setw(5) << "|" << left << setw(10) << course[i]->getA1() << left << setw(5) << "|" << left << setw(10) << course[i]->getA2() << left << setw(5) << "|" << left << setw(10) << course[i]->getA3() << left << setw(5) << "|" << left << setw(10) << course[i]->getT1() << left << setw(5) << "|" << left << setw(10) << course[i]->getT2() << left << setw(5) << "|" << left << setw(10) << course[i]->getE() << left << setw(5) << "|" << course[i]->getFinalCourseScore() << endl;
                for (int i = 0; i < 121; i++) cout << "-";
                cout << endl;
            }
        }
        ~UniSemester() {
            removeAllCourse();
        }
};

class CollegeSemester : public Semester {
    private:
        CollegeCourse *course[3];
        int count;
    public:
        CollegeSemester(int num, string *course_name) : Semester(num, course_name) {
            count = 0;
            for (int i = 0; i < 4; i++) {
                course[i] = new CollegeCourse(course_name[i]);
            }
        }
        const int& getSemNum() override {
            return sem_num;
        }
        CollegeCourse *getCourse(int idx) {
            return course[idx];
        }
        void displayCourseScore() override {
            cout << left << setw(20) << "     Course" << left << setw(5) << "|" << left << setw(15) << "Assmt"  << left << setw(5) << "|" << left << setw(15) << "Test" << left << setw(5) << "|" << left << setw(15) << "Exam" << left << setw(5) << "|" << "Final score" << endl;  
            for (int i = 0; i < 100; i++) cout << "-";
            cout << endl;
            for (int i = 0; i < 3; i++) {
            cout << left << setw(20) << course[i]->getCourseName() << left << setw(5) << "|" << left << setw(15) << course[i]->getA() << left << setw(5) << "|" << left << setw(15) << course[i]->getT() << left << setw(5) << "|" << left << setw(15) << course[i]->getE() << left << setw(5) << "|" << left << setw(15) << course[i]->getFinalCourseScore() << endl;
                for (int i = 0; i < 100; i++) cout << "-";
                cout << endl;
            }
        }
        void removeAllCourse() override {
            for (int i = 0; i < 4; i++) {
                if (course[i]) {
                    delete course[i];
                }
            }
        }
        double getAverageCourseScoreInASemester() {
            double result = 0;
            for (int i = 0; i < 3; i++) {
                result += course[i]->getFinalCourseScore();
            }
            return result / 3;
        }
        ~CollegeSemester() {
            removeAllCourse();
        }
};


class Student {
    protected:
        string name;
        string dob;
        string school_name;
        string *course_name;
        string institution;
        double average_sem_score;
    public:
        Student(string name, string dob, string school_name, string *course_name) : name(name), dob(dob), school_name(school_name), course_name(course_name) {}
        virtual void DoAssignment() = 0;
        virtual void TakeTest() = 0;
        virtual void TakeExam() = 0;
        virtual double calculateAverageFinalScore() = 0;
        const string& getname() {return name;}
        const string& getDoB() {return dob;}
        const string& getschoolname() {return school_name;}
        const string& getInstitution() {return institution;}
        virtual Semester* Sem(int idx) = 0;
        virtual ~Student() {}
};

class UniStudent : public Student {
    private:
        UniSemester *sem[8];
    public:
        UniStudent(string name, string dob, string school_name, string *course_name) : Student(name, dob, school_name, course_name) {
            this->institution = "University";
            for (int i = 0; i < 8; i++) {
                sem[i] = new UniSemester(i + 1, course_name + i * 4);
            }
        }
        Semester *Sem(int idx) override {
            return sem[idx];
        }
        void DoAssignment() override {
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 4; j++) {
                    int a1 = rand() % 101;
                    int a2 = rand() % 101;
                    int a3 = rand() % 101;
                    sem[i]->getCourse(j)->setScoreAssmt(a1, a2, a3);
                }
            }
        }
        
        void TakeTest() override {
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 4; j++) {
                    int t1 = rand() % 101;
                    int t2 = rand() % 101;
                    sem[i]->getCourse(j)->setScoreTest(t1, t2);
                }
            }
        }
        void TakeExam() override {
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 4; j++) {
                    int e1 = rand() % 101;
                    sem[i]->getCourse(j)->setScoreExam(e1);
                }
            }
        }
        double calculateAverageFinalScore() override {
            double average_sem = 0;
            for (int i = 0; i < 8; i++) {
                average_sem += sem[i]->getAverageCourseScoreInASemester();
            }
            return average_sem / 8;
        }
        ~UniStudent() {
            for (int i = 0; i < 8; i++) {
                delete sem[i];
            }
        }
};

class CollegeStudent : public Student {
    private:
        CollegeSemester *sem[4];
    public:
        CollegeStudent(string name, string dob, string school_name, string *course_name) : Student(name, dob, school_name, course_name) {
            this->institution = "College";
            for (int i = 0; i < 4; i++) {
                sem[i] = new CollegeSemester(i + 1, course_name + i * 3);
            }
        }
        Semester *Sem(int idx) override {
            return sem[idx];
        }
        void DoAssignment() override {
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 3; j++) {
                    int a1 = rand() % 101;
                    sem[i]->getCourse(j)->setScoreAssmt(a1);
                }
            }
        }
        void TakeTest() override {
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 3; j++) {
                    int t1 = rand() % 101;
                    sem[i]->getCourse(j)->setScoreTest(t1);
                }
            }
        }
        void TakeExam() override {
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 3; j++) {
                    int e1 = rand() % 101;
                    sem[i]->getCourse(j)->setScoreExam(e1);
                }
            }
        }
        double calculateAverageFinalScore() override {
            double average_sem = 0;
            for (int i = 0; i < 4; i++) {
                average_sem += sem[i]->getAverageCourseScoreInASemester();
            }
            return average_sem / 4;
        }
        ~CollegeStudent() {
            for (int i = 0; i < 4; i++) {
                delete sem[i];
            }
        }
};

class University {
    private:
        Student **list;
        int listsize;
    public: 
        University() {
            list = new Student*[capacity];
            listsize = 0;
        }
        const int& getlistsize() const {
            return listsize;
        }
        void add(const int& option, const string& name, const string& dob, const string& school_name, string *course_name) {
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
            if (option == 1) list[listsize++] = new UniStudent(name, dob, school_name, course_name);
            else if (option == 2) list[listsize++] = new CollegeStudent(name, dob, school_name, course_name);
            cout << "\n[" << name << "] " << "has been added on the list!\n";
        }
        void DoAssignment(const string& _name) {
            bool found = false;
            for (int i = 0; i < listsize; i++) {
                if (list[i]->getname() == _name) {
                    list[i]->DoAssignment();
                    found = true;
                }
            }
            cout << endl;
            if (!found) cout << "[" << _name << "] is not on the list\n";
            else cout << "[" << _name << "] has done Assignment\n"; 
        }

        void TakeTest(const string& _name) {
            bool found = false;
            for (int i = 0; i < listsize; i++) {
                if (list[i]->getname() == _name) {
                    list[i]->TakeTest();
                    found = true;
                }
            }
            cout << endl;
            if (!found) cout << "[" << _name << "] is not on the list\n";
            else cout << "[" << _name << "] has taken Test\n"; 
        }

        void TakeExam(const string& _name) {
            bool found = false;
            for (int i = 0; i < listsize; i++) {
                if (list[i]->getname() == _name) {
                    list[i]->TakeExam();
                    found = true;
                }
            }
            cout << endl;
            if (!found) cout << "[" << _name << "] is not on the list\n";
            else cout << "[" << _name << "] has taken Exam\n";
        }
        void display() {
            for (int i = 0; i < listsize; i++) {
                cout << i + 1 << ". Stu name: " << list[i]->getname() << "; School's name: " << list[i]->getschoolname() << "; Institution: " << list[i]->getInstitution() << endl; 
                cout << "Student's score:" << endl;
                int sem_size = (list[i]->getInstitution() == "University") ? 8 : 4;
                for (int j = 0; j < sem_size; j++) {
                    cout << "Semester " << j + 1 << ":" << endl;
                    list[i]->Sem(j)->displayCourseScore();
                    cout << "Average score in Semester " << j + 1 << ": " << list[i]->Sem(j)->getAverageCourseScoreInASemester() << endl;
                    cout << endl;
                }
                if (i != listsize - 1) cout << "====================================================================\n";
            }
        }
        void displaybestscore() {
            int idx_max = -1;
            double maxscore = -1;
            for (int i = 0; i < listsize; i++) {
                maxscore = (maxscore < list[i]->calculateAverageFinalScore()) ? list[i]->calculateAverageFinalScore() : maxscore;
            }
            cout << left << setw(10) << "No." << left << setw(33) << "Name" << "Student score" << endl; 
            for (int i = 0; i < 58; i++) cout << "-";
            cout << endl;
            int idx = 1;
            for (int i = 0; i < listsize; i++) {
                if (list[i]->calculateAverageFinalScore() == maxscore)
                    cout << left << setw(10) << idx++ << left << setw(38) << list[i]->getname() << list[i]->calculateAverageFinalScore() << endl; 
            }
        }

        void remove(const string& _name) {
            int cnt = 0;
            Student **tmp;
            for (int i = 0; i < listsize; i++) {
                if (list[i]->getname() == _name) {
                    cnt++;
                }
            }
            if (cnt == 0) {
                cout << "[" << _name << "] is not available on the list!\n"; 
            }
            else {
                int new_size = listsize - cnt;
                tmp = new Student*[capacity];
                int cnt_tmp = 0;
                for (int i = 0; i < listsize; i++) {
                    if (list[i]->getname() != _name) {
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
                cout << "[" << _name << "] has been removed on the list!\n"; 
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
    srand(time(nullptr));
    cout << "-------------------------------------------------\n";
    cout << "\t\t" << "STUDENT MANAGEMENT\n";
    University *edu = new University();

    while(1) {
        tryagain:
        cout << "Option:\n";
        cout << "1. Add new student\n"
            << "2. Do Assignment\n"
            << "3. Take Test\n"
            << "4. Take Exam\n"
            << "5. Display the student(s) list\n"
            << "6. Display the student(s) having the best score on the list\n"
            << "7. Remove student(s) on the list\n"
            << "8. Exit\n";
        cout << "Enter a number: "; string x; getline(cin, x);
        cout << endl;
        if (x == "1") {
            string institution, name, dob, school_name;
            int option = 0;
            
            
            cout << "Enter student's name: "; getline(cin, name);
            cout << "Enter day of birth: "; getline(cin, dob);
            cout << "Enter school's name: "; getline(cin, school_name);
            back:
            cout << "Select the educational institution (College/University): ";
            getline(cin, institution);
            
            if (institution == "University" || institution == "university") {
                option = 1;
            }
            else if (institution == "College" || institution == "college") {
                option = 2;
            }
            else {
                cout << "Try again\n";
                goto back;
            }
            int sem_course_size{};
            if (option == 1) sem_course_size = 32;
            else sem_course_size = 12; 
            string course_name[sem_course_size];
            cout << "Enter courses of the student in the " << ((option == 1) ? "University: " : "College: ") << endl;
            int sem_num = 1, course_num = 1;
            for (int i = 0; i < sem_course_size; i++) {
                if (option == 1) {
                    if (i == 0 || i == 4 || i == 8 || i == 12 || i == 16 || i == 20 || i == 24 || i == 28) {
                        cout << "Semester " << sem_num++ << ":" << endl;
                    }
                }
                else if (option == 2) {
                    if (i == 0 || i == 3 || i == 6 || i == 9) {
                        cout << "Semester " << sem_num++ << ":" << endl;
                    }
                }
                cout << "Course " << course_num++ << ": "; getline(cin, course_name[i]);
                if ((option == 1 && course_num == 5) || (option == 2 && course_num == 4)) course_num = 1; 
            } 
            edu->add(option, name, dob, school_name, course_name);
        }
        else if (x == "2") {
            string _name;
            cout << "Enter the name of student to do Assignment: "; getline(cin, _name);
            edu->DoAssignment(_name);
        }
        else if (x == "3") {
            string _name;
            cout << "Enter the name of student to take Test: "; getline(cin, _name);
            edu->TakeTest(_name);
        }
        else if (x == "4") {
            string _name;
            cout << "Enter the name of student to take Exam: "; getline(cin, _name);
            edu->TakeExam(_name);
        }
        else if (x == "5") {    
            if (!edu->getlistsize()) cout << "No students available on the list!\n";
            else {
                cout << "\t\t=================================================\n";
                cout << "\t\t" << "\t\t" << "Student name list\n\n";
                edu->display();
            }
        }
        else if (x == "6") {
            if (!edu->getlistsize()) cout << "No students available on the list\n";
            else {
                cout << "\n=================================================\n";
                cout << "\t" << "   Student's best score list\n\n";
                edu->displaybestscore();
                cout << "\n=================================================\n\n";
            }
        }
        else if (x == "7") {
            if (!edu->getlistsize()) cout << "No students available on the list\n";
            else {
                string _name;
                cout << "Enter the student's name: "; getline(cin, _name);
                cout << endl;
                edu->remove(_name);
            }
        }
        else if (x == "8") break;
        else {
            cout << "Try Again!\n";
            goto tryagain;
        }
        cout << "*****************************************\n";
        
    }    
    
    delete edu;

}