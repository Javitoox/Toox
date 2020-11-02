import urllib.request
import ssl
from colorama import Fore
import argparse

print(Fore.BLUE+" ▄▄ •              ▄▄ • ▄▄▌  ▄▄▄ .     ▄▄▄·  ▐ ▄  ▄▄▄· ▄▄▌   ▄· ▄▌▄▄▄▄▄▪   ▄▄· .▄▄ · ")
print(Fore.BLUE+"▐█ ▀ ▪▪     ▪     ▐█ ▀ ▪██•  ▀▄.▀·    ▐█ ▀█ •█▌▐█▐█ ▀█ ██•  ▐█▪██▌•██  ██ ▐█ ▌▪▐█ ▀. ")
print(Fore.BLUE+"▄█ ▀█▄ ▄█▀▄  ▄█▀▄ ▄█ ▀█▄██▪  ▐▀▀▪▄    ▄█▀▀█ ▐█▐▐▌▄█▀▀█ ██▪  ▐█▌▐█▪ ▐█.▪▐█·██ ▄▄▄▀▀▀█▄")
print(Fore.BLUE+"▐█▄▪▐█▐█▌.▐▌▐█▌.▐▌▐█▄▪▐█▐█▌▐▌▐█▄▄▌    ▐█ ▪▐▌██▐█▌▐█ ▪▐▌▐█▌▐▌ ▐█▀·. ▐█▌·▐█▌▐███▌▐█▄▪▐█")
print(Fore.BLUE+"·▀▀▀▀  ▀█▄▀▪ ▀█▄▀▪·▀▀▀▀ .▀▀▀  ▀▀▀      ▀  ▀ ▀▀ █▪ ▀  ▀ .▀▀▀   ▀ •  ▀▀▀ ▀▀▀·▀▀▀  ▀▀▀▀ ")
print("                                   ")
print(Fore.BLUE+"                                                                               ")
print(Fore.RESET)

# Apertura de ficheros necesarios
rutaClave="google-analytics"
f = open("url.txt", "r")
g = open("GA.txt", "w")

# Procesado de argumentos
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--timeout", help = "Maximum seconds to wait for a response from the server, by default 1")
parser.add_argument("-r", "--retry", help = "Generation file 'retry.txt' where the urls that cannot be accessed will be collected", action="store_true")
args = parser.parse_args()

# Procesado de timeout
segundos = 1
if args.timeout:
    try: 
        segundos = int(args.timeout)
    except:
        print("Timeout must be a number greater than 0")
        exit()

# Procesado de retry.txt
if args.retry:
    retry = open("retry.txt", "w")

print("If the color is red, that website has Google Analytics but there are not cookies:\n")

# Funcionalidad principal del programa
for linea in f:
    try:
        if(str(linea[0:4]) != "http"):
            linea="http://"+str(linea)
        context = ssl._create_unverified_context()
        respuesta = urllib.request.urlopen(linea.strip(), timeout=segundos, context=context)
        contenidoWeb = respuesta.read().decode("UTF-8")
        if((contenidoWeb.find(rutaClave) >= 0) and (contenidoWeb.find("usamos cookies") < 0)
	and (contenidoWeb.find("utilizamos cookies") < 0)
        and (contenidoWeb.find("utiliza cookies") < 0)
        and (contenidoWeb.find("uso de cookies") < 0)
        and (contenidoWeb.find("usa cookies") < 0)
        and (contenidoWeb.find("we use cookies") < 0)
        and (contenidoWeb.find("use cookies") < 0)
        and (contenidoWeb.find("use of cookies") < 0)):
            print(Fore.RED+str(linea))
            g.write(linea)
        else:
            print(Fore.GREEN+str(linea))
    except:
        if args.retry:
            retry.write(linea)
        print(Fore.YELLOW+"This url is incorrect or the server has interrupted the session:",linea)

f.close()
g.close()
print(Fore.RESET)