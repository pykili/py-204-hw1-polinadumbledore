t = ""
for k in range(10):
    s = input()
    for i in s:
        in_t = False
        for j in t:
            if i == j:
                in_t = True
        if in_t == False:
            t += i
print(t)
