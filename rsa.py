import urllib
from math import floor

random =urllib.request.urlopen(
    "https://www.random.org/integers/?num=1&min=1999&max=999999999&col=1&base=10&format=plain&rnd=new").read()
def isPrime(n):
    if n<=1:
        return False;
    elif n<=3:
        return True
    elif n%2==0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i=i+6
    return True
while isPrime(random)==False:
    random=random+1
p=random
random=random+1
while isPrime(random)==False:
    random=random+1
q=random
N=p*q
e=3 # Public key
while isPrime(e) and ((p-1)*(q-1))%e!=0:
    e=e+1
def gcd(x, y):
    if y == 0:
        return (x, 1, 0)
    else:
        (d, a, b) = gcd(y, x % y)
        return (d, b, a - floor(x/y)*b)
Nx=(p-1)*(q-1)
a,b,d=gcd(Nx,e)
d=d%Nx#private key
