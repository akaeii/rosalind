def parse_fasta(file_path):
    with open(file_path, "r") as f:
        s = f.read().strip().splitlines()

    header_pos = [i for i, b in enumerate(s) if ">" in b]
    sequences = []

    for start, end in zip(header_pos, header_pos[1:] + [len(s)]):
        sequences.append("".join(s[start + 1 : end]))

    return sequences


sequences = parse_fasta("datasets/rosalind_cons.txt")

seq_len = len(sequences[0])
A, T, C, G = [[0] * seq_len for _ in range(4)]

for seq in sequences:
    for index, base in enumerate(seq):
        if base == "A":
            A[index] += 1
        elif base == "T":
            T[index] += 1
        elif base == "C":
            C[index] += 1
        elif base == "G":
            G[index] += 1

# # LLM Suggestion
# for seq in sequences:
# for i, base in enumerate(seq):
# profile[base][i] += 1


concensus_l = []
for i in range(seq_len):
    I = [l[i] for l in [A, C, G, T]]
    max_index = I.index(max(I))
    concensus_l.append("ACGT"[max_index])

concensus_s = "".join(concensus_l)
print(concensus_s, sep="\n")

for b, j in zip("ACGT", [A, C, G, T]):
    print(f"{b}: {" ".join(map(str, j))}")
