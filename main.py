a = []
while True:
    inp = input(f"Adj meg egy számot({len(a)+1}): ")
    if inp == "":
        break
    else:
        a.append(int(inp))

for i in range (1,len(a)):
    j = i-1
    while j >= 0 and a[j] > a[j+1]:
        a[j], a[j+1] = a[j+1], a[j]
        j = j-1
print(a)
