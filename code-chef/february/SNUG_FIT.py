import math


def main():
    for _ in range(int(input())):
        sum = 0
        n = int(input())
        line1 = sorted(list(map(int, input().split())))
        line2 = sorted(list(map(int, input().split())))

        for _ in range(n):
            r = min(line1.pop(), line2.pop()) * 0.5
            sum += (2 * r)

        print(int(sum))


if __name__ == "__main__":
    main()
