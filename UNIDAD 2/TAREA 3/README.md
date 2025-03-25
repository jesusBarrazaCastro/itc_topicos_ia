# Tarea 3 - Resolver el problema de N (8) reinas con Recocido Simulado 🔥♛♟️  
### Trabajo realizado por:  
- Jesús Alberto Barraza Castro  
- Jesús Guadalupe Wong Camacho  

***  

## Descripción del problema  
El problema de las **N reinas** consiste en colocar **N reinas en un tablero de N × N** de manera que ninguna de ellas se ataque entre sí. Esto significa que **no pueden estar en la misma fila, columna o diagonal**. En el caso de las **8 reinas**, el objetivo es encontrar una disposición en un tablero de **8 × 8** que cumpla estas restricciones.  

Para resolverlo, se utiliza **Recocido Simulado**, un algoritmo inspirado en el proceso de enfriamiento de los metales. Se basa en la aceptación probabilística de soluciones subóptimas para evitar quedarse atrapado en **mínimos locales**. La temperatura inicial \(T_0\) disminuye gradualmente siguiendo la secuencia **logarítmica de Boltzmann**, lo que reduce la probabilidad de aceptar soluciones peores con el tiempo.  

***  

## Implementación del algoritmo en Python  
[📄 Click aquí para ir al archivo](https://github.com/jesusBarrazaCastro/itc_topicos_ia/blob/main/UNIDAD%202/TAREA%203/n_reinas_recocido.py)  

---

### 📌 Características  
✅ Generación de soluciones vecinas mediante **swaps**.  
✅ Enfriamiento con la **secuencia logarítmica de Boltzmann**.  
