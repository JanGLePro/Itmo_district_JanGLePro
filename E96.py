def math(num):
    global prost
    mas = []
    n = prost[num]
    for i in range(n + 1):
        new = [-num] * i + [num] * (n - i)
        k = 1
        for i in new:
            k *= i
        mas.append([new, k])
    return mas


def choice(n, ind, form):
    global mas
    global ans
    if n == 1:
        print(*form)
        return True
    elif n == -1:
        return False
    for item in mas[ind]:
        choice(n // item[1], ind + 1, form + item[0])


n = int(input())
n_back = n
prost = {}
num = 2
while abs(n) != 1:
    while n % num == 0:
        n //= num
        if num in prost:
            prost[num] = prost[num] + 1
        else:
            prost[num] = 1
    num += 1

mas = []
for item in prost:
    mas.append(math(item))

choice(n_back, 0, [])
