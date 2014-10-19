def left_side(A):
    return A[:(len(A)//2)]

def right_side(A):
    return A[int((len(A) + 0.5)//2):len(A)]

def merge_count_inv(B, C):
    i = 0
    j = 0
    inv = 0
    D = []
    #inv = []
    for k in range(len(B) + len(C)):
        if j >= len(C) or (i < len(B) and B[i] <= C[j]): #use logic shortcuts to prevent out of bounds list access
            D.append(B[i])
            i+=1
        else:
            D.append(C[j])
            #for x in range(i,len(B)):
                #inv.append((B[x],C[j]))
            inv += len(B) - i
            j+=1
    return inv, D

def count_inv(A):
    if len(A) <= 1:
        return (0, A)
        #return ([], A)
    left, B = count_inv(left_side(A))
    right, C = count_inv(right_side(A))
    split, D = merge_count_inv(B,C)
    return (left + right + split), D

    
import sys
 
A = []
if (len(sys.argv) <= 1):
    print("bad input")
else:
    with open(sys.argv[1]) as f:
        A = f.readlines()
        A = [int(x.strip("\n")) for x in A]
    inv, D = count_inv(A);
    print("inversions = ", inv)