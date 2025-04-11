import random

def Backtracking(map_csp):
    for var in range(len(map_csp.variables)):
        domain = map_csp.domain
        constrained = []
        for neighbor in map_csp.variables[var].neighbors:
            if neighbor.assigned_value > 0:
                constrained.append(neighbor.assigned_value)
        allowed = list(set(range(1, len(domain) + 1)).symmetric_difference(set(constrained)))
        if len(allowed):
            choice = random.choice(allowed)
            print(choice)
            map_csp.variables[var].assigned_value = choice
        else:
            print_line()
            print(f"Failure: Conflict occures at state: {map_csp.variables[var].name}")
            return -1
        
    print_line()
    print("Success! The final results are:")
    return map_csp

def print_line():
    print("----------------------------------------------")
    return 0
