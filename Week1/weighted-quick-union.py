def findRoot(lst,p):   
    if lst[p] == p:
        return p
    return findRoot(lst,lst[p])

def height(lst,n,p,m,c=0):
    for i in range(n):
        if i != p and lst[i] == p:
            m[0] = max(m[0],c+1)
            height(lst,n,i,m,c+1)

def quickUnion(n,edges):
    cc = [i for i in range(n)]

    for edge in edges:
        u, v = edge
        r1 = findRoot(cc,u)
        r2 = findRoot(cc,v)

        if r1 != r2:
            h1 = [0] ; h2 = [0]
            height(cc,n,r1,h1)
            height(cc,n,r2,h2)

            if h1 >= h2:
                cc[r2] = r1
            else:
                cc[r1] = r2
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