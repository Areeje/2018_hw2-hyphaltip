#!/usr/bin/env python3

codon_file = 'codon_table_compact.txt'

codon_count = 0
aa_count    = 0
aa_fourfold = 0
fourfold_aa_names = []

with open(codon_file,"r") as fh:
    for line in fh:
        line = line.strip() #  remove trailing \n
        cols = line.split("\t")
        AA = cols[1] # you should write code to get this from the string line
        codon_ct = len(cols[0].split(",")) # you should write code to get this from the string line
        aa_count += 1
        codon_count += codon_ct
        if codon_ct > 3:
            aa_fourfold += 1
            fourfold_aa_names.append(AA)
        print("Amino acid {} is coded for by {} codons".format(AA,codon_ct))

print("===")
print("There are {} total amino acids and {} codons".format(aa_count,codon_count))
print("There are {} AAs which are four-fold or six-fold degenerate".format(aa_fourfold))
print("These four-fold or six-fold AAs are:")
print(fourfold_aa_names)
