# Q.3 Python object ko json string mai convert karne ka program likho?



import json

# a={'Navgurukul': 100}
# mystring=json.dumps(a)
# print(mystring)

x={
    "name":"Rani",
    "Age":17,
    "city":"New York"
}
# y=open("Meraki q3.json","w")
# y.write(json.dump(x,y,indent=4))
# y.close()
y=json.dumps(x)
print(y)




# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# print(json.dumps(x, indent=4, separators=(". ", " = "),sort_keys=True))

