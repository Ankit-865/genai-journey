# 🧾 Queue Data Structure – Practice Problems  

This section of my **DSA Journey (Week 2-3)** is all about **Queues** – a linear data structure that follows **FIFO (First In, First Out)** order.  

Queues are widely used in real-world applications like **task scheduling, message queues, order processing systems, CPU job scheduling, and BFS traversal in graphs**.  

---

## ✅ Problems I Solved  

### 1️⃣ Food Ordering System (Producer-Consumer Problem)

**Goal:**  
Simulate a real-world restaurant scenario with two threads:  

- **Place Order Thread:** Places new order every `0.5 sec`  
- **Serve Order Thread:** Serves order every `2 sec` (starts with `1 sec` delay)  

**Example Orders:**  
`['pizza','samosa','pasta','biryani','burger']`

**Key Learnings:**  
- Understood how **Producer-Consumer problems** work in real systems.  
- Practiced **multithreading** with `threading.Thread()` in Python.  
- Learned to coordinate two tasks with **time delays** using `time.sleep()`.  

---

### 2️⃣ Generate Binary Numbers (1 to N) Using Queue

**Goal:**  
Generate binary numbers from `1` to `N` (for example `N=10`):  
1
10
11
100
101
110
111
1000
1001
1010

markdown
Copy code

**Approach:**  
- Start by enqueueing `"1"`  
- In each iteration:
  - Print the front element
  - Generate next two numbers by appending `"0"` and `"1"`
  - Dequeue the printed element  

**Key Learnings:**  
- Practiced **BFS-like traversal** using a queue  
- Learned how to generate sequential data using state expansion  

---

## 🔑 Takeaways
- **FIFO Concept:** First order placed → first order served  
- **Producer-Consumer Coordination:** Threads can run concurrently but in sync  
- **Algorithmic Use Case:** Queue helps in systematic generation of sequences like binary numbers  


