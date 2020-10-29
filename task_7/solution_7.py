s = input()
t = ""
is_palindrom = False
for i in range(len(s)-1, -1, -1):
	t += s[i]
if t == s:
    is_palindrom = True
print(is_palindrom)
