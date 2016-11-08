def consistOFzero(vector):
    OFzero = True
    for i in vector:
        if i != 0:
            OFzero = False
            break;
    return OFzero
def numberOFrows(M):
    return len(M[0])
def numberOfcolums(M):
    return len(M)
def ToReducedRowEchelonForm(M):
    Lead = 0
    rowCount = numberOFrows(M)
    columnCount = numberOfcolums(M)
    for r in range(rowCount):
