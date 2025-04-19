ciph = input("Enter the cipher text:")
for k in range(0,26):
    m=""
    for ch in ciph:
        if ch==' ':
            m = m+" "
        else:
            c=ord(ch)
            asc=c-k
            if asc<ord('a'):
                asc=asc+26
            m=m+chr(asc)
    print("For k = "+str(k)+" the message will be "+'\''+m+'\'')