import Graph as G


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    G = G.Graph(7)
    G.naive_backtrack()
    print(G.edges)
