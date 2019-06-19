n=int(input("Enter the limit:"))
list1=[]
odd=[]
print("Enter the numbers:")
for i in range(0,n):
    num=int(input(""))
    list1.append(num)

print("Numbers are")
print(list1)

for i in list1:
    if i %2 >0:
        odd.append(i)
        odd.sort()
print("Smallest odd nummbers are:")
print(odd[0])

