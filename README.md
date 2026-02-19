

# 🧮 Scientific Calculator (Python)

A menu-driven scientific calculator built in Python using modular programming.
This project separates all mathematical operations into a reusable module and uses a main program to handle user interaction and memory features.

It is designed for beginners who want to practice functions, modules, error handling, and the `math` library.

---

## ✨ Features

* Basic operations

  * Addition
  * Subtraction
  * Multiplication
  * Division

* Power operations

  * Square
  * Cube
  * Custom power (x^y)

* Root operations

  * Square root
  * Cube root (also works for negative numbers)

* Trigonometric functions (input in degrees)

  * sin, cos, tan

* Inverse trigonometric functions

  * asin, acos, atan (output in degrees)

* Logarithmic functions

  * Log base 10
  * Natural log (ln)
  * Antilog

* Error handling

  * Division by zero
  * Invalid input for logarithms
  * Invalid range for inverse trigonometric functions

* Memory feature (M+ style)

  * Store last result
  * Recall stored value

---

## 🗂 Project Structure

```
scientific-calculator/
│
├── main.py
├── operations.py
└── README.md
```

---

## 📄 File Description

### main.py

* Displays the menu
* Takes user input
* Calls functions from `operations.py`
* Handles memory (store and recall)
* Shows final results

### operations.py

* Contains all mathematical functions
* Uses the built-in `math` module
* Performs calculations only (no user input)

---

## ▶ How to Run

Make sure both files are in the same folder.

Open terminal in that folder and run:

```
python main.py
```

---

## 🧠 Memory Feature

* After any calculation, you can store the result using:

```
M+   (Store last result)
```

* You can recall the stored value using:

```
MR   (Memory recall)


## 🎯 Learning Objectives

This project helps you practice:

* Python functions
* Creating and importing modules
* Using the math library
* Menu-based programs
* Exception handling
* Clean and modular code design

