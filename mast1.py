n = 5
m = 1
h = 4
vi = [1,2,3,1,3]
vi.sort()

for x in range(m):
    if h >= vi[x] :
        h -= vi[x]
    else:
        h = 0
print(h)
    