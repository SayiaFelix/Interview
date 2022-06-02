from array import array


arr = {1, 2, 3, 4, 5, 6}

#format of solution

# Python program to find out
# Sum of elements at even and
# odd index positions separately
 
# Function to calculate Sum

def EvenOddSum(a, n):
    even = 0
    odd = 0
    array = []
    for i in range(n):
 
        # Loop to find even, odd Sum
        if i % 2 == 0:
            even += a[i]
        else:
            odd += a[i]
     
    print ("Even index positions sum ", even)
    print ("nOdd index positions sum ", odd)
 
 
# Driver Function
 
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
 
EvenOddSum(arr, n)
 
