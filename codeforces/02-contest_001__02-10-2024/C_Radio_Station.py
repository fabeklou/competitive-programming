n, m  = map(int, input().split())
dct = {}

for _ in range(n):
    name, ip = input().split()
    dct[ip] = name

for _ in range(m):
    cmd, ip = input().split()
    print(f"{cmd} {ip} #{dct[ip[:-1]]}")
