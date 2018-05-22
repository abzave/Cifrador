#Creado por: Abraham Meza Vega
#Fecha de creación: 9/4/18 7:30 p.m.
#Última módificación: 9/4/18 8:15 p.m.

#Importaciones
import smtplib
import imaplib
import email
from cifrado_binario import *
from cifrado_cesar import *
from cifrado_inversa import *
from cifrado_telefonico import *
from validaciones import *

"""
Entradas: mensaje de tipo string
Salidas: Correo descifrado o en caso de requerir más datos código del cifrado
Funcionamineto: Verifica la llave que se encuentra en el correo y determina el
algoritmo usado, si se requieren datos adicionales se devuelve el código del
algoritmo.
"""
def analizarCorreo(mensaje):
    if mensaje[-3] == "1":
        return validarGenericamente(mensaje[:-5], descifrarCesar)
    elif mensaje[-3] == "2":
        return 2
    elif mensaje[-3] == "3":
        return 3
    elif mensaje[-3] == "4":
        return separarFraseInv(mensaje[:-5])
    elif mensaje[-3] == "5":
        return cifrarInversa(mensaje[:-5])
    elif mensaje[-3] == "6":
        return validarTelefonico(mensaje[:-5])
    elif mensaje[-3] == "7":
        return validarBinario(mensaje[:-5])
    elif mensaje[-3] == "8":
        return 8
    else:
        return "El último correo no es un mensaje cifrado"

"""
Entradas: Correo y contraseña de tipo string
Salidas: Último correo recibido/mensaje de error
Funcionamiento: Busca en la bandeja de entrada el último correo proveniente del
usuario y lo devuelve
"""
def recuperarCorreo(correo, contrasenna):
    try:
        servidor = imaplib.IMAP4_SSL("imap.gmail.com")
        servidor.login(correo, contrasenna)
        servidor.select()
        estatus, mensaje = servidor.search(None, "FROM", correo)
        ultimoCorreo = mensaje[0].split()[-1]
        estatus, mensaje = servidor.fetch(ultimoCorreo, "(RFC822)")
        correoSinProcesar = mensaje[0][1].decode("utf-8")
        correoProcesado = email.message_from_string(correoSinProcesar)
        mensaje = correoProcesado.get_payload(decode = True)
        servidor.close()
        return mensaje.decode("utf-8")
    except imaplib.IMAP4.abort:
        return "Error del servidor"
    except imaplib.IMAP4.readonly:
        return "Error: El correo es de solo lectura"
    except imaplib.socket.gaierror:
        return "Error: No hay conexion a internet"
    except imaplib.socket.timeout:
        return "Error: Se ha excedido el tiempo de espera"
    except Exception as err:
        return "Error: " + str(err)

"""
Entradas: mensaje, contraseña y correo de tipo string y cifrado de tipo entero
Salidas: Mensaje de confirmación/error del envio del correo
Funcionamiento: Envia un correo a la dirección dada con el mensaje dado
"""
def enviarCorreo(correo, contrasenna, mensaje, cifrado):
    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.ehlo()
        servidor.login(correo, contrasenna)
        servidor.sendmail(correo, correo, mensaje + "\n" + str(cifrado))
        servidor.quit()
        return "¡Correo enviado con exito!"
    except smtplib.SMTPServerDisconnected:
        return "Error: Se perdio la conexión con el servidor"
    except smtplib.SMTPResponseException:
        return "Error del servidor"
    except smtplib.SMTPSenderRefused:
        return "Error: Se ha rechazado al remitente"
    except smtplib.SMTPRecipientsRefused:
        return "Error: Se rechazado el destinatario"
    except smtplib.SMTPDataError:
        return "Error: El servidor ha rechazado el mensaje"
    except smtplib.SMTPConnectError:
        return "Error: Al conectar con el servidor"
    except smtplib.SMTPHeloError:
        return "Error: Se rechazado el saludo al servidor"
    except smtplib.SMTPNotSupportedError:
        return "Error: La operación no es soportada por el servidor"
    except smtplib.SMTPAuthenticationError:
        return "Error: Usuario/contraseña erroneos"
    except smtplib.socket.error:
        return "Error: No hay conexión a internet"
    except smtplib.socket.timeout:
        return "Error: Se ha excedido el tiempo de espera"
    except Exception as err:
        return "Error: " + str(err)

"""
Entradas: correo de tipo string
Salidas: True si el correo es valido o un mensaje de error en caso contrario
Funcionamiento: Comprueba que el correo dado sea de tipo texto y que tenga los
caracteres mínimos en la estructura de un correo valido (@, .)
"""
def validarCorreo(correo):
    if not isinstance(correo, str):
        return "Error: Debe ingresar el correo como texto"
    if not("@" in correo and "." in correo):
        return "Error: El correo debe contener al menos un @ y un ."
    else:
        return True
