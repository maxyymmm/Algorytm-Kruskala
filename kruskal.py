# tworzy zbiór z jednym elementem
def make_set(v):
    return {v}

# łączy 2 zbiory rozłacznee
def union(u, v):
    set_u, set_v = find_set(u), find_set(v)
    if set_u != set_v:
        set_u.update(set_v)
        sets.remove(set_v)

# zwracaja zbiór, do którego należy wierzchołek v
def find_set(v):
    for s in sets:
        if v in s:
            return s
       
# do sortowania niemalejąco - daje
def get_weight(e):
    return W[E.index(e)][1]


if __name__ == "__main__":
    V = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] #Zbiór wierzchołków
    E = [['A', 'B'], ['B', 'C'], ['C', 'E'], ['E', 'G'], ['G', 'F'], ['F', 'D'], ['D', 'A'], ['D', 'B'], ['B', 'E'], ['D', 'E'], ['F', 'E']] #Zbiór krawędzi
    W = [[['A', 'B'], 7], [['B', 'C'], 8], [['C', 'E'], 5], [['E', 'G'], 9], [['G', 'F'], 11], [['F', 'D'], 6], [['D', 'A'], 5], [['D', 'B'], 9], [['B', 'E'], 7], [['D', 'E'], 15], [['F', 'E'], 8]]#Wagi


    # tworzenie zbioru z ppojedynczymi elementami
    sets = [make_set(v) for v in V]

    # sortowanie krawędzi niemalejąco
    E = sorted(E, key=get_weight)


    # tworzenie MST
    A = []
    for e in E:
        u, v = e
        if find_set(u) != find_set(v):
            A.append(e)
            union(u, v)

    print(A)