def vernam_encryption(pt,key):
    if (len(pt)!=len(key)):
        return "Vernam not possible, lengths don't match"

    pt = pt.upper()
    key = key.upper()
    pt_list = [ord(i)-65 for i in pt]
    key_list = [ord(i)-65 for i in key]

    enc = []
    for i in range(len(pt_list)):
        if (pt_list[i]+key_list[i] < 26):
            res = (pt_list[i] + key_list[i])
        else:
            res = ((pt_list[i] + key_list[i])-26)
        enc.append(res)
    enc = [chr(i+65) for i in enc]
    return "".join(enc)

def vernam_decryption(ct,key):
    key = key.upper()
    
    ct_list = [ord(i)-65 for i in ct]
    key_list = [ord(i)-65 for i in key]

    dec = []
    for i in range(len(ct)):
        if (ct_list[i]-key_list[i]>=0):
            res = (ct_list[i] - key_list[i])
        else:
            res = ((ct_list[i] - key_list[i])+26) 
        dec.append(chr(res+65))  
    return "".join(dec)

pt = input("Enter plain text: ")
key = input("Enter key of same length: ")

ct = vernam_encryption(pt,key)

print(ct)


print(vernam_decryption(ct,key))
