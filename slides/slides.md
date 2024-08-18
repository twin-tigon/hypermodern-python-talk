---
theme: default
background: https://plus.unsplash.com/premium_vector-1711987778419-60da1cc87cbf?q=80&w=2360&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
title: Hypermodern Web Development with Python and FastAPI
class: text-center
mdc: true
colorSchema: dark
hideInToc: true
addons:
  - slidev-addon-qrcode
---

# Hypermodern Web Development

## with Python and FastAPI

---
layout: intro
hideInToc: true
---

# About Me

- Countries
  - USA, UK, The Netherlands, Belgium, Italy, Costa Rica
- Roles
  - Full-stack, DevOps, Architect, Data Engineer, Data Science
- Industries
  - Healthcare, Finance, AI, Education, Marketing
- Languages
  - Python, TypeScript, JavaScript, Bash

---
hideInToc: true
---

# Outline

<Toc minDepth="1" maxDepth="2" listClass="text-sm"></Toc>

---
layout: section
---

# Language

---
level: 2
layout: two-cols
layoutClass: gap-16
---

# Background

- Created by Guido van Rossum
- Released in 1991
- Focus on readability
- The Zen of Python (PEP20)
- Python Enhancement Proposal (PEP)
- Python Software Foundation (PSF)

::right::

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

<style>
  pre {
    font-size: 10px !important;
    overflow-x: hidden !important;
  }
</style>

---
level: 2
---

# Demand within Telescoped

<TechnologyDemandChart/>

---
level: 2
layout: two-cols
---

# Recap
 
- Indentation
- List comprehension
- Decorators
- Context managers
- Self in class
- Private method and properties
- Scope of variables in loops and comprehensions

::right::

<v-switch>
  <template #1>
```py
def check_number(num):
    if num > 0:
        print("Positive")
    elif num == 0:
        print("Zero")
    else:
        print("Negative")

check_number(5)  # Output: Positive
```
  </template>
  <template #2>
```py
# Create a list of squares for even numbers from 0 to 9
squares = [x * x for x in range(10) if x % 2 == 0]
print(squares)  # Output: [0, 4, 16, 36, 64]
```
  </template>
  <template #3>
```py
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before the function runs
# Hello!
# After the function runs
```
  </template>
  <template #4>
```py
# Manual resource management
f = open('file.txt', 'w')
try:
    f.write('Hello, world!')
finally:
    f.close()

# Using a context manager
with open('file.txt', 'w') as f:
    f.write('Hello, world!')
```
  </template>
  <template #5>
```py
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy")
my_dog.bark()  # Output: Buddy says woof!
```
  </template>
  <template #6>
```py
class MyClass:
    def __init__(self):
        self._private_var = "This is a private var"
    
    def _private_method(self):
        print("This is a private method")

    def public_method(self):
        print("This is a public method")

obj = MyClass()
obj.public_method() # Output: This is a public method
obj._private_method()  # Output: This is a private method
print(obj._private_var)  # Output: This is a private var
```
  </template>
  <template #7>
```py
def create_counter():
    count = 0  # This variable is private to the closure

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = create_counter()

print(counter())  # Output: 1
print(counter())  # Output: 2

# `count` is not accessible directly
# print(count)  # NameError: name 'count' is not defined
```
  </template>
  <template #8>
```py
for i in range(3):
    print(i)
print(i)  # Output: 2

```
  </template>
</v-switch>


---
level: 2
layout: two-cols
---

# Newer Features

- F-Strings
- Type hints
- asyncio
- Generators

::right::

<v-switch>
  <template #1>
```py
first_name = "John"
last_name = "Doe"
full_name = f"{first_name} {last_name}"
print(full_name)  # Output: John Doe
```
  </template>
  <template #2>
```py
# Basic type hint example
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Union type example
def get_status_code(code: int | str) -> str:
    if isinstance(code, int):
        return f"Status code is {code}"
    elif isinstance(code, str):
        return f"Status message is '{code}'"
    return "Unknown type"

# Using the functions
print(greet("Alice"))
# Output: Hello, Alice!
print(get_status_code(404))
# Output: Status code is 404
print(get_status_code("Not Found"))
# Output: Status message is 'Not Found'
```
  </template>
  <template #3>
```py
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def main():
    await asyncio.gather(say_hello(), say_hello())

# Run the main function using the asyncio event loop
asyncio.run(main())

# Output:
# Hello
# Hello
# (After 1 second)
# World
# World
```
  </template>
  <template #4>
```py
# Generator function example
def count_up_to(max: int):
    count = 1
    while count <= max:
        yield count
        count += 1

# Using the generator with next()
counter = count_up_to(3)
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3
# print(next(counter))  # Raises StopIteration

# Iterating over the generator
for number in count_up_to(5):
    print(number)

# Output:
# 1
# 2
# 3
# 4
# 5
```
  </template>
</v-switch>


---
layout: section
---

# Tooling

---
level: 2
---

# Project Management

- pip
- venv
- pyenv
- Poetry
- Rye ✅

---
level: 2
---

# Code Quality

- Ruff ✅
- mypy
- Pyright ✅
- pre-commit ✅

---
layout: section
---

# Libraries

---
level: 2
---

# Web Frameworks

- Django
- Flask
- FastAPI ✅

---
level: 2
---

# HTTP Servers

- Gunicorn
- Uvicorn ✅
- Daphne

---
level: 2
---

# Serialization

- marshmallow
- Pydantic ✅

---
level: 2
---

# Database

- SQLAlchemy ✅
- SQLModel
- Alembic ✅

---
layout: statement
hideInToc: true
---

# Demo

---
hideInToc: true
---

# References

- [Full Stack FastAPI Template][full-stack-fastapi-template]
- [Hypermodern Python][hypermodern-python]
- [Beyond Hypermodern: Python is easy now][beyond-hypermodern]

[full-stack-fastapi-template]: https://github.com/fastapi/full-stack-fastapi-template
[hypermodern-python]: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
[beyond-hypermodern]: https://rdrn.me/postmodern-python/

---
layout: end
hideInToc: true
---

# Questions?

<QRCode
    :width="300"
    :height="300"
    type="svg"
    data="https://github.com/twin-tigon/hypermodern-python-talk"
    :margin="10"
    :imageOptions="{ margin: 10 }"
    :dotsOptions="{ type: 'extra-rounded', color: 'white' }"
/>

<PoweredBySlidev mx-auto block mt-10 />