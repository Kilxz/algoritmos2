from mylinkedlist import *

class AVLTree:
  root = None

class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None



#Ejercicio 1
"""
search(B,element)
Descripción: Busca un elemento en el TAD árbol.
Entrada: el árbol binario B en el cual se quiere realizar la búsqueda y el valor del elemento (element) a buscar.
Salida: Devuelve la key asociada a la primera instancia del elemento.
Devuelve None si el elemento no se encuentra.
"""

def search(B, element):
  return searchR(B.root, element)
  

def searchR(currentNode, element):
  if currentNode == None:
    return None
    
  if currentNode.value == element:
    return currentNode.key
    
  left = (searchR(currentNode.leftnode, element))
  if left != None:
    return left

  right = (searchR(currentNode.rightnode, element))
  if right != None:
    return right
    
  """
insertAVL(B,element,key)
Descripción: Inserta un elemento con una clave determinada del TAD
árbol binario. SIN MANTENER EL BALANCEO (PARA ESO UTILIZAR INSERT NORMAL).
Entrada: el árbol B sobre el cual se quiere realizar la inserción, el valor del elemento (element) a insertar y la clave
(key) con la que se lo quiere insertar.
Salida: Si pudo insertar con éxito devuelve la key donde se inserta el
elemento. En caso contrario devuelve None.
"""
  
def insertR(newNode, currentNode):
  if newNode.key > currentNode.key:
    if currentNode.rightnode == None:
      currentNode.rightnode = newNode
      newNode.parent = currentNode
      return newNode.key
    currentNode = currentNode.rightnode
    return insertR(newNode, currentNode)
  elif newNode.key < currentNode.key:
    if currentNode.leftnode == None:
      currentNode.leftnode = newNode
      newNode.parent = currentNode
      return newNode.key
    currentNode = currentNode.leftnode
    return insertR(newNode, currentNode)
  else:
    return None
    
def insertAVL(B, element, key):
  newNode = AVLNode()
  newNode.value = element
  newNode.key = key

  if B.root != None:
    return insertR(newNode, B.root)
  else:
    B.root = newNode
    return key
    
"""
deleteAVL(B,element)
Descripción: Elimina un elemento del TAD árbol binario. SIN MANTENER EL BALANCEO (PARA ESO UTILIZAR DELETE NORMAL).
Poscondición: Se debe desvincular el Node a eliminar.
Entrada: el árbol binario B sobre el cual se quiere realizar la
eliminación y el valor del elemento (element) a eliminar.
Salida: Devuelve clave (key) del elemento a eliminar. Devuelve None si
el elemento a eliminar no se encuentra.
"""

#Searchforelement y searchforminor buscan nodos utilizando recursividad que luego seran utilizados en la función delete
def searchforelement(currentNode, element):
  
  if currentNode == None:
    return None
    
  if currentNode.value == element:
    return currentNode
    
  left = (searchforelement(currentNode.leftnode, element))
  if left != None:
    return left

  right = (searchforelement(currentNode.rightnode, element))
  if right != None:
    return right

def searchforminor(currentNode):
  if currentNode.leftnode == None:
    if currentNode.rightnode != None:
      if currentNode.parent.leftnode == currentNode:
        currentNode.parent.leftnode = currentNode.rightnode
      else:
        currentNode.parent.leftnode = currentNode.rightnode
    else:
      if currentNode.parent.leftnode == currentNode:
        currentNode.parent.leftnode = None
      else:
        currentNode.parent.rightnode = None
    return currentNode
  else:
    return searchforminor(currentNode.leftnode)
    
