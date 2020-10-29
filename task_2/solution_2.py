a = input()
m = 0
res = ''
for i in a:
  count = a.count(i)
  if count > m:
    m = count
    res = i
print(res)
