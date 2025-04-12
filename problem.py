from variable import Variable
from map_csp import MapCSP

def get_simple_map():
    domain = ["Red", "Green", "Blue"]

    A = Variable("A", domain[:])
    B = Variable("B", domain[:])
    C = Variable("C", domain[:])
    D = Variable("D", domain[:])
    E = Variable("E", domain[:])

    A.neighbors = [B, C]
    B.neighbors = [A, C, D]
    C.neighbors = [A, B, D, E]
    D.neighbors = [B, C, E]
    E.neighbors = [C, D]

    return MapCSP([A, B, C, D, E], domain, "Adjacent regions must not share the same color.")

def get_circular_map():
    domain = ["Red", "Green", "Blue"]

    A = Variable("A", domain[:])
    B = Variable("B", domain[:])
    C = Variable("C", domain[:])
    D = Variable("D", domain[:])

    A.neighbors = [B, C, D]
    B.neighbors = [A, C, D]
    C.neighbors = [A, B, D]
    D.neighbors = [A, B, C]

    return MapCSP([A, B, C, D], domain, "Adjacent regions must not share the same color.")

def get_center_star_map():
    domain = ["Red", "Green", "Blue", "Yellow"]

    center = Variable("Center", domain[:])
    A = Variable("A", domain[:])
    B = Variable("B", domain[:])
    C = Variable("C", domain[:])
    D = Variable("D", domain[:])

    center.neighbors = [A, B, C, D]
    A.neighbors = [center, B, D]
    B.neighbors = [center, A, C]
    C.neighbors = [center, B, D]
    D.neighbors = [center, A, C]

    return MapCSP([A, center, B, C, D], domain, "Adjacent regions must not share the same color.")
