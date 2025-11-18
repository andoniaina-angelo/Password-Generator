def generateurmdp():
    password=input("veuillez entrer votre mot de passe : ")
    n=0 
    p=0
    i=0
    c=0
    d=0
    while i<len(password) and c<len(password) and n<len(password) and p<len(password):
        if len(password)<8:
            print("Error:too short")
            password=input("veuillez entrer votre mot de passe : ")
            i=0
            n=0 
            p=0
            c=0
            d=0
        else:
            d+=1
        while i<len(password):
            if password[i].islower():
                i+=1
            elif password[i].isupper():
                print("maj ok")
                d+=1
                break
        while i==len(password):
            if password[-1].isupper():
                print("maj ok")
                break
            else:
                print("Error:manque maj")
                password=input("veuillez entrer votre mot de hbpasse : ")    
                n=0 
                p=0
                i=0
                c=0
                d=0
    
        while c<len(password):
            if password[c].islower():
                print("min ok")
                d+=1
                break
   
            elif password[-1].islower():
                print("min ok")
                break
            elif password[-1].isupper():    
                print("Error:manque min")
                password=input("veuillez entrer votre mot de passe : ")
                n=0 
                p=0
                i=0
                c=0
                d=0
            else:
                c+=1
    
        for n in range(len(password)):
            if password[n].isdigit():
                print("nbr ok")
                d+=1
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
                i=0
                c=0
                d=0
    
        while p<len(password):
            if password[p] in"!@#$%^&*":
                print("chara ok")
                break
            else:
                p+=1
            while p==len(password):
                if password[-1] in "!@#$%^&*":
                    print("chara bonga ! ")
                    d+=1
                    break
                elif password[-1] not in "!@#$%^&*":
                    print("Error: manque chara")
                    password=input("veuillez entrer votre mot de passe : ")
                    p=0 
                    i=0
                    c=0
                    n=0
                    d=0
        if d==4:
            break
generateurmdp()
        

   

