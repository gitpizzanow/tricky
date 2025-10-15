w1 = "abcde"
w2 = "abcy"

idx = 0

for c in [i for i in w1]:
    if c not in w2:
        idx = w1.index(c)
        break

print(
    w1[:idx]
)
