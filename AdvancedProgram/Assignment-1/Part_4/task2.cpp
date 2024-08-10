#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;
    
int main()
{
    srand(time(0));
    int secret = rand() % 21;
    int x;
    while (1) {
        cout << "Please enter a number: ";
        cin >> x;
        if (x == secret) break;
        else if (x < secret) cout << "The number you guessed is smaller than the secret number\nTry Again!\n";
        else cout << "The number you guessed is greater than the secret number\nTry Again!\n";
    }
    cout << "Congratulation! You guessed the secret number correctly!";
    return 0;
}