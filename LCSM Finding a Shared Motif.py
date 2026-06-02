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

def find_lcsm(sequences):
    shortest_seq = min(sequences, key=len)
    len_shortest_seq = len(shortest_seq)
    
    current_lcsm = ""
    
    for start in range(len_shortest_seq):
        for end in range(start+1, len_shortest_seq+1):
            substring = shortest_seq[start:end]
            
            if all(substring in seq for seq in sequences):
                if len(substring) > len(current_lcsm):
                    current_lcsm = substring
        
    return current_lcsm

if __name__ == "__main__":
    sequences = parse_fasta("rosalind_lcsm.txt")
    lcsm = find_lcsm(sequences)
    
    print(lcsm)