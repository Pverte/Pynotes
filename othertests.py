from selectmenu import SelectMenu


menu = SelectMenu()
menu.add_choices(
    ["Infos", "Voir les notes des élèves", "Ajouter un élève", "Voir les informations d'un élève", "voir une classe"])
result = menu.select("Que souhaitez vous faire ?")
print(result)