# Concurso UPAO 2022
### Problema 1
El problema de las Torres de Hanoi es un problema clásico de recursión. Se tienen 3 torres y un conjunto de discos de diferentes tamaños. Cada disco tiene una perforación en el centro que le permite ensartarse en cualquiera de las torres. Los discos han de encontrarse siempre situados en alguna de las torres. Inicialmente todos están en la misma torre, ordenados de mayor a menor, como se muestra en el dibujo. Se deben averiguar los movimientos necesarios para pasar todos los discos a otra torre, utili- zando la tercera como auxiliar y cumpliendo las siguientes reglas:

- En cada movimiento solo puede intervenir un disco.

- No puede quedar un disco sobre otro de menor tamaño.

[![20221127-000550.jpg](https://i.postimg.cc/vBj6Dc3R/20221127-000550.jpg)](https://postimg.cc/DJrzMf95)

Para N=3 la solución del problema emplica los siguentes movimeintos.

1. De 1 a 2
2. De 1 a 3
3. De 2 a 3
4. De 1 a 2
5. De 3 a 1
6. De 3 a 2
7. De 1 a 2

### Problema 2
Realice un programa que realice el cifrado de un texto contenido en archivo, mediante la conversión de cada uno de sus caracteres al lenguaje, Marciano 1, el cual se describe a continuación:

| Carácter  | Equivalente (6 caracteres sin espacios)  |
| :------------: | :------------: |
| A |  ...... |
| B |  ...... |
| C  |  ...... |
| D |  ...... |
| E  |  ...... |
| F  |  ...... |
|  G |  ...... |
|  H |  ...... |
|  I |  ...... |
|  J |  ...... |
|  K |  ...... |
|  L |  ...... |
|  M |  ...... |
|  N |  ...... |
|  O |  ...... |
|  P |  ...... |
|  Q |  ...... |
|  R |  ...... |
|  S |  ...... |
|  T |  ...... |
|  U |  ...... |
|  V |  ...... |
|  W |  ...... |


Ejemplo del archivo de entrada:

    Esta es la frase a codificar

Ejemplo del archivo de salida:

    Frase a codificada xD

### Problema 3
La gente que prepara problemas para un concurso de programación, espera el fin de semana para hacer problemas que aterroricen a los concursantes. Asi que antes de que empiece un mes, los programadores de problemas tratan de calcular el número de dias de fin de semana que usan en ese mes y planes en consecuencia. ¿Puedes ayudarlos a Calcular esto? Hay siete dias en una semana es domingo (SUN), Lunes (lunes), martes (TUE), miércoles (WED), jueves (THU), viernes (FRI) y sábado (SAB).

Hay doce meses en un año, enero (JAN), febrero (FEB), marzo (MAR), Abril (abril), mayo (mayo), junio (junio), julio (julio), agosto (agosto), septiembre (septiembre), octubre (OCT), noviembre (NOV) y diciembre (DEC). Estos meses tienen 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 y 31 días, respectivamente. En los años bisiestos, el mes de febrero tiene 29 dias En el paréntesis se muestra el código de tres letras para cada mes y cada día. A diferencia de muchos países del mundo (FRI) y el sábado (SAT) se consideran días de fin de semana. Dado un mes y el nombre del primer día de ese mes, tendrá que averiguar el número total de dias de fin de semana en ese mes. 

### Datos de entrada
La primera linea contiene un número entero T (Ts 100), que indica el número de casos de prueba. La entrada para cada conjunto se da en una sola linea. Esta linea contiene dos cadenas MTH y el día, aquí es MTH los tres códigos de cuatro digitos del mes y el día es el código de tres digitos para el nombre del primer día de ese mes.

### Datos de Salida

Para cada línea de entrada produce una linea de salida. Contiene un solo entero que denota el número de los días de fin de semana (viernes y sábados) en ese mes:

Ilustración que muestra la 3era entrada: En la tercera entrada de muestra se nos pide qué Dias de fin de semana de un mes de octubre cuyo primer día (October 1) es el jueves. El calendario de la izquierda muestra esto y se puede ver que hay 10 días de fin de semana (color Rojo) en este mes.

[![20221127-000543.jpg](https://i.postimg.cc/3xVWHdrz/20221127-000543.jpg)](https://postimg.cc/YvNt62Wx)

Ejemplo de entrada

    3
    JAN SUN
    FEB SUN
    OCT THU
    29 30 

Salida de la muestra

    8
    8
    10