def deleteAVL(B, element):
  node = searchforelement(B.root, element)
  if node != None:
    
    if (node.rightnode != None) and (node.leftnode != None):
      minornode= searchforminor(node.rightnode)
      if B.root == node:
        
        minornode.parent = None
        minornode.leftnode = B.root.leftnode
        minornode.rightnode = B.root.rightnode
        if minornode.rightnode != None:
          minornode.rightnode.parent = minornode
        if minornode.leftnode != None:
          minornode.leftnode.parent = minornode
        B.root = minornode

      else:
        if node.parent.rightnode == node:
          node.parent.rightnode = minornode
        if node.parent.leftnode == node:
          node.parent.leftnode = minornode
        minornode.parent = node.parent
        minornode.leftnode = node.leftnode
        minornode.rightnode = node.rightnode
        if node.leftnode != None:
          node.leftnode.parent = minornode
        if node.rightnode != None:
          node.rightnode.parent = minornode
        
    elif (node.rightnode == None) and (node.leftnode == None):

      if B.root == node:
        B.root = None
      else:
        
        if node.parent.leftnode == node:
          node.parent.leftnode = None
        else:
          node.parent.rightnode = None

    elif (node.rightnode == None) or (node.leftnode == None):
      if B.root == node:
        if B.root.rightnode != None:
          B.root = B.root.rightnode
          B.root.parent = None
        else:
          B.root = B.root.leftnode
          B.root.parent = None
      else:
        
        if node.parent.rightnode == node:
          if node.rightnode != None:
            node.parent.rightnode = node.rightnode
            node.parent.rightnode.parent = node.parent
          else:
            node.parent.rightnode = node.leftnode
            node.parent.rightnode.parent = node.parent
        else:
          if node.rightnode != None:
            node.parent.leftnode = node.rightnode
            node.parent.leftnode.parent = node.parent
          else:
            node.parent.leftnode = node.leftnode
            node.parent.leftnode.parent = node.parent
    return node.key
  else:
    return None

"""
deleteKey(B,key)
Descripción: Elimina una clave del TAD árbol binario.
Poscondición: Se debe desvincular el Node a eliminar.
Entrada: el árbol binario B sobre el cual se quiere realizar la
eliminación y el valor de la clave (key) a eliminar.
Salida: Devuelve clave (key) a eliminar. Devuelve None si el elemento
a eliminar no se encuentra.
"""
#Utilizando recursividad, searchnode busca el nodo con la key indicada.
def searchnode(currentNode, key):
  
  if currentNode == None:
    return None
  if currentNode.key == key: 
    return currentNode
  else:
    if key > currentNode.key:
      return searchnode(currentNode.rightnode, key)
    else:
      return searchnode(currentNode.leftnode, key)

def deleteKey(B, key):
  node = searchnode(B.root, key)

  if node != None:
    
    if (node.rightnode != None) and (node.leftnode != None):
      minornode= searchforminor(node.rightnode)
      if B.root == node:
        
        minornode.parent = None
        minornode.leftnode = B.root.leftnode
        minornode.rightnode = B.root.rightnode
        minornode.rightnode.parent = minornode
        minornode.leftnode.parent = minornode
        B.root = minornode

      else:

        if node.parent.rightnode == node:
          node.parent.rightnode = minornode
        if node.parent.leftnode == node:
          node.parent.leftnode = minornode
        minornode.parent = node.parent
        
        minornode.leftnode = node.leftnode
        minornode.rightnode = node.rightnode
        if node.leftnode != None:
          node.leftnode.parent = minornode
        if node.rightnode != None:
          node.rightnode.parent = minornode
    elif (node.rightnode == None) and (node.leftnode == None):
      if B.root == node:
        B.root = None
      else:
        
        if node.parent.leftnode == node:
          node.parent.leftnode = None
        else:

          node.parent.rightnode = None

          
    elif (node.rightnode == None) or (node.leftnode == None):
      if B.root == node:
        if B.root.rightnode != None:
          B.root = B.root.rightnode
          B.root.parent = None
        else:
          B.root = B.root.leftnode
          B.root.parent = None
      else:
        if node.parent.rightnode == node:
          if node.rightnode != None:
            node.parent.rightnode = node.rightnode
            node.parent.rightnode.parent = node.parent
          else:
            node.parent.rightnode = node.leftnode
            node.parent.rightnode.parent = node.parent
        else:
          if node.rightnode != None:
            node.parent.leftnode = node.rightnode
            node.parent.leftnode.parent = node.parent
          else:
            node.parent.leftnode = node.leftnode
            node.parent.leftnode.parent = node.parent
    return key
    
  else:
    return None

