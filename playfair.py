import string

alphabet = string.ascii_uppercase
key = input("Enter KEY: ")
alphabet_set = []

for i in alphabet:
    if i.upper() not in key and i.lower() not in key:
        alphabet_set.append(i)
if "J" in alphabet_set:
    alphabet_set.remove("J")

key = key.upper()
key = key.replace("J","I")
key_list = []

for i in key:
    if i not in key_list:
        key_list.append(i)

# Generating the Matrix
        

matrix = []
c1 = 0 #For Key

c2 = 0 #For Matrix

for i in range (5):
    row = []
    for j in range (5):
        if (c1 < len(key_list)):
            row.append(key_list[c1])
            c1 += 1
        else:
            row.append(alphabet_set[c2])
            c2+=1
    matrix.append(row)

#Perform Playfair
ct = ""

PT = input("Enter plain text: ")

PT = PT.upper()

#Generating two grams
two_grams = []
i=0

#Pad
if len(PT)%2==1:
    PT+=" "

while (i<len(PT)):
    gram = []
    gram.append(PT[i])

    i+=1

    if (PT[i] in gram) or (PT[i]==" "):
        gram.append("X")

    else:
        gram.append(PT[i])
    i+=1

    two_grams.append(gram)
print(two_grams)

#Get Position
def get_pos(x,matrix):
    for i in range (5):
        for j in range (5):
            if matrix[i][j] == x:
                return i,j
    return -1

#Playfair Algorithm
CT = ""
for i in two_grams:
    row1,col1 = get_pos(i[0],matrix)
    row2,col2 = get_pos(i[1],matrix)

    if row1 == row2:
        CT+= matrix[row1][(col1+1)%5]
        CT+= matrix[row1][(col2+1)%5]
        continue

    elif col1 == col2:
        CT+= matrix[(row1+1)%5][col1]
        CT+= matrix[(row2+1)%5][col2]
        continue

    else:
        CT += matrix[row1][col2]
        CT += matrix[row2][col1]
        continue

print(CT)

    




        




