# Write a function:
# def solution(A, B, K)
# that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:
# { i : A ≤ i ≤ B, i mod K = 0 }
#
# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
#
# Assume that:
# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.
#
# Complexity:
# expected worst-case time complexity is O(1);
# expected worst-case space complexity is O(1).


def solution(A, B, K):
    diffs = B // K - A // K
    if A % K == 0:
        diffs += 1
    return diffs


print(solution(0, 0, 1), "(Right answer: 1)")
print(solution(0, 1, 1), "(Right answer: 2)")
print(solution(1, 2, 1), "(Right answer: 2)")
print(solution(0, 2, 2), "(Right answer: 2)")
print(solution(0, 4, 2), "(Right answer: 3)")
print(solution(1, 4, 2), "(Right answer: 2)")
print(solution(6, 11, 2), "(Right answer: 3)")
print(solution(6, 11, 3), "(Right answer: 2)")
print(solution(6, 12, 3), "(Right answer: 3)")
