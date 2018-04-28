#kod do uruchomienia zestwu plików z zajęć

import sys

f = open(sys.argv[1], mode='r')
a = f.read()
a = a.split()
edg_list = [int(item) for item in a]
f.close()

#Przykladowe wywolania:
graf1 = Graph(edg_list)
graf1.result()
