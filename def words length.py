
word = "abcderr"

"""
abcd , abc, ab, a ,
bcd, bc, b,
cd, c,
d

"""

# 0123, 012, 01,0
# 123,12,1
# 23,2
# 3



def affichage(word : str, k) -> list:
    L = list()
    for j in range(len(word)):
        for i in range(len(word)):
            myword = word[j:i+1]
            if len(myword) ==k:
                L.append(myword)
    return L


L = affichage(
    word, 4
)

print(L)
