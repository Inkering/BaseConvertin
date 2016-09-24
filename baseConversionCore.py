def bases(number, oldBase, newBase):
    decimalVal = toDecimal(number, oldBase)
    result = toNewBase(decimalVal, newBase)
    return result
def toNewBase(decimalNumber, base):
    hexVals = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    result = []
    count = 0
    while decimalNumber > 0:
        result.insert(0, decimalNumber % base)
        decimalNumber = decimalNumber // base
        count += 1
    for index, x in enumerate(result):
        if x > 9:
            result[index] = hexVals[x]
    return result
def toDecimal(string, base):
    n = len(string)
    b = base
    s = 0
    chars = list(string)
    for items in chars:
        n = n - 1
        newDecimal = int(items) * (b**n)
        s = s + newDecimal
    return s