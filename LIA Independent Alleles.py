from math import comb

with open("datasets/rosalind_lia.txt") as f:
    k, n = [int(i) for i in f.read().split()]

gc = 2**k
ip = 0.25
n_ip = 1 - ip

fp = []

for i in range(n):
    fp.append(comb(gc, i) * (ip**i) * (n_ip ** (gc - i)))

result = 1 - sum(fp)

print(result)
