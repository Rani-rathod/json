# Q.1 Json data ko python object main convert karne ka program likho?.

# import json

# a='{"name":"Rani","age":17,"education":11}'
# b=open("meraki Q1.json","w")
# b.write(a)
# b.close()





num=[1,2,3,4,5,6,7,8,9,10]
i=0
a=[]
b=[]
while i<len(num):
    if num[i]%2==0:
        a.append(num[i])
    else:
        b.append(num[i])
    i+=1
print("even number",a)
print("odd number",b)
print(a[len(a)//2])
print(b[len(b)//2])

