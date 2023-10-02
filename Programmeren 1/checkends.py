def checkend(s):
    result = True
    if len(s) <= 0:
        result = False
    elif len(s) == 1:
        result = True
    else:
        first = s[0]
        last = s[len(s)-1]
        result = (first == last)
    return result

print(checkend(""))
print(checkend(" "))
print(checkend("binka"))
print(checkend("A121r23r2 235r2r3 34t34binka"))