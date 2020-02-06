# Given the list of numbers, you are to sort them in non decreasing order.
#
# Input
# t – the number of numbers in list, then t lines follow [t <= 10^6].
# Each line contains one integer: N [0 <= N <= 10^6]
#
# Output
# Output given numbers in non decreasing order.


def turbo_sort():
    int_list = []
    t = int(input())
    for i in range(t):
        int_list.append(int(input()))
    for j in sorted(int_list):
        print(j)


if __name__ == "__main__":
    turbo_sort()