a =[]
while len(a) < 7:
    inp = int(input(f"Adj meg egy számot({len(a)+1}/7): "))
    a.append(inp)

for i in range (1,7):
    j = i-1
    while j >= 0 and a[j] > a[j+1]:
        a[j], a[j+1] = a[j+1], a[j]
        j = j-1
print(a)
