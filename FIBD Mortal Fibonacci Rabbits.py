with open("datasets/rosalind_fibd.txt") as f:
    data = f.read().strip().split(" ")

N, m = map(int, data)

b = [1]
a = [0]
t = [1]

for n in range(2, N + 1):

    b.append(a[-1])

    if n <= m:
        a.append(a[-1] + b[-2])
    else:
        a.append((a[-1] + b[-2]) - b[-m - 1])

    t.append(b[-1] + a[-1])


for i, total in zip(range(1, N + 1), t):
    print(i, total)
