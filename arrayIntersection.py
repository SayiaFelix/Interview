# array1=[6,2,4,5,1,7,9,0]
# array2=[0,6,4,7,8,7,9,10]
# array3=[9,4,7,5,1,6,11,0]

# def findIntersection(array1, array2, array3):
#     result=[]
#     x=0
#     y=0
#     z=0

# Python program to illustrate the intersection
# of two lists in most simple way
def intersection(lst1, lst2):
	lst3 = [value for value in lst1 if value in lst2]
	return lst3

#  Code
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))
   
# Python program to illustrate the intersection
# of two lists using set() method
def intersection(lst1, lst2):
	return list(set(lst1) & set(lst2))

# Driver Code
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
print(intersection(lst1, lst2))


# Python program to illustrate the intersection
# of two lists using set() and intersection()
def Intersection(lst1, lst2):
	return set(lst1).intersection(lst2)
	
# Driver Code
lst1 = [ 4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
lst2 = [9, 9, 74, 21, 45, 11, 63]
print(Intersection(lst1, lst2))
