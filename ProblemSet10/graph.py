class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)

class WeightedEdge(Edge):
    def __init__(self, src, dest, total_weight = 1.0, outdoor_weight = 1.0):
        self.src = src
        self.dest = dest
        self.total_weight = total_weight
        self.outdoor_weight = outdoor_weight
    def getTotalDistance(self):
        return self.total_weight
    def getOutdoorDistance(self):
        return self.outdoor_weight
    def __str__(self):
        return str(self.src) + '->' + str(self.dest) + ' (' + str(self.total_weight) + ', ' + str(self.outdoor_weight) +')'

class Digraph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

class WeightedDigraph(Digraph):
    def addEdge(self, edge):
        s = float(edge.getTotalDistance())
        o = float(edge.getOutdoorDistance())
        source = edge.getSource()
        dest = edge.getDestination()
        if not(source in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[source].append([dest, (s, o)])
             
    def childrenOf(self, node):
        r = []
        for k in self.edges[node]:
            n = k[0].getName()
            r.append(n)    
        return r
    
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d[0]) +  ' ' + str(d[1]) + '\n'
        return res[:-1]
        
 
    

def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result

##
##nh = Node('h')
##nj = Node('j')
##nk = Node('k')
##nm = Node('m')
##ng = Node('g')
##
##g = WeightedDigraph()
##g.addNode(nh)
##g.addNode(nj)
##g.addNode(nk)
##g.addNode(nm)
##g.addNode(ng)
##
##randomEdge = WeightedEdge(nh, nk, 10, 8)
##g.addEdge(randomEdge)
##randomEdge = WeightedEdge(nk, nj, 26, 12)
##g.addEdge(randomEdge)
##randomEdge = WeightedEdge(nm, nk, 65, 22)
##g.addEdge(randomEdge)
##randomEdge = WeightedEdge(nk, nh, 99, 6)
##g.addEdge(randomEdge)
##randomEdge = WeightedEdge(nh, nj, 38, 14)
##g.addEdge(randomEdge)
##randomEdge = WeightedEdge(nk, nm, 69, 22)
##g.addEdge(randomEdge)
##randomEdge = WeightedEdge(nj, nh, 16, 9)
##g.addEdge(randomEdge)
##randomEdge = WeightedEdge(nk, nj, 71, 48)
##g.addEdge(randomEdge)
##g.childrenOf(nh)
##g.childrenOf(nj)
##g.childrenOf(nk)
##g.childrenOf(nm)
##g.childrenOf(ng)




    
    
