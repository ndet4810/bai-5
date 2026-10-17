def solution(fishes, k, n):
    counter = [0] * 61
    for fish in fishes: 
        counter[fish] += 1

    cnt = 0
    for i in range(1, k + 1):
        cnt += counter[i]
    for i in range(k + 1, 61):
        if cnt >= n:
            return True
        cnt += counter[i]
        cnt -= counter[i - k]
    return False
d = list(map(int, __import__('sys').stdin.read().split()))
print("true" if solution(d[:-2], d[-2], d[-1]) else "false")
def _():
    return False
