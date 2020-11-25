##przesunięcie o 3 litery a->d itd
def encode(s):
    new = [x for x in s]
    list_ord = []
    result = []
    for el in new:
        list_ord.append(ord(el))
    for el in list_ord:
        if 96 < el < 119 or 64 < el <87:
            result.append(chr(el+3))
        elif el+3 > 122 or el+3 > 90:
            result.append(chr(el-23))
        else:
            result.append(chr(el))
    return result



def decode(s):
    new = [x for x in s]
    list_ord = []
    result = []
    for el in new:
        list_ord.append(ord(el))
    for el in list_ord:
        if 99 < el < 123 or 67 < el <91:
            result.append(chr(el-3))
        elif el > 64 and el-3 < 65:
            result.append(chr(el+23))
        elif el > 96 and el-3 < 97:
            result.append(chr(el+23))   
        else:
            result.append(chr(el))
    return result
