def motif_locator(s, t):
    locs = []

    for index, char in enumerate(s, start=0):
        if char == t[0]:
            if s[index : index + len(t)] == t:
                locs.append(index + 1)
    return locs


if __name__ == "__main__":
    with open("./datasets/rosalind_subs.txt") as f:
        s, t = f.read().splitlines()

    motif_locs = motif_locator(s, t)
    print(" ".join([str(l) for l in motif_locs]))
