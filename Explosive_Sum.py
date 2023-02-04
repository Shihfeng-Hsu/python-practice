'''
This solution spent too many times, it make the Codewar tester's execution timed out.

def exp_sum(n):

    def partition(n):
        answer = set()
        answer.add((n, ))
        for x in range(1, n):
            for y in partition(n - x):
                answer.add(tuple(sorted((x, ) + y)))
        return answer
    answer=partition(n)
    print(len(answer))
    return len(answer)

https://stackoverflow.com/questions/10035752/elegant-python-code-for-integer-partitioning
'''

'''
This solution spent too many times, it make the Codewar tester's execution timed out.
def exp_sum(n):
    counter = 0
    def partitions(n):
        if n == 0:
            yield []
            return
        for p in partitions(n-1):
            yield [1] + p
            if p and (len(p) < 2 or p[1] > p[0]):
                yield [p[0] + 1] + p[1:]
    partitions_map= partitions(n)
    
    for i in partitions_map:
        counter += 1
    print(counter)
    return counter


    https://code.activestate.com/recipes/218332-generator-for-integer-partitions/
    '''

def exp_sum(n):
    if n < 0:
        return 0
    dp = [1]+[0]*n
    for num in range(1,n+1):
        for i in range(num,n+1):
            dp[i] += dp[i-num]
    return dp[-1]

    '''
    https://www.twblogs.net/a/5d75719fbd9eee5327ff930f
    '''

exp_sum(1)#, 1)
exp_sum(2)#, 2)
exp_sum(3)#, 3)
exp_sum(4)#, 5)
exp_sum(5)#, 7)
exp_sum(10)#, 42)


'''
How many ways can you make the sum of a number?
From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)

In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
Examples
Basic
exp_sum(1) # 1
exp_sum(2) # 2  -> 1+1 , 2
exp_sum(3) # 3 -> 1+1+1, 1+2, 3
exp_sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
exp_sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3

exp_sum(10) # 42
Explosive
exp_sum(50) # 204226
exp_sum(80) # 15796476
exp_sum(100) # 190569292

See here for more examples.
http://www.numericana.com/data/partition.htm

https://www.codewars.com/kata/52ec24228a515e620b0005ef/train/python
'''