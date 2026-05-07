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
def fibonacci_bueno(n, cache = {}):
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

def rotar_lista(lista, n):
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

def encontrar_objetivo_ord(lista_ordenada, objetivo):
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



# LINKED LIST --> Simples apuntan al siguiente elemento, Dobles apuntan al anterior y al siguiente elemento, Circulares: el último elemento apunta al primero
# --> buscar O(n): hay que seguir los punteros para llegar al dato deseado, insertar o borrar O(1), solo cambiar los punteros, no tienes que decirle a los elementos siguientes que se muevan
# --> la linked list realmente es head, siempre hay que devolverlo y reasignarlo

class Nodo:
    """Nodo de una linked list"""
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

head = Nodo(10)
head.siguiente = Nodo(20)
head.siguiente.siguiente = Nodo(30)

def mostrar_lista_rec(head):
    """Muestra la linked list completa: Espacio O(n)
    
    Args:
    head (Nodo): Nodo inicial de la linked list
    """
    if head:
        print(head.valor)
        mostrar_lista_rec(head.siguiente)

def mostrar_lista(head):
    """Muestra la linked list completa: Espacio O(1)
    
    Args:
    head (Nodo): Nodo inicial de la linked list
    """
    if not head: return None
    curr = head # Hacemos una copia del puntero head llamada curr para lograr recorrer la linked list, conservamos a head intacto en el punto de partida por si necesitamos volver a usarlo
    while curr:
        print(curr.valor)
        curr = curr.siguiente



def encontrar_cola(head):
    """Encuentra el nodo final de una linked list: Tiempo O(n), Espacio O(1)
    
    Args:
    head (Nodo): Nodo inicial de la linked list

    Returns:
    Nodo: Nodo final de la linked list
    """
    if not head: return None
    curr = head # Hacemos una copia del puntero head llamada curr para lograr recorrer la linked list y devolver el nodo final
    while curr.siguiente:
        curr = curr.siguiente
    return curr

def insertar_inicio(head, nuevo_head):
    """Inserta un nodo al inicio de una linked list: Tiempo O(1), Espacio O(1)
    
    Args:
    nodo (Nodo): Nodo a insertar al inicio de la linked list

    Returns:
    Nodo: Nuevo head de la linked list
    """
    nuevo_head.siguiente = head
    return nuevo_head

def insertar_final(head, nuevo_nodo):
    """Inserta un valor al final de una linked list: Tiempo O(n), Espacio O(1)
    
    Args:
    nodo (Nodo): Nodo a insertar al final de la linked list

    Returns:
    Nodo: Nodo cabeza de la linked list modificada con el nuevo nodo al final
    """
    if not head: return nuevo_nodo # Si la linked list es vacía devolvemos el nuevo nodo directamente
    encontrar_cola(head).siguiente = nuevo_nodo
    return head

head = insertar_inicio(head, Nodo(3))
head = insertar_inicio(head, Nodo(2))
head = insertar_final(head, Nodo(60))

def eliminar_nodo(head, indice):
    """Elimina el enésimo nodo: Tiempo O(n), Espacio O(1)
    
    Args:
    head (Nodo): Cabeza de la linked list a eliminar el nodo
    indice (Int): Índice del nodo a eliminar de la linked list
    """
    if indice == 0: return head.siguiente
    curr = head # Hacemos una copia del puntero head llamada curr para lograr llegar al nodo deseado y eliminar el nodo
    for _ in range(indice - 1):
        if curr.siguiente: # Verificamos si curr todavía no ha llegado al final
            curr = curr.siguiente

    if curr.siguiente:
        curr.siguiente = curr.siguente.siguiente # Simplemente saltamos el nodo, PELIGRO: Python tiene garbage collector, por lo que no debemos ir ahora a poner en None el Nodo.siguiente ese nodo ya ha sido eliminado y estaríamos haciendo referencia al siguiente nodo (DECAPITARÍAMOS LA LISTA)
    return head
    
def invertir_linked_list(head):
    """Invierte una linked list: Tiempo O(n), Espacio O(1)
    
    Args:
    head (Nodo): Cabeza de la linked list a invertir
    
    Returns:
    head (Nodo): Cabeza de la linked list a invertir
    """
    previo = None
    actual = head
    while actual:
        siguiente = actual.siguiente
        actual.siguiente = previo
        previo = actual
        actual = siguiente
    return previo

