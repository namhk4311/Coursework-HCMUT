#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    string name[100];
    double score[100];
    int count = 0;
    for (int i = 0; i < 100; i++) {
        cout << "----------------------------\n";
        cout << "Please enter the student's name: "; getline(cin, name[i]);
        if (name[i] == "-1") {
            cout << "----------------------------\n";
            break;
        }
        cout << "Please enter the student's score: "; cin >> score[i];
        if (score[i] == -1) {
            cout << "----------------------------\n";
        end: break;
        }
        else if (score[i] < 0 && score[i] != -1) {
            while (score[i] < 0) {
                cout << "The score must be in the range from 0 to 100, try again!\nPlease enter the student's score: ";
                cin >> score[i];
                if (score[i] == -1) goto end;
            }
        }
        else if (score[i] > 100) {
            while (score[i] > 100) {
                cout << "The score must be in the range from 0 to 100, try again!\nPlease enter the student's score: ";
                cin >> score[i];
                if (score[i] == -1) goto end;
            }
        }
        ++count;
        cin.ignore();
    }
    
    cout << "========================================\nResult:\n";
    
    cout << "Name" << "\t\t\t\t" << "Score" << "\t\t" << "Status" << endl;
    cout << "---------------------------------------------------------\n";
    for (int i = 0; i < count; i++) {
        cout << name[i] << setw(36 - name[i].length()) << score[i] << "\t\t" << ((score[i] >= 50) ? "Passed" : "Failed") << endl;
    }

    return 0;
}