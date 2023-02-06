def DNA_strand(dna):
    arr=[]
    for word in dna:
        if word == "A":
            arr.append("T")
        if word == "T":
            arr.append("A")
        if word == "C":
            arr.append("G")
        if word == "G":
            arr.append("C")

    print("".join(arr))
    return "".join(arr)
    # code here

'''
Other solution

pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
return ''.join([pairs[x] for x in dna])

'''

'''
Another solution

import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))
'''

DNA_strand("AAAA")#,"TTTT","String AAAA is")
DNA_strand("ATTGC")#,"TAACG","String ATTGC is")
DNA_strand("GTAT")#,"CATA","String GTAT is")