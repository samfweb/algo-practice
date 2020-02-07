# Chef has a sequence A1,A2,…,AN. This sequence has exactly 2N subsequences.
# Chef considers a subsequence of A interesting if its size is exactly K and the sum of all its elements is
# minimum possible, i.e. there is no subsequence with size K which has a smaller sum.
#
# Help Chef find the number of interesting subsequences of the sequence A.
#
# Input
# The first line of the input contains a single integer T denoting the number of test cases.
# The description of T test cases follows.
# The first line of each test case contains two space-separated integers N and K.
# The second line contains N space-separated integers A1,A2,…,AN.

# Output
# For each test case, print a single line containing one integer ― the number of interesting subsequences.

import math


# binomial coefficient returns number of ways 'r' elems can be obtained from larger set of 'n' elems
def ncr(n, r):
    if r == 0 or n == r:
        return 1
    return ncr(n - 1, r) + ncr(n - 1, (r - 1))


def main():
    t = int(input())
    for test in range(t):
        int_list = []

        # get expected input
        k = int(input().split()[1])
        int_list = sorted(list(map(int, input().split())))

        # check count of largest number in subset
        max_num = int_list[k-1]
        count_total = int_list.count(max_num)
        count_subset = int_list[:k].count(max_num)

        print(f"total = {count_total}, subset = {count_subset}")

        print(ncr(count_total, count_subset))


if __name__ == '__main__':
    main()

