import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = []

    for _ in range(n):
        row = input().strip()  
        row_characters = list(row) 
        a.append(row_characters)

    c = 0
    for i in range(math.ceil(n / 2)):
        for j in range(math.ceil(n / 2)):
            count0 = 0
            count1 = 0
            if a[i][j]=='0':
                count0 += 1
            else:
                count1 += 1

            if a[j][i]=='0':
                count0 += 1
            else:
                count1 += 1

            if a[n-1-j][n-1-i]=='0':
                count0 += 1
            else:
                count1 += 1
            if a[n-1-i][n-1-j]=='0':
                count0 += 1
            else:
                count1 += 1
               
            c += min(count0,count1)
    print(c)
