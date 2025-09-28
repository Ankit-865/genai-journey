# 🧱 Stack Data Structure – Practice Problems  

In this section of my **DSA Journey (Week 2)**, I focused on **stacks**, one of the most important linear data structures.  
Stacks follow **LIFO (Last In First Out)** order and are widely used in parsing, recursion, undo/redo operations, and memory management.  

---

## ✅ Problems I Solved  

### 1. Reverse a String using Stack
**Goal:** Write a function that reverses a string using stack operations.  

```python
reverse_string("We will conquer COVID-19")
# Output: "91-DIVOC reuqnoc lliw eW"
Learning:
This exercise helped me understand how push() and pop() naturally reverse order of elements when retrieved from a stack.

2. Balanced Parentheses Checker
Goal: Verify whether all types of parentheses (), {}, [] are properly balanced.

python
Copy code
is_balanced("({a+b})")       # True  
is_balanced("))((a+b}{")     # False  
is_balanced("[a+b]*(x+2y)")  # True  
Learning:
This is a classic use case of stacks – every time we see an opening bracket, we push it, and every time we see a closing bracket, we pop and match it.
This gave me an intuition for expression validation and how compilers parse code internally.

🔑 Key Takeaways
Stack is the perfect data structure when order reversal or matching (LIFO) is required.

Practical applications:

Expression evaluation

Undo/Redo functionality

Browser back/forward history

Recursion call stack