# X-Serv-XML-ContentApp-Barrapunto
Gestor de contenidos con titulares de BarraPunto versión Django

## Enunciado

Realiza una aplicación Django con la misma funcionalidad que ``Django cms'', pero que devuelva para cada recurso para el cuál tenga un contenido asociado en su tabla de la base de datos una página que incluirá el contenido en cuestión, y los titulares de BarraPunto (para cada uno, título y URL).

Detalles del enunciado en el programa de la asignatura.

## ¿Como funciona?

#### Urls disponibles:

* __http://localhost:8000__ : Página principal. Devuelve una lista de urls dado el rss de barrapunto
* __http://localhost:8000/resource__ : Devuelve el contenido de 'resource' (siendo este un contenido que exista) y una lista de las urls dado el rss de barrapunto
* __http://localhost:8000/update__ : Actualiza el listado de rss de barrapunto en caso de que apareciesen nuevas noticias


# Cambios:

* Pruebas con templates.
