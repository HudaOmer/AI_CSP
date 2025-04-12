from collections import deque

def ac3(map_csp):
    queue = deque()
    for var in map_csp.variables:
        for neighbor in var.neighbors:
            queue.append((var, neighbor))

    while queue:
        xi, xj = queue.popleft()
        if revise(xi, xj):
            if not xi.domain:
                return False
            for xk in xi.neighbors:
                if xk != xj:
                    queue.append((xk, xi))
    return True

def revise(xi, xj):
    revised = False
    for val in xi.domain[:]:
        if not any(val != y for y in xj.domain):
            xi.domain.remove(val)
            revised = True
    return revised

def is_consistent(var, value, assignment):
    for neighbor in var.neighbors:
        if neighbor.name in assignment and assignment[neighbor.name] == value:
            return False
    return True

def select_unassigned_variable(map_csp, assignment):
    for var in map_csp.variables:
        if var.name not in assignment:
            return var

def backtrack(map_csp, assignment={}):
    if len(assignment) == len(map_csp.variables):
        return assignment

    var = select_unassigned_variable(map_csp, assignment)

    for i, value in enumerate(var.domain):
        if is_consistent(var, value, assignment):
            var.assigned_value = i + 1
            var.color = value
            assignment[var.name] = value

            saved_domains = {v.name: v.domain[:] for v in map_csp.variables}
            var.domain = [value]

            if ac3(map_csp):
                result = backtrack(map_csp, assignment)
                if result:
                    return result

            for v in map_csp.variables:
                v.domain = saved_domains[v.name][:]
            var.assigned_value = 0
            var.color = "Null"
            del assignment[var.name]

    return None
