from problem import get_simple_map, get_circular_map, get_star_map
from solver import Solver
from backtracking import Backtracking
from classic_backtrack import ClassicBacktracking
from arc_consistancy import ArcConsistancy
from ac3_bt import Ac3Bt

def main():
    # List of problems with labels
    problems = [
        ("Circular Map", get_circular_map()),
        ("Simple Map", get_simple_map()),
        ("Star Map", get_star_map())
    ]

    # Available algorithms
    algorithms = {
        "backtracking": Backtracking,
        "classic_backtracking": ClassicBacktracking,
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
