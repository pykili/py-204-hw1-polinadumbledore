s = input()
t = ""
in_t = False 
for i in s:
  for j in t:
    if i == j:
      in_t = True
  if in_t == False:
        t += i
print(t)
