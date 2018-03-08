loop = 'yes'
while loop =='yes':
	resultado=0
	numero1 = float(input('Ingresa un numero: \n'))
	numero2 = float(input('Ingresa un numero: \n'))
	opcion = int(input("""Eligue la opcion que deceas
		1.-Sumar
		2.-Restar
		3.-Multiplicar
		4.-Dividir
		5.-Modulo
		"""))
	if opcion==1:
		resultado = numero1+numero2
	elif opcion ==2:
		resultado=numero1 - numero2
	elif opcion == 3:
		resultado=numero1 * numero2
	elif opcion == 4:
		resultado = numero1/numero2
	elif opcion == 5 :
		resultado = numero2 % numero2
	else :
		print("Eligue una opcion valida")

	print('El reslutado es {}'.format( resultado))
	loop='false'