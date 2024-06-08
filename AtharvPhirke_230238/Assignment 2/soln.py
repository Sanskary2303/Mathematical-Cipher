import sys

input_file = open('cipher.txt','r')
input_str = input_file.read()
input_file.close()


output_file = open("plain.txt", "a")

arr = []

for i in range (0, len(input_str), 2) :

    arr.append(int(input_str[i:i+2], 16))

# print(arr)
# max = 0
# maxInd = -1
# totals = []
# for keylen in range (1, 10):
#     count = [0] * 256
#     for c in range (keylen):
#         count[arr[c]] += 1

#     sq_counts = []
#     for i in count :
#         sq_counts.append((i/sum(count)) ** 2)
#     totals.append(round(sum(sq_counts), 4))

# print(totals)
# print(maxInd)

totals = []
for k in range (1, 14): # why is range not upto len(arr)? can be limited only till 14
    count = [0]*256
    for i in arr[::k]:
        count[i] += 1
    
    sq_counts = [(i/sum(count)) ** 2 for i in count] # what does this line mean!?
    totals.append(round(sum(sq_counts), 4))
# print(totals)

keylen = totals.index(max(totals)) + 1
key = []
for keyletter in range (keylen):
    letter = []
    j = []
    for i in range (keyletter, len(arr), keylen):
        j.append(arr[i])
    for b in range (256):
        valid = True
        ch = []
        countAll = [0]*256
        for x in j:
            num = b^x
            ch.append(num)
            if num >= 256 :
                break
            
            countAll[num] += 1
        sq = [(i/sum(countAll)) ** 2 for i in countAll]
        sumsq = sum(sq)
        print(sumsq)
        if min(ch) >= 32 and max(ch) <= 127 and countAll[ord('e')]/sum(countAll) > 0.10 and countAll[ord('t')]/sum(countAll) > 0.07 and 0.055 <= sumsq and sumsq <= 0.075:
            letter.append(ch)
    
    key.append(letter)
print(key)
    
