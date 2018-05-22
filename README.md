# Cifrador

Funcionalidades implementadas:

El software contiene las funcionalidades de: Enviar los mensajes cifrados por medio de correos electrónicos, rescatar el último correo eléctrico que tenga como remitente sí mismo, analizar el correo electrónico recuperado con el fin de verificar si es un mensaje cifrado y de serlo saber cuál método se usó, cifrar y descifrar texto en código Cesar, por llave, sustitución Vigenére, RSA, Palabra Inversa, Mensaje Inverso, Telefónico y Binario.

Explicación paso a paso:

1- Ingrese su correo y contraseña en el momento que el programa se lo pida. Para que la contraseña sea invisible el programa se deberá ejecutar en el símbolo del sistema. El ejecutarlo en el Shell de Python no garantiza que su contraseña vaya a estar protegida.

2- Si desea cifrar ingrese 1.
2. a- Escoja mediante números del 1 al 8 qué tipo de cifrado quiere utilizar, en caso de querer volver al menú principal ingrese 9.
 
2. b-  Para utilizar el cifrado Cesar ingrese la opción 1 y luego ingrese el texto a cifrar, posteriormente se le enviará el mensaje cifrado a la dirección de correo electrónico que ingresó al inicio.
 
2. c- Para utilizar el cifrado por llave ingrese la opción 2, ingrese el texto a cifrar, el programa le solicitará la llave del cifrado puede escoger cualquiera mientras sea solo texto, posteriormente se le enviará el mensaje cifrado a la dirección de correo electrónico que ingresó al inicio.
 
2. d- Para utilizar el cifrado de sustitución vigenére ingrese la opción 3, ingrese el texto a cifrar, el programa le solicitará una cifra de 2 dígitos puede escoger cualquiera mientras sea una cifra de 2 dígitos, posteriormente se le enviará el mensaje cifrado a la dirección de correo electrónico que ingresó al inicio.
 
2. e- Para utilizar el cifrado RSA ingrese la opción 4 y luego ingrese el texto a cifrar.
 
2. e. a- Si tiene la clave de encriptación ingrese 1, se le pedirá el valor de e
y luego el de n, posteriormente se le enviará el mensaje cifrado a la dirección de correo electrónico que ingresó al inicio.
 
2. e. b- Si no tiene clave de encriptación ingrese 2, el programa le generará las claves correspondientes, se las imprimirá en pantalla para que tome nota de ellas y posteriormente se le enviará el mensaje cifrado a la dirección de correo electrónico que ingresó al inicio.
 
2. f- Para utilizar el cifrado de palabra inversa ingrese la opción 5 y luego ingrese el texto a cifrar, posteriormente se le enviará el mensaje cifrado a la dirección de correo electrónico que ingresó al inicio.
 
2. f- Para utilizar el cifrado de mensaje inverso ingrese la opción 6 y luego ingrese el texto a cifrar, posteriormente se le enviará el mensaje cifrado a la dirección de correo electrónico que ingresó al inicio.

2. f- Para utilizar el cifrado telefónico ingrese la opción 7 y luego ingrese el texto a cifrar, posteriormente se le enviará el mensaje cifrado a la dirección de correo electrónico que ingresó al inicio.
 
2. f- Para utilizar el cifrado binario ingrese la opción 8 y luego ingrese el texto a cifrar, posteriormente se le enviará el mensaje cifrado a la dirección de correo electrónico que ingresó al inicio.
 
3- Si desea descifrar ingrese 2
 
3. a- Si el último correo estaba cifrado con cifrado por llave deberá ingresar la llave que utilizó para cifrarlo y posteriormente se le imprimirá en pantalla el mensaje.
 
3. b- Si el último correo estaba cifrado con sustitución vigenére deberá ingresar la cifra que utilizó para cifrarlo y posteriormente se le imprimirá en pantalla el mensaje.
 
3. c- Si el último correo estaba cifrado con cifrado RSA deberá ingresar la clave privada “n” y la clave privada “d” que utilizó para cifrarlo y posteriormente se le imprimirá en pantalla el mensaje.
 
3. d- Para los demás casos el mensaje se descifrará automáticamente y el imprimirá el mensaje en pantalla.
 
4- Si desea salir presione 3
