def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())

for i in range(n):
    hang = list (map(int , input().split()))
    ket_qua_dong = []

    for so in hang:
        if la_so_nguyen_to(so):
            ket_qua_dong.append("1")
        else:
            ket_qua_dong.append("0")
    print(" ".join(ket_qua_dong))