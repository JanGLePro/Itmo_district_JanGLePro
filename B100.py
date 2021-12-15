n = int(input())
a = int(input())
b = int(input())
k = b - a + 1
mas = [['.'] * n for _ in range(n)]
coords_center = ((n - 1) // 2, (n - 1) // 2)
for x in range(n):
    for y in range(n):
        if a <= abs(coords_center[0] - x) + abs(coords_center[1] - y) <= b:
            mas[x][y] = '*'
for string in mas:
    print(*string, sep='')
