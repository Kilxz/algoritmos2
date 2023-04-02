from trie import *
import trieLinkedList

def ImprimirLetra(T, letra):
    inicio = searchInL(letra)
    print(inicio.key)
    while inicio != None:
        inicio = inicio.head.value
        print(inicio.key)
        print("isEndOfWord?", inicio.isEndOfWord)
        inicio = inicio.children
    return

T = Trie()

#CASOS DE PRUEBA PARA TRIE CON LISTAS DE PHYTON
print("-_-_-_-_- TRIE CON LISTAS DE PYTHON -_-_-_-_- ")
print("=========== PRUEBA Insert una palabra =========== ")
insert(T, "Aps")
print("Inserto aps")
print(T.root)
print(T.root[0].key)
print(T.root[0].children[0].key)
print(T.root[0].children[0].children[0].key)

print(" ")
print("=========== PRUEBA Insert dos palabras =========== ")
insert(T, "App")
print("Inserto App")
print(T.root)
print(T.root[0].key)
print(T.root[0].children[0].key)
print(T.root[0].children[0].children[1].key)

print(" ")
print("=========== PRUEBA isEndOfWord =========== ")
insert(T, "a")
print("Inserto a")
print(T.root[1].isEndOfWord)
print(T.root[0].children[0].isEndOfWord)

print(" ")
print("=========== PRUEBA search =========== ")

print("Busco a")
print(search(T, "a"))
print(" ")

print("Busco ap")
print(search(T, "ap"))
print(" ")

print("Busco app")
print(search(T, "app"))
print(" ")

print("Busco aps")
print(search(T, "aps"))
print(" ")

print("Busco App")
print(search(T, "App"))
print(" ")

print("Busco Aps")
print(search(T, "Aps"))
print(" ")

print(" ")
print("=========== PRUEBA delete =========== ")
print("Inserto temaiken, tema y te")
insert(T, "temaiken")
insert(T, "tema")
insert(T, "te")

print(" ")
print(" Delete de temaiken ")
print(delete(T, "temaiken"))

print(" ")
print("Encuentro te?")
print(search(T, "te"))
print("Encuentro tema?")
print(search(T, "tema"))
print("Encuentro temaiken?")
print(search(T, "temaiken"))

print(" ")
print("Inserto lodo y lodoso")
insert(T, "lodo")
insert(T, "lodoso")
print("Encuentro lodo?")
print(search(T, "lodo"))
print("Encuentro lodoso?")
print(search(T, "lodoso"))
delete(T, "lodo")
print("Despues del delete de lodo")
print("Encuentro lodo?")
print(search(T, "lodo"))
print("Encuentro lodoso?")
print(search(T, "lodoso"))

T = None
T = Trie()

#CASOS DE PRUEBA PARA TRIE CON LINKEDLIST
print(" ")
print("-_-_-_-_- TRIE CON LINKEDLISTS -_-_-_-_- ")
print("=========== PRUEBA Insert una palabra =========== ")
trieLinkedList.insert(T, "Aps")
print("Inserto Aps")
print(T.root)
print(T.root.head.value.key)
print(T.root.head.value.children.head.value.key)
print(T.root.head.value.children.head.value.children.head.value.key)

print(" ")
print("=========== PRUEBA Insert dos palabras =========== ")
trieLinkedList.insert(T, "App")
print("Inserto App")
print(T.root)
print(T.root.head.value.key)
print(T.root.head.value.children.head.value.key)
print(T.root.head.value.children.head.value.children.head.value.key)

print(" ")
print("=========== PRUEBA isEndOfWord =========== ")
trieLinkedList.insert(T, "a")
print("Inserto a")
print(T.root.head.value.key)
print(T.root.head.value.isEndOfWord)
print(T.root.head.nextNode.value.isEndOfWord)
print(T.root.head.nextNode.value.children.head.value.isEndOfWord)

print(" ")
print("=========== PRUEBA search =========== ")

print("Busco a")
print(trieLinkedList.search(T, "a"))
print(" ")

print("Busco ap")
print(trieLinkedList.search(T, "ap"))
print(" ")

print("Busco Ap")
print(trieLinkedList.search(T, "Ap"))
print(" ")

print("Busco app")
print(trieLinkedList.search(T, "app"))
print(" ")

print("Busco App")
print(trieLinkedList.search(T, "App"))
print(" ")

print("Busco Aps")
print(trieLinkedList.search(T, "Aps"))
print(" ")

print(" ")
print("=========== PRUEBA delete =========== ")
print("Inserto temaiken, tema y te")
trieLinkedList.insert(T, "temaiken")
trieLinkedList.insert(T, "tema")
trieLinkedList.insert(T, "te")

print(" ")
print("Delete de temaiken ")
print(trieLinkedList.delete(T, "temaiken"))

print(" ")
print("Encuentro te?")
print(trieLinkedList.search(T, "te"))
print("Encuentro tema?")
print(trieLinkedList.search(T, "tema"))
print("Encuentro temaiken?")
print(trieLinkedList.search(T, "temaiken"))

print(" ")
print("Inserto lodo y lodoso")
trieLinkedList.insert(T, "lodo")
trieLinkedList.insert(T, "lodoso")
print("Encuentro lodo?")
print(trieLinkedList.search(T, "lodo"))
print("Encuentro lodoso?")
print(trieLinkedList.search(T, "lodoso"))
trieLinkedList.delete(T, "lodo")
print("Despues del delete de lodo")
print("Encuentro lodo?")
print(trieLinkedList.search(T, "lodo"))
print("Encuentro lodoso?")
print(trieLinkedList.search(T, "lodoso"))
