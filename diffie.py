from __future__ import print_function
 
# Variables Used
"""sharedPrime = 23    # p
sharedBase = 5      # g
 
aliceSecret = 6     # a
bobSecret = 15      # b"""

 
# Begin
p=int(input("enter the value of p:-"))
g=int(input( "enter the value of g:-"))
a=int(input( "enter the value of secret a:-"))
b=int(input( "enter the value of secret b:-"))
# Alice Sends Bob A = g^a mod p
A = (g**a) % p
print( "\n  Alice Sends Over Public Chanel: " , A )
 
# Bob Sends Alice B = g^b mod p
B = (g** b) % p
print( "&amp;amp;amp;amp;amp;amp;quot;   Bob Sends Over Public Chanel: ", B )
 
print( "\n------------\n" )
print( "Privately Calculated Shared Secret:" )
# Alice Computes Shared Secret: s = B^a mod p
S= (B ** a) % p
print( "    Alice Shared Secret: ", S )
 
# Bob Computes Shared Secret: s = A^b mod p
S1 = (A**b) % p
print( "    Bob Shared Secret: ", S1)

######output######
gescoe@gescoe-OptiPlex-3020:~$ cd Desktop
gescoe@gescoe-OptiPlex-3020:~/Desktop$ python3 diffie.py
enter the value of p:-23
enter the value of g:-5
enter the value of secret a:-6
enter the value of secret b:-15

  Alice Sends Over Public Chanel:  8
&amp;amp;amp;amp;amp;amp;quot;   Bob Sends Over Public Chanel:  19

------------

Privately Calculated Shared Secret:
    Alice Shared Secret:  2
    Bob Shared Secret:  2
gescoe@gescoe-OptiPlex-3020:~/Desktop$ ^C
gescoe@gescoe-OptiPlex-3020:~/Desktop$ 




