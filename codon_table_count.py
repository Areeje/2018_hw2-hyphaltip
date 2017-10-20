#!/usr/bin/env python3

codon_file = 'codon_table_compact.txt'

codon_count = 0
aa_count    = 0
aa_fourfold = 0
with open(codon_file,"r") as fh:
    for line in fh:
        line = line.strip() #  remove trailing \n
        AA = "" # you should write code to get this from the string line
        codon_ct = 0 # you should write code to get this from the string line
        print("Amino acid {} is coded for by {} codons".format(AA,codon_ct))

print("===")
print("There are {} total amino acids and {} codons".format(aa_count,codon_count))
print("There are {} AAs which are four-fold or six-fold degenerate".format(aa_fourfold))

