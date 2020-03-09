#include <iostream>

using namespace std;

int main() {
    int n, input, currNum;
    bool ascending;
    bool ordered;
    cin >> n;
    cout << "Lumberjacks:" << endl;
    while (n--) {
        ordered = true;
        for (int i=0; i<10; i++) {
            cin >> input;
            if (ordered == true) {
                if (i==0) {
                    currNum = input;
                }
                else if (i==1) {
                    if (input > currNum) {
                        ascending = true;
                        currNum = input;
                    }
                    else {
                        ascending = false;
                        currNum = input;
                    }
                }
                else {
                    if ( (ascending == true && input < currNum) || (ascending == false && input > currNum) ) {
                        ordered = false;
                    }
                    currNum = input;
                }
            }
        }
        if (ordered == true) {
            cout << "Ordered" << endl;
        }
        else {
            cout << "Unordered" << endl;
        }
    }
    return 0;
}