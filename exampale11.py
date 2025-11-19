l1=[10,20,30] # selo copy
print(l1)
print("----------------------------------------")

l2=l1 #store addres of l1
print(l2)

print("----------------------------------------")

l1.append(100)
print(l1)
print(l2)

print("----------------------------------------")

l2.append("5050")
print(l1)
print(l2)