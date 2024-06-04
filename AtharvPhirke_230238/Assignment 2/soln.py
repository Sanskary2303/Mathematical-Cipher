input_file = open('cipher.txt','r')
input_str = input_file.read()
input_file.close()


output_file = open("plain.txt", "a")


key = "\0" 

inputlen = len(input_str)
# inputlen = 5

def encode(i, c, keylen) :
    return ord(c) ^ ord(key[i % keylen])


# def genKey(c) :
#     global key
#     if ord(key[c]) >= 255:
#         # key[c] = "\0"
#         key = key[:c-1] + "\0" + key[c+1:]
#         if len(key) == c+1:
#             key = key + chr(1)
#         else :
#             # key[c+1] += 1
#             if ord(key[c+1]) >= 255 :
#                 genKey(c+1)
#             else :
#                 key = key[:c] + chr(ord(key[c+1]) + 1) + key[c+2:]
#     return 

def genKey(c):
    global key
    if ord(key[c]) >= 256:
        key = key[:c] + "\0" + key[c+1:]
        if c < len(key) - 1:
            if ord(key[c+1]) >= 256:
                genKey(c+1)  
            else:
                key = key[:c+1] + chr(ord(key[c+1]) + 1) + key[c+2:] 
        elif c+1 == len(key):
            key = key + chr(1)
    return


def printASCII(key, keylen) :
    for i in range(keylen) :
        print(str(ord(key[i])), end = " ")
    return

for i in range (256 ** inputlen - 1):
    if ord(key[0]) >= 256 :
        genKey(0)
    else :
        if(len(key) == 1) :
            key = chr(ord(key[0]) + 1)
        else :
            key = chr(ord(key[0]) + 1) + key[1:]

    genKey(0)
    keylen = len(key)
    printASCII(key, keylen)
    print()
    output_file.write("0x")
    for i in range(inputlen) :
        # if want to represent the code in hex code uncomment this-
    #   output_file.write(str(hex(encode(i, input_str[i], keylen)) [2:]))
    #   output_file.write(" ")

        # if want to include only the chars of the keyboard ->
        c = encode(i, input_str[i], keylen)
        if c >= 126 or c <= 31 :
            break
        output_file.write(chr(c))
        
    output_file.write("\n")
