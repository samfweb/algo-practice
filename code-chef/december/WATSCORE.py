
def main():
    t = int(input())
    for _ in range(t):
        highestScores = [0] * 12
        num = input()
        n = int(num) if num != "" else 0
        for i in range(n):
            sub = input().split()
            q = int(sub[0])
            score = int(sub[1])
            if score > highestScores[q]:
                highestScores[q] = score
        total = 0
        for i in range(10):
            total += highestScores[i]
        print(total)


# Driver
if __name__ == "__main__":
    main()







