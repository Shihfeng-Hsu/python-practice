def parse_molecule (formula):
    #(C5H5)Fe(CO)2CH3
    #Pd[P(C6H5)3]4
    string = formula
    braces_mark=[]
 # step1
    for i in range (0, len(formula)):
        if formula[i] == "(":
            print(1)
            braces_mark.append([i])
        if formula[i] == ")":
            num=0
            p = i
            braces_mark[len(braces_mark)-1].append(i)
            if i < len(formula)-2:
                while formula[p+1].isdigit():
                    num += int(formula[p+1])
                    if i < len(formula)-1:
                        p += 1
            braces_mark[len(braces_mark)-1].append(num)
    # print(braces_mark)

    if len(braces_mark) != 0:
        for i in range (0, len(braces_mark)):
            target=string[braces_mark[i][0]+1:braces_mark[i][1]][::-1]
            transform_string=""
            print(target)
            useFlag=0
            for j in range (0, len(target)):
                if target[j].isdigit():
                    transform_string += target[j+1] + str(int(target[j])*int(braces_mark[i][2]))
                    useFlag = 1
                elif useFlag == 1:
                    useFlag = 0
                elif useFlag == 0:
                    print(target[j])
                    transform_string += target[j]
     
            string = string[0:braces_mark[i][0]] + transform_string + string[braces_mark[i][1]+1:]
            braces_mark=[]

#step2
    for i in range (0, len(string)):
        if string[i] == "[":
            print(1)
            braces_mark.append([i])
        if string[i] == "]":
            num=0
            p = i
            braces_mark[len(braces_mark)-1].append(i)
            if p+1 != len(string):
                while string[p+1].isdigit():
                    print(string)
                    num += int(string[p+1])
                    p += 1
                    if p+2 != len(string):
                     break
                        
            braces_mark[len(braces_mark)-1].append(num)
    # print(braces_mark)

    if len(braces_mark) != 0:
        for i in range (0, len(braces_mark)):
            target=string[braces_mark[i][0]+1:braces_mark[i][1]][::-1]
            transform_string=""
            print(target)
            useFlag=0
            for j in range (0, len(target)):
                if target[j].isdigit():
                    transform_string += target[j+1] + str(int(target[j])*int(braces_mark[i][2]))
                    useFlag = 1
                elif useFlag == 1:
                    useFlag = 0
                elif useFlag == 0:
                    print(target[j])
                    transform_string += target[j] + str(braces_mark[i][2])
     
            string = string[0:braces_mark[i][0]] + transform_string 
            braces_mark=[]



    print(string)

    atoms={}
    cur=""
    count = "0"
    for i in range(0, len(string)):
        chr = string[i]
        print(chr)
        if i == len(string)-1 and chr.isupper()  :
            cur = chr
            if cur in atoms :
                    atoms[cur] = atoms[cur] + int(count)|1
                    cur = chr
                    count = ""
            else:
                    atoms[cur] = int(count)|1
                    cur = chr
                    count = ""
                    
        if chr.isupper():
            if  cur == "" :
                cur = chr
            else:
                if cur in atoms :
                    atoms[cur] = atoms[cur] + int(count)|1
                    cur = chr
                    count = ""
                else:
                    atoms[cur] = int(count)|1
                    cur = chr
                    count = ""
        elif chr.islower():
            cur += chr
            # if cur in atoms :
            #     atoms[cur] += count
            #     cur = ""
            # else:
            #     atoms[cur] = count
            #     cur = ""
        elif chr.isdigit():
            count += chr
            if i == len(string)-1 :
                if cur in atoms :
                    atoms[cur] = atoms[cur] + int(chr)
                else:
                    atoms[cur] = int(chr)
     

    print(atoms)
        
        

################################################################
# def parse_molecule (formula):
#     number = ["1","2","3","4","5","6","7","8","9"] 
#     atoms={}
#     served_atoms=[]

#     #make a existed atoms dict.
#     for i in range (0, len(formula)):
#         if formula[i].isupper():
#             if i < len(formula)-1:
#                 if formula[i+1].islower():
#                     atoms[formula[i]+formula[i+1]]=0
#                 else:
#                   atoms[formula[i]]=0
#             else:
#                  atoms[formula[i]]=0

#     trans=str.maketrans("{][()}","      ")
#     chunk = formula.translate(trans).split(" ")
#     chunk.reverse()


#     # To plus number to the atom string in the list
#     def get_served_atoms(num,string):
#         atoms=[]
#         number = ["1","2","3","4","5","6","7","8","9"] 
#         for i in range (0, len(string)):
#             if string[i] not in number:
#                 if i == len(string)-1 or string[i+1] not in number:
#                     atoms = atoms + [string[i]+num]
#                 elif string[i+1] in number:
#                     plus = int(string[i+1])*int(num)
#                     atoms = atoms + [string[i]+str(plus)]

#         return atoms

#     print(chunk)
#     for i in range(0, len(chunk)):

#         if chunk[i] in number:
#             if(chunk[i+1]) in number:
#                 chunk[i+1] = str(int(chunk[i])*int(chunk[i+1]))
#                 served_atoms= served_atoms + get_served_atoms(chunk[i],chunk[i+3])
#                 chunk[i+3] = 0         
#             else:
#                 served_atoms= served_atoms + get_served_atoms(chunk[i],chunk[i+1])
#                 chunk[i+1] = 0 
#         else:
#             if chunk[i] == 0 :
#                 pass
#             else:
#                 for j in range(len(chunk[i])):
#                     if chunk[i][j].isupper():
#                         if j == len(chunk[i])-1:
#                             served_atoms= served_atoms + [chunk[i][j]]
#                         elif chunk[i][j+1].islower() or chunk[i][j+1] in number:
#                            served_atoms= served_atoms + [chunk[i][j]+chunk[i][j+1]] 
#                         else:
#                             served_atoms= served_atoms + [chunk[i][j]]
#                 # served_atoms= served_atoms + get_served_atoms("1",chunk[i])
        
#     print(served_atoms)  

#     for key in atoms :
#         for atom in served_atoms:
#             if key in atom :
#                 amount = atom.replace(key,"") or 1
#                 atoms[key]= atoms[key] + int(amount)
        
#     print(atoms)
#     return atoms


# parse_molecule("H2O")#, {'H': 2, 'O' : 1}, "Should parse water")
#parse_molecule("Mg(OH)2")#, {'Mg': 1, 'O' : 2, 'H': 2}, "Should parse magnesium hydroxide: Mg(OH)2")
parse_molecule("K4[ON(SO3)2]2")#, {'K': 4,  'O': 14,  'N': 2,  'S': 4}, "Should parse Fremy's salt: K4[ON(SO3)2]2")

#parse_molecule("(C5H5)Fe(CO)2CH3")#{'C': 8, 'H': 8, 'Fe': 1, 'O': 2}
# parse_molecule("C6H12O6")#{'C': 6, 'H': 12, 'O': 6}
# parse_molecule("Pd[P(C6H5)3]4")

'''
For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule and return an object (associative array in PHP, Dictionary<string, int> in C#, Map<String,Integer> in Java).

For example:

water = 'H2O'
parse_molecule(water)                 # return {H: 2, O: 1}

magnesium_hydroxide = 'Mg(OH)2'
parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

var fremy_salt = 'K4[ON(SO3)2]2'
parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}
As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to multiply count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two nitrogen atoms and six oxygen atoms.

Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.
'''