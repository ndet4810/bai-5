t = int(input())
chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for _ in range(t):
  line = input().split()
  n = int(line[0])
  b = int(line[1])

  if n == 0:
    print(0)
    continue

  ket_qua = ""
  while n > 0:
    du = n % b
    ket_qua += chars[du]
    n = n // b

  print(ket_qua[::-1])