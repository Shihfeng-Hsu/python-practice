def longest_consec(strarr, k):
    longestStr=""
    print(len(longestStr))
    for i in range(0,len(strarr),k):
        print(len(strarr[i]  + strarr[i+1]))
        if len(longestStr) == 0 | len( strarr[i]+strarr[i+1]) > len(longestStr):
            longestStr = strarr[i]+strarr[i+1]
    print(longestStr)
    return longestStr

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2)
longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15)