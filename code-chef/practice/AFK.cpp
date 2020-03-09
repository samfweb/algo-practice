#include <iostream>
using namespace std;

int main() {
    int t, a, b, c, ans;
    cin >> t;
    for (int i = 0; i < t; i++) {
        ans = 0;
        cin >> a >> b >> c;
        cout << "a = " << a << ", b = " << b << ", c = " << c << endl;
        while (b - a != c - b) {
            if ( (b - a) - (c - b) == 1) {
                a += 1;
            }
            else if ( (b - a) - (c - b) == -1) {
                a -= 1;
            }
            
            else if (b - a > c - b) {
                b -= 1;
            }
            else {
                b += 1;
            }
            ans += 1;
            cout << "a = " << a << ", b = " << b << ", c = " << c << endl;

        }
    }
    cout << ans << endl;

    return 0;

}