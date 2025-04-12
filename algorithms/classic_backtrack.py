def is_consistent(var, value, assignment, constraints):
    """Check if assigning value to var is consistent with current assignment."""
    for neighbor in var.neighbors:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True

def backtrack(assignment, variables, constraints):
    """Classic recursive backtracking algorithm."""
    # Base case: all variables assigned
    if len(assignment) == len(variables):
        return assignment

    # Select unassigned variable (simple ordering)
    unassigned = [v for v in variables if v not in assignment]
    var = unassigned[0]

    # Try values from domain
    for value in var.domain:
        if is_consistent(var, value, assignment, constraints):
            assignment[var] = value
            result = backtrack(assignment, variables, constraints)
            if result:
                return result
            del assignment[var]  # Backtrack

    return None

def ClassicBacktracking(map_csp):
    """Wrapper function to run classic backtracking on MapCSP."""
    assignment = {}
    result = backtrack(assignment, map_csp.variables, map_csp.constraints)

    if result:
        for var in result:
            var.color = result[var]
        print("\n✅ Success! Solution found, The final results are:")
        return True
    else:
        print("❌ No solution found!")
        return False
