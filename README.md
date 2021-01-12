# Cálculo del riesgo en terremotos
## Proyecto final de la materia Peligros y Riesgos
## Josué Francisco Soto Cortez
### ENES, Unidad Morelia, UNAM

## Introducción
Terremoto, un fenómeno que actúa como un movimiento brusco en la Tierra, causado por la liberación de energía acumulada durante un tiempo prolongado en las placas tectónicas. <br>
Estos eventos han sido presentes desde que existe la Tierra, aunque el estudio de los mismos es relativamente reciente por la sismología, esta rama de la geofísica, estudia los terremotos y cómo se comportan dentro de la superficie de la tierra. Hasta el día de hoy, la Sismología ha sido de gran ayuda para medir los terremotos. <br>
Con lo desarrollado que es el internet ahora, y con el alcance a datos que ofrece la comunidad, El Centro Nacional de Información de Terremotos (NEIC con sus siglas en Inglés) puso a su disposición un data set de terremotos que han ocurrido en todo el mundo durante 1965 hasta el 2016 con una magnitud mayor o igual a 5.5 para el uso de investigación científica. <br>

### Datos: Significant Earthquakes, 1965-2016
Acceso a los datos [en este link.](https://www.kaggle.com/usgs/earthquake-database)<br> 
Data set que contiene día, hora, lugar, profundidad, magnitud y fuente de todos los terremotos con magnitud mayor o igual a 5.5 desde 1965 hasta 2016. <br>

#### Atributos 
Fecha (Date): la fecha de cada evento viene definida como mm/dd/aaaa <br>
Hora (Time): la hora viene definida como hh:mm:ss. <br>
Lugar (Latitude y Longitude): el lugar viene definido en dos columnas, con latitud y longitud.<br>
Tipo (Type): Los terremotos mayormente son originados por las placas tectónicas, pero también pueden ser originados por explosiones nucleares o algún otro evento de una gran magnitud. <br>
Profundidad (Depht): es donde la energía se libera en un terremoto. <br>
Magnitud (Magnitude): Medición del terremoto. <br>
Tipo de Magnitud (Magnitude Type): Las diferentes escalas para medir un terremoto, como Escala de Richter (ML), entre otras. <br>

## Objetivo
En esta práctica, se va a hacer uso de esos datos para calcular el riesgo de ocurrecnia de temblores mayores a 6.5 en un periodo de 10 años (2017-2027) en todo el mundo. <br>
También se va a calcular el riesgo que tuvieron desde los años 1985 hasta el año 2017 para poder evaluar cual es la tendencia del riesgo y poder observar como se podría comportar el riesgo en años actuales.

## Desarrollo

Se comenzó con el analisis de los datos, dado que son datos publicos y que no conocemos, lo primero era ver que los datos estuvieran completos y localizar datos que no fueran uniformes para ver si podíamos modificarlos, o excluirlos.

### Observaciones para la manipulación de datos.
Para el cálculo del riesgo solo tomaremos el dato de la magnitud, con el tipo de magnitud MW, ya que es el tipo con mayores registros. Es una escala que no se satura al evaluar sismos de gran intensidad (mega terremotos) y es la que se ha desarrollado mas recientemente, que se considera una aproximación cuantitativamente con una base física más fuerte que la Escala Richter. <br>
Durante la observacion de los datos, se pudo observar que los registros de magnitud MW son muy variados desde 1965 hasta 1983, y apartir de 1984 empiezan a ser datos con mas uniformidad, así que excluí los registros del año 1965 hasta 1983, para que en la evaluacion de la tendencia no existan valores atípicos y que la tendencía sea mas precisa. <br>

#### Modificación de datos

* Para la exclusión de datos del 1965 hasta el 1983 eliminamos desde la linea 2 hasta la linea 6865 de nuestro archivo de datos `earthquakes.dat` y así quedarnos con un total de 16545 registros.
* Modificacion de formato de fecha en los registros 648 y 13784 (contando que ya excluí los datos de 1965 a 1983)
* Para que el codigo que se creó funcionara, agregué un registro al final de los datos que es el siguiente: `01/01/2017   5.0   MW` 