def encontrar_medio(head):
    """Encuentra el punto medio de una linked list: Tiempo O(n), Espacio O(1)
    
    Args:
    head (Nodo): Cabeza de la linked list

    Returns:
    Nodo: Nodo medio de la linked list
    """
    lento = rapido = head
    while rapido and rapido.siguiente: # Comprobamos primero si existe el nodo actual y luego si existe el siguiente nodo
        lento = lento.siguiente
        rapido = rapido.siguiente.siguiente
    return lento

# Algoritmo de Floyd
def detectar_ciclo(head):
    """Determina si existe un bucle infinito dentro de la linked list o no: Tiempo O(n), Espacio O(1)
    
    Args:
    head (Nodo): Nodo inicial de la linked list

    Returns:
    Boolean: True (hay bucle infinito) / False (todo correcto)
    """
    lento = rapido = head
    while rapido and rapido.siguiente:
        lento = lento.siguiente
        rapido = rapido.siguiente.siguiente
        if rapido == lento: return True
    return False

# Para pasar a Tiempo O(1) deberíamos tener clase LinkedList tanto con self.head como con self.tail --> de este modo no perderíamos tiempo recorriendo listas (sacrificamos espacio por tiempo)
def unir_linked_lists(head1, head2):
    """Une dos linked lists: Tiempo O(n), Espacio O(1)
    
    Args:
    head1: Cabeza de la linked list 1
    head2: Cabeza de la linked list 2

    Returns:
    Nodo: Cabeza de la nueva linked list
    """
    if not detectar_ciclo(head1) and not detectar_ciclo(head2):
        if not head1: return head2
        if not head2: return head1      
        curr = encontrar_cola(head1)
        curr.siguiente = head2
        return head1

def unir_linked_lists_ordenadas(head1, head2):
    """Une dos linked lists de forma ordenada: Tiempo O(n), Espacio O(1)
    
    Args:
    head1: Cabeza de la linked list 1
    head2: Cabeza de la linked list 2

    Returns:
    Nodo: Cabeza de la nueva linked list
    """
    pass

# STACK (PILA) --> Operaciones Push y Pop O(1). Ejs de uso real: Ctrl+Z, Parsers, Call Stack

class Pila:
    """Pila con historial de mínimos"""
    def __init__(self):
        self.pila = []
        self.min_pila = [] # No podemos poner una variable porque cuando se elimina un elemento tendríamos que recorrer toda la pila de nuevo para encontrar el mínimo destruyendo el espacio O(1)
    
    def push(self, el):
        self.pila.append(el)

        # Gestión de min_pila
        if not self.min_pila or el <= self.min_pila[-1]: # Debe ser <=, sino al borrar el elemento se borraría de self.min_pila pero todavía quedaría un valor igual en self.pila
            self.min_pila.append(el)
    
    def pop(self):
        if not self.pila.is_empty():
            erased = self.pila.pop()

            # Gestión de min_pila
            if self.min_pila[-1] == erased:
                self.min_pila.pop()
        return None
    
    def peek(self):
        if not self.pila.is_empty():
            return self.pila[-1]
    
    def is_empty(self):
        return len(self.pila) == 0
    
    def get_min(self):
        return self.min_pila[-1]

    def show(self):
        print(self.pila)

# Base de los parsers de cualquier compilador
def analizador_sintactico(cadena):
    """Valida si los símbolos de una cadena están bien estructurados o no: Tiempo O(n), Espacio O(n)
    
    Args:
    cadena (str): Sentencia a analizar sintácticamente

    Returns:
    bool: True (Cadena es correcta) / False (Cadena NO es correcta)
    """
    pila = Pila()
    mapeo = {"{":"}", "[":"]", "(":")"}
    for c in cadena:
        if c in mapeo:
            pila.push(c)
        elif c in mapeo.values():
            if not pila.is_empty() and mapeo[pila.peek()] == c:
                pila.pop()
            else:
                return False
    return pila.is_empty()


# QUEUES (COLAS) --> Operaciones Enqueue y Dequeue O(1). Ejs de uso real: colas de impresión, servidores y peticiones web de usuarios, algoritmos de búsqueda en grafos
from collections import deque # No implementar cola con una lista ya que lista.pop(0), es O(n) ya que todos los elementos tienen que moverse un paso hacia la derecha --> deque O(1)
class Cola:
    """Cola eficiente"""
    def __init__(self):
        self.cola = deque()

    def enqueue(self, el): # O(1)
        self.cola.append(el)

    def dequeue(self): # O(1)
        if self.cola:
            self.cola.popleft()
        return None
    
    def show(self):
        print(self.cola)

