# Q6.Python object key unique key value ko access karne ka program likho?


# import json

# d1={
#     "a":  1,
#     "a":  2,
#     "a":  3, 
#     "a": 4,   
#     "b": 1, 
#     "b": 2
# }
# a={}
# for i in d1:
#     if d1[i] not in a:
#         a.update(d1)
# print(a)



# a=[99,9,73,-5,0,-2,10,70,80]
# i=0
# b=[]
# while i<len(a):
#     if a[i]<0:
#         b.append(0)
#     else:
#         b.append(a[i])
#     i+=1
# print(b)
# i=0
# b=[]
# while i<len(a):
#     if a[i]>50:
#         b.append(0)
#     else:
#         b.append(a[i])
#     i+=1
# print(b)



# a=[99,9,73,-5,0,-2,10,70,80]
# i=0
# b=[]
# while i<len(a):
#     if a[i]<0:
#         b.append(0)
#     elif a[i]>50:
#         b.append(0)
#     else:
#         b.append(a[i])
#     i+=1
# print(b)


# num=[101,110,1101,1011]
# a=[]
# i=0
# while i<len(num):
#     h=str(num[i])
#     s=" "
#     j=0
#     while j<len(h):
#         if h[j] in "0":
#             pass
#         else:
#             s+=h[j]
#         j+=1
#     a.append(int(s))
#     i+=1
# print(a)


num=[2,5,3,4,7,10]
a=[]
i=0
while i<len(num):
    b=(num[i]**2)+1
    a.append(b)
    i+=1
print(a)
