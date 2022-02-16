# import json
# dict1 ={
#     "emp1": {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": "34",
#         "salary": "54000"
#     },
#     "emp2": {
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": "24",
#         "salary": "40000"
#     },
# }
# out_file = open("myfile.json", "w")
# json.dump(dict1, out_file, indent = 4)
# out_file.close()



# Notes :-
# String =>  json.loads() => json objects
# Json object => json.dumps() => string
# Python object=> json.dump() => json object
# Json object => json.load() => python object





# import json

# a={
#     "name":"Rani",
#     "age":17,
#     "city":"Nashik",
#     "age":13
# }
# myfile=open("Nav.json","w")
# json.dump(a,myfile,indent=4)
# myfile.close()

# print(type(a))
# j_data=json.dumps(a)
# print(j_data)


# y=json.dumps(a)
# print(type(y))




# import json
# x = '{ "name":"John", "age":30, "city":"pune"}'
# y = json.loads(x)
# print(type(y))
# print(y)





import json
import os


print("***","WELCOME TO LOGIN SIGN UP PAGE","***")

def storng_password(password):
    if len(password)>6 and len(password)<16:
        if ("#" in password or "@" in password or "$" in password):
            if "1"in password or"2"in password or"3"in password or"4"in password or"5"in password or "6"in password or "7"in password or "8"in password or"9"in password or"0" in password :
                return True
            else:
                print(password,"At least password should contain one number")
                password1=input("enter your 1st password : ")
                storng_password(password1)

        else:
            print(password,"At least password should contain one special character")
            password1=input("enter your 1st password : ")
            storng_password(password1)
        
        
    else:
            print(password,"At least password should length 6 to 16 digit")
            password1=input("enter your 1st password :")
            storng_password(password1)

def checkpassword(password1,password2):
    if password1==password2:
        print("password created.")
    else:
        print("Both password are not same")
        password2=input("enter your password : ")
        checkpassword(password1,password2)

login_signup=input("what you choose login or signup : ")

file=os.path.exists("user.json")

if file==False:  
   
    if login_signup=="1":
        user_name=input("enter your user name : ")
        password1=input("enter your 1st password : ")
        storng_password(password1)
        password2=input("enter your password : ")
        checkpassword(password1,password2)
        mobile_number=int(input("enter the mobile number:-"))
        print("ok nexst")
       
        description=input("Information about you :")
        date_of_birth=input("enter your date of birth : ")
        gender=input("enter your gender (m or f) :")
        print("congrats",user_name,"you are Signed up Successfully.")
        mylist=[]
        user={}
        list1=["username","password","mobile_number","description","Birth of date","gender"]
        list2=[user_name,password1,mobile_number,description,date_of_birth,gender]
        for i in range(len(list1)):
            user.update({list1[i]:list2[i]})
        mylist.append(user)

        with open ("user.json","a")as p:
            json.dump(mylist,p,indent=4,)

elif file==True:
    if login_signup=="1":
        user_name=input("enter your user name : ")
        password1=input("enter your 1st password : ")
        storng_password(password1)
        password2=input("enter your password : ")
        checkpassword(password1,password2)
        mobile_number=int(input("enter the mobile number:-"))
        print("ok nexst")
       
        m=open("user.json","r")
        usname=m.read()
        if user_name in usname:
            print("This account is already exists")
        else:
            description=input("Information about you : ")
            date_of_birth=input("enter your date of birth : ")
            gender=input("enter your gender (m or f) :")
            print("congrats",user_name,"you are Signed up Successfully.")
            
            user={}
            list1=["username","mobile_number","password","description","date_of_birth","gender"]
            list2=[user_name,mobile_number,password1,description,date_of_birth,gender]
            for i in range(len(list1)):
                user.update({list1[i]:list2[i]})


            with open("user.json","r")as p:
                data=json.load(p)
                data.append(user)
                with open("user.json","w")as p:
                    json.dump(data,p,indent=4)
    
    elif login_signup=="2":
        login_name=input("enter the name : ")
        login_password=input("enter the password : ")
        with open("user.json","r")as p:
            data=json.load(p)

            for i in data :

                if i["username"]==login_name:
                    if i["password"]==login_password:
                            print("LOGIN SUCCESSFULLY")
                            break
                    else:
                        print("password is incorrect")
                        break
            else:
                print("invalid account")

