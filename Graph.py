import math
import random


class Graph:
    v_degree = math.inf
    vertices = set()
    # dictionary of edges, where the key is each vertex
    edges = {}

    def __init__(self, v_degree):
        self.v_degree = v_degree
        v_total = v_degree + (v_degree - 1)*v_degree + 1
        for i in range(v_total):
            self.vertices.add(i)
            self.edges[i] = set()

        for i in range(v_degree + 1):
            # root
            if i == 0:
                for j in range(v_degree):
                    self.edges[i].add(j + 1)
                    self.edges[j + 1].add(i)
            # top layer init
            if i <= v_degree and i != 0:
                top_degree = v_degree - 1
                for j in range(top_degree):
                    cur = top_degree + i*top_degree - j + 1
                    self.edges[i].add(cur)
                    self.edges[cur].add(i)



    def test_edge(self, x, y):
        for a in self.edges[x]:
            if y == a:
                return False
            for b in self.edges[a]:
                if y == b:
                    return False
                for c in self.edges[b]:
                    if y == c:
                        return False
        return True

    def naive_random(self):
        for i in range(1, self.v_degree + 1):
            for v in self.edges[i]:
                while not self.verify_v(v):
                    count = 0
                    for j in range(i + 1, self.v_degree + 1):
                        idcs = list(range(i + 1, self.v_degree + 1))
                        print(idcs)
                        random.shuffle(idcs)
                        idx = idcs[count]
                        for u in self.edges[idx]:
                            if self.test_edge(u, v):
                                self.edges[u].add(v)
                                self.edges[v].add(u)
                        count += 1

    def verify(self):
        for v in self.vertices:
            if len(self.edges[v]) == self.v_degree:
                pass
            else:
                return False
        return True

    def verify_v(self, v):
        if len(self.edges[v]) == self.v_degree:
            return True
        else:
            return False
    # v is current vertex, i is current chunk, blocked is some u in i + 1 that can't be paired
    def find_next(self, v, i, blocked):
        for j in range(blocked, len(self.edges[i + 1])):
            u = self.edges[i + 1][j]
            if self.test_edge(u, v):
                return u
            else:
                return 0

    def naive_backtrack(self):
        for i in range(1, self.v_degree + 1):
            for v in self.edges[i]:
                for j in range(i + 1, self.v_degree + 1):
                    for u in self.edges[j]:
                        if self.test_edge(u, v):
                            self.edges[u].add(v)
                            self.edges[v].add(u)
                if not self.verify_v(v):
                    print("SHORT!")
                    print(v, self.edges[v])

    def recursive_backtrack(self, v, i, blocked):
        if self.verify():
            return True
        else:
            if self.find_next(v, i, blocked) != 0:
                # if new clump
                if (v + 1) % (self.v_degree - 1) == 0:
                    self.recursive_backtrack(v + 1, i + 1, 0)
                # otherwise, same clump
                else:
                    self.recursive_backtrack(v + 1, i, 0)
            # no available next for v
            else:
                # backtrack to last vertex and retry
                if (v) % (self.v_degree - 1) == 0:
                    self.find_next(v - 1, i - 1, )


    def hand_of_god(self, cur_v):
        if self.verify():
            return self.edges
        else:
            return self.hand_of_god()


