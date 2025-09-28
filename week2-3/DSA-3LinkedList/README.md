Linked List in Python – Week 2 (DSA)

Today I learned and practiced Linked Lists, one of the most important linear data structures.
Unlike arrays, linked lists don’t store elements in contiguous memory locations.
Instead, they are made of nodes, where each node stores:

Data → the value

Pointer(s) → a reference to the next (and sometimes previous) node

📌 Why Linked Lists?

I understood that linked lists are useful because:

They provide dynamic memory allocation (no fixed size like arrays).

Insertions and deletions are more efficient compared to arrays.

They form the basis for other data structures like stacks, queues, and graphs.

By practicing, I learned how nodes connect together, how traversal works, and how to manipulate nodes for insertions and deletions.

✅ Problems I Solved
1️⃣ Singly Linked List

Implemented a singly linked list with the following operations:

insert_at_beginning(data) → insert a node at the start

insert_at_end(data) → insert a node at the end

insert_at(index, data) → insert a node at a given index

insert_after_value(data_after, data_to_insert) → insert after a given value

remove_at(index) → remove node at a specific index

remove_by_value(data) → remove a node by its value

print() → print all elements in the list

get_length() → count the number of nodes

Key Takeaway: I understood how to traverse a linked list node by node, and how inserting/removing changes the chain of references.

2️⃣ Doubly Linked List

Extended the idea of singly linked list into a doubly linked list where each node has:

data → stores the value

next → pointer to next node

prev → pointer to previous node

Implemented operations:

insert_at_beginning(data)

insert_at_end(data)

insert_at(index, data)

remove_at(index)

insert_values(data_list) → populate the list from a list of values

print_forward() → traverse forward

print_backward() → traverse backward

Key Takeaway: With an extra prev pointer, I can traverse in both directions and handle insertions/removals more flexibly.

🔑 What I Understood

Arrays are great for random access, but linked lists are better for insertion/deletion.

In linked lists, pointers (references) are the real backbone — forgetting to update them breaks the chain.

Singly linked lists move only forward, while doubly linked lists allow two-way traversal.

These concepts directly connect to real-world applications like memory management, undo-redo features, and data navigation.

📂 All solutions are in this folder → LinkedList

🔜 Next: Hash Table, Stack, and Queue