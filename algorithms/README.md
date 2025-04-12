## 🧠 My Backtracking Algorithm – Type & Description

The version of backtracking I implemented is a **stochastic, heuristic-based approach** to solving CSPs like the Map Coloring Problem. It’s not a classical recursive backtracking algorithm, but a simplified, iterative version with built-in randomness and control over execution flow.

---

### 🔍 What Kind of Algorithm Is It?

My version falls under **non-deterministic backtracking**, meaning it doesn’t systematically explore all possibilities. Instead, it introduces randomness, keeps track of allowed values, and uses limited retries to avoid infinite loops or overly long execution times.

---

### ✅ Key Features of My Version:

| Feature | Description |
|--------|-------------|
| 🎲 **Random Value Selection** | Instead of trying values in order, I use `random.choice()` to pick a color from the remaining allowed options. This introduces a degree of randomness to the solving process. |
| 🔙 **Backtracking Mechanism** | When no valid color can be assigned to a variable, I backtrack by stepping back and retrying with a different value. The variable pointer (`var`) and a `back` counter control how far to step back. |
| ⏳ **Iteration Control** | To prevent the algorithm from getting stuck or running indefinitely, I added an `iterations` limit. If it’s exhausted, the algorithm halts and reports failure. |
| 🚫 **Constraint Filtering** | Before assigning a color, I filter out colors already used by adjacent regions using a symmetric difference. This ensures that constraints are respected. |
| 🧠 **Domain History Tracking** | I maintain a history of allowed values for each variable, which I use when backtracking to make smarter retries instead of starting from scratch. |

---

### 🆚 Compared to Classic Backtracking

| Classic Backtracking | My Version |
|----------------------|------------|
| Recursive, exhaustive | Iterative with controlled flow |
| Systematic domain exploration | Random selection from remaining options |
| Guaranteed completeness | May miss a solution if retries run out |
| No iteration limit | Uses a fixed iteration cap to stop early |

---

### 🏷️ Classification of My Algorithm

Based on how it works, my version can be classified as:

- ✅ **Heuristic Backtracking**
- ✅ **Stochastic CSP Solver**
- ⚠️ **Incomplete**, because it doesn’t guarantee a solution will be found even if one exists.

---

### 🚀 Why I Chose This Approach

This version is meant to be **simple, fast, and good enough for small to medium-sized CSPs**. It works well for map coloring scenarios where performance and quick feedback are more important than guaranteed completeness. In practice, it often finds a solution quickly without needing full backtracking.

---






---

## 🔧 Enhancements to My Backtracking Algorithm

To improve the performance, consistency checking, and decision-making of my CSP solver, I’ve integrated the following:

### 1. ✅ **Arc Consistency (AC-3)**
### 2. ✅ **Minimum Remaining Values (MRV) Heuristic**
### 3. ✅ **Least Constraining Value (LCV) Heuristic**

---

### 1️⃣ Arc Consistency (AC-3)

Before or during backtracking, I apply **AC-3** to prune the domains by removing values that can’t satisfy constraints with any neighbor.

#### 📜 Pseudocode (AC-3)

```python
def AC3(csp):
    queue = [(Xi, Xj) for Xi in csp.variables for Xj in Xi.neighbors]

    while queue:
        Xi, Xj = queue.pop(0)
        if revise(Xi, Xj):
            if len(Xi.domain) == 0:
                return False  # Inconsistency found
            for Xk in Xi.neighbors:
                if Xk != Xj:
                    queue.append((Xk, Xi))
    return True

def revise(Xi, Xj):
    revised = False
    for x in Xi.domain[:]:
        if not any(constraint_satisfied(x, y) for y in Xj.domain):
            Xi.domain.remove(x)
            revised = True
    return revised
```

#### ✅ Benefit:
It **simplifies the search space** by removing invalid options early on, improving efficiency and reducing unnecessary backtracking.

---

### 2️⃣ Minimum Remaining Values (MRV)

