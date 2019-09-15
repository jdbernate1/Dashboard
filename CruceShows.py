import difflib
import pandas as pd
from fuzzywuzzy import fuzz, process

##Funcion para eliminar tildes
def normalizar(s):
    reemplazos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        (" ", "_"),
    )
    for a, b in reemplazos:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s



file = "Archivos prueba/YouTube.xlsx"

# Leer excel
ds= pd.ExcelFile(file)

#Separar hojas
dsVideos=ds.parse('Videos')
Shows=ds.parse('Shows')['Shows']

#Eliminar los null y duplicados de los shows
Shows=Shows[Shows.notnull()].drop_duplicates()


#Series y Dataframe a listas
lista_Shows= Shows.to_list()
videos=dsVideos[['Video Title','Video Description']].values.tolist()


#Convierto en listas los df en listas, me siento más comodo con listas.
#videos es una lista de listas donde el primer elemento es el titulo y el segundo la descripción del video
lista_Shows=[normalizar(x.upper()) for x in lista_Shows]
videos=[[normalizar(str(x).upper()) for x in lista] for lista in videos]


#Usamos la libreria fuzzywuzzy basada en difflib para identificar el show con el mejor ratio de acuerdo a la distancia Levensthein
show_video=[]
for i in videos:
    prueba = process.extract(i[0], lista_Shows, limit=1)
    show_video.append([i[0],prueba[0][0],prueba[0][1]])
    # print(prueba[0][0])

#Imprimimos csv para dashboard
csv= pd.DataFrame(show_video)
csv.to_csv("asociacionShows.csv",index=False)












# def contains_word(s, w):
#     return (' ' + w + ' ') in (' ' + s + ' ')

# print(contains_word('the quick brown fox', 'brown'))  # True
# contains_word('the quick brown fox', 'row') 

# lista_prueba=[]
# for i in videos:
# 	cercarno=difflib.get_close_matches(i[0], lista_Shows)
# 	print(i[0],cercarno)
	
	# for j in lista_Shows:
	# 	if contains_word(i[0],j):
	# 		print(i[0] +"---"+j)


			

