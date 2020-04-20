def cliques(num):
    link3 = num
    link2 = 2*link3
    link1 = 2*link2
    return link1

num_cliques = (2, 25)
r = map(cliques, num_cliques)
print(list(r))