MRV selects the next variable to assign based on which variable has **the fewest legal values left**.

#### 📜 Pseudocode (MRV)

```python
def select_unassigned_variable(variables):
    unassigned = [v for v in variables if v.assigned_value == 0]
    return min(unassigned, key=lambda var: len(var.domain))
```

#### ✅ Benefit:
This helps **fail early** by choosing the most constrained variable, which is likely to cause conflicts — so it handles it sooner.

---

### 3️⃣ Least Constraining Value (LCV)

When choosing a value for a variable, I prefer the one that **rules out the fewest choices** for the variable’s neighbors.

#### 📜 Pseudocode (LCV)

```python
def order_domain_values(var, csp):
    return sorted(var.domain, key=lambda val: count_constraints(val, var, csp))

def count_constraints(value, var, csp):
    count = 0
    for neighbor in var.neighbors:
        if value in neighbor.domain:
            count += 1
    return count
```

#### ✅ Benefit:
LCV tends to **keep options open** for other variables, leading to fewer dead ends and smoother progression.

---

## ✅ Putting It All Together

You can integrate all of these techniques into your existing algorithm by:

1. **Preprocessing with AC-3** to prune domains.
2. Using **MRV** to choose which variable to assign next.
3. Using **LCV** to pick the most "harmless" value.
4. Falling back to your **backtracking with randomness** when needed — or replacing the randomness with LCV and domain ordering for a smarter approach.

---

### 🧠 Summary of My Enhanced CSP Solver

| Technique | Role |
|----------|------|
| **Backtracking** | Core recursive search mechanism |
| **AC-3** | Enforces arc consistency to prune domains |
| **MRV** | Chooses the next variable with least remaining options |
| **LCV** | Selects the value that reduces conflict potential |
| **Random fallback (optional)** | Provides variety and quick search in small problems |

---






 

## 🎯 **Classic Recursive Backtracking with Arc Consistency and MRV**

### 📜 **Algorithm Overview**
The **classic recursive backtracking algorithm** is enhanced by applying **Arc Consistency (AC-3)** and the **Minimum Remaining Values (MRV)** heuristic. This combination ensures that we find the solution more efficiently by pruning invalid values early and selecting variables wisely.

---

### 1️⃣ **Classic Recursive Backtracking Algorithm**

Backtracking is the core strategy for solving **Constraint Satisfaction Problems (CSPs)**, where the algorithm assigns values to variables one by one, checking for conflicts. If a conflict occurs (i.e., a constraint is violated), the algorithm **backtracks** and tries a different value.

---

### 2️⃣ **Arc Consistency (AC-3)**

**AC-3** is used to reduce the size of the domains before or during backtracking. It removes values that can't satisfy the constraints with any of the neighbors.

#### **AC-3 Algorithm Flow:**
- Start with a queue containing all arcs (pairs of variables).
- For each arc, check if revising one variable leads to an empty domain.
- If a variable domain becomes empty, the problem has no solution.
- If any domain is revised, re-add affected arcs to the queue.

---

### 3️⃣ **Minimum Remaining Values (MRV) Heuristic**

**MRV** helps the algorithm by selecting the variable with the **fewest remaining legal values**. This prioritizes the most constrained variable, guiding the algorithm towards failure points earlier.

#### **MRV Selection:**
- From all unassigned variables, select the one with the smallest domain.
- This helps to minimize branching and fail faster.

---

### 4️⃣ **Least Constraining Value (LCV) Heuristic**

**LCV** selects the value for a variable that rules out the fewest choices for its neighbors. This heuristic helps maintain flexibility for neighboring variables, reducing the chance of dead ends.

#### **LCV Selection:**
- For each value, count how many neighboring variables would have their domains reduced if that value were assigned.
- Choose the value that constrains neighbors the least.

---

## 🧠 **Putting It All Together:**

Here’s how the **algorithm works step-by-step**:

