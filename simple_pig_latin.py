def pig_it(text):
    print(text)
    arr=text.split(" ")
    for i in range(0, len(arr)):
        if arr[i]== "!" or arr[i]== "?":
            arr[i]
        else:    
            arr[i]= arr[i][1:]+arr[i][0]+"ay"
    
    print(" ".join(arr))
    return " ".join(arr)


# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
    

pig_it('Pig latin is cool')#,'igPay atinlay siay oolcay')
pig_it('This is my string')#,'hisTay siay ymay tringsay')