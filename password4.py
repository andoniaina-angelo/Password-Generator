def mdp():
    import hashlib
    password=input("entrez votre mot de passe: ")
    if set(password) & set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  and set(password) & set("abcefghijklmnopqrstuvwxyz") and set(password) & set("!@#$%^&*") and set(password) & set("0123456789") and len(password)>=8:
        print("mot de passe valide")
        password= hashlib.sha256(password.encode("utf-8")).hexdigest()

    else:
        print("erreur: mot de passe insuffisant")
        mdp()
    print(password) 

mdp()
