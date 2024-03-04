# t = int(input())

# for _ in range(t):
#     arr = [*input()]
#     arr_s = sorted(arr)
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] != arr_s[i]:
#             count += 1

#     print("NO" if count == 3 else "YES")


t = int(input())

for _ in range(t):
    st = input()
    print("NO" if st in {'bca', 'cab'} else "YES")
