s1 = "GAGCCTACTAACGGGAT"
s2 = "CATCGTAATGACGGCCT"

def dH(s1,s2):
    dist = 0
    for n1, n2 in zip(s1, s2):
        if n1 != n2:
            dist += 1
        else: continue

    return dist

if __name__ == "__main__":
    with open("../rosalind_hamm.txt") as file:
        s1, s2 = file.readlines()        

    print(dH(s1, s2))
