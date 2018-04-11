def bigger_than_0(num):
    if num > 0:
        return num
    else:
        exit()

vertices = bigger_than_0(int(raw_input("Podaj liczbe wierzcholkow:\n")))
v_list = []

i = 1
while vertices >= i:
    neighbors = raw_input("Podaj sasiadow wierzcholka nr. %i \n" % (i)) #Podaj numery sasiadow po przecinku
    neighbors = list(neighbors.split(","))
    amount = len(neighbors)
    v_list.append(amount)
    i += 1

i = 1
for i, items in enumerate(v_list):
    print "deg(%i) = %i" % (i, items)

print "delta deg =", max(v_list)