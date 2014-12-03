#coding: utf-8
#librerias que inportamos
import smtplib, getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#d = a los datos que ingresemos los guardara hai 
d = {}
#parte de los def donde se realiza opoeraciones 
def pais():
	respuesta = 0
	while (respuesta==0):	
		while True:
			e = raw_input("Ingrese País: ")
			f = raw_input("Ingrese la capital del país: ")
			if e.isalpha() and f.isalpha():
				break
			else:
				print "Solo puedes ingresar letras, intenta nuevamente."
		d[e] = f	
		print d
		a =	raw_input  ("Desea agregar otro pais? si/no ")
		b = a.lower()
		if b == "si":
			respuesta = 0
		elif b == "no":
			break
			respuesta = 1
		else:
			print "Debe ingresar una opción valida"

def paises():
	print "Aca esta la lista de paises que ingreso: "
	for i in d:
		print i
		print "*" * 5

def capitales():
	print "Aca estan las capitales de los paises que ingreso: "
	for i in d:
		print d[i]
		print "*" * 5

def ordenar():
	print "\n Aca estan los paises ordenados alfabeticamente:"
	l = d.items()
	l.sort()
	for i in l:
		print " ".join(i)

def todo():
	print "El listado completo de los paises y capitales que agrego: "
	print d
	print "*" * 5

class TodoMail(object): 
	

	def envioCorreo (self):
			user = raw_input("Cuenta de gmail: ")		
			password = getpass.getpass("Password: ")
			remitente = raw_input("From, ejemplo: administrador <admin@gmail.com>: ")
			de = raw_input("To, ejemplo: amigo <amigo@gmail.com>: " )
			asunto = raw_input("Subject, Asunto del mensaje: ")
			mensaje = d
			self.user = user
			self.password = password
			self.remitente = remitente
			self.de = de 
			self.asunto = asunto 
			self.mensaje = mensaje 
			#Host y puerto SMTP de Gmail
			gmail = smtplib.SMTP('smtp.gmail.com', 587 )

			#protocolo de cifrado de datos utilizado por gmial
			gmail.starttls()

			#Credenciales
			gmail.login(user,password)

			#muestra la depuracion de la operacion de envio 1=true
			gmail.set_debuglevel(1)

			header = MIMEMultipart()
			header['Subjecto'] = asunto
			header['From'] = remitente
			header['To'] = de

			mensaje = MIMEText (mensaje,'plain')
			header.attach(mensaje)


			#Enviar email
			gmail.sendmail(remitente, de, header.as_string())

			#Cerrar la conexion SMTP
			gmail.quit()


#parte donde se opera el menu
respuesta = 0
while (respuesta==0):
	try:
		opcion = raw_input("1 ingreso de pais\n2 Ver la lista de Paises\n3 ver la lista de Capitales\n4 Ver todo \n5 ver todo ordenado \n6 TodoMail \n> ")
	except(NameError, ValueError, SyntaxError):
		print "Intenta colocar una de las opciones que estan en el menu"
	if opcion == "6": #dirige hacia funcion1()
		start = TodoMail()
		start.envioCorreo()
		respuesta = 0
	elif opcion == "2":
		paises()
		respuesta == 0
	elif opcion == "3":
		capitales()
		respuesta == 0
	elif opcion == "4":
		todo()
		respuesta == 0
	elif opcion == "5":
		ordenar()
		respuesta == 0
	elif opcion == "1":
		pais()
		respuesta == 0
	elif opcion == "7":
		print "Gracias por utilizar nuestro servicio, que tenga un buen dia"
		respuesta = 1		
	else:
		print "Ingrese algo valido"



