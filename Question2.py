# Q.2 Python object ko json data main convert karne ka program likho?


import json

dict1={
  "name":"david",
  "class":"I",
  "age":6
}
my_file=open("MYFILE.json","w")
json.dump(dict1,my_file,indent=6)
my_file.close()





import json
python_obj = {
  "name": "David",
  "class":11,
  "age": 17 
}
print(type(python_obj))
j_data = json.dumps(python_obj)
print(j_data)

