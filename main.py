from nltk.stem import PorterStemmer, SnowballStemmer    #stemmer de Porter et snowball
from stemmer_fr import STEMMING                 #stemmer conçu par mes soins
from tokenizer import TOKENIZE      #tokenizer de Zak

text = """C'est l'endroit, asseyez-vous, vous êtes en sécurité maintenant.
Vous avez été coincé dans un ascenseur, nous avons essayé de vous joindre, Thom.
C'est l'endroit, ça ne fera plus jamais mal l'odeur de la climatisation.
Les poissons sont sur le ventre.
Videz toutes vos poches.
Parce qu'il est temps de rentrer à la maison.
C'est l'endroit.
Souviens-toi de moi.
Je suis le visage que tu vois toujours.
Vous avez été coincé dans un ascenseur.
Dans le ventre d'une baleine, au fond de l'océan.
L'odeur de la climatisation.
Les poissons sont sur le ventre.
Videz toutes vos poches parce qu'il est temps de rentrer à la maison/
L'odeur de la climatisation
Les poissons sont sur le ventre.
Aujourd'hui est le premier jour du reste de tes jours."""


test = TOKENIZE(text)
res, res2, res3 = test.show_sentences()

resp = res3
resiris = res3
ressnow = res3
iris = STEMMING(resiris)
print("STEMMER IRIS", ressnow)

snow = SnowballStemmer("french")
ps = PorterStemmer()

snowball = []
porter = []

for word in ressnow:
    snowball.append(snow.stem(word))
    porter.append(ps.stem(word))


print("STEMMER SNOWBALL: ", snowball, "\nSTEMMER PORTER: ", porter)


