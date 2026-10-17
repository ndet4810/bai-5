so = input().strip()

while len(so) > 1:
    n = len(so)
    mid = n // 2
    phan_dau = so[:mid]
    phan_sau = so[mid:]
    tong = int(phan_dau) + int(phan_sau)
    print(tong)
    so = str(tong)
print()
