# Impresión de todos lo elementos
# Al no ser repetidos y ser inmutables
my_set = {3, 4, 5}
print(my_set)

# Impresión de los elementos ignorando el orden de inicialización
my_set2 = {'Hola', 23.3, False, True}
print(my_set2)

# Impresión de los elementos ignorando los repetidos
my_set3 = {3, 3, 2}
print(my_set3)

# Impresión con error al inicializar el set con un elemento mutable(lista)
my_set4 = {[1, 2, 3], 4}
print(my_set4)


# Inicialización de un diccionario
my_set = {} # Por defecto Python creará un diccionario vacío
print(type(my_set))
# Inicialización de un set
my_set = set()
print(type(my_set))

# Haciendo cast desde y hacía un set
my_list = [1, 1, 2, 3, 4, 4, 5]
my_set = set(my_list)
print(my_set)
# {1,2,3,4,5}

my_tuple = ('Hola', 'Hola', 'Hola', 1)
my_set = set(my_tuple)
print(my_set)
# {'Hola', 1}


# Añadir elementos a un set
my_set = {1, 2, 3}
print(my_set)
# {1, 2, 3}

my_set.add(4)
print(my_set)
# {1, 2, 3, 4}

my_set.update([1, 2, 5])
print(my_set)
# {1, 2, 3, 4, 5}

my_set.update((1, 7, 8), {6})
print(my_set)
# {1, 2, 3, 4, 5, 6, 7, 8}


# Quitar o remover elementos de un set
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(my_set)
# {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Descartar si existe el elemento 1
my_set.discard(1)
print(my_set)
# {2, 3, 4, 5, 6, 7, 8, 9}

# Quitar estrictamente el elemento 2
my_set.remove(2)
print(my_set)
# {3, 4, 5, 6, 7, 8, 9}

# Descartar un elemento inexistente
my_set.discard(10)
print(my_set)
# {3, 4, 5, 6, 7, 8, 9}

# Remover un elemento inexistente
my_set.discard(10)
print(my_set)
# KeyError

# Operando con Sets
# Unión
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
my_set3 = my_set1 | my_set2
# Alternativamente my_set3 = my_set1.union(my_set2)
print(my_set3)
# {1, 2, 3, 4, 5}

# Intersección
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
my_set3 = my_set1 & my_set2
# Alternativamente my_set3 = my_set1.intersection(my_set2)
print(my_set3)
# {3}

# Diferencia
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}
my_set3 = my_set1 - my_set2
# Alternativamente my_set3 = my_set1.difference(my_set2)
print(my_set3)
# {3, 4}
my_set3 = my_set2 - my_set1
print(my_set3)
# {6, 7}

# Diferencia simétrica
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}
my_set3 = my_set1 ^ my_set2
# Alternativamente my_set3 = my_set1.symmetric_difference(my_set2)
print(my_set3)