def bin_poisk(mas, item):
    if item > mas[-1]:
        return k
    elif item < mas[0]:
        return 0
    left = -1
    right = k
    while right > left + 1:
        center = (left + right) // 2
        if mas[center] >= item:
            right = center
        else:
            left = center
    return right


n, k, m = map(int, input().split())
mas = list(map(int, input().split()))
minnimum = sorted(mas[:k])
glob_min = minnimum[m - 1]

for i in range(n - k):
    ind = bin_poisk(minnimum, mas[i])
    minnimum.pop(ind)
    ind = bin_poisk(minnimum, mas[i + k])
    minnimum.insert(ind, mas[i + k])

    glob_min = max(minnimum[m - 1], glob_min)

s = 0
for i in range(n):
    if mas[i] > glob_min:
        s += mas[i]
print(s - glob_min)

'''
8 4 2
3 7 4 1 5 9 2 6
'''
'''
5 2 1
2 2 2 2 2
'''
