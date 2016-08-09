def toNewBase(number, base):
    result = []
    while number > 0:
        result.insert(0, number % base)
        number = number // base
    return result



























#def fromBase(number, base):
#    n = 0
#    for d in number:
#        n = base * n + d
#    return n