class ColaDosPilas:
    """Implementación de cola usando 2 pilas"""
    def __init__(self):
        self.pilaEntrada = []
        self.pilaSalida = []
    
    def enqueue(self, el): # O(1)
        self.pilaEntrada.append(el)
    
    def dequeue(self): # O(n) --> Si se elimina un elemento se vuelca toda la self.pilaEntrada a la self.pilaSalida, aunque como cada elemento solo se vuelca una vez, el promedio de todas las operaciones es casi instantáneo, LO MALO DE VERDAD SERÍA HABERLO IMPLEMENTADO CON UNA SOLA LISTA
        if self.pilaEntrada:
            while self.pilaEntrada:
                self.pilaSalida.append(self.pilaEntrada.pop()) # ahora self.pilaSalida tiene el orden de los elementos invertidos --> LIFO -> FIFO
        
        return self.pilaSalida.pop() if self.pilaSalida else None



# TABLAS HASH / DICCIONARIOS (en python dict + set)
# función matemática convierte cada clave en hash, ordenador luego va directo ahí --> buscar, insertar, borrar O(1)
# --> a veces 2 claves diferentes dan mismo resultado matemático - colisión --> SOLUCIÓN: chaining, guardar ambas claves en mismo contenedor dentro de una linked list

def encontrar_objetivo(lista, objetivo):
    """Dada cualquier lista (no tiene por qué ser ordenada). Encuentra los índices de los 2 números que sumados dan el objetivo. Tiempo O(n), Espacio O(n)
    
    Args:
    lista (list): Lista inicial
    objetivo (int): Suma objetivo

    Return:
    tuple: Tupla de los 2 índices
    """
    if not lista: return None
    historial = {} # Diccionario almacena números ya vistos
    for i, num in enumerate(lista):
        resto = objetivo - num
        if resto in historial: return (historial[resto], i)
        historial[num] = i

def primer_caracter_norep(cadena):
    """Devuelve el primer caracter no repetido de una cadena. Tiempo O(n), Espacio O(k) k = número de caracteres distintos
    
    Args:
    cadena (str): Cadena a analizar

    Returns:
    str: Primer caracter no repetido
    """
    caracteres = {}
    for c in cadena:
        if not c in caracteres:
            caracteres[c] = 1
        else:
            caracteres[c] += 1
    
    for c in caracteres:
        if caracteres[c] == 1: return c
    return None

class LinkedList:
    """Implementación de linked list con puntero al último nodo"""
    def __init__(self):
        self.head = None
        self.tail = None # Logramos tiempo O(1)

    def append(self, node):
        if not self.head and not self.tail: self.head = self.tail = node
        else:
            self.tail.siguiente = node
            self.tail = node
        return self

    def append_lista(self, node_list):
        for n in node_list:
            self.append(n)
        return self
    
    def __repr__(self): # Cada objeto linked list se visualizará de este modo
        curr = self.head
        rep = []
        while curr:
            rep.append(str(curr.valor))
            curr = curr.siguiente
        return str(' -> '.join(rep))


class TablaHash:
    """Implementación de HashTable"""
    def __init__(self):
        self.HASH_TABLE_SIZE = 10 # Con solo 10 elementos provocamos colisiones como prueba
        self.tabla = [None] * self.HASH_TABLE_SIZE

    def _hash(self, cad):
        return hash(cad) % self.HASH_TABLE_SIZE

    def _check_clave(self, lista, clave):
        if not lista: return None
        curr = lista.head
        while curr:
            if curr.valor[0] == clave: return curr
            curr = curr.siguiente
        return None

    def put(self, clave, valor):
        index = self._hash(clave)
        lista_interna = self.tabla[index]
        if not lista_interna: self.tabla[index] = LinkedList().append(Nodo([clave, valor]))
        else:
            clave_existente = self._check_clave(lista_interna, clave)
            if clave_existente:
                clave_existente.valor[1] = valor
            else:
                lista_interna.append(Nodo([clave, valor]))

    def get(self, clave):
        lista_interna = self.tabla[self._hash(clave)]
        if lista_interna:
            curr_par = self._check_clave(lista_interna, clave)
            if curr_par: return curr_par.valor[1]
        return None

    def show(self):
        for i, cajon in enumerate(self.tabla):
            print(f"Cajón {i}: {cajon}")

