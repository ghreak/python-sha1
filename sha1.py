# Sha1 Hashing Algorithm Python, Sha1
#   start date: 8/28/2019

import utilities as utils

def sha1(text):

    #Initial Digest in Binary:
    h0 = '01100111010001010010001100000001'
    h1 = '11101111110011011010101110001001'
    h2 = '10011000101110101101110011111110'
    h3 = '00010000001100100101010001110110'
    h4 = '11000011110100101110000111110000'

    numstring=""
    chunkwords = []

    #1. Take input text and split it into an array of the characters' ASCII codes

    asciiText = utils.stringToCharList(text)
    asciiList = utils.charToASCII(asciiText)

    #2. Convert ASCII codes to binary
    #3. Pad zeros to the front of each until they are 8 bits long

    binaryAscii = utils.asciiListToBinaryList(asciiList)
    paddedBinaryAscii = utils.padZeroList(binaryAscii, 8)
    
    #4. join them together and append a 1
    
    numstring = numstring.join(paddedBinaryAscii) + '1'
	
    #5. pad the binary message with zeros until its length is 512 mod 448

    while ( (len(numstring) % 512) != 448):
        numstring = numstring + '0'

    #6. take binar 8-bit ASCII code array from step 3, get its length in binary
    length = ''
    length = len(length.join(paddedBinaryAscii) )
    binaryLength = bin(length)[2:]
    binaryLength = utils.padZeroString(binaryLength, 64)
    
    #8. append to your previously created binary message from step 5

    numstring = numstring + binaryLength
    
    #9. break the message into an array of 'chunks' of 512 characters
    n = 512
    chunks = [numstring[i:i+n] for i in range(0, len(numstring), n)]

    #10. break each chunk into a subarray of sixteen 32-bit 'words'
    n = 32
    for ch in chunks:
        chunkwords.append([ch[i:i+n] for i in range(0, len(ch), n)])
    
    #11. loop through each 'chunk' array of sixteen 32-bit 'words' and extend each array to 80 'words' using bitwise operations

    word80 = []
    for chunk in chunkwords:
        for i in range(16, 80):
            wordA = chunk[i - 3]
            wordB = chunk[i - 8]
            wordC = chunk[i - 14]
            wordD = chunk[i - 16]
            
            xorA = utils.xOR(wordA, wordB)
            xorB = utils.xOR(xorA, wordC)
            xorC = utils.xOR(xorB, wordD)
            
            newWord = utils.leftRotate(xorC, 1)
            chunk.append(newWord)

        word80.append(chunk)

    #13. Looping through each chunk: bitwise operatiosn and variable reassignment
        
    for wordArray in word80:
        
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for j in range (80):
            f = ''
            k = ''
            if j >= 0 and j <= 19:
                BandC = utils.andBinStr(b, c)
                notB = utils.andBinStr(utils.notBinStr(b, len(b)), d )
                f = utils.xOR(BandC, notB)
                k = '01011010100000100111100110011001'
            elif j >= 20  and j <= 39:
                BxorC = utils.xOR(b, c) 
                f = utils.xOR(BxorC, d)
                k = '01101110110110011110101110100001'
            elif j >= 40 and j <= 59:
                BandC = utils.andBinStr(b, c)
                BandD = utils.andBinStr(b, d)
                CandD = utils.andBinStr(c, d)
                BandCxorBandD = utils.xOR(BandC, BandD)
                f = utils.xOR(BandCxorBandD, CandD)
                k = '10001111000110111011110011011100'
            elif j >= 60 and j <= 79:
                BxorC = utils.xOR(b, c)
                f = utils.xOR(BxorC, d)
                k = '11001010011000101100000111010110'

            word = wordArray[j]

            tempA = utils.binaryAddition(utils.leftRotate(a,5), f)
            tempB = utils.binaryAddition(tempA, e)
            tempC = utils.binaryAddition(tempB, k)
            temp = utils.binaryAddition(tempC, word)
            temp = utils.truncate(temp, 32)
         
            e = d
            d = c
            c = utils.leftRotate(b, 30)
            b = a
            a = temp

        # Add working elements to the digest after 80 iterations.
        # This occurs for each chunk of 512 bits, 80 words 
        h0 = utils.binaryAddition(h0, a)
        h1 = utils.binaryAddition(h1, b)
        h2 = utils.binaryAddition(h2, c)
        h3 = utils.binaryAddition(h3, d)
        h4 = utils.binaryAddition(h4, e)

    # Convert Digest to Hex,     
    h0 = utils.binaryToHex(h0)
    h1 = utils.binaryToHex(h1)
    h2 = utils.binaryToHex(h2)
    h3 = utils.binaryToHex(h3)
    h4 = utils.binaryToHex(h4)

    #Create the Hash value    
    hashvalue = h0+h1+h2+h3+h4

    #return the hash value. 
    return hashvalue
    
