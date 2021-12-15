sl = {'RR': 0, 'RG': 0, 'RB': 0,
      'GR': 0, 'GG': 0, 'GB': 0,
      'BR': 0, 'BG': 0, 'BB': 0}
n = int(input())
for _ in range(n):
    string = input()
    sl[string[0] + string[-1]] = sl[string[0] + string[-1]] + 1
    while len(string) > 1:
        sl[string[0] + string[1]] = sl[string[0] + string[1]] + 1
        string = string[1:]
new_sl = {}
for item in sl:
    if item[::-1] not in new_sl:
        new_sl[item] = sl[item]
    else:
        new_sl[item[::-1]] = new_sl[item[::-1]] + sl[item]

maxim = -1
ans = []
for item in new_sl:
    if new_sl[item] > maxim:
        maxim = new_sl[item]
        ans = [item]
    elif new_sl[item] == maxim:
        ans.append(item)
for item in ans:
    print(item)
