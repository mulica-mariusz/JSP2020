from SzyfrCezara import decode,encode


w = input()
print("".join(encode(w)))
print("".join(decode(encode(w))))
