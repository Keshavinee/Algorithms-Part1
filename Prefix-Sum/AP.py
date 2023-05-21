'''
Description

    Given an array of N integers and Q queries. In each query two integers L, R is given, you have to find (A[L] + A[L+1]*2 + A[L+2]*3 + A[L+3]*4...A[R]*(R-L+1)) % 10^9+7.

Input Format

    The first line contains two space-separated integers N, Q where 1<=N<=10^6, 1<=Q<=10^6.

    Next line contains N space-separated integers (-1e9<=Ai<=1e9).

    Next Q lines contain two space-separated integers L, R where 1<=L<=R<=N.

Output Format

    For each query print the value of (A[L] + A[L+1]*2 + A[L+2]*3 + A[L+3]*4...A[R]*(R-L+1)) % 10^9+7 in a new line.

$ = Summation from L to R 

${A[i]*(i-L+1)} = ${A[i]*i} + (1-L)*${A[i]}

'''
def prefix_sum(lst,n):
    sum = 0
    A = []
    for i in range(n):
        sum += lst[i]
        A.append(sum)
    return A

if __name__ == '__main__':
    n, q = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    B = [A[i]*(i+1) for i in range(n)]

    C = prefix_sum(A,n)
    D = prefix_sum(B,n)

    for i in range(q):
        l, r = [int(i) for i in input().split()]
        print( (D[r]-D[l]) + (1-l)*(C[r]-C[l]) )
        