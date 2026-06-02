CODON_TABLE = {
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
    "UAA": "-",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": "-",
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
    "UGA": "-",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G",
}

def parse_fasta(file_path):
    with open(file_path, "r") as f:
        fasta = f.read().strip().splitlines()
    
    fasta_length = len(fasta)
    header_positions = [index for index, line in enumerate(fasta) if ">" in line]
    sequences = []
    
    for head, tail in zip(header_positions, header_positions[1:] + [fasta_length]):
        sequence = "".join(fasta[head+1:tail])
        sequences.append(sequence)
    
    return sequences

def splice_exons(sequence, introns):
    for intron in introns:
        sequence = sequence.replace(intron, "")
    return sequence

def exon_to_protein(spliced_sequence):
    mrna = spliced_sequence.replace("T","U")
    codons = []
    
    for codon_start in range(0,len(mrna)-2,3):
        codons.append(mrna[codon_start:codon_start+3])
    
    protein_string = "".join(CODON_TABLE[c] for c in codons[:-1])
    
    return protein_string
        
    
if __name__ == "__main__":
    sequences = parse_fasta("rosalind_splc.txt")
    pre_mrna = sequences[0]
    introns = sequences[1:]
    
    spliced_sequence = splice_exons(pre_mrna, introns)
    print(exon_to_protein(spliced_sequence))