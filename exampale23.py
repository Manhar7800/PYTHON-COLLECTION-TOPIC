#nested loop : loop ke ander loop exampale:

l1=[1,2,3]
l2=["python","java","android"]

result=[(i,j) for i in l1 for j in l2]
print(l1)
print(l2)
print(result)