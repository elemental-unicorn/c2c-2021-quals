
from Crypto.PublicKey import RSA
from factordb.factordb import FactorDB
from math import prod
import binascii
import gmpy2


f = open('public-key.pub','r')
pub = RSA.import_key(f.read())

c = int.from_bytes( open('killswitch','rb').read(), 'big')

fdb = FactorDB(pub.n)
fdb.connect()
primes = fdb.get_factor_list()

print(primes)

assert(pub.n==prod(primes))

phi = prod([p-1 for p in primes])
phi = (primes[0]-1)*primes[1]
d = gmpy2.invert(pub.e, phi)

# debug 
#print("c: ", c)
print("d: ", d)
#print("n: ", pub.n)
#print("e: ", pub.e)

#print( RSA.construct( ( pub.n, pub.e, d, primes[0], primes[1]), consistency_check=False ) )


m = pow(c,d,pub.n)
print("m: ",m)
mm = hex(m)[2:]
print(mm)
pt = binascii.unhexlify('0'+mm)

print(pt)

