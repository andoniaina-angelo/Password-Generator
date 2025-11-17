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
            password=input("veuillez entrer votre mot de passe : ")    

c=0
while c<len(password):
    if password[c].islower():
        print("contient min")
        break
   
    elif password[-1].islower():
        print("la dernière est minuscule")
        break
    elif password[-1].isupper():    
        print("Error:manque min")
        password=input("veuillez entrer votre mot de passe : ")
        c=0
    else:
        c+=1

        
        

   

