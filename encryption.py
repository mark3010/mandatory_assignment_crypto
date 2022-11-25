# Assignment: crack the following password: $6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0

# We know the password is a type 6 password, which means SHA-512 is used
# We know from the assignment that the password is a 3-digit number

# there is no way to decrypt this, since the sha-512 is a oneway hashing algorithm
# the solution must be to brute force this by calculating all possible answers and matching with the expected output.

# REMEMBER: to install passlib, console: "pip install passlib"

import hashlib
from passlib.hash import sha512_crypt

#We can tell by the string that the salt used is "penguins"

solution = "$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0"

for i in range(1000):
    test = sha512_crypt.using(salt="penguins",rounds=5000).hash(str(i))

    if test == solution:
        print("congrats! you found the solution")
        print("the solution is: " + str(i))
        break

# if a solution is printed in the console, we know we have succeeded. (spoiler alert: we do, the answer is 479)