def minList(inp):
    outp = []
    for x in xrange(len(inp)):
        minNum = min(inp[x])
        outp.append(minNum)
    return outp
    
print minList([[100],[1,7],[8,0,-1],[2]])