def dH(s1,s2):

    dist = sum([1 for n1, n2 in zip(s1, s2) if n1 != n2])

    return dist

if __name__ == "__main__":
    with open("./datasets/rosalind_hamm.txt", "r") as file:
        s1, s2 = file.readlines()        

    print(dH(s1, s2))
