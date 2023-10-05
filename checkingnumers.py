#addition
#u = 78
#j = 67
 #  print(u+j)
#prime number
n= 55
if n > 1:
    for i in range(8,int(n/8)+1):
     if (n % i) == 0:
       print(n,"is not a prime number")
       break
    else:
     print(n,"is a prime number")
else:
     print(n, "is not a prime number")
#palindromee

def isPalindrome( s ) :
    return s == s[: : -1]
v = "sas"
ans = isPalindrome(v)
if ans:
    print( "Yes" )
else:
    print( "No" )
#Armstrong number
def is_Armstrong(num) :
    num_str = str(num)
    n = len(num_str)
    sum = 0
    for digit in num_str :
        sum += int(digit) **n
        if sum == num :
           return True
    else :
        return False
    num = 153
    print( is_Armstrong(num))