"""
access(B,key)
Descripción: Permite acceder a un elemento del árbol binario con una
clave determinada.
Entrada: El árbol binario y la key del elemento al cual
se quiere acceder.
Salida: Devuelve el valor de un elemento con una key del árbol
binario, devuelve None si no existe elemento con dicha clave.
"""
  
def accessR(key, currentNode):
  if currentNode == None:
    return None
  if key > currentNode.key:
    currentNode = currentNode.rightnode
    return accessR(key, currentNode)
  elif key < currentNode.key:
    currentNode = currentNode.leftnode
    return accessR(key, currentNode)
  else:
    return currentNode.value

def access(B, key):
  return accessR(key, B.root)
  
"""
update(L,element,key)
Descripción: Permite cambiar el valor de un elemento del árbol binario
con una clave determinada.
Entrada: El árbol binario y la clave (key) sobre la cual
se quiere asignar el valor de element.
Salida: Devuelve None si no existe elemento para dicha clave. Caso
contrario devuelve la clave del nodo donde se hizo el update.
"""

def updateR(key, currentNode, element):
  if currentNode == None:
    return None
  if key > currentNode.key:
    currentNode = currentNode.rightnode
    return updateR(key, currentNode,element)
  elif key < currentNode.key:
    currentNode = currentNode.leftnode
    return updateR(key, currentNode, element)
  else:
    currentNode.value = element
    return currentNode.key

def update(L, element, key):
  return updateR(key, L.root, element)

#Ejercicio 2
  
#Función auxiliar para insertar nodos al final de una lista. Utilizada a la hora de realizar las listas en las funciones con los recorridos de los arboles
def addatend(L, element):
  if L.head == None:
    newNode = Node()
    L.head = newNode
    L.head.value = element
  else:
    currentNode = L.head
    while currentNode != None:
      if currentNode.nextNode == None:
        newNode = Node()
        currentNode.nextNode = newNode
        newNode.value = element
        return element
      currentNode = currentNode.nextNode
      
"""
traverseInOrder(B)
Descripción: Recorre un árbol binario en orden
Entrada: El árbol binario
Salida: Devuelve una lista (LinkedList) con los elementos del árbol en
orden. Devuelve None si el árbol está vacío.
"""

def traverseInOrder(B):
  if B.root == None:
    return None
  L = LinkedList()
  return traverseInOrderR(L, B.root)

def traverseInOrderR(L, currentNode):
  if currentNode == None:
    return None
    
  traverseInOrderR(L, currentNode.leftnode)
  addatend(L, currentNode.value)
  traverseInOrderR(L, currentNode.rightnode)
  return L
  
"""
traverseInPostOrder(B)
Descripción: Recorre un árbol binario en post-orden
Entrada: El árbol binario 
Salida: Devuelve una lista (LinkedList) con los elementos del árbol en
post-orden. Devuelve None si el árbol está vacío.
"""
def traverseInPostOrder(B):
  if B.root == None:
    return None
  L = LinkedList()
  return traverseInPostOrderR(L, B.root)
  
def traverseInPostOrderR(L, currentNode):

  if currentNode == None:
    return None
    
  traverseInPostOrderR(L, currentNode.leftnode)
  traverseInPostOrderR(L, currentNode.rightnode)
  addatend(L, currentNode.value)
  return L
  
"""
traverseInPreOrder(B)
Descripción: Recorre un árbol binario en pre-orden
Entrada: El árbol binario 
Salida: Devuelve una lista (LinkedList) con los elementos del árbol en
pre-orden. Devuelve None si el árbol está vacío.
"""

def traverseInPreOrder(B):
  if B.root == None:
    return None
  L = LinkedList()
  return traverseInPreOrderR(L, B.root)
  
def traverseInPreOrderR(L, currentNode):
  if currentNode == None:
    return None
  addatend(L, currentNode.value)
  left = traverseInPreOrderR(L, currentNode.leftnode)
  right = traverseInPreOrderR(L, currentNode.rightnode)
  if right == None:
    return L

"""
traverseBreadFirst(B)
Descripción: Recorre un árbol binario en modo primero anchura/amplitud
Entrada: El árbol binario
Salida: Devuelve una lista (LinkedList) con los elementos del árbol
ordenados de acuerdo al modo primero en amplitud. Devuelve None si el
árbol está vacío.
"""

