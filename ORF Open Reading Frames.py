dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
rna = dna.replace("T", "U")

rev_dna = dna[::-1].translate(str.maketrans("ATCG", "TAGC"))
rev_rna = rev_dna.replace("T", "U")


codon_table = {
    "UUU": "F",
    "CUU": "L",
    "AUU": "I",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "UAA": "Stop",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": "Stop",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": "Stop",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G",
}


def step_reading_frame(rna_sequence):
    orf2, orf3 = [rna_sequence[i:] for i in range(1, 3)]
    return rna_sequence, orf2, orf3


def codon_translator(rna_sequence):
    codons = [rna_sequence[i : i + 3] for i in range(0, len(rna_sequence) + 1, 3)]

    start_locations = [i for i, c in enumerate(rna_sequence) if c == "AUG"]
    stop_locations = [
        i for i, c in enumerate(rna_sequence) if c in ["UAA", "UAG", "UGA"]
    ]


orf1, orf2, orf3 = step_reading_frame(rna)
orf4, orf5, orf6 = step_reading_frame(rev_rna)

for orf in [orf1, orf2, orf3, orf4, orf5, orf6]:
    (codon_translator(orf))
