#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, k, in, i, count = 0;
    vector<int> vec;
    cin >> n >> k;
    for (i=0; i<n; i++) {
        cin >> in;
        vec.push_back(in);
    }

    sort(vec.begin(), vec.begin()+n);

    for (i=0; i<n-1; i++) {
        int j = 1;
        while (vec[i+j]-vec[i] <= k && i+j < n) {
            if (vec[i+j]-vec[i] == k) {
                count++;
            }
            j++;
        } 
    }
    cout << count;
    return 0;
}