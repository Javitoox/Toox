Este programa desarrollado en python ayuda a la búsqueda de aquellas webs que utilizan google analytics pero 
no avisan de ello al usuario. 
El programa está desarrollado usando las siguientes librerías, las cuales deberán estar instaladas en su 
sistema operativo correspondiente

A rasgos generales el programa lee del fichero "url.txt" las urls que queremos comprobar. En el fichero
"retry.txt" se guardarán aquellas urls a las cuales no se ha podido acceder (por errores de certificados,
servidores caídos...). En el fichero "GA.txt" se guardarán aquellas urls de las webs que contienen el uso
de google analytics pero no avisan de sus cookies al usuario.

En cuanto a cuestiones técnicas:
- Se ha usado la librería ssl para solucionar algunos errores de certificados, los cuales en la versión
  anterior de este programa supuso el no acceso a las webs que daban errores de certificados.
- Se acepta tanto el formato de url  "http://xxxxxx" como el "xxxxxxxx".
- Para la búsqueda de lo que queremos se hace una llamada a la página web, de la cual posteriormente extraemos
  su código html para realizar una filración de palabras clave que nos dictarán si se usa google analytics y 
  aviso de cookies.
- Se ha impuesto un timeout de 10s a la llamada de la página web, ya que en la versión anterior si una página
  no cargaba (por hechos desconocidos), el programa se quedaba paralizado.

IMPORTANTE: en raras ocasiones el programa no detecta el programa no detecta el uso de google analytics, 
aunque en el código fuente de la página si aparece la palabra clave que buscamos (parece ser que dicha 
parte que buscamos no se descarga con el código html). Este programa es de ayuda automática a la búsqueda 
que queremos realizar, no es 100% eficaz.
