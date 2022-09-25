"""
 project for school,
% = Pverte
£ = Luna
$=terminé
Project :
- Make an "school software" to get informations about students
CDC:
1-annees en trimestres$
02/09 - 26/11
27/11 - 04/03
05/03 - 10/06
2-pouvoir ajouter le nom d'un élève$

3-pouvoir obtenir les données sur l'élève en recherchant son nom$
4-pouvoir avoir accès aux moyennes EN PLUS DES NOTES$
5-calcul de la moyenne d'un devoir£
6-calcul de la moyenne annuelle de classe$
7-affichage liste resultats triés selon moy generale$
8-affichage liste eleve par moy décroissante$
9-une autre fonctionnalité au choix$
Fonctionnalitées créées : 8/9
---------------------------------------
"""
import json
import time
from selectmenu import SelectMenu
from prettytable import PrettyTable
from prettytable import DOUBLE_BORDER
"""On importe les bibliothèques nécessaires :
json pour lire le fichier comportant les données
time pour les temps d'attente pour rendre plus dynamique 
selectmenu pour les menus
prettytable pour les tableaux"""

f = open('school.json', "r+", encoding="utf8")
data = json.load(f)
#On ouvre le fichier en json et on le "convertis" pour que le code python y ai accès
f.close() # On oublie pas de fermer le fichier à la fin

def trimestre(date): #fonction pour identifier les trimestres
  date=list(map(int, date.split("/")))
  if date[1]==9:
    while date[0]<2 or date>30:
      print("entrez une date valide svp")
      date=str(input("entrez une date valide svp"))
      date=date.split("/")
      date[0], date[1]=int
    #trimestre1
  if date[1]==10:
    while date[0]<1 or date[0]>31:
      print("entrez une date valide svp")
      date=str(input("entrez une date valide svp"))
      date=date.split("/")
      date=int
    #trimestre1
  if date[1]==11:
    while date[0]<1 or date[0]>26:
      print("entrez une date valide svp")
      date=str(input("entrez une date valide svp"))
      date=date.split("/")
      date=int
    #trimestre1
  if date[1]==11:
    while date[0]<27 or date[0]>30:
      print("entrez une date valide svp")
      date=str(input("entrez une date valide svp"))
      date=date.split("/")
      date=int
    #trimestre2
  if date[1]==12:
    while date[0]<1 or date[0]>31:
      print("entrez une date valide svp")
      date=str(input("entrez une date valide svp"))
      date=date.split("/")
      date=int
    #trimestre2
  if date[1]==1:
    while date[0]<1 or date[0]>31:
      print("entrez une date valide svp")
      date=str(input("entrez une date valide svp"))
      date=date.split("/")
      date=int
    #trimestre2
  if date[1]==2:
    while date[0]<1 or date[0]>29:
      print("entrez une date valide svp")
      date=str(input("entrez une date valide svp"))
      date=date.split("/")
      date=int
    #trimestre2
  if date[1]==3:
    while date[0]<1 or date[0]>4:
      print("entrez une date valide svp")
      date=str(input("entrez une date valide svp"))
      date=date.split("/")
      date=int
    #trimestre2  
  if date[1]==3:
    while date[0]<5 or date[0]>31:
      print("entrez une date valide svp")
      date=str(input("entrez une date valide svp"))
      date=date.split("/")
      date=int
    #trimestre3  
  if date[1]==4:
    while date[0]<1 or date[0]>30:
      print("entrez une date valide svp")
      date=str(input("entrez une date valide svp"))
      date=date.split("/")
      date=int
    #trimestre3  
  if date[1]==5:
    while date[0]<1 or date[0]>31:
      print("entrez une date valide svp")
      date=str(input("entrez une date valide svp"))
      date=date.split("/")
      date=int
    #trimestre3  
  if date[1]==6:
    while date[0]<1 or date[0]>10:
      print("entrez une date valide svp")
      date=str(input("entrez une date valide svp"))
      date=date.split("/")
      date=int
    #trimestre3
  print(date)
#trimestre("10/02")






