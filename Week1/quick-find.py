def quickFind(n,edges):
    cc = [i for i in range(n)]

    for edge in edges:
        u, v = edge
        if cc[u] != cc[v]:
            c1 = cc[v]
            c2 = cc[u]

        for i in range(n):
            if cc[i] == c2:
                cc[i] = c1

    return cc

if __name__ == "__main__":
    n = int(input("n->"))
    edges = []
    line = input("->")
    while line:
        edges.append([int(vertex) for vertex in line.split()])
        line = input("->")

    cc = quickFind(n,edges)
    print(cc)