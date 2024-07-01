import copy

import networkx as nx

from database.DAO import DAO
from database.DB_connect import DBConnect


class Model:
    def __init__(self):
        self.grafo = nx.Graph()

    def creaGrafo(self, squadra):
        self.grafo.clear()
        nodi = DAO.getAnni(squadra)
        self.grafo.add_nodes_from(nodi)

        archi = DAO.getArchi(squadra)
        for arco in archi:
            self.grafo.add_edge(arco[0], arco[1], weight=arco[2])
        for nodo1 in self.grafo.nodes:
            for nodo2 in self.grafo.nodes:
                if not self.grafo.has_edge(nodo1, nodo2):
                    self.grafo.add_edge(nodo1, nodo2, weight=0)
        return nodi

    def grafoDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)

    def getDettagli(self, anno):
        ris = []
        for nodo in self.grafo.neighbors(anno):
            ris.append([anno, nodo, self.grafo[anno][nodo]["weight"]])
        ris.sort(key=lambda x: x[2], reverse=True)
        return ris