def add_student():
  """Fonction permettant d'ajouter un élève dans une classe
  Le programme demande le nom, le prénom, les options si elles sont disponibles (dire True si il en as) et crée ensuite l'entrée dans le fichier school.json"""
  classe=str(input("Entrez la classe de l'élève (sous la forme '1A')"))
  if classe not in list(data["classes"].keys()):
      print("Cette classe n'existe pas")
      print("retour au menu")
      principMenu()
  numb = data["classes"][classe]["number"]
  num = str(int(numb)+1)
  nom=input("Entrez le nom de l'élève")
  prenom=input("Entrez le prénom de l'élève")
  spe1=input("Entrez la spé 1 de l'élève")
  spe2=input("Entrez la spé 2 de l'élève")
  spe3=input("Entrez la spé 3 de l'élève")
  option=input("Options ?")
  if option == True:
    options=input("Entrez les options séparées par une ,")
    options=options.split(",")
    options=[True, options]
    print(options)
  else:
    options=False
    # Ajoute l'entrée dans le dictionnaire data
  data["classes"][classe]["students"][num]={
	"ID":num,
	"nom":nom, 
	"prenom":prenom, 
	"matiere":{
		"spes":{
			spe1:{"DS1":[0,0]}, 
			spe2:{"DS1":[0,0]}, 
			spe3:{"DS1":[0,0]}
			},
		"options":{
			options:{"DS1":[0,0]}
			}
		}
}
  data["classes"][classe]["number"]+=1
  
  print(data)
  # Écrit dans le fichier le dictionnaire data modifié
  with open("school.json", "w") as f:
    json.dump(data, f)
  print("DUmp effectué")

#add_student()
          




def moyeleve(classe,eleve):
  names=[i for i in data["classes"][classe]["students"][eleve]["matiere"]["spes"].keys()] #Mettres tout les noms de spécialitées dans une liste
  names2=[i for i in data["classes"][classe]["students"][eleve]["matiere"]["options"].keys()] #Mettres tout les noms de options dans une liste
  names=names+names2 #On ajoute dans une liste tout ces noms
  #print(names)
  spee=0 # nombre de matières pour permettre la division de la moyenne générale
  moyge={}
  for matiere in data["classes"][classe]["students"][eleve]["matiere"].values():
    #pour chaques matières (spécialitées et options)
    n=0
    L=[]
    S=0
    for spe in matiere.values():
      #Entrée une par une des matières (d'abord les spécialités puis les options, grâce à la boucle du dessus)
      n=0
      L=[]
      S=0
      for eval in spe:
        #Pour chaques évaluations dans une matière :
        n=spe[str(eval)][0] # On prends la note
        coef=spe[str(eval)][1] #On prends le coeff
        if coef < 1: #Si le coef est plus petit que 1 :
          """Comme une évaluation avec un coefficient inférieur à 1 est petit, on le multiplie pour qu'il devienne ainsi une note coefficient 1"""
          n=spe[str(eval)][0]*spe[str(eval)][1]
          L.append(n)
          #print(n)
        else:
          """Et si c'est plus grand que 1, alors on rajoute plusieurs fois la note (2 fois si c'est coefficient 2, comme elle est 2 fois plus importante"""
          for i in range(spe[str(eval)][1]):
            
            L.append(n) # On ajoute dans la liste 
        #print(L)
        #print(len(L))
      for i in range(0,len(L)):
        #On fait la somme de chaques notes
          S=S+L[i]
         # print("S:     " + str(S))
      moyspe={names[spee]:S/len(L)}
      #Et ici on indique la moyenne par spécialitée
      moyge.update(moyspe)
      spee=spee+1
      #print(moyge)
  S=0
  i=0
  for keys in moyge:
    S=S+moyge[keys]
    i=i+1
  moygene=S/len(moyge)
  #Enfin ici on calcule la moyenne générale par rapport aux moyennes de chaques spécialiées
  return int(moygene)# ET on retourne ici la moyenne générale en integer, pour plus de lisibilitée




