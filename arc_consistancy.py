import random
from helper import print_line, smallPrint

def ArcConsistancy(map_csp):
    for var in range(len(map_csp.variables)):
        if len(map_csp.variables[var].domain):
            color = random.choice(map_csp.variables[var].domain)
        else:
            print_line()
            print(f"Backtracking from {map_csp.variables[var].name}")
            smallPrint()
            print("No solution exists!")
            return -1

        map_csp.variables[var].color = color
        map_csp.variables[var].domain = [map_csp.variables[var].color]
        # print(map_csp.variables[var])
        for neighbor in map_csp.variables[var].neighbors:
            # print(f"{neighbor.name}: {neighbor.domain},")
            if len(neighbor.domain):
                if color in neighbor.domain:
                    neighbor.domain = [_ for _ in neighbor.domain if _ != color ]
            else:
                print("Conflict!!")
                return -1
            print(f"{neighbor.name}: {neighbor.domain}", end=", ")
        print()
    
    smallPrint()
    print("Success! The final results are:")

    return 0
        
        