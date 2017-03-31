# p0 = 0
# p1 = a0
# p2 = a0 + a1
# p3 = a0 + a1 + a2
# . . .
# pn = a0 + a1 + . . . + an−1
# O(n)


def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


# assume that you are asked about the totals of m slices
# [x..y] such that 0 =< x =< y < n,
# where the total is the sum
# ax + ax+1 + . . . + ay−1 + ay
# O(1)


def count_total(P, x, y):
    return P[y + 1] - P[x]
