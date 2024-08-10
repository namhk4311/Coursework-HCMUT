#include <iostream>
using namespace std;
    
float square(float edge) {
    return edge * edge;
}

float rectangle(float width, float length) {
    return width * length;
}

float circle(float radius) {
    return 3.1415 * radius * radius;
}

float triangle(float height, float base) {
    return height * base / 2;
}

int main()
{
    while (1) {
        cout << "Please choose the shape to calculate areas ([1]: square, [2]: rectangle, [3]: circle, [4]: triangle, [-1]: exit): ";
        int x; cin >> x;
        if (x == 1) {
            back1:
            cout << "Enter the side value: "; float e; cin >> e;
            if (e < 0) {
                cout << "Invalid value!" << endl;
                goto back1;
            }
            cout << "The area of the square is: " << e * e << endl;
        }
        else if (x == 2) {
            back2:
            cout << "Enter the length value: "; float l; cin >> l;
            if (l < 0) {
                cout << "Invalid value!" << endl;
                goto back2;
            }
            back3:
            cout << "Enter the width value: "; float w; cin >> w;
            if (w < 0) {
                cout << "Invalid value!" << endl;
                goto back3;
            }
            cout << "The area of the rectangle is: " << rectangle(w, l) << endl;
        }
        else if (x == 3) {
            back4:
            cout << "Enter the radius value: "; float r; cin >> r;
            if (r < 0) {
                cout << "Invalid value!" << endl;
                goto back4;
            }
            cout << "The area of the circle is: " << circle(r) << endl;
        }
        else if (x == 4) {
            back5:
            cout << "Enter the height value: "; float h; cin >> h;
            if (h < 0) {
                cout << "Invalid value!" << endl;
                goto back5;
            }
            back6:
            cout << "Enter the base value: "; float b; cin >> b;
            if (b < 0) {
                cout << "Invalid value!" << endl;
                goto back6;
            }
            cout << "The area of the triangle is: " << triangle(h, b) << endl;
        }
        else if (x == -1) {
            cout << "End program";
            break;
        }
        else {
            cout << "Try again!\n";
            continue;
        }
        cout << "====================================\n";
    }
    return 0;
}