n = int(input())
l =  [ int(item) for item in input().split() ]
avg = round(sum(l)/len(l), 12)
avg_str = str(avg)
print(avg_str + ((12 - len(avg_str.split('.')[1])) * '0'))
