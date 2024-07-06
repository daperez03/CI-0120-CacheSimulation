# Tarea 3: Jerarquía de Memoria

## Objetivo

El objetivo de esta tarea es implementar una jerarquía de memoria caché de tres niveles con política de escritura write-back. Cada nivel de caché tendrá su propio TLB (Translation Lookaside Buffer) y el último nivel de la jerarquía será una memoria RAM.

## Descripción

El sistema de memoria caché diseñado para esta tarea consta de los siguientes componentes:

1. **Caché de Nivel 1 (L1):**
   - Tamaño: 3 páginas.
   - Política de reemplazo: Least Recently Used (LRU).

2. **Caché de Nivel 2 (L2):**
   - Tamaño: 5 páginas.
   - Política de reemplazo: Least Recently Used (LRU).

3. **Caché de Nivel 3 (L3):**
   - Tamaño: 8 páginas.
   - Política de reemplazo: Least Recently Used (LRU).

4. **RAM:**
   - Tamaño: 10 páginas.

Cada nivel de caché utilizará un TLB para acelerar la traducción de direcciones y mejorar la eficiencia del sistema. La política de write-back se implementará para reducir el número de escrituras a niveles de caché inferiores y a la RAM, mejorando así el rendimiento global.

## Restricciones

El programa está diseñado para ejecutarse en sistemas operativos Windows.

## Ejecución

Para ejecutar este programa, se debe utilizar el siguiente comando en la terminal:

```sh
python3 src/Main.py
```

Asegúrese de estar en el directorio raíz del proyecto antes de ejecutar el comando.

## Dependencias

Las siguientes dependencias son necesarias para ejecutar el programa:

- Python 3

## Integrantes

- [Alberto González Avendaño](mailto:alberto.gonzalezavendano@ucr.ac.cr)
- [Daniel Pérez Morera](mailto:daniel.perezmorera@ucr.ac.cr)
- [Sebastián Sánchez Sandí](mailto:sebastian.sanchezsandi@ucr.ac.cr)
