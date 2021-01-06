##przesunięcie o 3 litery a->d itd
def encode(s, n):
    new = [ord(x) for x in s]
    result = []
    for el in new:
        if 96 < el < (123-n) or 64 < el < (91-n):
            result.append(chr(el+n))
        elif el+n > 123 or el+n > 91:
            result.append(chr(el-26+n))
        else:
            result.append(chr(el))
##    print("".join(result))
    return "".join(result)


def decode(s, n):
    new = [ord(x) for x in s]
    result = []
    for el in new:
        if 96+n < el < 123 or 64+n < el <91:
            result.append(chr(el-n))
        elif el > 64 and el-n < 65:
            result.append(chr(el+26-n))
        elif el > 96 and el-n < 97:
            result.append(chr(el+26-n))   
        else:
            result.append(chr(el))
    return "".join(result)
