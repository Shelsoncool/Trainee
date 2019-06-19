tup=(1,2,3,4,5,6,7,8,9,10)
list1=[]
for i in tup:
    if i % 2 ==0:
            list1.append(i)
tupp=tuple(list1)
print("The Sequence of numbers are:")
print(tup)
print("The Even numbers are:")
print(tupp)
