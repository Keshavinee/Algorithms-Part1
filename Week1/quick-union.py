def findRoot(lst,p):   
    if lst[p] == p:
        return p
    return findRoot(lst,lst[p])

def quickUnion(n,edges):
    cc = [i for i in range(n)]

    for edge in edges:
        u, v = edge
        r1 = findRoot(cc,u)
        r2 = findRoot(cc,v)

        if r1 != r2:
            cc[r1] = r2
        print(cc)
    return cc

if __name__ == "__main__":
    n = int(input("n->"))
    edges = []
    line = input("->")
    while line:
        edges.append([int(vertex) for vertex in line.split()])
        line = input("->")

    cc = quickUnion(n,edges)
    print(cc)