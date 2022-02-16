import json


dic={
    "shopping_list":
        { 
            "chaco":15,
            "biscuits":50,
            "diary_milk":30,
            "ice_cream":20,
        } 
}
# my_file=open("MYFILE.json","w")
# json.dump(dic,my_file,indent=4)
# my_file.close()
s=input("enter the key:-")
num=int(input("enter the number:-"))
add=0
for i in dic:
    for j in dic[i]:
        if s in j:
            add=dic[i][j]+num
print(add)
print(json.dumps(dic,indent=4))
