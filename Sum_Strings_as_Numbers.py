import sys
sys.set_int_max_str_digits(0)
def sum_strings(x, y):
    
    return str(int(x or 0)+int(y or 0))



sum_strings("1", "1")#, "2")
sum_strings("123", "456")#, "579")

sum_strings("9999999999999999", "1")#, "10000000000000000")
sum_strings("712569312664357328695151392","8100824045303269669937")#'712577413488402631964821329'


'''
Given the string representations of two integers, return the string representation of the sum of those integers.

For example:

sumStrings('1','2') // => '3'
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

I have removed the use of BigInteger and BigDecimal in java

Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.


'''


'''
JS solution

function sumStrings(a,b) { 
  let number=BigInt(a)+BigInt(b)
    
 return BigInt(number).toString()

}
'''