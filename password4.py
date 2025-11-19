def mdp():
    password=input("entrez votre mot de passe: ")
    if set(password) & set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  and set(password) & set("abcefghijklmnopqrstuvwxyz") and set(password) & set("!@#$%^&*") and set(password) & set("0123456789") and len(password)>=8:
        print("mot de passe valide")
    else:
        print("erreur: mot de passe insuffisant")
        mdp()
mdp()

         
