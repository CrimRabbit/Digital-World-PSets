def binaryToDecimal(binaryStr):
    return int(binaryStr,2)
    
#print binaryToDecimal ('10101 ')

def uncompressed(s):
    s = list(s)
    returnable = ""
    for x in xrange(0,len(s),2):
        returnable += int(s[x])*s[x+1]
    return returnable
    
#print uncompressed("2a5b1c")

def getBaseCounts2(dna):
    dictDna = {'A':0,'C':0,'G':0,'T':0}
    for x in xrange(len(dna)):
        if(dna[x].isupper()):
            curr = dictDna.get(dna[x])
            if(curr!=None):
                dictDna[dna[x]] =curr+1
        else:
            return "The input DNA string is invalid"

    return dictDna
    
#print getBaseCounts2("AAARCCGGTT")

def fundamentalConstants(f):
    f = open(f,"r")
    diction = {}
    lineCount = 0
    for line in f:
        lineContent = line.split()
        if(lineCount > 1):
            if(diction.has_key(lineContent[0])):
                pass
            else:
                diction[lineContent[0]] = float(lineContent[1])
        else:
            lineCount += 1
    return diction
    
#print fundamentalConstants("constants.txt")

def scores(f):
    f = open(f,"r")
    avg = 0.0
    total = 0.0
    count = 0
    for line in f:
        total += float(line)
        count += 1
    avg = total/count
    return total, avg
    
print scores("scores.txt")