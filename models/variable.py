class Variable:
    def __init__(self, name, domain, neighbors=[], assigned_value=0, color="Null"):
        self.name = name
        self.domain = domain
        self.neighbors = neighbors
        self.assigned_value = assigned_value
        self.color = color

    def __str__(self):
        return f"\n{self.name} -> Value: {self.assigned_value},  Domain: {self.domain} , Color: {self.color} , Neighbors: {[self.neighbors[_].name for _ in range(len(self.neighbors))]}"
    def __repr__(self):
        return self.__str__()