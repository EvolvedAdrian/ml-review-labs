# COMPLEJIDAD --> Notación Big O
# Indica como crece tiempo de ejecución o espacio en memoria cuando el número de datos aumenta (n) --> las constantes se ignoran ya que solamente nos importa el cómo no el cuánto

# Tiempo: cuántas operaciones/pasos hace el procesador
# Espacio: cuánta memorial RAM o disco consume el algoritmo mientras se ejecuta (cuántas funciones están en el call stack o cuántas variables se crean)

# OBJETIVO: Tiempo O(1) o O(n) y Espacio O(1) (liberar memoria)

# TIPOS DE COMPLEJIDAD

# Complejidad 0(1) --> 1 solo paso sin importar tamaño de lista (búsqueda diccionario)
def imprimir_primero(lista):
    print(lista[0])

# Complejidad O(n) --> lineal, n operaciones (loop simple)
def imprimir_todos(lista):
    for el in lista:
        print(el)

# Complejidad O(n²) --> cuadrática, n² operaciones (búsqueda binaria)
def pares_posibles(lista):
    for i in lista:
        for j in lista:
            print(f"{i}, {j}")

# Complejidad O(2^n) --> exponencial, es la muerte (recursión sin control)
def fibonacci_mortal(n):
    if n <= 1: return n
    return fibonacci_mortal(n-1) + fibonacci_mortal(n - 2)

# Alternativa eficiente O(n) + Espacio O(1)
cache = {}
def fibonacci_bueno(n):
    if n in cache: return cache[n]
    u, u2 = 0, 1
    for i in range(n):
        u, u2 = u2, u + u2
        cache.setdefault(i+1,u)
    return u



# Complejidad O(log n) --> algorítmica cuando el espacio de búsqueda se reduce a la mitad en cada iteración (pej: búsqueda binaria). Casi tan eficiente como O(1) --> genial para búsquedas por rango, para busquedas directas casi todo el mundo usa tablas hash / diccionarios
def divide_y_venceras(n):
    i = n
    while i > 1:
        i = i // 2
        print(i)

# Complejidad O(n log n) --> estándar de ordenamiento (no puede descartar datos, debe procesar todos al menos una vez)


# MÉTODOS DE ORDENAMIENTO MALO O(n²)
# - Bubble sort --> compara parejas
# - Selection sort --> Busca los mínimos y los va poniendo al principio
# - Insertion sort --> Va insertando los números correctos en su lugar en base a lo que ya lleva visto

# MÉTODOS DE ORDENAMIENTO BUENO O(n log n)
# - Merge sort --> divide a la mitad y a la mitad y así sucesivamente hasta tener listas de un solo elemento y luego las junta ordenadas
# - Quick Sort --> El más rápido. Elige número pivote y pone menores a un lado y mayores a otro, así sucesivamente
# - Timsort (lo usa .sort() de python) --> Híbrido entre Merge Sort e Insertion Sort

# DETERMINAR COMPLEJIDAD DE OPERACIONES

# O(n) + O(n) = O(n + n) = O(n) --> ignoramos constantes, término mayor determina complejidad
def algoritmos_mezclados(lista):
    for x in lista:
        print(x)
    for y in lista:
        print(y)

# O(1 + n + n²) = O(n²) --> término mayor determina complejidad
def proceso_complejo(lista):
    # Un paso O(1)
    a = 10 + 20
    
    # Un bucle O(n)
    for x in lista:
        print(x)
        
    # Bucle anidado O(n^2)
    for i in lista:
        for j in lista:
            print(i, j)

def crear_matriz(n):
    matriz = []
    for _ in range(n):
        fila = [0] * n
        matriz.append(fila)
    return matriz


# ARRAYS: datos almacenados secuencialmente en memoria
# --> buscar: O(1) ya que los datos están seguidos en memoria, insertar o borrar O(n) (hay que mover todos los elementos siguientes)

# Procesamos datos en O(1) para ahorrar espacio
def invertir_lista(lista):
    """ Invierte los elementos de una lista: Tiempo O(n), Espacio O(1) 

    Args:
        lista: Lista

    Returns:
        list: Lista inicial invertida
    """
    ini_i = 0
    fin_i = len(lista) - 1

    while ini_i < fin_i:
        # Intercambio de valores
        lista[ini_i], lista[fin_i] = lista[fin_i], lista[ini_i]
        ini_i, fin_i = ini_i + 1, fin_i + 1

