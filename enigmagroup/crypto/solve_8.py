def pow_mod(x, y, z):
    "Calculate (x ** y) % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number
	
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m
	
e = 3
p = 149
q = 173
n = p*q
phi = (p-1)*(q-1)
d = modinv(e, phi)
# print d


given = '07484 14541 07484 14541 14541 14541 07484 14541 07484 07484 14541 07484 14541 14541 07484 14541 14541 07484 07484 14541 07484 07484 07484 14541 14541 07484 07484 07484 14541 14541 14541 14541 14541 14541 07484 14541 14541 07484 07484 14541 07484 07484 07484 14541 07484 07484 14541 14541 07484 14541 07484 07484 07484 14541 07484 07484 14541 14541 14541 14541 07484 14541 14541 07484 14541 14541 14541 07484 07484 07484 14541 07484 14541 07484 14541 14541 14541 07484 07484 07484'

c1 = 7484
c2 = 14541

m1 = pow_mod(c1, d, n)
m2 = pow_mod(c2, d, n)
# print m1, m2

modded = ''
nums = given.split()
for num in nums:
    if num == '07484':
        modded += str(m1) + ' '
    elif num == '14541':
        modded += str(m2) + ' '

# print modded

nums = modded.split()
binary = ''
for num in nums:
    if num == str(m1):
        binary += '0'
    elif num == str(m2):
        binary += '1'
first = binary[:len(binary)/2]
second = binary[len(binary)/2:]
# print binary
# print first
# print second
# res_xor = bin(int(first, 2) ^ int(second, 2))
# print res_xor
# res_xor = res_xor[2:]
# print res_xor
# have to do own custom XOR as the one above strips off the leading 0
res_xor = ''
for i in range(0,len(first)):
    if first[i] == '0' and second[i] == '1' or first[i] == '1' and second[i] == '0':
        res_xor += '1'
    elif first[i] == '0' and second[i] == '0':
        res_xor += '0'
    elif first[i] == '1' and second[i] == '1':
        res_xor += '0'

res_ascii = ''
x = 0
while x < len(res_xor):
    res_ascii += chr(int(res_xor[x:x+8], 2))
    x += 8
print res_ascii
