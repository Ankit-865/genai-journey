# 🌳 Tree & Binary Search Tree (BST) – DSA Practice

This folder contains my practice problems and solutions for **General Trees** and **Binary Search Trees (BST)** in Python.  
It helped me understand **hierarchical data structures**, how to build, traverse, and manipulate them efficiently.

---

## 📌 Problems I Solved

### ✅ 1. General Tree – Name & Designation Printer
**Goal:**  
Build a general tree representing an organization chart (CEO → CTO → Managers → Employees).  
Extend `print_tree()` function to support 3 modes:
- **Name Only**
- **Designation Only**
- **Both Name & Designation**

**Key Learnings:**
- Learned **tree hierarchy**, `parent → children` relationships.
- Implemented **recursive traversal** to print data with indentation for each level.
- Understood how tree depth impacts indentation and readability.

---

### ✅ 2. Binary Search Tree (BST)
**Goal:**  
Implement a **BST** with:
- Insertion (`add_child`)
- Search (`search`)
- Traversals (`in-order`, `pre-order`, `post-order`)
- Utility functions (`find_min`, `find_max`, `calculate_sum`)

**Key Learnings:**
- Understood how BST maintains **sorted order**.
- Learned how **in-order traversal** always returns a sorted list.
- Practiced recursion for tree traversal.

---

### ✅ 3. Deletion in Binary Search Tree
**Goal:**  
Implement `delete()` method for BST using **maximum value from left subtree** to replace a deleted node.

**Key Learnings:**
- Learned different **deletion cases**:
  1. Node with **no children** → Simply remove it.
  2. Node with **one child** → Replace node with its child.
  3. Node with **two children** → Replace node with **max value from left subtree** (or min from right).
- Improved understanding of how BST properties are preserved after deletion.

---

## 🧠 What I Learned

- Trees are **perfect for hierarchical data representation** (e.g., file systems, org charts).
- BSTs allow:
  - **Fast searching** (O(log n) in average case)
  - **Sorted data traversal** with in-order traversal
- Learned recursion deeply as every tree operation (insert, search, delete, traversal) is recursive.
- Understood **real-world applications**:
  - Trees are used in compilers, file systems, databases, XML/HTML parsing.
  - BSTs power search operations and indexing.

---

## 📂 Folder Structure

