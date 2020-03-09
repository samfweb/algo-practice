#include <iostream>
#include <bits/stdc++.h>

using namespace std;



int main() {
    int t, n, in;
    cin >> t;
    while (t--) {
        int maxSubseq = 0;
        int maxSubArray = INT_MIN;
        int localMax = 0;
        cin >> n;
        for (int i=0; i<n; i++) {
            cin >> in;
            if (in>=0) {
                maxSubseq += in;
            }
            if (i==0){
                localMax = in;
            }
            else {
                localMax = max(localMax+in, in);
            }
            if (maxSubArray < localMax) {
                maxSubArray = localMax;
            }
        }
        if (maxSubArray <= 0) {
            maxSubseq = maxSubArray;
        }
        cout << maxSubArray << " " << maxSubseq << endl;
    }
    return 0;
}