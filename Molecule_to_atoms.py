def parse_molecule (formula):
    
    # open the braces:
    string = formula
    braces = str.maketrans("()","  ")
    brace_off_arr=string.translate(braces).split(" ")
   
    if len(brace_off_arr) > 1:
        times = ""
        for i in range(1, len(brace_off_arr),2):
            for j in range(0, len(brace_off_arr[i+1])):
                if brace_off_arr[i+1][j].isdigit():
                    times += brace_off_arr[i+1][j]
                elif brace_off_arr[i+1][j].isdigit() == False and times == "":
                    times= 1
                    break
                elif brace_off_arr[i+1][j].isdigit() == False:
                    break
            
            brace_off_arr[i] = brace_off_arr[i]*int(times)
            brace_off_arr[i+1] = brace_off_arr[i+1].replace(str(times),"", 1)
            times = ""
                
        string ="".join(brace_off_arr) 

    # open the Square_brackets:
    Square_brackets= str.maketrans("[]","  ")
    brace_off_arr=string.translate(Square_brackets).split(" ")

    if len(brace_off_arr) > 1:
        times = ""
        for i in range(1, len(brace_off_arr),2):
            for j in range(0, len(brace_off_arr[i+1])):
                if brace_off_arr[i+1][j].isdigit():
                    times += brace_off_arr[i+1][j]
                elif brace_off_arr[i+1][j].isdigit() == False and times == "":
                    times= 1
                    break
                elif brace_off_arr[i+1][j].isdigit() == False:
                    break
            
            brace_off_arr[i] = brace_off_arr[i]*int(times)
            brace_off_arr[i+1] = brace_off_arr[i+1].replace(str(times),"", 1)
            times = ""
                
        string ="".join(brace_off_arr) 

    
# open the curly braces: 

    Square_brackets= str.maketrans("}{","  ")
    brace_off_arr=string.translate(Square_brackets).split(" ")

    if len(brace_off_arr) > 1:
        times = ""
        for i in range(1, len(brace_off_arr),2):
            for j in range(0, len(brace_off_arr[i+1])):
                if brace_off_arr[i+1][j].isdigit():
                    times += brace_off_arr[i+1][j]
                elif brace_off_arr[i+1][j].isdigit() == False and times == "":
                    times= 1
                    break
                elif brace_off_arr[i+1][j].isdigit() == False:
                    break
            
            brace_off_arr[i] = brace_off_arr[i]*int(times)
            brace_off_arr[i+1] = brace_off_arr[i+1].replace(str(times),"", 1)
            times = ""
                
        string ="".join(brace_off_arr) 
    


    atoms={}
    cur=""
    count = ""
    for i in range(0, len(string)):

        if string[i].isupper():
            if i == len(string)-1:
                if cur in atoms :
                    atoms[cur] = atoms[cur] + int(count or 1)
                else:
                    atoms[cur] = int(count or 1)
                    cur = string[i]
                if string[i] in atoms :
                    atoms[string[i]] = atoms[string[i]] + 1
                else:
                    atoms[string[i]] =  1
            else:
                if i == 0 :
                    cur = string[i]
                else:
                    if cur in atoms :
                        atoms[cur] = atoms[cur] + int(count or 1)
                    else:
                        atoms[cur] = int(count or 1)
                    cur = string[i]
            count = ""
        if string[i].islower():
            cur = cur + string[i]
        if string[i].isdigit():
            count = count + string[i]
            if i == len(string)-1:
                if cur in atoms :
                    atoms[cur] = atoms[cur] + int(count or 1)
                else:
                    atoms[cur] = int(count or 1)
                    cur = string[i]
        

    print(atoms)
    return atoms

#Shit... I spent a week trying to figure out how to get the right answer.


'''
# Other solution 
# However, it imported a built-in module called "re", which isn't imported by my solution.
# It was my solution that solved the problem without any modules.

from collections import Counter
import re

COMPONENT_RE = (
    r'('
        r'[A-Z][a-z]?'
        r'|'
        r'\([^(]+\)'
        r'|'
        r'\[[^[]+\]'
        r'|'
        r'\{[^}]+\}'
    r')'
    r'(\d*)'
)


def parse_molecule(formula):
    counts = Counter()
    for element, count in re.findall(COMPONENT_RE, formula):
        count = int(count) if count else 1
        if element[0] in '([{':
            for k, v in parse_molecule(element[1:-1]).items():
                counts[k] += count * v
        else:
            counts[element] += count
    return counts

'''


parse_molecule("H2O")#, {'H': 2, 'O' : 1}, "Should parse water")
parse_molecule("Mg(OH)2")#, {'Mg': 1, 'O' : 2, 'H': 2}, "Should parse magnesium hydroxide: Mg(OH)2")
parse_molecule("K4[ON(SO3)2]2")#, {'K': 4,  'O': 14,  'N': 2,  'S': 4}, "Should parse Fremy's salt: K4[ON(SO3)2]2")

