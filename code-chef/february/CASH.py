def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        coins = list(map(int, input().split()))
        need = list(map(lambda x: 0 if (x % k == 0) else k - (x % k), coins))+[0]
        taken = 0
        for i in range(len(coins)):
            # print(f"current coin: {coins[i]}")
            taken += (coins[i] % k)
            # print(f"taken: {taken}")
            if i == len(coins)-1:
                print(taken)
                break
            elif taken >= sum(need[i+1:]):
                print(taken % sum(need[i+1:]))
                break


if __name__ == "__main__":
    main()