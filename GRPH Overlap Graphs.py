import graphviz


def parse_fasta(file_path):
    with open(file_path, "r") as f:
        s = f.read().strip().splitlines()

    header_pos = [i for i, b in enumerate(s) if ">" in b]
    headers = [s[i] for i in header_pos]

    sequences = []

    for start, end in zip(header_pos, header_pos[1:] + [len(s)]):
        sequences.append("".join(s[start + 1 : end]))

    return headers, sequences


headers, sequences = parse_fasta("datasets/rosalind_grph.txt")
names = [h.replace(">", "") for h in headers]

matches = []

overlap_graph = {}

for i, seq in enumerate(sequences):
    compare_seq = [sequences[ic] for ic in range(len(sequences)) if ic != i]
    compare_header = [names[ic] for ic in range(len(sequences)) if ic != i]

    for ic, comp_seq in enumerate(compare_seq):

        if seq == comp_seq:
            print("bitch shove this edge case up your puckered butthole")

        if seq[-3:] == comp_seq[:3]:
            matches.append((names[i], compare_header[ic]))

og = graphviz.Digraph("overlap-graph", comment="Genetic Sequence Overlap Graph")

for n in names:
    og.node(n)

for s, t in matches:
    og.edge(s, t)
    print(s, t)
og.render(directory=".", view=True)
