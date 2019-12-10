
def main():
    t = int(input())
    for _ in range(t):
        count = 0
        n = int(input())
        for i in range(n):
            for j in range(n)[i+1:]:
                count += 1 if i+j == i*j else _
        print(count)


if __name__ == "__main__":
    main()