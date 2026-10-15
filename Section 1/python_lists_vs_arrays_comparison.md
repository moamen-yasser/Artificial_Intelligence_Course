# Comparison: Python Lists vs. Arrays (NumPy)

This document outlines the fundamental differences between built-in Python lists and NumPy arrays for data storage and manipulation.

## Comparison Table

| Feature / Aspect | Python List (`list`) | NumPy Array (`numpy.array`) |
| :--- | :--- | :--- |
| **Origin / Library** | Built-in data type (no import required). | Requires the external `numpy` library (`import numpy as np`). |
| **Data Homogeneity** | Can store **heterogeneous** data types (e.g., integers, strings, booleans, and floats all in the same list). | Must store **homogeneous** data (all elements must be of the exact same data type). |
| **Memory Allocation** | Elements are scattered across memory; stores references/pointers to the actual objects. | Elements are stored in **contiguous** (adjacent) blocks of memory for high performance. |
| **Mathematical Operations** | Direct arithmetic operations do not work element-wise. For example, `[1, 2, 3] * 2` results in duplication (`[1, 2, 3, 1, 2, 3]`). | Supports **vectorization**. Arithmetic operations apply element-wise directly (e.g., `np.array([1, 2, 3]) * 2` results in `[2, 4, 6]`). |
| **Performance & Speed** | Slower when performing large mathematical computations or looping over millions of elements. | Extremely fast and optimized for numerical operations and matrix math. |
| **Primary Use Cases** | General-purpose data storage, mixed-type collections, stacks, queues, and dynamic sizing. | Scientific computing, data science, machine learning, and heavy numerical analysis. |

---

## Quick Code Example

### 1. Python List Behavior
```python
my_list = [1, 2, 3]
print(my_list * 2)  # Output: [1, 2, 3, 1, 2, 3] (Concatenation/Duplication)
```

### 2. NumPy Array Behavior
```python
import numpy as np

my_array = np.array([1, 2, 3])
print(my_array * 2)  # Output: [2 4 6] (Element-wise multiplication)