def traverseBreadFirst(B):
  if B.root == None:
    return None
  L = LinkedList()
  addatend(L, B.root.value)
  return traverseBreadFirstR(L, B.root)
  
def traverseBreadFirstR(L, currentNode):
  if currentNode == None:
    return None
    
  if currentNode.leftnode != None:
    addatend(L, currentNode.leftnode.value)
  if currentNode.rightnode != None:
    addatend(L, currentNode.rightnode.value)
  traverseBreadFirstR(L, currentNode.leftnode)
  traverseBreadFirstR(L, currentNode.rightnode)
  return L


#Función para calcular la altura del árbol
def height(currentNode):
  if currentNode == None:
    return 0
  else:
    Lheight = height(currentNode.leftnode)
    Rheight = height(currentNode.rightnode)

    if Lheight > Rheight: 
      return Lheight + 1
    else:
      return Rheight + 1
    
#TP 2 DE ALGORITMOS 2 

"""
Descripción: Actualiza los bf de los nodos a partir de un nodo, hasta la raíz del árbol.
"""
def update_bf(AVLTree, currentNode):
  currentNode.bf = height(AVLNode.leftnode) - height(AVLNode.rightnode)
  if currentNode.bf == AVLTree.root:
    return AVLTree
  else:
    update_bf(AVLTree, currentNode.parent)

#Ejercicio 1
"""
Descripción: Implementa la operación rotación a la izquierda 
Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  izquierda
Salida: retorna la nueva raíz
"""
def rotateLeft(Tree, avlnode):

#Caso si el nodo es la raíz de todo el árbol
  if Tree.root == avlnode:
    Tree.root = avlnode.rightnode
    Tree.root.parent = None
    if Tree.root.leftnode != None:
      avlnode.rightnode = Tree.root.leftnode
      Tree.root.leftnode.parent = avlnode
    else:
      avlnode.rightnode = None
    Tree.root.leftnode = avlnode
    avlnode.parent = Tree.root
    return Tree.root
    
  #Verifico si el nodo esta a la derecha o a la izquierda del padre
  if avlnode.parent.rightnode == avlnode:
    padreHijo = "right"
  else:
    padreHijo = "left"

  #Inserto la nueva raiz dependiendo de PadreHijo
    avlnode.rightnode.parent = avlnode.parent
  if padreHijo == "right":
    avlnode.parent.rightnode = avlnode.rightnode
  else:
    avlnode.parent.leftnode = avlnode.rightnode
  #Si tiene hijo izquierdo, pasa a ser el hijo derecho de la antigua raiz. Posteriormente, la antigua raiz se inserta a la izquierda de la nueva raíz.
  newRoot = avlnode.rightnode
  if newRoot.leftnode != None:
    avlnode.rightnode = newRoot.leftnode
    newRoot.leftnode.parent = avlnode
  else:
    avlnode.rightnode = None
  newRoot.leftnode = avlnode
  avlnode.parent = newRoot
  return newRoot

"""
Descripción: Implementa la operación rotación a la derecha 
Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  derecha
Salida: retorna la nueva raíz
"""

def rotateRight(Tree, avlnode):
#Caso si el nodo es la raíz de todo el árbol
  if Tree.root == avlnode:
    Tree.root = avlnode.leftnode
    Tree.root.parent = None
    if Tree.root.rightnode != None:
      avlnode.leftnode = Tree.root.rightnode
      Tree.root.rightnode.parent = avlnode
    else:
      avlnode.leftnode = None
    Tree.root.rightnode = avlnode
    avlnode.parent = Tree.root
    return Tree.root
    
  #Verifico si el nodo esta a la derecha o a la izquierda del padre
  if avlnode.parent.rightnode == avlnode:
    padreHijo = "right"
  else:
    padreHijo = "left"

  #Inserto la nueva raiz dependiendo de PadreHijo
    avlnode.leftnode.parent = avlnode.parent
  if padreHijo == "right":
    avlnode.parent.rightnode = avlnode.leftnode
  else:
    avlnode.parent.leftnode = avlnode.leftnode
  #Si tiene hijo derecho, pasa a ser el hijo izquierdo de la antigua raiz. Posteriormente, la antigua raiz se inserta a la derecha de la nueva raíz.
  newRoot = avlnode.leftnode
  if newRoot.rightnode != None:
    avlnode.leftnode = newRoot.rightnode
    newRoot.rightnode.parent = avlnode
  else:
    avlnode.leftnode = None
  newRoot.rightnode = avlnode
  avlnode.parent = newRoot
  return newRoot

