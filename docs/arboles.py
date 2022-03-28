class Arbol(object):
  def __init__(self):
    self.der = None    
    self.izq  = None   
    self.dato  = None  
    
#Definir árbol    
raiz = Arbol()

#Agregar
raiz.dato = 'Raiz'
raiz.izq = Arbol()
raiz.izq.dato = 'Izquierda'
raiz.der = Arbol()
raiz.der.dato = 'Derecha'
raiz.izq.izq = Arbol()
raiz.izq.izq.dato = 'Izquierda 2'
raiz.izq.der = Arbol()
raiz.izq.der.dato = 'Izquierda - Derecha'

#Editar
raiz.izq.izq.dato = 'Segunda Izquierda'

#Eliminar
raiz.der = None

#Mostrar
print(raiz.izq.dato)
print(raiz.izq.izq.dato)