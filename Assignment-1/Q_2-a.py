m = input("Enter the message to be encoded:")
k = int(input("Enter the key:"))
str=""
for ch in m:
    if ch==' ':
        str=str+ch
    else:
        asc=ord(ch)
        c=asc+k
        if c>ord('z'):
            c=c-26
        str=str+chr(c)
print(str)