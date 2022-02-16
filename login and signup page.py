


import json

print("***","WELCOME TO LOGIN SIGN UP PAGE","***")

login_signup=input("you wants to login(2) or signup(1):-")



if login_signup=="1":
    user_name=input("enter the user name:-")
    password=input("enter the password:-")
    password2=input("enter your confirm password:-")
    if password==password2:
        print("your password is confirmed")
        birth_of_date=input("enter the birth of date:-")
        mobile_number=int(input("enter the number:-"))
        gender=input("enter the gender M/F:-")

        print("congrats",user_name,"you are Signed up Successfully.")
        a=open("user.json","r")
        r=a.read()
        data = json.loads(r)
        user={}
        list1=["user_name","password","birth_of_date","mobile_number","gender"]
        list2=[user_name,password,birth_of_date,mobile_number,gender]
        for i in range(len(list1)):
            user.update({list1[i]:list2[i]})
        data.append(user)
    
        with open("user.json","w") as f:
            b=json.dump(data,f,indent=4)
        
    else:
        print("wrong password")
else:
    if login_signup=="2":
        password=input("enter the user name:-")
        password2=input("enter the password:-")
        with open("user.json","r") as f:
            b=json.load(f)
            print("login succesfully")
    else:
        print("wrong details")