def agrupar_anagramas(lista):
    """Agrupa una lista de palabras por anagramas:

    Tiempo O(n * k log k) (n=bucle for, k*logk=sorted()[timsort][k=letras de cada palabra]) --> no se abrevia a O(n) ya que hay que diferenciar constantes de variables/dimensiones, en este caso hay 2 variables que pueden crecer: el número de palabras (n) o el número de letras de cada palabra (k = segunda dimensión)
    - Constantes se ignoran, variables/dimensiones jamás
    SUMA: O(n + k): un proceso va después de otro
    MULTIPLICACIÓN O(n*k): un proceso va dentro de otro
    
    Espacio O(n)
    
    Args:
    lista (list): Lista de palabras

    Return:
    list[list]: Lista de anagramas
    """
    anagramas = {}
    for p in lista:
        clave = "".join(sorted(p))
        if not clave in anagramas:
            anagramas[clave] = []
        anagramas[clave].append(p)

    return list(anagramas.values())

# Memoización: almacenar resultados en caché para agilizar programa

def fibonacci_optimo(num):
    """Fibonacci óptimo pero no nos estaríamos beneficiando de la memoización, que permite no tener que recalcular resultados"""
    if num == 1: return 0
    if num == 2: return 1
    ini = 0
    sig = 1
    for _ in range(num-2):
        acc = ini + sig
        ini = sig
        sig = acc
    return acc

def fibonacci_memo(n, cache=None): # Como Python detecta llamadas a la misma función detecta diccionario anterior asociado, caché se comparte entre ejecuciones, si pusiéramos cache={}, la memoria se compartiría con las siguientes ejecuciones, para evitar eso ponemos cache=None y la inicializamos en cada ejecución externa nueva
    if not cache: cache = {}

    """Fibonacci con implementación manual de cache, la cache nos evita entrar en O(2^n) y nos deja O(n), ya que al ir almacenando valores en caché evitamos que el árbol de recursividad se abra por la derecha, todas las llamadas de la derecha, simplemente se convirtieron en llamada a la caché"""
    if n == 0: return 0
    if n == 1: return 1
    
    # Si ya lo calculamos en el subárbol izquierdo de la recursión, lo devolvemos de inmediato (O(1))
    if n in cache: return cache[n]
    
    # Si no, lo calculamos y lo guardamos en la cache
    cache[n] = fibonacci_memo(n - 1, cache) + fibonacci_memo(n - 2, cache)
    
    return cache[n]

# Método perfecto, caché optimizada
from functools import lru_cache

@lru_cache(maxsize=None) # Convierte la función en una Tabla Hash automática que va guardando resultados (optimizado en c --> constante de tiempo mucho menor)
def fibo(n):
    if n <= 1: return n
    return fibo(n-1) + fibo(n-2)


# ESTRUCTURAS DE DATOS NO LINEALES:
# ÁRBOLES: estructura jerárquica (raíz, ramas, nodos, hojas)
# ÁRBOLES BINARIOS: cada nodo tiene máximo 2 hijos.
# BST (Binary Search Tree): Arbol binario de búsqueda, hijos a la izquierda son menores, a la derecha mayores. Árbol totalmente equilibrado (mejor caso): O(log n), Árbol totalmente desequilibrado (peor caso): O(n) --> prácticamente una linked list

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

raiz = NodoArbol(3)


# Algoritmos DFS (Depth-First Search)
def arbol_in_order(nodo):
    """DFS In-Order

    Primero recorre todo el subárbol izquierdo, luego el nodo, luego el derecho
    
    Args:
    nodo (NodoArbol): Nodo raíz
    """
    if nodo:
        arbol_in_order(nodo.left)
        print(nodo.valor) # Cuando escribe los valores es a la vuelta de la recursión
        arbol_in_order(nodo.right)


def arbol_pre_order(nodo):
    """DFS Pre-Order
    
    Primero visita el nodo actual, luego baja por la izquierda, luego baja por la derecha

    Args:
    nodo (NodoArbol): Nodo raíz
    """
    if nodo:
        print(nodo.valor)
        arbol_pre_order(nodo.left)
        arbol_pre_order(nodo.right)

def arbol_post_order(nodo):
    """DFS Post-Order
    
    Visita ambos subárboles y finalmente el nodo

    Args:
    nodo (NodoArbol): Nodo raíz
    """
    if nodo:
        arbol_post_order(nodo.left)
        arbol_post_order(nodo.right)
        print(nodo.valor)

