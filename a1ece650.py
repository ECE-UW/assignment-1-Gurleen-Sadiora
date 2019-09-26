import re

dict = {}
a = 0
#POI = []
V = {}
E = set()
Edges = set()

print("Enter the commands...")
print("You can enter these 4 commands")
print('(1) add a street,     FORMAT:  a "King Street S" (4,2) (4,8) ')
print('(2) change a street,  FORMAT:  c "King Street S" (4,1) (4,8) ')
print('(3) remove a street,  FORMAT:  r "King Street S"  ')
print('(4) generate a graph, FORMAT:  g ')

def main():
   
    try:
        while (True):
            string = raw_input()
            if (inputvalidate(string)):
                print("input validated")
            if (string == 'g'):
                break

            #print(dict)
        E = printing(a)
        #print(E)
        E = list(E)
        #print(E)
        E = list(map(eval, E))
        modify(E)
        #print(E)
        final_output(E)

        print("Another Command..??")
        print("Enter Y or N")
        command = raw_input()
        if(command == 'Y'):
            main()






    except Exception as e:
        print( e)


def inputvalidate(string):
    list1 = re.findall(r'"([^"]*)"', string)
    # list2 = re.findall(r'\(([^\(]*)\)', str)
    if (re.match('^[a]\s"[\s\w]+"((\s\([-]?\d,[-]?\d\)){2,})$', string)):
        if (streetexist(string)):
            print("Error: Street already exists")
            return False
        else:
            # list.append(list1[0])
            # print(list)
            dict[list1[0]] = string.split()[index_of_split(string):]
            # list.append(list2)
            return True

    elif (re.match('^[c]\s"[\s\w]+"((\s\([-]?\d,[-]?\d\)){2,})$', string)):
        if (streetexist(string)):
            # dict[list1[0]] = re.findall(r'\(([^\(]*)\)', str)
            dict[list1[0]] = string.split()[index_of_split(string):]
            return True
        else:
            print("Error: This street is not added to the map, so cannot be changed")
            return False

    elif (re.match('[r]\s"[\s\w]+"', string)):
        if (streetexist(string)):
            del dict[list1[0]]
            return True
        else:
            print("Error: This street is not added to the map, so cannot be removed")
            return False

    elif (string == 'g'):
        return True

    else:
        print("Error: Incorrect Format")
        return False

def index_of_split(string):
    c = 0
    for i in string:
        if (i == " "):
            c += 1
        if (i == '('):
            break

    return c

def streetexist(string):
    street = re.findall(r'"([^"]*)"', string)
    if(street[0] in dict.keys()):
        return True
    else:
        return False

def printing(a):
    dictlist = list(dict.values())
    for x in range(0, len(dictlist) - 1):
        for y in range(0, len(dictlist[x]) - 1):
            for p in range(x + 1, len(dictlist)):
                for z in range(0, len(dictlist[p]) - 1):
                    P1 = eval(dictlist[x][y])
                    P2 = eval(dictlist[x][y + 1])
                    P3 = eval(dictlist[p][z])
                    P4 = eval(dictlist[p][z + 1])
                    P = line_intersect(P1, P2, P3, P4)
                    # POI.append(P)
                    # print(P1,P2,P3,P4)
                    if (P):
                        # print(P)
                        V[check_point(P, a)] = P
                        a += 1
                        V[check_point(P1, a)] = P1
                        a += 1
                        V[check_point(P2, a)] = P2
                        a += 1
                        V[check_point(P3, a)] = P3
                        a += 1
                        V[check_point(P4, a)] = P4
                        a += 1
                        # E.add("<" + str(check_point(P1,a))+ "," + str(check_point(P,a))+ ">")
                        # E.add("<" + str(check_point(P,a))+ "," + str(check_point(P2,a))+ ">")
                        # E.add("<" + str(check_point(P3,a))+ "," + str(check_point(P,a))+ ">")
                        # E.add("<" + str(check_point(P,a))+ "," + str(check_point(P4,a))+ ">")
                        E.add(str(check_point(P1, a)) + "," + str(check_point(P, a)))
                        E.add(str(check_point(P, a)) + "," + str(check_point(P2, a)))
                        E.add(str(check_point(P3, a)) + "," + str(check_point(P, a)))
                        E.add(str(check_point(P, a)) + "," + str(check_point(P4, a)))
    return E


def line_intersect(p1, p2, p3, p4):
    A1 = (p1[1] - p2[1])
    B1 = (p2[0] - p1[0])
    C1 = -(p1[0] * p2[1] - p2[0] * p1[1])
    A2 = (p3[1] - p4[1])
    B2 = (p4[0] - p3[0])
    C2 = -(p3[0] * p4[1] - p4[0] * p3[1])

    D = A1 * B2 - B1 * A2
    Dx = C1 * B2 - B1 * C2
    Dy = A1 * C2 - C1 * A2
    if D != 0:
        x = Dx / D
        y = Dy / D
        if ((min(p1[0], p2[0]) <= x <= max(p1[0], p2[0])) and (min(p3[0], p4[0]) <= x <= max(p3[0], p4[0])) and \
                (min(p1[1], p2[1]) <= y <= max(p1[1], p2[1])) and (min(p3[1], p4[1]) <= y <= max(p3[1], p4[1]))):
            return x, y
    return False

def check_point(PTemp, a):
    for index, value in V.items():
        if (PTemp == value):
            return index
    return a

def modify(E):
    for P in range(0,len(E)):
        for V1 in V.keys():
        #print(E[P][0], E[P][1], V1)
            #if():
            if(E[P][0] != V1 and E[P][1] != V1 and points_are_collinear_and_edges_overlap(E[P][0], E[P][1], V1)):
                #print("True")
                E.append((E[P][0],V1))
                E.append((V1,E[P][1]))
                E.remove(E[P])
                modify(E)


def points_are_collinear_and_edges_overlap(E1, E2, E3):
    P1 = V[E1]
    P2 = V[E2]
    P3 = V[E3]
    # print(P1, P2, P3)
    if ((P3[1] - P2[1]) * (P2[0] - P1[0])) == ((P2[1] - P1[1]) * (P3[0] - P2[0])):
        if (min(P1[0], P2[0]) <= P3[0] <= max(P1[0], P2[0]) and min(P1[1], P2[1]) <= P3[1] <= max(P1[1], P2[1])):
            return True

def final_output(E):
    for i in E:
        Edges.add("<" + str(i[0]) + "," + str(i[1]) + ">")
    print(" V = " , V)
    print(" E = " ,Edges)


if __name__ == '__main__':
    main()
