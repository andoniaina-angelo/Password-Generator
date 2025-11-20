
import hashlib
import json
import os
def mdp():
    password=input("entrez votre mot de passe: ")
    if set(password) & set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  and set(password) & set("abcefghijklmnopqrstuvwxyz") and set(password) & set("!@#$%^&*") and set(password) & set("0123456789") and len(password)>=8:
        print("mot de passe valide")
        password= [hashlib.sha256(password.encode("utf-8")).hexdigest()]
        
        if os.path.exists("datapassword.json") and os.path.getsize("datapassword.json") > 0:
           with open("datapassword.json",'r') as f:
               datapassword=json.load(f)
        else:
            datapassword
        nouveau_mdp=password    
        if nouveau_mdp:
            datapassword.append(nouveau_mdp)
        with open("datapassword.json",'w') as f:
            json.dump(datapassword,f,ensure_ascii=False)
            
    else:
        print("erreur: mot de passe insuffisant")
        mdp()
    print(password)
mdp()