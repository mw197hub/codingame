import sys
import math

def suche(delta,gene,geneS):
    for pos in range(len(geneS)-len(gene)+delta+1):
        f=0
        for i in range(len(gene)):
            if pos +i < len(geneS):
                if not gene[i] == geneS[pos+i]:
                    f+=1
            else:
                f+=1
        if f <= delta:
            return pos,f
    return 0,999

delta=0 #1
gene="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
geneList=['AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCTCGTGGAGGAGGGTGTCTCCTGCTTGCTGAACATGACTAAAGAATTATTAAATTTTACGTAGGAAATCTTATGTCATAGGGGTG']

delta=3 #3
gene="CCGATATTGGTAAGCTCATATTTCCGGCGGGGACCGTGCCAG"
geneList=['TCTTCCCGTTCGAAGCGCGCGACCCGGGTTCGAAATCTAGCATGTCCTGTTTCAATTCTTCTCCGCCAATGCACCCTGAGAATGCGATCTGTCCTATCACTCGATGCACATGCGCTCCTTATGTGACC', 'TCCAACCGATTGCCAGATCAAAGACGTGGTCCAAATAGCCGATATTGGTAAGCTCATATTTCCGTGCCGTACCGCTTCAGGATAGACAAATATCTTTTAACCGGATAAGAGCATAGGGCCGCCGCCGT', 'TTTGGTTGGGTGAGATTGATGTCGGGGTTCCTCACTACTTTTCTGGTTACGCACCAAAATAGAGTACCGCTTCGCCCAACATGAGCACAACCTACTGGCACACGGGACAAAAGACCTAGTTCGATCCC', 'TAATCGTAACACGCTCTAGGCAGACACGCCTTGTAGTACGCACTTCCTGCGGAACATGGATACTGATATATAAGTCGCACCTCCGTATTTTTACCAATTGGACTGCAGCAAGTACGGTTTACAAAGCA', 'TGGGATATATAGTCTATGCCCCGACCGACCGGCAGTGGGCTCTGATTTTCTAGCACAATGCGTAGTGGTCTAACGCTACCCACACAGTTCTGGTTCAGATCATAATGAGAACTCAATAGTATGCATCA', 'CTGTATGTTCAAATTTCGGCCCGGCCGGGGAGGCACGGCTGTGGTACCATGGAGAACACCTTAGCCCGACAGACATGTGGGGCTTGGTCAACTGCGCAAGACCCGGAGCACCCAGCTGTGGTCTATGC', 'GGGTCTTGTAAATGAGGTCGTTAATGAAAATACTATAGTCTTAGCGAATGGCTTAACTATGAAGGGTACATGAGAACTCTTTTCCAGACCATCCATGAAAACCATGTGTGTGTGGACAGGTAACCAGG', 'CGATTCGTGAAGTTCACTACCTGCTATGGTTATCAACACAGAACGGGGGATCTCAGTTCGAACGAAAAGTCGTACAGATGTGGCTCTAATTAAGAATGACGACATAAAGAAGAAGCTGGGAATAGCAT', 'GTAACAAACGATGAGGAGGCCGTGCAAGTATGGATTATAACTCTCTGTGATCGCTTGCATTGACGGAGTGTCGTTGGAATCACGGAACGACGTATTCTATGTCATCGACGGGTGCCACGTAAACCTAG', 'GAATACATCGCCAAGTATTCACGTCGATAACTTATTGTCCGTTCAGGTCTAGCCGGCCCTAACCATGGCGTTTCCGTATGACGATACTATGGTTACGGGAAGCTCGTACCGGTGGGAGAGGTCTAACA', 'AGCATCCACTAATCCTCACAAGGGATTTCAAATGACGGAGTAGAGGGAGTCATGCTCGCATGATCCCTGAGCCCCATACGGATCGACCGATATTGGTAAGCTCATATTTAAGGCGGGGACCGTGCCAG']

delta=5 #4
gene="ATACTACTAGGCCCTTTCATACGGATACCTTCTGCTTAATCG"
geneList=['TCGAGCACTGTAGCAAGAACTCTTTAATAGCGATACCAGGATCCCCTGCGTATCTAGACACAGTACGTGAAGCGTCGGCTTGTATCCCTGCTCCCTGCCACAAGAACTAACAATTGCCGGAGGTGTTC', 'ATACGTCCCCCGGTGTCAATTATTGTGTATCGGCCGGTAGCCGAAAAAAAGAGTTAGTTTTATGGCCTAGTATGGACAAAGGTAATTAGTGATACTACTAGGCCCTTTCATACGGATACCTTCTGCTT', 'ATATTTGCGGTTACAGTACCCCCACGGCGCGTGGTTCTGGGTTATCACTCTTTTTTCCTACGCTAGCCGCGTCGGAATTAGTTAGCCGGATGACTGGTCTGTATCCGCTGGTGCATTATAGTCCCTGG']

#                                                                                            ATACTACTAGGCCCTTTCATACGGATACCTTCTGCTTAATCG
#ATACGTCCCCCGGTGTCAATTATTGTGTATCGGCCGGTAGCCGAAAAAAAGAGTTAGTTTTATGGCCTAGTATGGACAAAGGTAATTAGTG ATACTACTAGGCCCTTTCATACGGATACCTTCTGCTT

treffer=False
for i in range(len(geneList)):
    index,fehler = suche(delta,gene,geneList[i])
    if fehler <= delta:
        print(str(i)+" "+str(index)+" "+str(fehler));treffer=True
        break
if not treffer:
    print("NONE")