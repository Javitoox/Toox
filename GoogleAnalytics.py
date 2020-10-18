import urllib.request
import ssl
from colorama import Fore

print(Fore.BLUE+" ▄▄ •              ▄▄ • ▄▄▌  ▄▄▄ .     ▄▄▄·  ▐ ▄  ▄▄▄· ▄▄▌   ▄· ▄▌▄▄▄▄▄▪   ▄▄· .▄▄ · ")
print(Fore.BLUE+"▐█ ▀ ▪▪     ▪     ▐█ ▀ ▪██•  ▀▄.▀·    ▐█ ▀█ •█▌▐█▐█ ▀█ ██•  ▐█▪██▌•██  ██ ▐█ ▌▪▐█ ▀. ")
print(Fore.BLUE+"▄█ ▀█▄ ▄█▀▄  ▄█▀▄ ▄█ ▀█▄██▪  ▐▀▀▪▄    ▄█▀▀█ ▐█▐▐▌▄█▀▀█ ██▪  ▐█▌▐█▪ ▐█.▪▐█·██ ▄▄▄▀▀▀█▄")
print(Fore.BLUE+"▐█▄▪▐█▐█▌.▐▌▐█▌.▐▌▐█▄▪▐█▐█▌▐▌▐█▄▄▌    ▐█ ▪▐▌██▐█▌▐█ ▪▐▌▐█▌▐▌ ▐█▀·. ▐█▌·▐█▌▐███▌▐█▄▪▐█")
print(Fore.BLUE+"·▀▀▀▀  ▀█▄▀▪ ▀█▄▀▪·▀▀▀▀ .▀▀▀  ▀▀▀      ▀  ▀ ▀▀ █▪ ▀  ▀ .▀▀▀   ▀ •  ▀▀▀ ▀▀▀·▀▀▀  ▀▀▀▀ ")
print("                                   ")
print(Fore.BLUE+"                                                                               ")

print("If the color is red, that website has Google Analytics but there are not cookies: \n")
rutaClave="google-analytics"
f = open("url.txt", "r")
g = open("GA.txt", "w")
retry = open("retry.txt", "w")
for linea in f:
    try:
        if(str(linea[0:4]) != "http"):
            linea="http://"+str(linea)
        context = ssl._create_unverified_context()
        respuesta = urllib.request.urlopen(linea.strip(), timeout=10, context=context)
        contenidoWeb = respuesta.read().decode("UTF-8")
        if((contenidoWeb.find(rutaClave) >= 0) and (contenidoWeb.find("usamos cookies") < 0)
	and (contenidoWeb.find("utilizamos cookies") < 0)
        and (contenidoWeb.find("utiliza cookies") < 0)
        and (contenidoWeb.find("uso de cookies") < 0)
        and (contenidoWeb.find("usa cookies") < 0)):
            print(Fore.RED+str(linea))
            g.write(linea)
        else:
            print(Fore.GREEN+str(linea))
    except:
        retry.write(linea)
        print(Fore.YELLOW+"This url is incorrect or the server has interrupted the session:",linea)

f.close()
g.close()
print(Fore.RESET)