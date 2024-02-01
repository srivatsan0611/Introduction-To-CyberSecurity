import numpy as np

key = [[3,7],[5,12]]

pt = input("Plain Text: ")
pt = pt.upper()

digrams = []
i = 0

if len(pt)%2!=0:
    pt+=" "
while i<len(pt):
    gram = []
    gram.append(pt[i])
    i = i+1

    if pt[i] in gram or pt[i]==" ":
        gram.append("X")
    else:
        gram.append(pt[i])
    i+=1

    digrams.append(gram)

digram_nums = []

for i in digrams:
    dum = []
    
    dum.append(ord(i[0])-64)
    dum.append(ord(i[1])-64)

    digram_nums.append(dum)

print(digram_nums)

key = np.array(key)
digram_nums = np.array(digram_nums)

enc_nums = []
for i in digram_nums:
    i = i.reshape(-1,1)
    enc = key@i
    enc = (enc%26)

    enc = enc.T
    enc_nums.append(enc)

encrypted_text = ""

for i in enc_nums:
    encrypted_text+=chr(i[0][0]+64)
    encrypted_text+=chr(i[0][1]+64)

print(encrypted_text)


#Decryption


key_inverse = np.linalg.inv(key)
key_inverse = key_inverse%26
print("KEY INVERSE",key_inverse)

j = 0
digrams_dec = []

while j<len(encrypted_text):
    gram = []
    gram.append(encrypted_text[j])
    j+=1
    gram.append(encrypted_text[j])
    j+=1
    digrams_dec.append(gram)

digrams_dec_nums = []
for i in digrams_dec:

    dum = []
    dum.append(ord(i[0])-64)
    dum.append(ord(i[1])-64)

    digrams_dec_nums.append(dum)

digrams_dec_nums = np.array(digrams_dec_nums)
#print(digrams_dec_nums)

dec_nums = []
for i in digrams_dec_nums:
    i = i.reshape(-1,1)

    dec = (key_inverse@i) % 26 

    dec = dec.T
    dec_nums.append(dec)

decrypted_text = ""
for i in dec_nums:
    decrypted_text+= chr(int(round((i[0][0])))+64)
    decrypted_text+= chr(int(round((i[0][1])))+64)

print(decrypted_text)