#Solucion:

Ejercicio calculadora REST:
(restcalc.py en version mas simple)

##Recurso '/':
* Metodo GET:
  * Cuerpo: _Vacio_
  * Respuesta: 
    * Código: _200 Ok_
    * Cuerpo: _Devuelve las calculadoras disponibles_

##Recurso '/suma':

* Metodo POST:
  * Cuerpo: _Vacio_
  * Respuesta: 
    * Código: _200 Ok_
    * Cuerpo: _Devuelve el ID de la calculadora a utilizar_

####Recurso '/suma/ID':
* Metodo GET:
  * Cuerpo: _Vacio_
  * Respuesta: 
    * Código: _200 Ok_
    * Cuerpo: _Devuelve el resultado de la operacion_

* Metodo PUT:
  * Cuerpo: _Operandos_
  * Respuesta: 
    * Código: _200 Ok_
    * Cuerpo: _Vacio_

* Metodo DELETE:
  * Cuerpo: _Vacio_
  * Respuesta: 
    * Código: _200 Ok_
    * Cuerpo: _Vacio_

##Recurso '/resta':

* Metodo POST:
  * Cuerpo: _Vacio_
  * Respuesta: 
    * Código: _200 Ok_
    * Cuerpo: _Devuelve el ID de la calculadora a utilizar_

####Recurso '/resta/ID':

* Metodo GET:
  * Cuerpo: _Vacio_
  * Respuesta: 
    * Código: _200 Ok_
    * Cuerpo: _Devuelve el resultado de la operacion_

* Metodo PUT:
  * Cuerpo: _Operandos_
  * Respuesta: 
    * Código: _200 Ok_
    * Cuerpo: _Vacio_

* Metodo DELETE:
  * Cuerpo: _Vacio_
  * Respuesta: 
    * Código: _200 Ok_
    * Cuerpo: _Vacio_

##Recurso '/mult':

* Metodo POST:
  * Cuerpo: _Vacio_
  * Respuesta: 
    * Código: _200 Ok_
    * Cuerpo: _Devuelve el ID de la calculadora a utilizar_

####Recurso '/mult/ID':
* Metodo GET:
  * Cuerpo: _Vacio_
  * Respuesta: 
    * Código: _200 Ok_
    * Cuerpo: _Devuelve el resultado de la operacion_

* Metodo PUT:
  * Cuerpo: _Operandos_
  * Respuesta: 
    * Código: _200 Ok_
    * Cuerpo: _Vacio_

* Metodo DELETE:
  * Cuerpo: _Vacio_
  * Respuesta: 
    * Código: _200 Ok_
    * Cuerpo: _Vacio_

##Recurso '/div':

* Metodo POST:
  * Cuerpo: _Vacio_
  * Respuesta: 
    * Código: _200 Ok_
    * Cuerpo: _Devuelve el ID de la calculadora a utilizar_

####Recurso '/div/ID':
* Metodo GET:
  * Cuerpo: _Vacio_
  * Respuesta: 
    * Código: _200 Ok_
    * Cuerpo: _Devuelve el resultado de la operacion_

* Metodo PUT:
  * Cuerpo: _Operandos_
  * Respuesta: 
    * Código: _200 Ok_
    * Cuerpo: _Vacio_

* Metodo DELETE:
  * Cuerpo: _Vacio_
  * Respuesta: 
    * Código: _200 Ok_
    * Cuerpo: _Vacio_

