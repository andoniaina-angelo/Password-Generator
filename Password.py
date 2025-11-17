password=input("veuillez entrer votre mot de passe : ")
i=0
while i<len(password):
    if len(password)<8:
        print("Error:too short")
        password=input("veuillez entrer votre mot de passe : ")
        i=0
    elif password[i].islower():
        i+=1
    elif password[i].isupper():
        print("maj ok")
        break
    while i==len(password):
        if password[-1].isupper():
            print("maj ok")
            break
        else:
            print("Error:manque maj")
            i=0
            password=input("veuillez entrer votre mot de hbpasse : ")    

c=0
while c<len(password):
    if password[c].islower():
        print("min ok")
        break
   
    elif password[-1].islower():
        print("min ok")
        break
    elif password[-1].isupper():    
        print("Error:manque min")
        password=input("veuillez entrer votre mot de passe : ")
        c=0
    else:
        c+=1
n=0
for n in range(len(password)):
    if password[n].isdigit():
        print("nbr ok")
        break
    else:
        n+=1
    while n==len(password):
        if password[-1].isdigit():
            print("nbr ok")
            break
        else:
            print("Error:manque nbr")
            password=input("veuillez entrer votre mot de passe : ")
            n=0 
p=0
while p<len(password):
    if password[p] in"!@#$%^&*":
        print("chara ok")
        break
    else:
        p+=1
    while p==len(password):
        if password[-1] in "!@#$%^&*":
            print("chara bonga ! ")
            break
        elif password[-1] not in "!@#$%^&*":
            print("Error: manque chara")
            password=input("veuillez entrer votre mot de passe : ")
            p=0 
        

   

