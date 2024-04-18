from hasPath import undirected_path

edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

assert undirected_path(edges, "j", "m") == True


edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

assert undirected_path(edges, "m", "j") == True


edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

assert undirected_path(edges, "l", "j") == True


edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

assert undirected_path(edges, "k", "o")  == False


edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

assert undirected_path(edges, "i", "o")  == False


edges = [
    ("b", "a"),
    ("c", "a"),
    ("b", "c"),
    ("q", "r"),
    ("q", "s"),
    ("q", "u"),
    ("q", "t"),
]


assert undirected_path(edges, "a", "b") == True


edges = [
    ("b", "a"),
    ("c", "a"),
    ("b", "c"),
    ("q", "r"),
    ("q", "s"),
    ("q", "u"),
    ("q", "t"),
]

assert undirected_path(edges, "a", "c") == True


edges = [
    ("b", "a"),
    ("c", "a"),
    ("b", "c"),
    ("q", "r"),
    ("q", "s"),
    ("q", "u"),
    ("q", "t"),
]

assert undirected_path(edges, "r", "b")  == False


edges = [
    ("s", "r"),
    ("t", "q"),
    ("q", "r"),
]

assert undirected_path(edges, "r", "t") == True
