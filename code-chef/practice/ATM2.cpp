#include <iostream>

int main() {
    int t, n, k;
    std::cin >> t;

    while (t--) {
        std::string ans;
        std::cin >> n >> k;

        while (n--) {   
            int a;
            std::cin >> a;
            if (k >= a) {
                k -= a;
                ans.push_back('1');
            }
            else {
                ans.push_back('0');
            }
        }

        std::cout << ans << std::endl;

    }
    return 0;
}