import math

def main():
    t = int(input())
    out = [0]*t
    for test in range(t):
        count0 = 0
        count2 = 0
        total = 0
        n = int(input())
        nums = [int(x) for x in input().split()]
        for i in range(n):
            if nums[i] == 0:
                count0 += 1
            if nums[i] == 2:
                count2 += 1
        if count0 > 1:
            total += sum([x for x in range(1, count0)])
        if count2 > 1:
            total += sum([x for x in range(1, count2)])
        out[test] = total
    for test in range(t):
        print(out[test])


if __name__ == "__main__":
    main()