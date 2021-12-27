import unittest
from src import DiGraph
from src.DiGraph import DiGraph
from src import GraphAlgo
from GraphAlgo import GraphAlgo
class TestGraphAlgo(unittest.TestCase):
    def test_shortPath(self):
        graph = DiGraph()
        graph.add_node(0, (1, 0, 0))
        graph.add_node(1, (0, 0, 0))
        graph.add_node(2, (0, 1, 0))
        graph.add_node(3, (342, 1241, 32))
        graph.add_edge(0,1,10)
        graph.add_edge(0,2,0.1)
        graph.add_edge(2,3,1)
        graph.add_edge(3,1,1)
        algo=GraphAlgo(graph)
        ShortPath1=algo.shortest_path(0,1)
        self.assertEqual(ShortPath1[0],2.1)
        ans=[0,2,3,1]
        j=0
        for i in ans:
            self.assertEqual(i,ShortPath1[1][j])
            j=j+1
        ShortPath2=algo.shortest_path(3,0)
        self.assertEqual(len(ShortPath2[1]),0)
        self.assertEqual(ShortPath2[0],float('inf'))
        ShortPath3=algo.shortest_path(0,8)
        self.assertEqual(len(ShortPath3[1]),0)
        self.assertEqual(ShortPath3[0],float('inf'))
    def test_center(self):
        graph = DiGraph()
        graph.add_node(0, (1, 0, 0))
        graph.add_node(1, (0, 0, 0))
        graph.add_node(2, (0, 1, 0))
        graph.add_node(3, (342, 1241, 32))

        graph.add_edge(0, 3, 4)
        graph.add_edge(3, 2, 5)
        graph.add_edge(2, 1, 1)
        graph.add_edge(0, 2, 3)
        graph.add_edge(1, 2, 1)
        graph.add_edge(1, 0, 2.5)
        graph.add_edge(0, 1, 1)
        algo=GraphAlgo(graph)
        center=algo.centerPoint()
        # self.assertEqual(center[0],0)
        # self.assertEqual(center[1],4)
    def test_TSP(self):
        graph = DiGraph()
        graph.add_node(0, (1, 0, 0))
        graph.add_node(1, (0, 0, 0))
        graph.add_node(2, (0, 1, 0))
        graph.add_node(3, (342, 1241, 32))

        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 3, 4)
        graph.add_edge(1, 2, 1)
        graph.add_edge(2, 3, 2)
        algo=GraphAlgo(graph)
        tsp=algo.TSP([0,1,3])
        self.assertEqual(tsp[1],4)
    def test_save_load(self):
        graph1 = DiGraph()
        graph1.add_node(0, (1, 0, 0))
        graph1.add_node(1, (0, 0, 0))
        graph1.add_node(2, (0, 1, 0))
        graph1.add_node(3, (342, 1241, 32))

        graph1.add_edge(0, 3, 4)
        graph1.add_edge(3, 2, 5)
        graph1.add_edge(2, 1, 1)
        graph1.add_edge(0, 2, 3)
        graph1.add_edge(1, 2, 1)
        graph1.add_edge(1, 0, 2.5)
        graph1.add_edge(0, 1, 1)
        algo1=GraphAlgo(graph1)
        t=algo1.save_to_json("tal.json")
        self.assertTrue(t)
        graph2=DiGraph()
        algo2=GraphAlgo(graph2)
        self.assertTrue(algo2.load_from_json("tal.json"))
        for i in algo1.graph.v:
            self.assertTrue(algo1.graph.v[i].equal(algo2.graph.v[i]))
        for i in algo1.graph.outE:
            for j in algo1.graph.outE[i]:
                self.assertEqual(algo1.graph.outE[i][j],algo2.graph.outE[i][j])
    def test_plot(self):
        graph = DiGraph()
        algo=GraphAlgo(graph)
        algo.load_from_json("../data/A1.json")
        print(algo.v[0].getKey())
        algo.plot_graph()

