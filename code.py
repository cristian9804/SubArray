def isSubArray(A,B):
    for i in range(len(A)):
        j=A[i: i+len(B)]
        y=0
        if B[y] == j[y]:
            if B[y+1] == j[y+1]:
                if B[y+2] == j[y+2]:
                    return True
    return False
