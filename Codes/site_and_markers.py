import random

RESTRICTION_SITES = {
    "EcoRI": "GAATTC",
    "BamHI": "GGATCC",
    "HindIII": "AAGCTT",
    "PstI": "CTGCAG",
    "SphI": "GCATGC",
    "SalI": "GTCGAC",
    "XbaI": "TCTAGA",
    "KpnI": "GGTACC",
    "SacI": "GAGCTC",
    "SmaI": "CCCGGG"
}

GENE_SEQUENCES = {
    # Antibiotic resistance markers
    "AmpR": "ATGAAAGCGTTGCTGATGCTGCTGCTAA",
    "KanR (nptII/aphA)": "ATGAGCCATATTCAACGGGAAACGCTAA",
    "CmR (cat)": "ATGACGTTGATCGATCGATGACGACTAA",
    "TetR (tetA/tetR)": "ATGTTGACCTGCTGCTGACGATGACTAA",
    "SpecR (aadA)": "ATGCGTATTGACGCTGACGCTGACTAA",

    # Screening markers
    "lacZ_alpha": "ATGACCATGATTACGCCAAGCTGCTAA",
    "GFP": "ATGGTGAGCAAGGGCGAGGAGCTGCTAA",
    "mCherry": "ATGGTGAGCAAGGGCGAGGAGGATAACAA",
}

def add_sequnces_and_genes(ori_seq,design_lines):
    for line in design_lines:
        # print(line)
        line = line.strip()
        line = line.split(', ')
        # print(line)
        # print(line[0],line[1])
        if line[0].strip('_site') in RESTRICTION_SITES:
            enzyme = line[0].strip('_site')
            site = RESTRICTION_SITES[enzyme]
            if site:
                ori_seq += site
                # Adding small spacer
                ori_seq += ''.join(random.choice(['A', 'T', 'G', 'C']) for _ in range(6))
                print(f"Added restriction site for {enzyme}: {site}")
        elif line[0].strip('_gene') in GENE_SEQUENCES:
            gene = line[0].strip('_gene')
            gene = gene.strip('_gene')
            gene_seq = GENE_SEQUENCES[gene]
            if gene_seq:
                ori_seq += gene_seq  # Simplified: appending gene to the end
                print(f"Added gene {gene}: {gene_seq}")

    # Final plasmid sequence
    print("Final plasmid sequence:", ori_seq)
    return ori_seq

