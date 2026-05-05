with open("./datasets/rosalind_fib.txt") as f:
    n, k = map(int, f.readline().strip().split())

pairs = [1, 1]

for _ in range(3, n + 1):
    pairs.append(pairs[-1] + (pairs[-2] * k))

for i, p in enumerate(pairs, start=1):
    print(f"{i} \t {p}")

print(
    f"\nTotal No. of Pairs after {n} months, with every pair of reproduction age producing a litter of {k} pairs is: {pairs[-1]}"
)
