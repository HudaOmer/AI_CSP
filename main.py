from problem import get_simple_map, get_circular_map, get_star_map
from solver import Solver
from backtracking import Backtracking
from arc_consistancy import ArcConsistancy
from ac3_bt import Ac3Bt

def main():
    # List of problems with labels
    problems = [
        ("Simple Map", get_simple_map()),
        ("Circular Map", get_circular_map()),
        ("Star Map", get_star_map())
    ]

    # Available algorithms
    algorithms = {
        "backtracking": Backtracking,
        "ac3_bt": Ac3Bt,
        "arc_consistancy": ArcConsistancy
    }

    # Loop over problems
    for label, problem in problems:
        print(f"\n🔍 CSP Map: {label}")
        solver = Solver(problem)

        # Register all algorithms
        for name, func in algorithms.items():
            solver.register(name, func)

        # Run all algorithms for this problem
        for name in algorithms.keys():
            solver.run(name)
            print()

if __name__ == "__main__":
    main()
