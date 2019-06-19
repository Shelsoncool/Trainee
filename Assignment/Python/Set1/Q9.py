fname=input("Enter filename(test.txt):")
nword=0;
nline=0;
nchar=0;
with open(fname,'r') as f:
    print("The Data in files are:")
    for i in f:
        print(i)
        word=i.split(" ")
        nword+=len(word)
        nline+=1
        #print(len(word))
        #character
        nchar+=len(i)
        
        
    print("Number of character:"+ str(nchar))
    print("Number of Words are:" + str(nword))
    print("Number of Lines are:"+ str(nline))
    
    
