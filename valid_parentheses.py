def valid_parentheses(string):
    head=[]
    last=[]
    for i in range(0, len(string)):
        if string[i] == "(":
            head.append(i)
        if string[i] == ")":
            last.append(i)
    if len(head) == 0 and len(last) == 0:
        print("True")
        return True

    if len(head) == 0 or len(last) == 0:
        print("False")
        return False
    if len(head) != len(last) :
        print("False")
        return False

    # if head[-1] > last[-1]:
    #     print("False")
    #     return False
    for i in range(0,len(head)):
        if head[i] > last[i]:
            print("False")
            return False
    print("True")
    return True

'''
Better solution
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False

'''


valid_parentheses("  (")#,False, "should work for '  ('"
valid_parentheses("")#,True, "should work for ''"
valid_parentheses("hi())(")#,False, "should work for 'hi())('"
valid_parentheses("hi(hi)()")#,True, "should work for 'hi(hi)()'"
valid_parentheses(")test")#,False, "should work for ')test'"
valid_parentheses('())(()')#False
valid_parentheses( '((())()())')#true

