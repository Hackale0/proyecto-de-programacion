# Proyecto de Turismo Nacional

Este proyecto busca desarrollar una plataforma de turismo nacional donde los usuarios pueden encontrar las rutas más cortas entre diferentes ciudades utilizando el algoritmo de Dijkstra. El proyecto utiliza Django como framework web y permite interactuar con una base de datos que contiene las distancias entre las ciudades.

## ¿Qué se hizo?

En este proyecto se implementó un algoritmo de Dijkstra para calcular las rutas más cortas entre diferentes ciudades de un conjunto predefinido. Se utilizaron objetos de tipo `Ciudad` y `Ruta` para representar las ciudades y las distancias entre ellas.

El algoritmo de Dijkstra se implementó de manera eficiente utilizando una cola de prioridad para garantizar que las ciudades con menor distancia acumulada se procesaran primero.

## Análisis de Complejidad

La complejidad temporal del algoritmo de Dijkstra es **O(E log V)**, donde:
- **V** es el número de vértices (ciudades) en el grafo.
- **E** es el número de aristas (rutas) en el grafo.

La complejidad de espacio es **O(V + E)**, ya que necesitamos almacenar las distancias y las rutas de cada ciudad.

## ¿Qué funciona y qué no funciona?

### Funciona:
- El cálculo de las rutas más cortas entre ciudades usando Dijkstra.
- La visualización de los resultados de las rutas más cortas.

### No funciona:
- El cálculo de rutas cuando hay ciudades sin rutas conectadas.

### Mejoras futuras:
- Optimizar la representación del grafo para manejar grandes volúmenes de datos de forma más eficiente.
