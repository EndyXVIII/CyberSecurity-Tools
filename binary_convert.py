
def intToBinary(number):    #returns the binary value of the number
    return format(number,'b')

#-------------------------------EXAMPLE#-------------------------------
n = 100 
print(intToBinary(n)) #Output: 1100100
#----------------------------------------------------------------------


def binaryToInt(number):
    return int(str(number),2)   #Simply returns the integer number 


#-------------------------------EXAMPLE--------------------------------
n = 1101010111010100011001
print(binaryToInt(n)) #Output: 3503385
#----------------------------------------------------------------------
