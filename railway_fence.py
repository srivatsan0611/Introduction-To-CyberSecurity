pt = input("Enter plain text: ")
key = int(input("Enter key: "))

matrix = []

for i in range (key):
    row = ["" for _ in range (len(pt)) ]
    matrix.append(row)

#Fill the matrix according to the algorithm:

row,col = 0,0
direction = False
for i in range (len(pt)):
    if row==0 or (row==key-1):
        direction = not direction
    matrix[row][col] = pt[i]
    col+=1


    if direction:
        row+=1
    else:
        row-=1

encrypted = ""
for i in range (key):
    for j in range (len(pt)):
        if (matrix[i][j]!=""):
            encrypted+=matrix[i][j]

print(encrypted)


#Decryption

def decryptRailFence(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
                for j in range(key)]
     
    dir_down = None
    row, col = 0, 0
     
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
         
        rail[row][col] = '*'
        col += 1
         
        if dir_down:
            row += 1
        else:
            row -= 1
             
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
            (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
         
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             

        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)

print(decryptRailFence(cipher=encrypted,key=key))
