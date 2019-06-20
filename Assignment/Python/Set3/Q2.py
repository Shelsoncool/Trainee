import re
email=input("Enter the email:")
patt="^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
#print(patt)
if len(email)>7:
    if re.match(patt,email):
        print("Email is valid")
    else:
        print("Email is Invalid")
else:
    print("Email should contain atleat 8 character")