#Ejercicio2
"""
calculateBalance(AVLTree) 
Descripción: Calcula el factor de balanceo de un árbol binario de búsqueda. 
Entrada: El árbol AVL  sobre el cual se quiere operar.
Salida: El árbol AVL con el valor de balanceFactor para cada subarbol

"""
def calculateBalance(AVLTree):
  return calculateBalanceR(AVLTree, AVLTree.root)

def calculateBalanceR(AVLTree, AVLNode):
  if AVLNode == None:
    return None
  
  AVLNode.bf = height(AVLNode.leftnode) - height(AVLNode.rightnode)

  calculateBalanceR(AVLTree, AVLNode.leftnode)
  calculateBalanceR(AVLTree, AVLNode.rightnode)
  return AVLTree


#Ejercicio 3
"""
reBalance(AVLTree) 
Descripción: balancea un árbol binario de búsqueda. Para esto se deberá primero 
calcular el balanceFactor del árbol y luego en función de esto aplicar la estrategia de rotación que corresponda.
Entrada: El árbol binario de tipo AVL  sobre el cual se quiere operar.
Salida: Un árbol binario de búsqueda balanceado. Es decir luego de esta operación se cumple 
que la altura (h) de su subárbol derecho e izquierdo difieren a lo sumo en una unidad.

"""

#Se recorre el árbol verificando los bf
def recorrerBf(AVLNode):
  
  if (AVLNode == None):
    return None
  
  if (abs(AVLNode.bf) != 1) and (AVLNode.bf != 0):
    return AVLNode

  
  left = recorrerBf(AVLNode.leftnode)
  if left != None:
    return left
  right = recorrerBf(AVLNode.rightnode)
  if right != None:
    return right
  return None

def reBalanceR(AVLTree, AVLNode):
  if (AVLNode.bf < -1):
    if AVLNode.rightnode != None:
      if AVLNode.rightnode.bf > 0:
        rotateRight(AVLTree, AVLNode.rightnode)
    rotateLeft(AVLTree, AVLNode)
  else:
    if (AVLNode.bf > 1):
      if AVLNode.leftnode != None:
        if AVLNode.leftnode.bf < 0:
          rotateLeft(AVLTree, AVLNode.leftnode)
      rotateRight(AVLTree, AVLNode)
  return AVLTree
      
def reBalance(AVLTree):
  AVLTree = calculateBalance(AVLTree)
  bfVerification = recorrerBf(AVLTree.root)
  if bfVerification != None:
    reBalanceR(AVLTree, bfVerification)
    reBalance(AVLTree)
  return AVLTree


#EJERCICIO 4
"""
Implementar la operación insert() en  el módulo avltree.py garantizando que el árbol 
binario resultante sea un árbol AVL. 
"""
def updateBfAndFix(AVLTree, AVLNode):
  AVLNode.bf = height(AVLNode.leftnode) - height(AVLNode.rightnode)

  if (AVLNode.bf < -1):
    if AVLNode.rightnode != None:
      if AVLNode.rightnode.bf > 0:
        rotateRight(AVLTree, AVLNode.rightnode)
    rotateLeft(AVLTree, AVLNode)
  else:
    if (AVLNode.bf > 1):
      if AVLNode.leftnode != None:
        if AVLNode.leftnode.bf < 0:
          rotateLeft(AVLTree, AVLNode.leftnode)
      rotateRight(AVLTree, AVLNode)

  if AVLNode == AVLTree.root:
    return AVLTree
  else:
    updateBfAndFix(AVLTree, AVLNode.parent)
  return AVLTree

