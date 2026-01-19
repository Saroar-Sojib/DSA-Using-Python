ransomNote = "aa"
magazine = "aab"
temp_char = {}
if ransomNote in magazine:
    print(True)
for x in ransomNote:
    if x in temp_char:
        temp_char[x]+=1
    else:
        temp_char[x]=0
for y in temp_char:
    if magazine.count(y)<=temp_char[y]:
        print(False)
        break 
print(True)

