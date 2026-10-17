t = int(input())

for _ in range(t):
    s = input()
    parts = s.split('.')
    if len(parts) != 4:
        print('NO')
    else:
        valid = True
        for part in parts:
            if not part.isdigit() or not (0 <= int(part) <= 255):
                valid = False
                break
        if valid:
            print('YES')
        else:
            print('NO')
