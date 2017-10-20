#!/usr/bin/env python3

codon_file = 'codon_table_compact.txt'

with open(codon_file,"r") as fh:
    for line in fh:
        line = line.strip() #  remove trailing \n
        print(line)
