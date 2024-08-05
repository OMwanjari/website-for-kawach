s = "ababcc"
d=dict()
for x in s:
    d[x] = s.count(x)
print(d)
print(min(d.values()))