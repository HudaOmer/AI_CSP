class Variable:
    def __init__(self, name, domain, neighbors=[], assigned_value=0):
        self.name = name
        self.domain = domain
        self.neighbors = neighbors
        self.assigned_value = assigned_value

    def __str__(self):
        return f"{self.name}: {self.domain}, value: {self.assigned_value}"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        return self.name == other.name