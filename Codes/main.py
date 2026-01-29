# Imports


import random
from ori_finder import get_ori_sequence
from site_and_markers import add_sequnces_and_genes
import sys
import os

def get_plasmid(fastafile, designfile):

    # reading the fasta file and getting sequnce
    with open(fastafile, 'r') as f:
        lines = f.readlines()
        dna_seq = ''.join([line.strip() for line in lines[1:]])

    # Getting the ori sequence
    ori_seq = get_ori_sequence(dna_seq)
    
    # Adding spacer to ori sequence
    random_spacer = ''.join(random.choice(['A', 'T', 'G', 'C']) for _ in range(48))
    ori_seq = ori_seq + random_spacer

    print("Predicted ORI:", ori_seq)
    
    # Reading design file and changing plasmid sequence accordingly
    with open(designfile, 'r') as f:
        design_lines = f.readlines()
        f.close()
    # adding restriction sites and genes
    plasmid_dna = add_sequnces_and_genes(ori_seq,design_lines)
    
    # Output final plasmid sequence to a fasta file
    with open(".\Output\Output.fa", 'w') as f:
        f.write(">designed_plasmid\n")
        f.write(ori_seq + "\n")
        f.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <fasta_file> <design_file>")
        sys.exit(1)

    # Extract inputs from sys.argv
    input_fasta = sys.argv[1]
    input_design = sys.argv[2]
    
    if not os.path.exists(input_fasta):
        print(f"Error: {input_fasta} not found.")
        sys.exit(1)
    if not os.path.exists(input_design):
        print(f"Error: {input_design} not found.")
        sys.exit(1)

    get_plasmid(input_fasta, input_design)