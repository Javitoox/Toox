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

# Palabras clave de detección de Google Analytics
key_1 = "google-analytics"
key_2 = "gtag.js"
key_3 = "ga.js"
key_4 = "analytics.js"

# Apertura del fichero de urls
f = open("url.txt", "r")

# Procesado de argumentos
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--timeout", help = "Maximum seconds to wait for a response from the server, by default 1." +
" Please note that for low timeouts you may not get a response from the web page. Accepted formats: x.x(decimal) / x(integer)")
parser.add_argument("-r", "--retry", help = "Generation file where the urls that cannot be accessed will be collected")
parser.add_argument("-o", "--output", help = "Generation of file where the results will be collected")
args = parser.parse_args()

# Procesado de timeout
segundos = 1.0
if args.timeout:
    try: 
        segundos = float(args.timeout)
        if segundos < 1.0:
            exit()
    except:
        print("Timeout must be a number greater than 0\n")
        exit()

# Procesado de retry
if args.retry:
    retry = open(args.retry, "w")

# Procesado de output
if args.output:
    g = open(args.output, "w")

print("If the color is red, that website has Google Analytics but there are not cookies:\n")

# Funcionalidad principal del programa
for linea in f:
    try:
        if(str(linea[0:4]) != "http"):
            linea="http://"+str(linea)
        context = ssl._create_unverified_context()
        respuesta = urllib.request.urlopen(linea.strip(), timeout=segundos, context=context)
        contenidoWeb = respuesta.read().decode("UTF-8")
        if(((contenidoWeb.find(key_1) >= 0) or (contenidoWeb.find(key_2) >= 0) or (contenidoWeb.find(key_3) >= 0) or (contenidoWeb.find(key_4) >= 0)) 
        and (contenidoWeb.find("usamos cookies") < 0)
	    and (contenidoWeb.find("utilizamos cookies") < 0)
        and (contenidoWeb.find("utiliza cookies") < 0)
        and (contenidoWeb.find("uso de cookies") < 0)
        and (contenidoWeb.find("usa cookies") < 0)
        and (contenidoWeb.find("we use cookies") < 0)
        and (contenidoWeb.find("use cookies") < 0)
        and (contenidoWeb.find("use of cookies") < 0)):
            print(Fore.RED+str(linea))
            if args.output:
                g.write(linea)
        else:
            print(Fore.GREEN+str(linea))
    except:
        if args.retry:
            retry.write(linea)
        print(Fore.YELLOW+"This url is incorrect or the server has interrupted the session:",linea)

f.close()
if args.output:
    g.close()
if args.retry:
    retry.close()
print(Fore.RESET)