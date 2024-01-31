def encrypt(pt,key):
    enc_list = []

    for i in pt:
        if i.isupper():
            enc_list.append(ord(i)-65)
        else:
            enc_list.append(ord(i)-97)
    enc_list = [(i+key)%26 for i in enc_list]
    ct = ""
    for i in enc_list:
        ct += chr(i+65)

    return ct
    

def decrypt(ct,key):
    
    dec_list = [ord(i)-65 for i in ct]
    dec_list = [(i-key)%26 for i in dec_list]
    
    dt = ""
    for i in dec_list:
        dt += chr(i+65)

    return dt
    
pt = input("Enter Plain Text: ")

#(Say)

KEY = 5

ct = encrypt(pt,KEY)
print(encrypt(pt,key=KEY))
print(decrypt(ct,KEY))