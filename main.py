# Beszúró rendezés
a = []
while 6 > len(a):
    inp = input(f"Adj meg egy számot({len(a)+1}/6): ")
    a.append(int(inp))

for i in range (1,6):
    j = i-1
    while j >= 0 and a[j] > a[j+1]:
        a[j], a[j+1] = a[j+1], a[j]
        j = j-1
print(a)

# Beszúró rendezés továbbfejlesztése
a = []
while 6 > len(a):
    inp = input(f"Adj meg egy számot({len(a)+1}/6): ")
    a.append(int(inp))

for i in range (1,6):
    j = i-1
    tmp = a[i]
    while  j>=0 and a[j]>tmp:
        a[j+1] = a[j]
        j = j-1
    a[j+1] = tmp
print(a)
