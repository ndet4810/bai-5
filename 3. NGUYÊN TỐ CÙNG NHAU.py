def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(n):
    for j in range(i + 1, n):
        if gcd(a[i], a[j]) == 1:
            print(f"{a[i]} {a[j]}") 