# Cálculo del riesgo en terremotos
## Proyecto final de la materia Peligros y Riesgos
## Josué Francisco Soto Cortez
### ENES, Unidad Morelia, UNAM

Terremoto, un fenómeno que actúa como un movimiento brusco en la Tierra, causado por la liberación de energía acumulada durante un tiempo prolongado en las placas tectónicas. <br>
Estos eventos han sido presentes desde que existe la Tierra, aunque el estudio de los mismos es relativamente reciente por la sismología, esta rama de la geofísica, estudia los terremotos y cómo se comportan dentro de la superficie de la tierra. Hasta el día de hoy, la Sismología ha sido de gran ayuda para medir los terremotos. <br>
Con lo desarrollado que es el internet ahora, y con el alcance a datos que ofrece la comunidad, El Centro Nacional de Información de Terremotos (NEIC con sus siglas en Inglés) puso a su disposición un data set de terremotos que han ocurrido en todo el mundo durante 1965 hasta el 2016 con una magnitud mayor o igual a 5.5 para el uso de investigación científica. <br>

## Objetivo
En esta práctica, se va a hacer uso de esos datos para calcular el riesgo respecto de la magnitud de los temblores mayores a 5.5 en un periodo de 2 años.

## Datos: Significant Earthquakes, 1965-2016
Acceso a los datos [en este link.](https://www.kaggle.com/usgs/earthquake-database)<br> 
Data set que contiene día, hora, lugar, profundidad, magnitud y fuente de todos los terremotos con magnitud mayor o igual a 5.5 desde 1965 hasta 2016. <br>

### Atributos 
Fecha (Date): la fecha de cada evento viene definida como mm/dd/aaaa <br>
Hora (Time): la hora viene definida como hh:mm:ss. <br>
Lugar (Latitude y Longitude): el lugar viene definido en dos columnas, con latitud y longitud.<br>
Tipo (Type): Los terremotos mayormente son originados por las placas tectónicas, pero también pueden ser originados por explosiones nucleares o algún otro evento de una gran magnitud. <br>
Profundidad (Depht): es donde la energía se libera en un terremoto. <br>
Magnitud (Magnitude): Medición del terremoto. <br>
Tipo de Magnitud (Magnitude Type): Las diferentes escalas para medir un terremoto, como Escala de Richter (ML), entre otras. <br>

### Observaciones
Para el cálculo del riesgo solo tomaremos el dato de la magnitud, con el tipo de magnitud MW, ya que es el tipo con mayores registros. Es una escala que no se satura al evaluar sismos de gran intensidad (mega terremotos) y es la que se ha desarrollado mas recientemente, que se considera una aproximación cuantitativamente con una base física más fuerte que la Escala Richter.






