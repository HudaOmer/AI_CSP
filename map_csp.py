class MapCSP:
    def __init__(self, variables, domain, constraints):
        self.variables = variables
        self.domain = domain
        self.constraints = constraints
        

    def __str__(self):
        return f"Variables: {self.variables}\nConstraints: {self.constraints}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.variables == other.variables and self.constraints == other.constraints

    def print_results(self):
        result = []
        for var in self.variables:
            color = var.domain[var.assigned_value - 1]
            result.append(f"{var.name}: {color}")
        return "\n".join(result)