def obtener_altura(nodo):
    """Cuenta la altura de un árbol
    
    Args:
    nodo (NodoArbol): Nodo raíz

    Returns:
    int: Altura del árbol
    """
    if not nodo: return 0
    return 1 + max(obtener_altura(nodo.left),obtener_altura(nodo.left))

def contar_nodos(nodo):
    """Cuenta el número de nodos de un árbol
    
    Args:
    nodo (NodoArbol): Nodo raíz

    Returns:
    int: Número de nodos del árbol
    """
    if not nodo: return 0
    return 1 + contar_nodos(nodo.left) + contar_nodos(nodo.right) # Va sumando 1s según todas las ramas contadas, va todo a la izquierda primero antes de ir a la derecha

# Inserción de elementos en BST (Binary Search Tree)
def insertar_bst(nodo, valor):
    """Inserta un valor en un BST
    
    Args:
    nodo (NodoArbol): Nodo raíz del árbol
    valor (int): Valor numérico a insertar

    Returns:
    NodoArbol: Nodo raíz del árbol con el elemento insertado
    """
    if not nodo: return NodoArbol(valor)
    curr = nodo
    if valor < curr.valor:
        curr.left = insertar_bst(curr.left, valor)
    else:
        curr.right = insertar_bst(curr.right, valor)

    return curr # Cuando llega a un None en el que pueda insertar el nuevo valor, lo devuelve y lo inserta a la izquierda o derecha del elemento actual, luego rehace el árbol de vuelta

insertar_bst(raiz, 2)
insertar_bst(raiz, 6)
insertar_bst(raiz, 1)
insertar_bst(raiz, 0)

def buscar_arbol(nodo, valor):
    """Buscar un valor en un árbol
    
    Args:
    nodo (NodoArbol): Nodo raíz del árbol
    valor (int): Valor numérico a buscar
    Returns:
    NodoArbol: Elemento encontrado
    """
    if not nodo: return False
    if nodo.valor == valor: return True
    if valor < nodo.valor:
        return buscar_arbol(nodo.left, valor)
    else:
        return buscar_arbol(nodo.right, valor)


def arbol_bfs(nodo):
    """Algoritmo de BFS (Breadth-First Search)
    
    Args:
    nodo (NodoArbol): Nodo raíz del árbol
    """
    if not nodo: return
    cola = deque([nodo])
    while cola: # Mientras haya elementos en la cola
        nodo_actual = cola.popleft() # Eliminamos elemento de la cola y lo guardamos
        print(nodo_actual.valor)

        # Accedemos a los nodos hijos si existen y los metemos en la cola para luego ser procesados
        if nodo_actual.left: 
            cola.append(nodo_actual.left)
        if nodo_actual.right:
            cola.append(nodo_actual.right)



# ÁRBOLES BALANCEADOS: Altura de los subárboles izquierdo y derecho difiere como máximo en 1 unidad.
# - AVL: primeros en inventarse, diferencia máxima 1. Búsqueda ultrarápida, pero al modificar(insertar/borrar) se autorota muchas veces para mantener un equilibrio tan estricto.
# - RB (Red-Black): estándar de la industria, ninguna rama es el doble de otra. Equilibrio entre búsqueda y modificaciones
# - B/B+: sistemas de archivos y DB gigantes, cada nodo puede tener cientos de hijos

def calcular_factor_equilibrio(nodo):
    """Calcula el factor de equilibrio de un árbol binario
    
    De este modo sabemos si un árbol necesita una rotación o no

    Args:
    nodo (NodoArbol): Nodo raíz del árbol binario

    Returns:
    int: Factor de equilibrio del árbol
    """
    if not nodo: return 0
    return obtener_altura(nodo.right) - obtener_altura(nodo.left)

def rotar_derecha(nodo):
    """Rota a la derecha
    
    Args:
    nodo (NodoArbol): Nodo raíz del subárbol a balancear

    Returns:
    NodoArbol: Nuevo nodo raíz del subárbol balanceado
    """
    if not nodo: return None
    nueva_raiz = nodo.left
    t2 = nueva_raiz.right
    nueva_raiz.right = nodo
    nodo.left = t2
    return nueva_raiz

def rotar_izquierda(nodo):
    """Rota a la izquierda
    
    Args:
    nodo (NodoArbol): Nodo raíz del subárbol a balancear

    Returns:
    NodoArbol: Nuevo nodo raíz del subárbol balanceado
    """
    if not nodo: return None
    nueva_raiz = nodo.right
    t2 = nueva_raiz.left
    nueva_raiz.left = nodo
    nodo.right = t2
    return nueva_raiz