def insertR(newNode, currentNode):
  if newNode.key > currentNode.key:
    if currentNode.rightnode == None:
      currentNode.rightnode = newNode
      newNode.parent = currentNode
      return newNode.key
    currentNode = currentNode.rightnode
    return insertR(newNode, currentNode)
  elif newNode.key < currentNode.key:
    if currentNode.leftnode == None:
      currentNode.leftnode = newNode
      newNode.parent = currentNode
      return newNode.key
    currentNode = currentNode.leftnode
    return insertR(newNode, currentNode)
  else:
    return None
    
def insert(AVLTree, element, key):
  newNode = AVLNode()
  newNode.value = element
  newNode.key = key

  if AVLTree.root != None:
    key = insertR(newNode, AVLTree.root)
  else:
    AVLTree.root = newNode
    newNode.bf = 0
    return key
  
  if key != None:
    updateBfAndFix(AVLTree, newNode)
  return key

#EJERCICIO 5
"""
Implementar la operación delete() en  el módulo avltree.py garantizando que el árbol 
binario resultante sea un árbol AVL.
"""

#Searchforelement y searchforminor buscan nodos utilizando recursividad que luego seran utilizados en la función delete
def searchforelement(currentNode, element):
  
  if currentNode == None:
    return None
    
  if currentNode.value == element:
    return currentNode
    
  left = (searchforelement(currentNode.leftnode, element))
  if left != None:
    return left

  right = (searchforelement(currentNode.rightnode, element))
  if right != None:
    return right

def searchforminor(currentNode):
  if currentNode.leftnode == None:
    if currentNode.rightnode != None:
      if currentNode.parent.leftnode == currentNode:
        currentNode.parent.leftnode = currentNode.rightnode
      else:
        currentNode.parent.leftnode = currentNode.rightnode
    else:
      if currentNode.parent.leftnode == currentNode:
        currentNode.parent.leftnode = None
      else:
        currentNode.parent.rightnode = None
    return currentNode
  else:
    return searchforminor(currentNode.leftnode)
    
def delete(AVLTree, element):
  node = searchforelement(AVLTree.root, element)
  if node != None:
    
    if (node.rightnode != None) and (node.leftnode != None):
      minornode= searchforminor(node.rightnode)
      if AVLTree.root == node:
        
        minornode.parent = None
        minornode.leftnode = AVLTree.root.leftnode
        minornode.rightnode = AVLTree.root.rightnode
        if minornode.rightnode != None:
          minornode.rightnode.parent = minornode
        if minornode.leftnode != None:
          minornode.leftnode.parent = minornode
        AVLTree.root = minornode

      else:
        if node.parent.rightnode == node:
          node.parent.rightnode = minornode
        if node.parent.leftnode == node:
          node.parent.leftnode = minornode
        minornode.parent = node.parent
        minornode.leftnode = node.leftnode
        minornode.rightnode = node.rightnode
        if node.leftnode != None:
          node.leftnode.parent = minornode
        if node.rightnode != None:
          node.rightnode.parent = minornode
        
    elif (node.rightnode == None) and (node.leftnode == None):

      if AVLTree.root == node:
        AVLTree.root = None
      else:
        
        if node.parent.leftnode == node:
          node.parent.leftnode = None
        else:
          node.parent.rightnode = None

    elif (node.rightnode == None) or (node.leftnode == None):
      if AVLTree.root == node:
        if AVLTree.root.rightnode != None:
          AVLTree.root = AVLTree.root.rightnode
          AVLTree.root.parent = None
        else:
          AVLTree.root = AVLTree.root.leftnode
          AVLTree.root.parent = None
      else:
        
        if node.parent.rightnode == node:
          if node.rightnode != None:
            node.parent.rightnode = node.rightnode
            node.parent.rightnode.parent = node.parent
          else:
            node.parent.rightnode = node.leftnode
            node.parent.rightnode.parent = node.parent
        else:
          if node.rightnode != None:
            node.parent.leftnode = node.rightnode
            node.parent.leftnode.parent = node.parent
          else:
            node.parent.leftnode = node.leftnode
            node.parent.leftnode.parent = node.parent
    updateBfAndFix(AVLTree, node.parent)
    return node.key
  else:
    return None