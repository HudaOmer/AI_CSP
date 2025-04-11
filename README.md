

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
  Shows step-by-step assignments, including decisions that lead to backtracking.
  **Step 1:** Start by assigning a color to variable A. Let's say A = Red.
  ![](https://github.com/HudaOmer/AI_CSP/blob/master/Images/Solution_1_A.png)
  **Step 2:** Move to variable B. B cannot be Red (adjacent to A). Let's try B = Green.
  ![](https://github.com/HudaOmer/AI_CSP/blob/master/Images/Solution_1_B.png)
  **Step 3:** Move to variable C. C cannot be Red (adjacent to A). Let's try C = Green. However, B is also Green, and B is not adjacent to C, so this is a valid assignment so far.
  ![](https://github.com/HudaOmer/AI_CSP/blob/master/Images/Solution_1_C.png)
  **Step 4:** Move to variable D. D cannot be Green (adjacent to B) and cannot be Green (adjacent to C). So, D must be Blue.
  ![](https://github.com/HudaOmer/AI_CSP/blob/master/Images/Solution_1_D.png)
  **Step 5:** Move to variable E. E cannot be Green (adjacent to C) and cannot be Blue (adjacent to D). So, E must be Red.
  ![](https://github.com/HudaOmer/AI_CSP/blob/master/Images/Solution_1_final.png)
  ▪ We have found a valid assignment: A=Red, B=Green, C=Green, D=Blue, E=Red.
  The solution is direct, No backtracking was needed!
  
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
  Describes the order of assignment and conflicts.
- **Arc Consistency**:  
  Used before and during the search to reduce domains.

#### Final Result:
- ✅ Problem is solved using only **3 colors**.
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
