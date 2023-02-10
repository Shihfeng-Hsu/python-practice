def sum_strings(x, y):
    if len(x) == 0 and len(y) == 0:
        return "0"
    if x == 0 and y == 0:
        return "0"
    
    maxlen = len(x)
    if maxlen < len(y):
        maxlen = len(y)
    x = x.zfill(maxlen)
    y = y.zfill(maxlen)

    tens_digit = 0
    sum = ""

    for i in range(-1,-maxlen-1,-1):
        temp = ord(x[i]) + ord(y[i]) - 96 + tens_digit
        if temp >= 10:
            tens_digit = 1 
            temp = temp - 10
        else:
            tens_digit = 0
        sum += str(temp)
    if tens_digit != 0:
        sum += str(tens_digit)
    sum = sum.rstrip('0')
    if sum == "":
        return "0"
    return sum[::-1]


'''
# other solution
# This solution is just simply import the mpz module then sloved the problem.
from gmpy2 import mpz

def sum_strings(x, y):
    return str(mpz(x or '0') + mpz(y or '0'))
'''



'''
# Another solution
# By using the decimal function, the counting speed can be easily increased. 

from decimal import *

setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN))
int = Decimal
def sum_strings(x, y):
    if not x:
        x = '0'
    if not y:
        y = '0'
    x = int(x) + int(y)
    
    return str(x)

'''


sum_strings("1", "1")#, "2")
sum_strings("123", "456")#, "579")

sum_strings("9999999999999999", "1")#, "10000000000000000")
sum_strings("712569312664357328695151392","8100824045303269669937")#'712577413488402631964821329'
sum_strings("","")#, "0")




'''
JS code from other developer
Thanks for this code work, I am inspair

function sumStrings(a, b) {
  let arrA, arrB;
  if (a.length >= b.length) {
    arrA = [...a].reverse();
    arrB = [...b].reverse();
  } else {
    arrA = [...b].reverse();
    arrB = [...a].reverse();
  }
  const doSum = (c, n) => {
    let [x, y] = n;
    c = c || "0";
    return String(parseInt(x) + parseInt(y) + parseInt(c)).padStart(2, "0");
  };
  let zip = arrA.map(function (e, i) {
    return [e, arrB[i] || "0"];
  });
  let result = zip.reduce(
    function (acc, n) {
      let appo = doSum(acc[0], n).split("");
      return [appo[0], appo[1] + acc[1]];
    },
    ["0", ""]
  );
  console.log(result.join("").replace(/^(0+)/, ""));
  return result.join("").replace(/^(0+)/, "");
}

sumStrings("712569312664357328695151392", "8100824045303269669937");

'''

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



'''
def sum_strings(x, y):
    if not x and not y:
        print("0")
        return "0"  
    if x == "0" and y == "0":
        return "0"
    

    arrA=[]
    arrB=[]
    combined_arr=[]

    if len(x) >= len(y):
        arrA = list(x)
        arrB = list(y)
    elif len(y) > len(x):
        arrA = list(y)
        arrB = list(x)

    arrA.reverse()
    arrB.reverse()

    
    # To match the length of arrA and arrB
    gap_length = len(arrA) -len(arrB)
    for i in range(gap_length):
        arrB.append("0")
    
    # To generate combine_arr
    for i in range(len(arrA)):
        combined_arr.append([arrA[i], arrB[i]])
    


    #accalculate the combined_arr
    result = []
    acc = ["0",""]

    def combine_arr_item(cal,item):
        a = item[0]
        b = item[1]
        cal = cal or "0"
        return str(int(a)+int(b)+int(cal)).rjust(2,"0")


    for item in combined_arr:
        
        two_num_combine = list(combine_arr_item(acc[0],item))
        acc = [two_num_combine[0],two_num_combine[1]+acc[1]]
        result = acc
        two_num_combine = ""
    
    print("".join(result).lstrip('0'))
    return "".join(result).lstrip('0')


'''