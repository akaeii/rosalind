with open("datasets/rosalind_iev.txt") as f:
    couples = [int(i) for i in f.read().split()]

probs = [1, 1, 1, 0.75, 0.5, 0]
solution = sum([c * p * 2 for c, p in zip(couples, probs)])

print(solution)
