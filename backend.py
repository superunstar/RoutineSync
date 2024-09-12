from db_function import *

user = input("Entrez votre nom : ")

userdb = read_data(user)
if userdb is not None:
    print("Content de vous revoir", user)
else:
    insert_data(user)
    print("Bienvenue", user)
