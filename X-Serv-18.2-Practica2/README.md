# Práctica Hosteada en: [Click aqui (si no se ha caido)](http://193.147.53.163:8000/)
# X-Serv-18.2-Practica2

Práctica 2 (Ejercicio 18.2): Web acortadora de URLs con Django

# ¿Cómo funciona?

### Urls disponibles:

* __http://localhost:8000__ : Página principal. Devuelve un formulario (que utiliza POST) y una lista de urls ya acortadas.
* __http://localhost:8000/n__ : Direccion de url acortada. Redirige a la url acortada correspondiente a "n" (si hay).

# Cambios:

* Añadido detección automatica de IP.
* Pruebas con templates.
* Añadida prueba con fondos y aparienciade la web.
* Arreglado el error de empty qs.
* Quitado autocompletar formulario.
* Añadida protección de XSS.
