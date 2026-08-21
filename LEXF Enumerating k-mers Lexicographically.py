from itertools import product as pr

with open("datasets/rosalind_lexf.txt") as f:
    sequence, n = f.read().splitlines()
    sequence = sequence.replace(" ", "")
    n = int(n)

# sequence = "ACGT"
# n = 2


result = list(pr(sequence, repeat=n))

for i in result:
    print(*i, sep="")