def infosclass(classes=''):
  """Donne la liste des élèves"""
  if classes== '': #Si il n'y a pas d'arguments, alors le demander
    classes=input("Entre le code d'une classe (sous la forme 1A)")
  
  tri="N°" #On installe la variable tri, qui est le tri par défaut
  reverse=False #On installe la variable reverse, qui par défaut est False
  while True: 
    classe=data["classes"][classes] #Pour simplifier, on mets le dictionnaire de la classe dans la variable classe
    x = PrettyTable() #Définition de la variable x commme un tableau
    x.set_style(DOUBLE_BORDER) #Modifie le style du tableau
    x.field_names = ["N°", "Nom", "Prénom", "Classe", "Spécialitées", "Options", "Moy Gé"] #Mets en place la première ligne 
    for i in range(classe["number"]): #Pour chaques élèves dans la classe, rajouter une ligne avec le numéro de l'élève, son nom, son prénom, sa classe, les spécialitées, les options, et la moyenne générale
      stud=classe["students"][str(i+1)]
      x.add_row([i+1, stud["nom"], stud["prenom"], classe["name"], list(stud["matiere"]["spes"].keys()), list(stud["matiere"]["options"].keys()), moyeleve(classe["name"], str(i+1))])
    print(x.get_string(sortby=tri, reversesort=reverse)) #Imprime le tableau, avec le tri spécifique
    menu = SelectMenu() #Défini la variable menu comme un menu 
    menu.add_choices(
    ["Trier par défaut", "Trier par Moyenne générale - croissant", "Trier par Moyenne générale - décroissant", "Quitter", "Ajouter un élève"]) #Ajoute les options du menu
    result = menu.select("Que souhaitez vous faire ?")
    #Ici, par rapport au résultat, le tableau sera réaffiché avec une autre méthode de tri différente
    if result == "Trier par défaut":
      tri="N°"
      reverse=False
    elif result == "Trier par Moyenne générale - croissant":
      tri="Moy Gé"
      reverse=False
    elif result == "Trier par Moyenne générale - décroissant":
      tri="Moy Gé"
      reverse=True
    elif result == "Quitter":
      principMenu()
    elif result == "Ajouter un élève":
      add_student()
  
#infosclass()


def searchstudent(name=""):
  students=[]
  x="Not Found"
  if name=="":
    name=input("Entrez le nom de l'élève")
  for keys in data["classes"]:
    i=1
    for j in range(data["classes"][keys]["number"]):
      students.append(data["classes"][keys]["students"][str(i)])
      i+=1
  for i in students:
    if i["nom"] == name:
      x = PrettyTable()
      x.set_style(DOUBLE_BORDER)
      x.field_names = ["Nom", "Prénom", "Classe", "Spécialitées", "Options", "Moy Gé"]
      stud=i
      x.add_row([stud["nom"], stud["prenom"], keys, list(stud["matiere"]["spes"].keys()), list(stud["matiere"]["options"].keys()), moyeleve("1A", str(stud["ID"]))])
  print(x)
  principMenu()

#searchstudent("FORTANER")

#FONCTION MOYENNE D'UNE CLASSE NON IMPLANTÉE DANS LE CODE AVEC INTERFACE      
def moyclass(ID=None):
  if ID == None:
    ID = input("Entrez une classe")
  moy=0
  for i in range(1, data["classes"][ID]["number"]+1):
    print(i)
    moy=moyeleve(ID, str(i))+moy
  return moy/data["classes"][ID]["number"]

#print(moyclass("1A"))

def start(): #Fonction de départ pour accueillir les utilisateurs
  print("Bienvenue sur Pynotes ! Le logiciel en pythonthon pour mettre des notes")
  time.sleep(0.5)
  print("Codé par Pverte et Luna Fortaner ©")
  principMenu()

def infos(): #petite fonction pour expliquer ce qu'est le code et comment l'utiliser
  print("Pynotes est un code en python créé pour un projet en classe de NSI, pour l'utiliser, il suffit de choisir les options, avec les flèches, ou entrer ce que le logiciel demande")
  principMenu()

def principMenu(): #Menu principal, pour choisir quoi faire
  menu = SelectMenu()
  menu.add_choices(
    ["Infos", "Voir les informations d'un élève", "voir une classe"])
  result = menu.select("Que souhaitez vous faire ?")
  if result == "Infos":
    infos()
  elif result =="Voir les informations d'un élève":
    searchstudent()
  elif result =="voir une classe":
    infosclass()

start() #invocation de la fonction de démarrage
