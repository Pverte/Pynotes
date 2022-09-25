import getpass

user = getpass.getpass("Entrez votre Identifiant")

if user == 'admin':
    password = getpass.getpass(
        "Bienvenue maître, entrez votre mot de passe pour être sûr que c'est vous"
    )
else:
    print("INCORRECT")
