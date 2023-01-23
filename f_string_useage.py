item, price = "Coke", 32.54
print(f"Price:{item:>4s},${price:6.1f}") #Price:Coke,$  32.5

######
#syntax= : [align] [+] [#] [0] [width] [,] [.precision] [type]
# align : < left, ^ center, > right
# + : to show the positive number
# 0 : to append "0" to the empty space in the placeholder space
# width : to setting the width of the space
# , : to show thousandths symbol
# .precision : to set the digits below the decimal point
# type : s = string, d = decimal, b = binary, o = octal, x=hexadecimal, f = float, e=scientific notation  
######

i,f,s = 12000, 3.14, "python"
print(f"i={i} f={f} s={s}")#i=12000 f=3.14 s=python
print(f"int={f:+} float={f:6.2f}")#int=+3.14 float=  3.14
print(f"int={i:b}") #int=10111011100000
print(f"int={i:#x}") #int=0x2ee0
print(f"int={i:08}")#int=00012000
print(f"int={i:^08}")#int=01200000
print(f"int={i:<+08}")#int=+1200000


print(f"str={s:<10}")#str=python    
print(f"str={s:^10}")#str=  python 
print(f"str={s:>10}")#str=    python

####
#A pair of curly braces is stand for a placeholder.

print(f"Test: {{4+5:^3d}}")#Test: {4+5:^3d}

print(f"Test: {{{4+5:^3d}}}")#Test: { 9 }