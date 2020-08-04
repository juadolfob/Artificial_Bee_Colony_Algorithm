import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.simple_paths import all_simple_paths
from networkx.algorithms.tournament import hamiltonian_path


class ACO:
    def __init__(self, edges):
        self.G = nx.Graph()
        for edge in edges:
            self.G.add_edge(*edge[:2], length=edge[-1])

        # nodes
        nodes = self.G.number_of_nodes()
        source = "a"
        target = "a"
        cutoff = nodes

    def _offset_succsesor(self):
        pass

    def hamilton(self, source):
        starting_vertex = [vertex for vertex in self.G.edges if source in vertex]

        paths = []
        for vertex in starting_vertex:
            offset_source = vertex.index(source) + 1 % 2
            print(offset_source, ", ", vertex[offset_source])
            offset_paths = all_simple_paths(self.G, vertex[offset_source], source)  # "cicle" from offset
            print(offset_paths)
            paths.extend([[source,*path] for path in offset_paths])

        print([path for path in paths if len(path) == self.G.number_of_nodes()+1])

    def plot(self):
        elarge = [(u, v) for (u, v, d) in self.G.edges(data=True) if d['length'] > 0.5]
        esmall = [(u, v) for (u, v, d) in self.G.edges(data=True) if d['length'] <= 0.5]

        ## DRAW
        pos = nx.spring_layout(self.G)  # positions for all nodes

        nx.draw_networkx_nodes(self.G, pos, node_size=700)
        # edges
        nx.draw_networkx_edges(self.G, pos, edgelist=elarge,
                               width=6)
        nx.draw_networkx_edges(self.G, pos, edgelist=esmall,
                               width=6, alpha=0.5, edge_color='b', style='dashed')

        # labels
        nx.draw_networkx_labels(self.G, pos, font_size=20)

        plt.axis('off')
        plt.show()


network = [("a", "b", 2), ("a", "e", .1), ("a", "c", 1), ("b", "c", 1), ("b", "d", .4), ("c", "d", .7), ("c", "e", 5),
           ("d", "e", 8)]

colony = ACO(network)
colony.plot()
print(colony.hamilton("a"))
