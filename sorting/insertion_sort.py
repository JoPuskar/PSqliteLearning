def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j
        while i > 0:
            if A[i-1] > key:
                A[i] = A[i-1]
                i = i - 1
                A[i] = key
            else:
                break
    return A


A = [23, 3, 4, 45, 7, 9]
print(insertion_sort(A))