from ast import Return


list = [ ]
exit = False
def createList():
    while exit == False:
        i = 0
        inp = input()
        if inp == "done":
            return list
        else:
            list.append(inp)

listaCompleta = createList()
print("lista completa:")
i = 0
for elem in list:
    i += 1
    print(i, "-", elem)