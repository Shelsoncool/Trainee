import re
phone=input("Enter the sentence:")
patt="^([6-9])\d{9}$"
patt1="[0-9]{10}"
num=re.findall(patt1,phone)
print(num)
