# Hash Table with Quadratic Probing (Python)

**Description:**  
This project implements a **hash table** in Python using **quadratic probing** to resolve collisions.  
It supports insertion, searching, deletion, and automatic resizing (rehashing) when the load factor exceeds 0.7.

---

## Features
- Insert **key-value pairs** into the hash table.
- Search for a value by its key.
- Delete a key-value pair.
- Resolves collisions using **quadratic probing**.
- Automatically resizes the table when the **load factor** exceeds 0.7.
- Handles deleted slots efficiently using a **DELETED marker**.

---

## Example Usage

```python
ht = Hash()

# Inserting key-value pairs
ht.insert(1, "A")
ht.insert(2, "B")
ht.insert(3, "C")

# Searching for a key
print(ht.search(2))  # Output: B

# Deleting a key
ht.delete(2)
print(ht.search(2))  # Output: None

# Inserting more keys
ht.insert(4, "D")
ht.insert(5, "E")
ht.insert(6, "F")
ht.insert(7, "G")

# Searching a key
print(ht.search(7))  # Output: G
Sample Output
B
None
G

