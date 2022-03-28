import networkx as nx

#Definir grafo  
grafo = nx.Graph() 

#Añadir nodos
grafo.add_node("Calle Madero")
grafo.add_node("Calle Francisco I. Madero")
grafo.add_nodes_from(["Av. 5 de Mayo", "Av. Independecia", "Calle Mina"])
 
#Añadir aristas
grafo.add_edge("Calle Madero", "Calle Francisco I. Madero")
grafo.add_edge("Calle Madero", "Av. 5 de Mayo")
grafo.add_edges_from([('Av. 5 de Mayo'),('Calle Francisco I. Madero','Calle Mina'),('Av. 5 de Mayo','Calle Mina')])

#Eliminar
grafo.remove_node('Calle Madero')

#Mostrar
print(grafo.nodes)

    