1. **Apply Arc Consistency (AC-3)** to prune the domains of variables before starting backtracking.
2. **Use MRV** to select the variable with the smallest domain, reducing the search space early.
3. **Apply LCV** to choose the least constraining value for the selected variable.
4. **Perform recursive backtracking**:
   - If a solution is found, return it.
   - If a conflict is encountered, backtrack to the previous variable and try another assignment.

---

## 📌 **code**


```python
def AC3(csp):
    queue = [(Xi, Xj) for Xi in csp.variables for Xj in Xi.neighbors]
    
    while queue:
        Xi, Xj = queue.pop(0)
        if revise(Xi, Xj):
            if len(Xi.domain) == 0:
                return False  # No solution exists
            for Xk in Xi.neighbors:
                if Xk != Xj:
                    queue.append((Xk, Xi))
    return True

def revise(Xi, Xj):
    revised = False
    for x in Xi.domain[:]:
        if not any(constraint_satisfied(x, y) for y in Xj.domain):
            Xi.domain.remove(x)
            revised = True
    return revised

def constraint_satisfied(x, y):
    return x != y  # No adjacent regions can have the same color

def select_unassigned_variable(csp):
    unassigned = [v for v in csp.variables if v.assigned_value is None]
    return min(unassigned, key=lambda var: len(var.domain))  # MRV heuristic

def order_domain_values(var, csp):
    return sorted(var.domain, key=lambda val: count_constraints(val, var, csp))  # LCV heuristic

def count_constraints(value, var, csp):
    count = 0
    for neighbor in var.neighbors:
        if value in neighbor.domain:
            count += 1
    return count

def backtracking(csp, assignment):
    if len(assignment) == len(csp.variables):  # All variables assigned
        return assignment
    
    var = select_unassigned_variable(csp)  # MRV heuristic
    for value in order_domain_values(var, csp):  # LCV heuristic
        if is_consistent(var, value, assignment):  # Check if the value is valid
            var.assigned_value = value
            assignment[var] = value
            if AC3(csp):  # Apply AC-3 to prune domains
                result = backtracking(csp, assignment)  # Recurse to the next variable
                if result:
                    return result  # Found a solution
            var.assigned_value = None  # Backtrack
            del assignment[var]
    
    return None  # No solution found

def is_consistent(var, value, assignment):
    for neighbor in var.neighbors:
        if neighbor.assigned_value == value:  # Check if the assignment violates any constraint
            return False
    return True
```

---

## 🌟 **Algorithm Summary**

| **Technique**      | **Purpose**                                               |
|--------------------|-----------------------------------------------------------|
| **Backtracking**    | Core algorithm that assigns values to variables and backtracks if conflicts arise. |
| **Arc Consistency (AC-3)** | Prunes domains by removing inconsistent values, improving efficiency. |
| **Minimum Remaining Values (MRV)** | Chooses the variable with the fewest remaining legal values to assign next, reducing search space. |
| **Least Constraining Value (LCV)** | Chooses the value that least restricts future choices for neighboring variables, helping avoid dead ends. |

---

## ✅ **Advantages of the Enhanced Algorithm:**

- **Efficient Search**: MRV and LCV heuristics focus the search on the most promising paths, helping the algorithm fail fast and find solutions faster.
- **Arc Consistency**: AC-3 ensures the domains are pruned early, preventing the algorithm from exploring impossible solutions.
- **Smarter Backtracking**: By intelligently selecting variables and values, the algorithm can find solutions without unnecessarily large search trees.

---

### **Limitations:**

- **Memory Intensive**: The algorithm can consume a lot of memory as it keeps track of variable domains and assignment states.
- **Still Backtracking**: Though optimized, backtracking remains a brute-force technique and might take time for large or highly constrained CSPs.

---

### **Real-World Applications:**

This algorithm is great for solving problems like:

- **Map coloring** (assigning colors to regions without conflicts).
- **Sudoku** or **N-Queens Problem** (placing numbers or pieces with constraints).
- **Scheduling Problems** (assigning tasks without overlap).

---
