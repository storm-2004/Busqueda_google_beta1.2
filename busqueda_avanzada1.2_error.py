"""
Este es una mejora del codigo anterior version 1.1
"""
# Palabras claves listas 

#word_list = ["tienda + colegio + problema"]
"""
class busqueda():
	def __init__(self, word, url):
		self.url = url
		self.word = []

	def url():
		self.url = input("dijite la url del buscador a utilizar: ")

"""

from googlesearch import search

print("dijite una lista de palabras claves a buscar en google.")
cont = int(input("dijite la cantidad de palabras claves a dijitar: "))

palabras = []
i = 0
while i < cont:

	frase = input("palabra: ")
	palabras.append(frase)

	i=i+1

print("palbras claves dijitadas  ")
for j in palabras:
	print(j)

""" Parametros que se usan para ajilizar la busqueda mas exhautiva
tld = "com" #Esta bandera es el dominio
lang = "en" #Esta bandera es el lenguaje español
num = 200 #Esta bandera es el umero de links a mostrar
start = 20 #Salta los primeros 10 o 100 resultados
stop = num #Para si el valor es false la busqueda es infinita
pause = 2.0 #TIEMPO DE ESPERA DE 2.0 SEGUNDOS PARA BUSQUEDAS ESTO SI ESTA MUY LARGO GOOGLE NOS BANEA POR LA IP
"""
tld = input("dijte la")
