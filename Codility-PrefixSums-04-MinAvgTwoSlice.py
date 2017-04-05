# A non-empty zero-indexed array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N,
# is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the
# sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice.
# To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).
#
# For example, array A such that:
#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# contains the following example slices:
# slice (1, 2), whose average is (2 + 2) / 2 = 2;
# slice (3, 4), whose average is (5 + 1) / 2 = 3;
# slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
# The goal is to find the starting position of a slice whose average is minimal.
#
# Write a function:
# def solution(A)
# that, given a non-empty zero-indexed array A consisting of N integers, returns the starting position of the slice with the minimal average.
# If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.
#
# For example, given array A such that:
#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# the function should return 1, as explained above.
#
# Assume that:
# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−10,000..10,000].
#
# Complexity:
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
# Elements of input arrays can be modified.

def solution(A):
    n = len(A)
    min_res = (A[0] + A[1]) / float(2)
    min_index = 0
    for i in range(n - 1):
        # sum of slice of 2 elements
        total = A[i] + A[i + 1]
        avg = total / float(2)
        if avg < min_res:
            min_res = avg
            min_index = i
        # sum of slice of 3 elements
        if (i + 2 < n):
            total += A[i + 2]
            avg = total / float(3)
            if avg < min_res:
                min_res = avg
                min_index = i
    return min_index


print(solution([1, 2]), "(Right answer: 0)")
print(solution([1, 2, 3]), "(Right answer: 0)")
print(solution([3, 2, 1]), "(Right answer: 1)")
print(solution([3, 1, 2]), "(Right answer: 1)")
print(solution([1, -2]), "(Right answer: 0)")
print(solution([1, -2, 3]), "(Right answer: 0)")
print(solution([1, -2, 3,-3]), "(Right answer: 1)")
print(solution([4, 2, 2, 5, 1, 5, 8]), "(Right answer: 1)")
