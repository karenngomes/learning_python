def toString(n, base):
    convString = "0123456789ABCDEF"
    if n < base:
        return convString[n]
    else:
        return toString(n//base, base) + convString[n%base]

print(toString(10,2))