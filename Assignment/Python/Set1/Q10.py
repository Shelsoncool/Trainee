a=[]
n=int(input("Enter the limit:"))
if n==0:
        print("Nobody like this")
        
for i in range(0,n):
    name=input("Enter the names:")
    a.append(name)
    
#print(len(a))
if len(a)==1:
    print(name +"Likes this")
elif len(a)==2:
    print(a[0]+" and "+ a[1] + " likes this")
elif len(a)==3:
    print(a[0]+", "+ a[1] + " and " + a[2]+ " likes this")
elif len(a)>3:
    print(a[0]+", "+a[1] +" and "+ str(len(a)-2)+" others likes this")
