def read_fasta(fasta_dir):
    with open(fasta_dir) as file:
        data = file.read().strip().splitlines()

    header_indeces = [i for i, l in enumerate(data) if ">" in l]

    sequences = []

    for start, end in zip(header_indeces, header_indeces[1:] + [len(data)]):
        sequences.append("".join(data[start + 1 : end]))

    return sequences


def get_tran_ratio(sequences):
    nb_type = {
        "A": "purine",
        "G": "purine",
        "T": "pyrimidine",
        "C": "pyrimidine",
        "U": "pyrimidine",
    }

    s1, s2 = sequences
    trant = tranv = 0

    for nb1, nb2 in zip(s1, s2):
        if nb1 != nb2:
            if nb_type[nb1] == nb_type[nb2]:
                trant += 1
            else:
                tranv += 1

    return trant / tranv


sequences = read_fasta("datasets/rosalind_tran.txt")
r = get_tran_ratio(sequences)
print(r)