def rotar(lista, n):
    """Rota los elementos de una lista n posiciones: Tiempo O(n), Espacio O(1)
    
    Args:
        lista (list)
        n (Int): número de posiciones a rotar los elementos
        
    Returns:
        list: Lista inicial rotada n elementos
    """
    l = len(lista)
    n %= l
    
    def invertir(ini, fin):
        while ini < fin:
            lista[ini], lista[fin] = lista[fin], lista[ini]
            ini, fin = ini + 1, fin - 1
    
    invertir(0, l - 1)
    invertir(0, n - 1)
    invertir(n, l - 1)

# Puntero al inicio y al final
def eliminar_duplicados(lista_ordenada):
    """Elimina los duplicados contiguos de una lista ordenada: Tiempo O(n), Espacio O(1)
    
    Args:
    lista_ordenada (list): Lista ordenada inicial con duplicados
    
    Returns:
    Int: Nueva longitud de la lista ordenada sin duplicados
    """
    if not lista_ordenada: return 0
    escribir = 1
    for leer in range(1, len(lista_ordenada)):
        if lista_ordenada[leer] != lista_ordenada[leer - 1]:
            lista_ordenada[escribir] = lista_ordenada[leer]
            escribir += 1
    del lista_ordenada[escribir:]
    return escribir

def encontrar_objetivo(lista_ordenada, objetivo):
    """Dada una lista de números ordenados, encuentra los 2 números cuya suma es igual al objetivo: Tiempo O(n), Espacio O(1)
    
    Args:
    lista_ordenada (list): Lista ordenada inicial
    objetivo (Int): Número igual a la suma objetivo

    Returns:
    Tuple: Los dos números del array cuya suma es igual al objetivo
    None: No ha encontrado un par que sume el objetivo
    """
    ini = 0
    fin = len(lista_ordenada) - 1
    
    while ini < fin:
        suma = lista_ordenada[ini] + lista_ordenada[fin]
        if suma == objetivo:
            return (lista_ordenada[ini], lista_ordenada[fin])
        elif suma < objetivo:
            ini += 1
        else:
            fin += 1

    return None
    
# Sliding window --> Algoritmo de Kadane. NLP y series temporales
def max_suma_subgrupo(lista):
    """Devuelve la mayor suma generada por un subgrupo contiguo: Tiempo O(n), Espacio(1)
    
    Args:
    lista (list): Lista inicial (puede contener números negativos)

    Returns:
    Int: Mayor suma contigua dentro de la lista
    """
    max_actual = lista[0]
    max_global = lista[0]

    for i in range(1, len(lista)):
        # Algoritmo de Kadane: Si resta de lo anterior es menor que número actual me vale la pena empezar en este número
        max_actual = max(lista[i], max_actual + lista[i])
        max_global = max(max_global, max_actual)

    return max_global

# Transponer matriz --> operación más frecuente en redes neuronales: Backpropagation
# Para matrices cuadradas se puede hacer con espacio O(1), pero matrices rectangulares obligatoriamente necesitamos espacio O(n²) para recrearla
def transponer_matriz(matriz):
    """Transpone una matriz cuadrada (convertir filas en columnas o viceversa): Tiempo O(n), Espacio O(1)
    
    Args:
    matriz: Matriz cuadrada original
    
    Returns:
    list[list]: Matriz cuadrada traspuesta
    """
    n = len(matriz)
    for i in range(n):
        for j in range(i+1,n):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

# Operaciones vectoriales --> Neurona artificial multiplica entradas por pesos y los suma --> así procesa la información
def producto_punto(m1, m2):
    """Obtiene el producto escalar de dos matrices: Tiempo O(n), Espacio O(1)
    
    Args:
    m1 (list)
    m2 (list)

    Returns:
    Int: Producto escalar
    """
    suma = 0
    if len(m1) != len(m2): return None
    for i in range(len(m1)):
        suma += m1[i]*m2[i]
    return suma

# NumPy es mucho más rápido porque usa instrucciones de hardware (SIMD)
# np.dot(m1,m2)

