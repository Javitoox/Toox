Video explicativo: https://www.youtube.com/watch?v=sr1cYGYr3Bo&ab_channel=JaviMart%C3%ADnez
Este programa desarrollado en python ayuda a la búsqueda de aquellas webs que utilizan Google Analytics pero 
no avisan de ello al usuario.

A rasgos generales el programa lee del fichero "url.txt" las urls que queremos comprobar. El progarama mostrará
en rojo las urls de las webs que contienen el uso de Google Analytics pero no avisan de sus cookies al usuario.
Mediante la opción -h o --help se mostrarán todas las funcionalidades que ofrece el programa.

En cuanto a cuestiones técnicas:
- Se ha usado la librería ssl para solucionar algunos errores de certificados, los cuales en la versión
  anterior de este programa supuso el no acceso a las webs que daban errores de certificados.
- Se acepta tanto el formato de url  "http://xxxxxx" como el "xxxxxxxx".
- Para la búsqueda de lo que queremos se realiza una llamada a la página web, de la cual posteriormente 
  extraemos su código html para realizar una filtración de palabras clave que nos dictarán si se usa Google 
  Analytics y cookies.

IMPORTANTE: en raras ocasiones el programa no detecta el uso de Google Analytics, aunque en el código 
fuente de la página si aparece la palabra clave que buscamos (parece ser que dicha parte que buscamos no se 
descarga con el código html). Este programa es de ayuda automática a la búsqueda que queremos realizar, no es 
100% eficaz. ES NECESARIO BORRAR LAS COOKIES DEL NAVEGADOR ANTES DEL USO DEL PROGRAMA
