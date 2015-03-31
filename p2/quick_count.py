def quick_count(A, left, right, piv_fn, rec):
    #print("left index = ", left, "right index =", right)
    #print("recursion depth =", rec)
    #print(A)
    if (left == right) or right < 0 or left < 0 or left > right:
        #print("no comparisons !!!!!!!!!!", left, right)
        return 0;
    comparisons = right - left;
    pivot = piv_fn(A, left, right)
    p = partition(A, pivot, left, right)
    rec += 1
    #print("rec",rec, "comps on this level and side =", comparisons)
    comparisons += quick_count(A, left, p-1, piv_fn, rec)
    comparisons += quick_count(A, p+1, right, piv_fn, rec)
    #print("rec",rec, "summed comparisons =", comparisons, "l/r", left, right)
    return comparisons

def partition(A, pivot, first, last):
    if first == last:
        return first, first, last
    if pivot != first:
        #print("swap to first", A)
        A[first], A[pivot] = A[pivot], A[first]
        #print("\t", A)
    min = first + 1;
    for seen in range(first+1,last+1):
        #print("looking at index", seen, "with value =", A[seen], "min =", min)
        if A[seen] < A[first]:
         #   print("swap to min", A)
            A[seen], A[min] = A[min], A[seen]
          #  print("\t", A)
            min+=1
    min -= 1
    #print("final swap to min", A)
    A[first], A[min] = A[min], A[first]
    #print("\t", A)
    #print("\t\tpartition returning", min)
    return min
    
def piv_first(A, left, right):
    return left
def piv_last(A, left, right):
    return right
def piv_median(A, left, right):
    first = A[left]
    last = A[right]
    middle = A[(right-left)//2 + left]
    #print(A[left:right+1],"\nleft/right =", left, right)
    #print("middle index =", ((right-left)//2) + left)
    #print("f/m/l =", first, middle, last)
    B = [first, middle, last]
    B.sort()
    if B[1] == first:
        return left
    elif B[1] == last:
        return right
    elif B[1] == middle:
        return ((right-left)//2) + left
    
import sys
A = []
with open(sys.argv[1]) as f:
    A = [int(line.rstrip()) for line in f]
B=A[:]
C=A[:]

#D = [8,2,4,5,7,1]
#print ("median pivot of D, ", D, ", is index = ", piv_median(D, 0, len(D)-1))

comparisons = quick_count(A, 0, len(A)-1, piv_first, 0)
print("First Comparisons = ", comparisons)

comparisons = quick_count(B, 0, len(B)-1, piv_last, 0)
print("Last Comparisons = ", comparisons)

comparisons = quick_count(C, 0, len(C)-1, piv_median, 0)
print("Median Comparisons = ", comparisons)
