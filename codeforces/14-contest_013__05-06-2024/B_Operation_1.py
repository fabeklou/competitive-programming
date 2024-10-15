a, m = map(int, input().split())

found=False
twos=a//2
ones=a%2

while twos >=0:
    if (twos + ones) % m == 0:
        print(twos + ones)
        found=True
        break
    twos-=1
    ones+=2

if not found:
    print(-1)
