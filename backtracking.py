import random
from helper import print_line, smallPrint

def Backtracking(map_csp):
    var , iterations, back = 0 , 5, 0
    domain = map_csp.domain
    color = ["null"] + domain
    allowed = list(range(1, len(domain) + 1))
    allowed_history = [[] for _ in range(len(map_csp.variables))]
    while var < len(map_csp.variables) and iterations:
        constrained = []
        for neighbor in map_csp.variables[var].neighbors:
            if neighbor.assigned_value > 0:
                constrained.append(neighbor.assigned_value)
        
        
        allowed = list(set(range(1, len(domain) + 1)).symmetric_difference(set(constrained)))
        allowed_history[var] = allowed
        if len(allowed):
            choice = random.choice(allowed)
            map_csp.variables[var].assigned_value = choice
            var += 1
        else:
            print_line()
            print(f"Backtracking from {map_csp.variables[var].name}")
            print(map_csp.print_results())
            map_csp.variables[var].assigned_value = 0
            allowed_history[var] = []

            var -= back
            back += 1
            if len(allowed_history[var]):
                map_csp.variables[var - 1].assigned_value = random.choice(allowed_history[var])
            
            iterations -= 1
            print(f"{var}")
        print(f"{allowed_history=} & {allowed=}")

    smallPrint()

    if iterations:
        print("Success! The final results are:")
    else:
        print("No solution exists!")
        return -1
    return map_csp