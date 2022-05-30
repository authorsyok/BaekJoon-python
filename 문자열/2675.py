n = int(input())

for i in range(n):
    nums, word = input().split()

    for j in word:
        print(j * int(nums), end='')
    print()

