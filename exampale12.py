#deep copy

a=[10,20,30]
print(a)

print("-------------------------------------")


b=a.copy()#store value of a
print(b)

print("----------------------------------------------------")

a.append(100)
print(a)
print(b)