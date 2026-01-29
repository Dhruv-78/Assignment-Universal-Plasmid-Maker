

def at_fraction(seq):
    a_count = seq.count('A')
    t_count = seq.count('T')
    return (a_count + t_count) / len(seq)

def gc_skew(seq):
    g_count = seq.count('G')
    c_count = seq.count('C')
    if (g_count + c_count) == 0:
        return 0
    return (g_count - c_count) / (g_count + c_count)

def get_ori_sequence(dna_seq):
    WINDOW = 500
    best_score = -1
    best_pos = None

    for i in range(0, len(dna_seq) - 1000, 100):
        window = dna_seq[i:i+1000]

        at = at_fraction(window)
        skew = abs(gc_skew(window))

        score = at - skew

        if score > best_score:
            best_score = score
            best_pos = i
    ori_seq = dna_seq[best_pos:best_pos+WINDOW+1]
    return ori_seq
    
