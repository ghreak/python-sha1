# Binary Utilities
#   by: Jason Robertson
#   start date: 8/30/2019

def stringToCharList(string):

    return [char for char in string]

def charToASCII(charList):
    ASCII = map(ord, charList)

    return ASCII

# asciiToBinary Takes in a list of ASCII number and converts them to binary without the proceeding 0b
#     for example the number 5 will be converted to 0b101 to 101. 
def asciiListToBinaryList(asciiList):
    newBinList = []
    for ascii in asciiList:
        newBinList.append(bin(ascii)[2:])

    return newBinList

def asciiStringToBinary(string):

    return (bin(ascii)[2:])

# pass a list of binary strings to the function and pad zeros until the length is 8 bits.
# return the new list of 8 bit binary strings.
def padZeroList(listBinaryStrings, length):
    newListBinaryStrings = []
    for item in listBinaryStrings:
        if(length <= len(item) ):
           print("length argument is smaller than number length")
        else:
            newListBinaryStrings.append(item.zfill(length) )
            
    return newListBinaryStrings
#### Pass a string and pad with zeros to length 'length'
def padZeroString(string, length):

    return string.zfill(length)

### Pass two binary strings to the function.
### If their lengths are the same then through an Exception
### Return the bitwise OR operation of the two strings of the same length received.

def orBinStr(stringA, stringB):
    lengthA = len(stringA)
    lengthB = len(stringB)
    if lengthA != lengthB:
        print('Strings passed are not the same length')
        return 0
    else:
        return bin(int(stringA, 2) | int(stringB, 2))[2:].zfill(lengthA)

# Accept a binary string and rotates the register by num times to the left:
def leftRotate(string, num):
    xLLn = ''
    xRRn = ''
    length = len(string)
    if num > length:
        print("Error: Cannot shift a number above string length")
    else:
        xLLn = string[num:length]
        while(len(xLLn) < length):
            xLLn = xLLn +'0'
        xRRn = string[0: num]
        while(len(xRRn) < length):
            xRRn = '0' + xRRn
        string = orBinStr(xLLn, xRRn)
    return string

#### Converts a binary string to hex
#### The Hex value reutnred is 8 characters long, pad with zeros if to short.

def binaryToHex(string):
    
    return hex(int(string, 2) ).lstrip("0x").rstrip("L").zfill(8)

### Perform Bitwise Exclusive OR operation to two binary strings. 
def xOR(stringA, stringB):
    lengthA = len(stringA)
    lengthB = len(stringB)
    if lengthA != lengthB:
        print('Strings passed are not the same length')
        return 0
    else:
        return bin(int(stringA, 2) ^ int(stringB, 2))[2:].zfill(lengthA)

### Perform Bitwise AND operation to two binary strings. 
def andBinStr(stringA, stringB):
    lengthA = len(stringA)
    lengthB = len(stringB)
    if lengthA != lengthB:
        print('Strings passed are not the same length')
        return 0
    else:
        return bin(int(stringA, 2) & int(stringB, 2))[2:].zfill(lengthA)

### Perform Ones compliment to a binary string. 
def notBinStr(string, length):
    notString = ""
    for i in range(0, length ):
        if string[i] == '0':
            notString = notString + '1'
        if string[i] == '1':
            notString = notString + '0'
    return notString

### Perform binaryAddition to two binary strings modulo 2^32            
def binaryAddition(stringA, stringB):
    lengthA = len(stringA)
    numA = int(stringA, 2)
    numB = int(stringB, 2)
    sumNum = (numA + numB) % 2**32
    binarySum = bin(sumNum)[2:]

    while(len(binarySum) <= lengthA):
        binarySum = '0' + binarySum

    while (len(binarySum) > lengthA):
        binarySum = binarySum[1:]
        
    return binarySum

### splice the left most characters of a string until the length is met. 
def truncate(string, length):   
    if (len(string) - length) > 0:
        while (len(string) > length):
            string = string[1:]
            
    return string.zfill(length)
   
