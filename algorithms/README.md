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
