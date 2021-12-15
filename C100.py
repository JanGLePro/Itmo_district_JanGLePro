n = int(input())
trains = list(map(int, input().split()))
ans = 0
for ind in range(n):
    x, y = map(int, input().split())
    if trains[ind]:
        if y - x > 0:
            ans += (y - x)

print(ans)
'''5
0 1 0 1 0
80000 81000
80500 81500
81500 81000
80500 80000
80000 81800'''
