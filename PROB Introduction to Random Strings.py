from math import log10

with open("datasets/rosalind_prob.txt") as file:
    data = file.read().splitlines()
    dna_sequence = data[0]
    A = [float(i) for i in data[1].split(" ")]


def get_prob(dna_sequence, gc_content):
    gc_prob = gc_content / 2  # why 2 and not 4?
    at_prob = (1 - gc_content) / 2  # why 2 and not 4?

    gc = ["G", "C"]
    prob = 0

    for nb in dna_sequence:
        if nb in gc:
            prob += log10(gc_prob)
        else:
            prob += log10(at_prob)

    return round(prob, 3)


results = [get_prob(dna_sequence, gc) for gc in A]
print(*results)
