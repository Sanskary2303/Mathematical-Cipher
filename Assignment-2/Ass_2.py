import collections
import statistics

line = 'F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794'

ciphertext = []

for i in range(0, len(line)-2, 2):
    b = line[i] + line[i+1]
    ciphertext.append(int(b, 16))

def hex_print(c):
    for i in c:
        print("{:02X} ".format(i), end="")
    print()

def ischar(c):
    return (c >= 32 and c <= 47) or (c >= 57 and c < 127)

qis = []

for hkl in range(2, 10):
    # hkl - hypothetical key length
    # take each hkl-th character and form a string hcr - hypothetical cryptogram
    hcr = ciphertext[::hkl]
    #print('*** Trying key length', hkl)
    #hex_print(hcr)
    counter = collections.Counter(hcr)
    q = [x/len(hcr) for x in counter.values()]
    #print('q=', q)
    q2 = [x**2 for x in q]
    #print('q2=', q2)
    q3 = sum(q2)
    #print('q3=', q3, 'N=', hkl)
    if q3 > 0.065:
        print('*** Found key length N=', hkl)
        N = hkl

keystream = []

print('*** Trying to break key bytes')

english = 'etaoinshrdlcumwfgypbvkjxqz'

def distance(s1, s2):
    s2 = s2[:len(s1)]
    return sum(abs(ord(x) - ord(y)) for x,y in zip(s1, s2))

import difflib

for i in range(N):
    stream = ciphertext[i::N]
    print('stream=', end='')
    hex_print(stream)
    candidates = {}
    for k in range(256):
        fail = False
        stream_p = []
        for c in stream:
            p = c ^ k

            # even one non-alpha char means this key byte is wrong
            if not ischar(p):
                fail = True
                #print('x')
                break

            # append decrypted char to stream plaintext
            p = chr(p).lower()
            if p >= 'a' and p <= 'z':
                stream_p.append(p)

        if not fail:
            print('stream_p=', ''.join(stream_p))

        # test 1/2 all decrypted chars must be alpha
        if not fail:
            # test 2/2 letter frequency matches English
            print('*** Trying key byte i={} k={:02x}'.format(i, k))
            c = collections.Counter(stream_p)
            # because c.most_common() is a dictionary and dictionary hashes in Python
            # are randomized, the exact sequence returned here will be *different on each run*
            freq = ''.join(x[0] for x in c.most_common())
            ratio = difflib.SequenceMatcher(a=freq, b=english).ratio()
            print('freq=', freq, 'ratio=', ratio)
            candidates[k] = ratio

    keystream.append(max(candidates, key=candidates.get))

print('Keystream')
hex_print(keystream)

i = 0
plaintext = []
for c in ciphertext:
    p = c ^ keystream[i % len(keystream)]
    i += 1
    plaintext.append(chr(p))

for c in plaintext:
    print(c, end='')