def insertar_avl(nodo, valor):
    """Inserta un valor en un árbol AVL
    
    1. Recorre recursivamente el árbol hasta encontrar el sitio (None) donde hay que insertar el valor
    2. Cuando llega ahí lo devuelve ya quedando insertado como hijo del nodo previo (nodo.left o nodo.right)
    3. Al volver hacia atrás por cada nodo recorrido calcula su factor de equilibrio
    4. Si hay algún tipo de desequilibrio lo corrige devolviendo el nuevo nodo padre y con el subárbol nuevamente balanceado, si no hay, simplemente devuelve el nodo actual ya que está perfecto

    Args:
    nodo (NodoArbol): Nodo raíz del árbol
    valor (int): Valor a insertar en el árbol

    Returns:
    NodoArbol: Nodo raíz del árbol rebalanceado y con el elemento insertado
    """
    if not nodo: return NodoArbol(valor)
    if valor < nodo.valor:
        nodo.left = insertar_avl(nodo.left, valor)
    elif valor > nodo.valor:
        nodo.right = insertar_avl(nodo.right, valor)
    else:
        print(f"Error: El valor {valor} ya existe.")
        return nodo
    
    fe = calcular_factor_equilibrio(nodo)
    
    # Desequilibrio LL
    if fe < -1 and valor < nodo.left.valor: # El que generó el desequilibrio es el nuevo valor insertado, ANTES EL ÁRBOL ESTABA PERFECTAMENTE BALANCEADO, si valor > nodo.left.valor el nuevo valor desequilibrador entró por la izquierda, se podría hacer mirando que fe < 0, pero hay que llamar a la función, lo ideal: que cada Nodo guardase su propia altura en self.height, pero esto también es eficiente
        return rotar_derecha(nodo)
    # Desequilibrio LR
    if fe < -1 and valor > nodo.left.valor:
        nodo.left = rotar_izquierda(nodo.left)
        return rotar_derecha(nodo)
    # Desequilibrio RR
    if fe > 1 and valor > nodo.right.valor:
        return rotar_izquierda(nodo)
    # Desequilibrio RL
    if fe > 1 and valor < nodo.right.valor:
        nodo.right = rotar_derecha(nodo.right)
        return rotar_izquierda(nodo)

    return nodo
    

# - HEAP: Dos tipos, el max-heap cada elemento padre siempre es mayor que sus hijos, min-heap, cada elemento padre siempre es menor que sus hijos --> utilización real en colas de prioridad

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _subir(self, i):
        """Subir a la posición correcta el elemento del heap que acabamos de insertar"""
        if i <= 0: return # Si el índice es 0 o "menor" ya no hay nada más que subir
        padre_i = (i - 1) // 2
        if self.heap[i] > self.heap[padre_i]:
            self.heap[i], self.heap[padre_i] = self.heap[padre_i], self.heap[i]
            self._subir(padre_i)

    def _bajar(self, i):
        """Bajar al elemento mas pequeño del heap mal posicionado
        
        Si el hijo mayor es mayor al elemento a bajar debemos intercambiarlos
        """
        heap_last_index = len(self.heap) - 1
        # Determinamos cuál es el hijo mayor:
        # 1. Vemos si existe el hijo 1: NO --> fuera, SI --> seguimos
        # 2. Vemos si existe el hijo 2 y es mayor que el hijo 1: SÍ --> valoramos intercambio contra hijo 2, NO --> valoramos intercambio contra hijo 1
        hijo_index = 2 * i + 1
        if heap_last_index < hijo_index: return
        if heap_last_index >= hijo_index + 1 and self.heap[hijo_index] < self.heap[hijo_index + 1]: hijo_index += 1

        if self.heap[hijo_index] > self.heap[i]:
            self.heap[i], self.heap[hijo_index] = self.heap[hijo_index], self.heap[i]
            self._bajar(hijo_index)

    def insertar(self, valor):
        """Insertar nuevo valor en el max heap
        Se inserta al final y luego se sube
        """
        if valor is None: return
        self.heap.append(valor)
        self._subir(len(self.heap) - 1)
    
    
    def extraer_maximo(self):
        """Extraer el elemento más grande del heap
        Se intercambia el máximo con el mínimo y se elimina el máximo, ahora hay que bajar el mínimo
        """
        if not self.heap: return
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        if len(self.heap) > 1: self.bajar(0)

    def mostrar(self):
        print(self.heap)

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