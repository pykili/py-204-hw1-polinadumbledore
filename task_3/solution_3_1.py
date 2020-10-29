s = input()
t = ""
in_t = False 
for i in s:
  for j in t:
    if i == j:
      in_t = True
    else:
      in_t = False
  if in_t == False:
        t += i
print(t)
