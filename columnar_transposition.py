#------ CREDITS - RAHUL RAM -------------------

key = input("Enter Key: ")
pt = input("Enter Plain Text: ")
#key = "nice"
et = "ahrhtsa"

#Rank Key

col = ["" for _ in range(len(key))]

for idx, i in enumerate(pt):
    col[idx%len(key)] += i

key_idx = [[ch, idx] for idx, ch in enumerate(key)]
key_idx.sort(key = lambda x : x[0])

encrypted_text = ""
for _, idx in key_idx:
    encrypted_text += col[idx]

print(encrypted_text)

#Decrypt

key_idx = key_idx = [[ch, idx] for idx, ch in enumerate(key)]
key_idx.sort(key = lambda x : x[0])

length = [0 for _ in range(len(key))]
for idx in range(len(et)):
    length[idx%len(key)] += 1

index = 0
col = ["" for _ in range(len(key))]
for ch, idx in key_idx:
    col[idx] = et[index: index+length[idx]]
    index += length[idx]

col = [list(i) for i in col]

pt = ""
for i in range(len(et)):
    pt += col[i%len(key)].pop(0)

print(pt)
# --- CREDITS -> RAHUL RAM ------
# key_list = list(key)

# ord_list = [ord(i) for i in key_list]
# ord_list.sort()

# char_list = [chr(i) for i in ord_list]

# print(ord_list)
# print(char_list)

# rank_list = np.zeros(len(key_list))

# for i in range(len(key_list)):
#     for j in range(len(key_list)):
#         if char_list[i] == key_list[j]:
#             rank_list[j] = j+1
# print(rank_list)
