# -*- coding: utf-8
# v0.1.1
# by jtmeros

import sys, os, string, random

caracteres = string.ascii_letters + string.digits + '!@#$%^&*()' # string que incluye letras, números y caracteres especiales
random.seed = (os.urandom(1024))

if len(sys.argv) >= 2:
	longitud = int(sys.argv[1]) # longitud elegida por el usuario

	if len(sys.argv) >= 3:
		if (str(sys.argv[2]) == "-l"):
			caracteres = string.ascii_letters # solo letras

		if (str(sys.argv[2]) == "-n"):
			caracteres = string.digits # solo números

		if (str(sys.argv[2]) == "-nl"):
			caracteres = string.digits + string.ascii_letters # letras y números


else:
	longitud = 10 # longitud por defecto
	

print ''.join(random.choice(caracteres) for i in range(longitud)) # muestra la contraseña