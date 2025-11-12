# Python: Filter even numbers using list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension approach
even_numbers_python = [x for x in numbers if x % 2 == 0]
print("Python result:", even_numbers_python)
print("Type:", type(even_numbers_python))

# Equivalent JavaScript code (as reference)
javascript_code = """
// JavaScript: Filter even numbers using arrow function
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Filter method approach
const evenNumbers = numbers.filter(x => x % 2 === 0);
console.log("JavaScript result:", evenNumbers);
console.log("Type:", typeof evenNumbers);
"""

print("\n--- Equivalent JavaScript Code ---")
print(javascript_code)

# Key differences discussion
differences = """
DIFFERENCES IN SYNTAX AND OUTPUT:

1. Syntax:
    - Python: [x for x in numbers if x % 2 == 0]
    - JS: numbers.filter(x => x % 2 === 0)

2. Comparison Operators:
    - Python uses: == (equality)
    - JS uses: === (strict equality)

3. Array Methods:
    - Python: Built-in list comprehension syntax
    - JS: Array.filter() method with callback function

4. Output Format:
    - Python: [2, 4, 6, 8, 10] (list type)
    - JS: [2, 4, 6, 8, 10] (array type)
    - Both produce identical values, different data structures

5. Performance:
    - Python comprehensions are typically faster
    - JS filter() creates a new array (similar behavior)
"""

print(differences)