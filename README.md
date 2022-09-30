# Tarea-1-Algoritmos-Metahuristicos
## Problema de las N-reinas
### El problema consistirá principalmente en desarrollar e idear un algoritmo genético que solucione el problema de las N-reinas, el cual consiste en colocar n reinas en un tablero de ajedrez de n x n de tal manera que no sea posible que dos reinas se capturen entre si, es decir, que no estén en la misma fila, ni en la misma columna ni en la misma diagonal.

## Programas utilizados 

* [GitHub Desktop](https://desktop.github.com/) - Programa de control de versiones
* [Visual Studio Code](https://visualstudio.microsoft.com/es/) - IDE para la creación del Algoritmo

## Instalación
* La versión utilizada para python será [3.10.7](https://www.python.org/downloads/).
* Se necesitara instalar la libreria [numpy](https://numpy.org/)
 ```
 pip install numpy
 ```
 * Link zip

## Ejecución del programa
 ```
 python.exe .\Reinas.py 1 5 5 0.90 0.20 100
 ```

## Definición de Variables
* ***Seed***, el cuál sera un número real randomico entre 0 y 1.
* ***Tamaño del tablero***, número entero entre 1 y N(tamaño población).
* ***Tamaño de la poblacion***, número entero a criterio del usuario.
* ***Probabilidad de cruza***, número real 95 = 0.95
* ***Probabilidad de mutación***,  número real 5 = 0.05
* ***Número de Iteraciones***, número entero a criterio del usuario.

## Ejemplo
```
Ingrese la semilla: 1
Ingrese el numero de reinas: 5
Ingrese la población: 5
Ingrese la probabilidad de cruzar: 0.90
Ingrese la probabilidad de mutacion: 0.20
Ingrese la cantidad de iteraciones: 100
```

### Autores
* Diego Araneda Hidalgo - daranedah@ing.ucsc.cl
* Gustavo Sepulveda Ocampo - gsepulveda@ing.ucsc.cl
* Javier Victoriano Rivas - jvictoriano@ing.ucsc.cl
