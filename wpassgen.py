# -*- coding: utf-8
# v0.1.5
# by jtmeros

import sys, os, string, random

caracteres = string.ascii_letters + string.digits + '!@#$%&*-' # string que incluye letras, números y caracteres especiales
random.seed = (os.urandom(1024))


if len(sys.argv) >= 2:

	numargv = 1 # primer argv como el opcional


	try: # si no se introduce un número en el segundo argumento
		longitud = int(sys.argv[1]) # longitud elegida por el usuario
		if len(sys.argv) >= 3:
			numargv = 2 # el argv segundo es el opcional
	except:
		longitud = 10 # longitud por defecto


	if (str(sys.argv[numargv]) == "-l"):
		caracteres = string.ascii_letters # solo letras

	if (str(sys.argv[numargv]) == "-ll"):
		caracteres = string.ascii_lowercase #solo letras minúsculas

	if (str(sys.argv[numargv]) == "-lL"):
		caracteres = string.ascii_uppercase #solo letras mayúsculas

	if (str(sys.argv[numargv]) == "-n"):
		caracteres = string.digits # solo números

	if (str(sys.argv[numargv]) == "-s"):
		caracteres = '!@#$%&*-' # solo símbolos

	if (str(sys.argv[numargv]) == "-p"):
		caracteres = string.punctuation # solo signos puntuación

	if (str(sys.argv[numargv]) == "-h"):
		caracteres = string.hexdigits # hexadecimal

	if (str(sys.argv[numargv]) == "-nl"):
		caracteres = string.digits + string.ascii_letters # letras y números

	if (str(sys.argv[numargv]) == "-ns"):
		caracteres = string.digits + '!@#$%&*-' # números y símbolos

	if (str(sys.argv[numargv]) == "-ls"):
		caracteres = string.ascii_letters + '!@#$%&*-' # letras y símbolos

else:
	longitud = 10 # longitud por defecto


print ''.join(random.choice(caracteres) for i in range(longitud)) # muestra la contraseña
