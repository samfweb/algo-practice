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
from collections import Counter


# binomial coefficient returns number of ways 'r' elems can be obtained from larger set of 'n' elems
def ncr(n, r):
    fac = math.factorial
    return fac(n) // (fac(r) * fac(n-r))


def main():
    t = int(input())
    for test in range(t):
        int_list = []

        # get expected input
        line_1 = input().split(" ")
        line_2 = input().split(" ")

        k = int(line_1[1])

        # convert line 2 to sorted list of ints
        for integer in line_2:
            int_list.append(integer)
        int_list = sorted(int_list)

        # check count of largest number in subset
        max_num = int_list[k-1]
        count_total = Counter(int_list)[max_num]
        count_subset = Counter(int_list[0:k])[max_num]

        print(f"total = {count_total}, subset = {count_subset}")

        # count_max_subset = num_count(int_list[0:k], max_num)
        # count_max_total = num_count(int_list, max_num)

        print(ncr(count_total, count_subset))


if __name__ == '__main__':
    main()

