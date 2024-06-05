# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oG-TcrEu9ebtOWTFg5Msnr59l7WQpkoN
"""

import matplotlib.pyplot as plt
from statistics import mode

with open("/content/cipher.txt", "r") as file:
    c = file.read().replace("\n", "")
f=open("/content/plain.txt","w")
print(type(c))
# c="F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794"
c=list(c)
d=""
d=list(d)
for i in range(int(len(c)/2)):
  e=""
  e=c[2*i]+c[2*i+1]
  d.append(e)

n=7#i know that key length is 7 because its the only length that can satisfy
t=""
t=list(t)
for j in range(n):
  r=""
  r=list(r)
  for i in range(int(len(d)/n)):
   e=d[n*i+j]
   r.append(e)
  c=mode(r)
  t.append(c)
print(t)

def check_key(c,d,i,n):
  for i1 in range(int(len(d)/n)):
    e=int(d[i+i1*n], 16)
    e=e^k
    if(e==44 or e==46 or e==32):
      continue
    if(e<65 or e>122):
      return False
    if(e>90 and e<97):
      return False

  return True

key=""
key=list(key)
for i in range(len(t)):
  r= int(t[i], 16)
  for j in range(128):
    k=r^j
    if(check_key(k,d,i,n)):
      key.append(k)
      break
print(key)
T=""

def decipher(d,key,T):
  for i in range(len(d)):
    r=int(d[i],16)
    x=i%len(key)
    r=r^key[x]
    t=chr(r)
    T+=t
  return T

  print(d)

TEXT=decipher(d,key,T)
print(TEXT)
f.write(TEXT)
f.close()

