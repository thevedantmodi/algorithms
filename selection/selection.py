def Select(A, left, right, k):
    pivot = A[right]
    p = left

    for i in range(left, right):
        if A[i] < pivot:
            A[i], A[p] = A[p], A[i]
            p += 1

    # Finally swap the right and pivot
    A[p], A[right] = A[right], A[p]
        
    if k == p:
        return A[p]
    elif k < p:
        return Select(A, left, p - 1, k)
    else:
        return Select(A, p + 1, right, k)
        

assert(Select([2, 12, 4, 123, 3, 1], 0, 5, 2) == 3)
