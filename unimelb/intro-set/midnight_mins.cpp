#include <iostream>
using namespace std;

const int MAX_H = 24;
const int MAX_M = 60;
const int MINS_IN_H = 60;

int main() {
    int t, h, hLeft, m, mLeft;
    cin >> t;
    while (t--) {
        hLeft = 0;
        mLeft = 0;
        cin >> h >> m;
        
        if (m != 0) {
            hLeft = MAX_H - h - 1;
            mLeft = MAX_M - m;
            mLeft += hLeft * MINS_IN_H;
        }

        else {
            hLeft = MAX_H - h;
            mLeft += hLeft * MINS_IN_H;
        }

        cout << mLeft << endl;

    }
    return 0;
}
