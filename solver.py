from helper import bigPrint

class Solver:
    def __init__(self, map_csp):
        self.map_csp = map_csp
        self.algorithms = {}

    def register(self, name, function):
        """Register a solver algorithm by name."""
        self.algorithms[name.lower()] = function

    def run(self, name):
        name = name.lower()
        if name not in self.algorithms:
            print(f"❌ Unknown algorithm '{name}'. Available algorithms: {list(self.algorithms.keys())}")
            return

        bigPrint(f"{name.upper()} SOLVER")
        print(f"Running {name.title()}...\n")
        result = self.algorithms[name](self.map_csp)

        if name == "arc_consistancy":
            print(self.map_csp.print_colors())
        elif hasattr(self.map_csp, "print_results") and callable(getattr(self.map_csp, "print_results")):
            print(self.map_csp.print_results())
        elif hasattr(self.map_csp, "print_colors") and callable(getattr(self.map_csp, "print_colors")):
            print(self.map_csp.print_colors())

        return result