# Normalización de valores
def normalizacion_min_max(lista):
    """Normaliza todos los valores de un array a valores entre 0 y 1: Tiempo O(n), Espacio O(1)
    
    Args:
    lista (list): Lista inicial

    Returns:
    List: Lista normalizada
    """
    min_lista = min(lista)
    max_lista = max(lista)
    if max_lista == min_lista:
        for i in range(len(lista)):
            lista[i] = 0
    else:
        for i in range(len(lista)):
            x = lista[i]
            lista[i] = (x - min_lista) / (max_lista - min_lista)

# Normalización min-max con Numpy mucho más rápida --> aplica vectorización, sigue siendo Tiempo O(n) pero la constante de tiempo es mucho más pequeña
# Numpy está optimizado con C++ --> datos directos en RAM, nada de interpretación
import numpy as np
from numpy.typing import NDArray
def normalizacion_min_max_numpy(arr: NDArray):
    """Normaliza todos los valores de un array a valores entre 0 y 1 usando Numpy: Tiempo O(n), Espacio O(1)
    
    Args:
    lista (list): Lista inicial

    Returns:
    List: Lista normalizada
    """
    min_v = np.min(arr)
    max_v = np.max(arr)
    
    # Operaciones in-place, espacio O(1): no crean copia del array --> O(n): arr = (arr - min_v) / (max_v - min_v)
    arr -= min_v
    arr /= (max_v - min_v)

arr = np.array([1,4,6,2,7], dtype=np.float32) 
# Numpy no puede meter decimales en array de enteros, hay que transformar a float
# float64 ocupa 8B en vez de 4B por dígito y es innecesario 15 decimales de precisión para entrenar modelo y que aprenda cosas, con 7 decimales llega (además es mucho más rápido), incluso ahora se usa float16.
# Usar astype crea copia y convierte en espacio O(n) mejor especificar dtype en la creación del ndarray para mantener espacio O(1)
normalizacion_min_max_numpy(arr)





# TABLAS HASH / DICCIONARIOS (en python dict + set)
# función matemática convierte cada clave en hash, ordenador luego va directo ahí --> buscar, insertar, borrar O(1)
# --> a veces 2 claves diferentes dan mismo resultado matemático - colisión --> SOLUCIÓN: chaining, guardar ambas claves en mismo contenedor dentro de una linked list


# ESTRUCTURAS DE DATOS NO LINEALES:
# ÁRBOLES: estructura jerárquica (raíz, ramas, hojas)
# ÁRBOLES BINARIOS: cada nodo máximo 2 hijos.
# - BST todo lo que está a la izquierda es menor que el padre y lo de la derecha es mayor. Si los datos están medianamente balanceados su complejidad tiende a O(log n) como por ejemplo [3,1,5,2,4] pero sino su complejidad tiende a O(n), por ejemplo [1,2,3,4,5] genera un árbol totalmente desbalanceado, prácticamente una linked list
# - HEAP: Dos tipos, el max-heap cada elemento padre siempre es mayor que sus hijos, min-heap, cada elemento padre siempre es menor que sus hijos --> utilización real en colas de prioridad
# - AVL: BST autoequilibrado con diferencia de altura entre subárboles máxima de 1 --> optimiza búsquda ya que reduce complejidad, usado en DB en memoria
# - ROJO-NEGRO: BST autoequilibrado más relajado (diferencia de altura entre subarboles puede ser hasta el doble del camino más corto) --> el más usado en mayoría de implementaciones en lenguajes por su rendimiento equilibrado inserciones/búsquedas

# ÁRBOLES N-ARIOS: cada nodo puede tener n hijos
# ÁRBOLES MULTICAMINO (B-TREES): B y B+ --> árboles balanceados para consultas rapidísimas en bases de datos

# HEAPS (árbol binario especial) --> USO: colas de prioridad
# TRIE (ÁRBOL DE PREFIJOS)

# GRAFOS: estructuras no jerárquicas (nodos/vértices, aristas/edges)
# TIPOS:
# DIRIGIDOS: conexiones de un solo sentido (seguidores de X)
# NO DIRIGIDOS: conexiones de ambos sentidos (amigos de facebook)
# PONDERADOS (WEIGHTED): conexiones tienen un costo o distancia

# BÚSQUEDAS:
# BFS(Breadth-First Search): Expansión - encontrar el camino más corto (usa Colas)
# DFS(Depth-First Search): Un camino hasta chocar luego retrocede - resolver laberintos (usa Pilas)