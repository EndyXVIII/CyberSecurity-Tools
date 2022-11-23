
def xorInt (num, key):
    return num ^ key #xor between two integers

#--------------------------EXAMPLE---------------------------
num = 20
key = 4
print(xorInt(num, key)) #It prints 16
#------------------------------------------------------------

def xorBinary(nBinary, key):
    y = nBinary ^ key
    print(bin(y)[2:].zfill(len(nBinary)))


s = 1001010101
d = 10
xorBinary(s, d)