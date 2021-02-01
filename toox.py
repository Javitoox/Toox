import urllib.request
import ssl
from colorama import Fore
import argparse

print(Fore.BLUE+r" _______ ____   ______   __ ")
print(Fore.BLUE+r"|__   __/ __ \ / __ \ \ / /")
print(Fore.BLUE+r"   | | | |  | | |  | \ V /")
print(Fore.BLUE+r"   | | | |  | | |  | |> <|")
print(Fore.BLUE+r"   | | | |__| | |__| / . \ ")
print(Fore.BLUE+r"   |_|  \____/ \____/_/ \_\ ")
print(Fore.RESET)

# Palabras clave de detección de Google Analytics
key_1 = "google-analytics"
key_2 = "gtag.js"
key_3 = "ga.js"
key_4 = "analytics.js"

# Procesado de argumentos
parser = argparse.ArgumentParser(description="This program has been developed to help search for websites that use Google Analytics and do not notify their users about it. " +
                                 "Our found targets will be shown in red on the screen. Apart from the previous functionality as the main one, this program also serves for " +
                                 "other functionalities")
parser.add_argument("-t", "--timeout", help="Maximum seconds to wait for a response from the server, by default 1." +
                    " Please note that for low timeouts you may not get a response from the web page. Accepted formats: x.x(decimal) / x(integer)")
parser.add_argument("-r", "--retry", help="Generation of file where the urls that cannot be accessed will be collected. Extension: .txt")
parser.add_argument("-o", "--output", help="Generation of file where the results will be collected. Extension: .txt")
parser.add_argument("-e", "--entry", help="Required input file, which must contain the urls to be analyzed, each one being written on a different line. Extension: .txt", required=True)
parser.add_argument("-a", "--analytics", help="If this option is activated, only those websites that are using google analytics will be searched", action="store_true")
parser.add_argument("-s", "--secure", help="If this option is activated, the result will indicate if the connection of the pages is secure", action="store_true")
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

# Procesado de entry
if args.entry:
    try:
        f = open(args.entry, "r")
    except:
        print("No such file or directory:", args.entry, "\n")
        exit()

# Mensajes de información
if args.analytics:
    print("If the color of the url is red, that website has Google Analytics:\n")
else:
    print("If the color of the url is red, that website has Google Analytics but there are not cookies:\n")

# Función para el cálculo de conexiones seguras
def security (respuesta):
    url = respuesta.geturl()
    if url[0:5] == "https":
        tipo = "["+url+": secure connection]"
        print(Fore.GREEN+tipo)
    else:
        tipo = "["+url+": insecure connection]"
        print(Fore.RED+tipo)
        if args.output:
            g.write(tipo+"\n")

# Funcionalidad principal del programa
for linea in f:
    linea = linea.strip()
    try:
        if(linea[0:4] != "http"):
            linea = "http://"+linea
        context = ssl._create_unverified_context()
        respuesta = urllib.request.urlopen(linea, timeout=segundos, context=context)
        contenidoWeb = respuesta.read().decode("UTF-8")
        if args.analytics:
            if((contenidoWeb.find(key_1) >= 0) or (contenidoWeb.find(key_2) >= 0) or (contenidoWeb.find(key_3) >= 0) or (contenidoWeb.find(key_4) >= 0)):
                print(Fore.RED+linea)
                if args.output:
                    g.write(linea+"\n")
            else:
                print(Fore.GREEN+linea)
        else:
            if(((contenidoWeb.find(key_1) >= 0) or (contenidoWeb.find(key_2) >= 0) or (contenidoWeb.find(key_3) >= 0) or (contenidoWeb.find(key_4) >= 0))
               and (contenidoWeb.find("usamos cookies") < 0)
               and (contenidoWeb.find("utilizamos cookies") < 0)
               and (contenidoWeb.find("utiliza cookies") < 0)
               and (contenidoWeb.find("uso de cookies") < 0)
               and (contenidoWeb.find("usa cookies") < 0)
               and (contenidoWeb.find("we use cookies") < 0)
               and (contenidoWeb.find("use cookies") < 0)
               and (contenidoWeb.find("use of cookies") < 0)):
                print(Fore.RED+linea)
                if args.output:
                    g.write(linea+"\n")
            else:
                print(Fore.GREEN+linea)
        if args.secure:
            security(respuesta)
    except:
        if args.retry:
            retry.write(linea+"\n")
        print(Fore.YELLOW+"This url is incorrect or the server has interrupted the session:", linea)

f.close()
if args.output:
    g.close()
if args.retry:
    retry.close()
print(Fore.RESET)