parse_molecule("(C5H5)Fe(CO)2CH3")#{'C': 8, 'H': 8, 'Fe': 1, 'O': 2}
parse_molecule("C6H12O6")#{'C': 6, 'H': 12, 'O': 6}
parse_molecule("Pd[P(C6H5)3]4")

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



################################################################
# fail solutions .....

# def parse_molecule (formula):
#     #(C5H5)Fe(CO)2CH3
#     #Pd[P(C6H5)3]4
#     string = formula
#     braces_mark=[]
#     print(formula,"input"),
#  # step1
#     for i in range (0, len(formula)):
#         if formula[i] == "(":
#             braces_mark.append([i])
#         if formula[i] == ")":
#             num=""
#             p = i
#             braces_mark[len(braces_mark)-1].append(i)
#             for p in range(i+1, len(formula)):
#                 print(formula[p],"p")
#                 if formula[p].isdigit():
#                     num += formula[p]
#                 else:
#                     if num == "":
#                         num = "1"
#                     break
#             braces_mark[len(braces_mark)-1].append(int(num))
#     print(braces_mark,"braces_mark")

#     if len(braces_mark) != 0:
#         for i in range (0, len(braces_mark)):
#             target=string[braces_mark[i][0]+1:braces_mark[i][1]][::-1]
#             transform_string=""
#             print(target,"target")
#             useFlag=0
#             for j in range (0, len(target)):
#                 if target[j].isdigit():
#                     transform_string += target[j+1] + str(int(target[j])*int(braces_mark[i][2]))
#                     useFlag = 1
#                 elif useFlag == 1:
#                     useFlag = 0
#                 elif useFlag == 0:
#                     # print(target[j])
#                     transform_string += target[j]+ str(braces_mark[i][2])
                
#                 print(transform_string,"transform string")
     
#             string = string[0:braces_mark[i][0]] + transform_string + string[braces_mark[i][1]+2:]
#             braces_mark=[]
#     print(string,"string1")
# #step2
#     for i in range (0, len(string)):
#         if string[i] == "[":
#             braces_mark.append([i])
#         if string[i] == "]":
#             num=""
#             p = i
#             braces_mark[len(braces_mark)-1].append(i)
#             for p in range(p+1, len(formula)):
#                 if formula[p].isdigit():
#                     num += formula[p]
#                 else:
#                     break
                        
#             braces_mark[len(braces_mark)-1].append(num)
#     print(braces_mark,"braces_mark")

#     if len(braces_mark) != 0:
#         for i in range (0, len(braces_mark)):
#             target=string[braces_mark[i][0]+1:braces_mark[i][1]][::-1]
#             transform_string=""
#             print(target,"target 2")
#             for j in range (0, len(target)):
#                 if target[j].isdigit():
#                     transform_string += target[j+1] + str(int(target[j])*int(braces_mark[i][2]))
#                 elif target[j-1].isdigit():
#                     continue
#                 else:
#                     print(target[j])
#                     transform_string += target[j] + str(braces_mark[i][2])
#             print(transform_string,"transform_string 2")
#             string = string[0:braces_mark[i][0]] + transform_string 
#             braces_mark=[]



#     print(string,"Final string")

#     atoms={}
#     cur=""
#     count = ""
#     for i in range(0, len(string)):
#         chr = string[i]
#         # print(chr)
#         if i == len(string)-1 and chr.isupper()  :
#             cur = chr
#             if cur in atoms :
#                     atoms[cur] = atoms[cur] + int(count or 1)
#                     cur = chr
#                     count = ""
#             else:
#                     atoms[cur] = int(count or 1)
#                     cur = chr
#                     count = ""
                    
#         if chr.isupper():
#             if  cur == "" :
#                 cur = chr
#                 if i == 0 :
#                     if cur in atoms :
#                         atoms[cur] = atoms[cur] + int(count or 1) 
#                         cur = chr
#                         count = ""
#                     else:
#                         atoms[cur] = int(count or 1)
#                         cur = chr
#                         count = ""

#             else:
#                 if cur in atoms :
#                     atoms[cur] = atoms[cur] + int(count or 1) 
#                     cur = chr
#                     count = ""
#                 else:
#                     atoms[cur] = int(count or 1)
#                     cur = chr
#                     count = ""
#         elif chr.islower():
#             cur += chr
#             # if cur in atoms :
#             #     atoms[cur] += count
#             #     cur = ""
#             # else:
#             #     atoms[cur] = count
#             #     cur = ""
#         elif chr.isdigit():
#             count += chr
#             if i == len(string)-1 :
#                 if cur in atoms :
#                     atoms[cur] = atoms[cur] + int(chr)
#                 else:
#                     atoms[cur] = int(chr)
     

#     print(atoms)
        





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


