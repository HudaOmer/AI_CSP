

# Assignment 4: Map Coloring Problems  
**UofK AI Lectures 2024–2025**

## Introduction

This assignment investigates the **Map Coloring Problem** as an application of **Constraint Satisfaction Problems (CSPs)**. The objective is to assign colors to regions on a map such that:

- No two adjacent regions have the same color.
- The total number of colors used is minimized.

Each map scenario is modeled as a CSP by identifying:
- **Variables**: Regions to be colored.
- **Domains**: A set of colors each region can take.
- **Constraints**: Adjacency restrictions between regions.

Solutions are obtained using:
- **Backtracking Search**
- **Arc Consistency (AC-3 algorithm)**

---

## 📍 Maps and Tasks

### 🗺 Map 1: Simple Map

![](https://github.com/HudaOmer/AI_CSP/blob/master/Images/Figure_1.jpg)

#### CSP Definition:
- **Variables**: A, B, C, D, E  
- **Domain**: {Red, Green, Blue}  
- **Constraints**: Adjacent regions must not share the same color.

#### Solution:
- **Backtracking**:

##### 🔍 Step-by-Step Backtracking Solution

Shows step-by-step assignments, including decisions that lead to backtracking.

---

**Step 1:**  
Start by assigning a color to variable **A**.  
Let’s say: `A = Red`  
<img src="https://github.com/HudaOmer/AI_CSP/blob/master/Images/Solution_1_A.png?raw=true" alt="Step 1" width="50%"/>

---

**Step 2:**  
Move to variable **B**.  
`B ≠ Red` (adjacent to A) → Try: `B = Green`  
<img src="https://github.com/HudaOmer/AI_CSP/blob/master/Images/Solution_1_B.png?raw=true" alt="Step 2" width="50%"/>

---

**Step 3:**  
Move to variable **C**.  
`C ≠ Red` (adjacent to A) & `C ≠ Green` (adjacent to B) → Try: `C = Blue`
<img src="https://github.com/HudaOmer/AI_CSP/blob/master/Images/Solution_1_C.png?raw=true" alt="Step 3" width="50%"/>

---

**Step 4:**  
Move to variable **D**.  
`D ≠ Green` (adjacent to B) & `D ≠ Blue` (adjacent to C) → Try: `D = Red`  
<img src="https://github.com/HudaOmer/AI_CSP/blob/master/Images/Solution_1_D.png?raw=true" alt="Step 4" width="50%"/>

---

**Step 5:**  
Move to variable **E**.  
`E ≠ Blue` (adjacent to C) & `E ≠ Red` (adjacent to D) → Try: `E = Green`  
<img src="https://github.com/HudaOmer/AI_CSP/blob/master/Images/Solution_1_final.png?raw=true" alt="Step 5" width="50%"/>

---

##### ✅ Final Assignment:
- A = Red  
- B = Green  
- C = Blue  
- D = Red  
- E = Green

**Result:**  
🎉 A valid solution was found with **no backtracking required**!

---
  
- **Arc Consistency**:  
  Domains are filtered using AC-3 to eliminate inconsistent values early.
  
#### Final Result:
- ✅ A valid coloring with **3 colors** is found.
- 👁 Step-by-step breakdown and visual trace included in the solution PDF.

---

### 🌀 Map 2: Circular Map

![](https://github.com/HudaOmer/AI_CSP/blob/master/Images/Figure_2.jpg)

#### CSP Definition:
- **Variables**: A, B, C, D  
- **Domain**: {Red, Green, Blue}  
- **Constraints**: Each region is adjacent to two others in a circular fashion.

#### Solution:
- **Backtracking**:

##### 🔍 Step-by-Step Backtracking Solution

Shows step-by-step assignments, including decisions and conflicts that lead to backtracking.

---

**Step 1:**
Start by assigning a color to variable **A**.
Let’s say: `A = Red`

---

**Step 2:**
Move to variable **B**.
`B ≠ Red` (adjacent to A) → Try: `B = Green`

---

**Step 3:**
Move to variable **C**.
`C ≠ Red` (adjacent to A) & `C ≠ Green` (adjacent to B) → Try: `C = Blue`

---

**Step 4:**
Move to variable **D**.
`D ≠ Red` (adjacent to A) & `D ≠ Green` (adjacent to B) & `D ≠ Blue` (adjacent to C)

At this point, we have encountered a **constraint violation**. According to the adjacencies you provided, **D is adjacent to A, B, and C**. Since A is Red, B is Green, and C is Blue, there is **no remaining color in the domain {Red, Green, Blue} that can be assigned to D** without violating the constraint that no two adjacent regions can have the same color.

---

**Backtracking:**
Since we cannot assign a valid color to D, we must **backtrack** to the previous step and try a different color for C.

---

**Step 3 (Backtrack 1):**
Move back to variable **C**. The current assignment is `C = Blue`. Let's try the next available color in the domain (assuming we tried them in the order Red, Green, Blue). However, since A is Red and B is Green, there are no other valid colors for C that are different from both Red and Green.

---

**Backtracking:**
Since we cannot find a valid color for C, we must **backtrack** to the previous step and try a different color for B.

---

**Step 2 (Backtrack 2):**
Move back to variable **B**. The current assignment is `B = Green`. Let's try the next available color in the domain: `B = Blue`.

---

**Step 3 (Backtrack 2):**
Move to variable **C**.
`C ≠ Red` (adjacent to A) & `C ≠ Blue` (adjacent to B) → Try: `C = Green`

---

**Step 4 (Backtrack 2):**
Move to variable **D**.
`D ≠ Red` (adjacent to A) & `D ≠ Blue` (adjacent to B) & `D ≠ Green` (adjacent to C)

Again, we have encountered a **constraint violation**. D is adjacent to A (Red), B (Blue), and C (Green), and there are no other colors in the domain.

---

**Further Backtracking:**
We would continue to backtrack through the assignments for B and potentially A, trying all possible color combinations. However, given that **every region is adjacent to every other region**, and we only have **three colors available**, it is **impossible to find a valid coloring**. Each of the four regions requires a different color, but only three are available in the domain.

Therefore, the Map 2 problem as a CSP with the domain {Red, Green, Blue} has **no solution**. This demonstrates that with these fully connected adjacencies, three colors are **not sufficient** to solve the problem. It would require at least four distinct colors.


- **Arc Consistency**:  
  Used before and during the search to reduce domains.

#### Final Result:
- ❌ Problem can't be solved using only **3 colors**, a fourth one is needed.
- 🔍 Includes explanation of variable ordering and consistency enforcement.

---

### 🌟 Map 3: Star Map

![](https://github.com/HudaOmer/AI_CSP/blob/master/Images/Figure_3.jpg)

#### CSP Definition:
- **Variables**: Center, A, B, C, D  
- **Domain**: {Red, Green, Blue, Yellow}  
- **Constraints**: The Center is adjacent to A, B, C, and D; outer nodes may or may not be adjacent.

#### Solution:
- **Backtracking**:  
  Detailed steps showing how the center node constrains others.
- **Arc Consistency**:  
  Simplifies the problem by shrinking domains before deeper recursion.

#### Final Result:
- ✅ The map is solvable using **3 colors**, despite having 4 in the domain.
- 🧠 Includes domain reduction insights and optimization choices.

---

## ✅ Submission Guidelines

- 📄 Submit your solution as a **PDF** named:  
  `Assignment4_MapColoring_<YourName>.pdf`
- 📝 Include your **name** and **index number**.
- 🔧 If you used code, attach it as an appendix or submit separately.
- 📚 Explain your process clearly, step-by-step, for each map.

---

## 💡 Notes

- Use diagrams to support adjacency representation where applicable.
- Clearly highlight points where backtracking or arc consistency is applied.
- Keep explanations intuitive—clarity matters more than technical jargon!

---
