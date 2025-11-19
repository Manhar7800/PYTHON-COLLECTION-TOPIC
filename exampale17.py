#without list comprehension::

l1=[45,2,64,7,8,12,49]
even_list=[]


for i in l1:
    if i%2==0:
        even_list.append(i)
        print(even_list)