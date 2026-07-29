# Python_00

*This project has been created as part of the 42 curriculum by [pnarvaez](https://github.com/Pau-Narvaez-Roy).*

---

## Description

**Python_00** is a foundational 42 school module introducing students to Python programming. This project marks the beginning of the Python curriculum pathway and provides essential exercises to develop core programming concepts in Python, including basic syntax, string manipulation, data structures, and fundamental algorithms.

### Objective

The goal of this module is to:
- Learn Python fundamentals and syntax
- Understand basic data types and operations
- Develop skills in string manipulation and formatting
- Practice working with collections (lists, dictionaries, tuples)
- Build foundational problem-solving capabilities
- Prepare for more advanced Python concepts in subsequent modules

### Overview

Python_00 serves as the introduction to Python programming in the 42 curriculum. Unlike the C-based projects (Libft, ft_printf, get_next_line), this module focuses on Python-specific idioms, syntax, and concepts. The exercises progress from basic "Hello World" style programs to more complex algorithmic challenges, building a solid foundation in Python programming principles.

---

## Project Structure

This module is organized into 8 exercises (ex0 through ex7), each focusing on specific programming concepts:

| Exercise | Topic | Learning Focus |
|----------|-------|-----------------|
| **ex0** | Introduction | Basic output and function definitions |
| **ex1** | String Formatting | String manipulation and formatting techniques |
| **ex2** | Data Structures | Working with lists, tuples, and basic algorithms |
| **ex3** | Iteration & Counting | Loops and frequency analysis |
| **ex4** | Conditionals & Logic | Decision-making and complex conditions |
| **ex5** | Functions | Function definition and parameter handling |
| **ex6** | Collections | Dictionary operations and key-value pairs |
| **ex7** | Advanced Concepts | Integrating multiple concepts |

---

## Instructions

### Prerequisites

- Python 3.x installed on your system
- Basic familiarity with command-line terminals
- A text editor or IDE for viewing/editing Python files

### Installation

1. Clone the repository:
```bash
git clone git@github.com:Pau-Narvaez-Roy/Python_00.git
```

2. Verify Python installation:
```bash
python3 --version
```

### Running the Exercises

Each exercise is self-contained in its own directory. To run an exercise:

```bash
python3 ex0/ft_hello_garden.py
```

Or, to import and test a function:

```bash
python3
>>> from ex0.ft_hello_garden import ft_hello_garden
>>> ft_hello_garden()
Hello, Garden Community!
```

### Project Organization

```
Python_00/
├── ex0/                   
├── ex1/                    
├── ex2/                    
├── ex3/                    
├── ex4/                    
├── ex5/                    
├── ex6/                   
├── ex7/                   
├── README.md              # This file
└── .gitignore
```

---

## Core Concepts Covered

### Python Fundamentals
- Variable assignment and naming conventions
- Basic data types: `int`, `str`, `float`, `bool`
- Type conversion and casting
- Comments and documentation

### Data Structures
- **Lists**: ordered, mutable collections
- **Tuples**: ordered, immutable collections
- **Dictionaries**: key-value data structures
- **Sets**: unordered, unique element collections

### Control Flow
- `if`, `elif`, `else` conditional statements
- `for` loops with range and iteration
- `while` loops and loop control (`break`, `continue`)
- List comprehensions and generator expressions

### Functions
- Function definition with `def`
- Parameters and arguments
- Return values and type hints
- Lambda functions and anonymous functions
- Scope and variable lifetime

### String Operations
- String concatenation and repetition
- String methods and operations
- F-strings and string formatting
- String indexing and slicing

### Working with Collections
- Iterating over lists and dictionaries
- Filtering and mapping operations
- Counting occurrences and frequency analysis
- Sorting and organizing data

---

## Algorithm Explanation

### Example: ft_hello_garden (ex0)

The first exercise demonstrates basic Python structure:

```python
def ft_hello_garden() -> None:
    print("Hello, Garden Community!")
```

**Key Concepts**:
1. **Function Definition**: Uses `def` keyword to define a reusable function
2. **Type Hints**: The `-> None` annotation indicates the function returns nothing
3. **Built-in Functions**: `print()` is used for output
4. **Code Style**: Follows Python PEP 8 conventions

### Progression Through Exercises

As you progress through Python_00:

- **ex0-ex1**: Master basic syntax and string operations
- **ex2-ex3**: Learn how to work with collections and iterate efficiently
- **ex4-ex5**: Develop problem-solving with conditionals and functions
- **ex6-ex7**: Integrate multiple concepts into complete solutions

### Why Python?

Python is chosen for the second phase of 42 curriculum because:
1. **Readability**: Clear, English-like syntax makes logic visible
2. **Rapid Development**: Faster to write and test than C
3. **Rich Standard Library**: Extensive built-in functionality
4. **Versatility**: Used in web, data science, automation, and more
5. **Community**: Large ecosystem of libraries and resources
6. **Bridging Concepts**: Moves from low-level C to high-level Python, emphasizing algorithmic thinking

---

## Features

- ✅ Progressive difficulty from basic to intermediate concepts
- ✅ Clear exercise structure with well-organized directories
- ✅ Introduces Python idioms and best practices
- ✅ Focus on problem-solving and algorithmic thinking
- ✅ Type hints for better code documentation
- ✅ Exercises designed for incremental learning
- ✅ Foundation for advanced Python modules

---

## Running Tests

### Manual Testing

```bash
# Test ex0
python3 -c "from ex0.ft_hello_garden import ft_hello_garden; ft_hello_garden()"
```

### Interactive Testing

```bash
python3
>>> import sys
>>> sys.path.append('.')
>>> from ex0.ft_hello_garden import ft_hello_garden
>>> ft_hello_garden()
```

### Best Practices for Testing

- Test each exercise independently
- Verify output matches expected results
- Try edge cases and boundary conditions
- Use Python's built-in `dir()` and `help()` functions
- Experiment with the Python REPL (interactive shell)

---

## Resources

### Official Documentation
- [Python 3 Documentation](https://docs.python.org/3/) - Official Python reference
- [Python Tutorial](https://docs.python.org/3/tutorial/) - Comprehensive Python tutorial
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/) - Python code style conventions
- [Built-in Functions](https://docs.python.org/3/library/functions.html) - Python built-in function reference

### Learning Resources
- [Real Python](https://realpython.com/) - High-quality Python tutorials
- [Python for Beginners](https://www.python.org/about/gettingstarted/) - Official beginners guide
- [W3Schools Python Tutorial](https://www.w3schools.com/python/) - Interactive Python lessons
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) - Free online book

### Python Tools & Environments
- [Python REPL](https://www.python.org/) - Interactive Python shell
- [pip](https://pip.pypa.io/) - Package installer for Python
- [Virtual Environments](https://docs.python.org/3/library/venv.html) - Isolated Python environments
- [pytest](https://pytest.org/) - Python testing framework

### Data Structures & Algorithms
- [Python Collections](https://docs.python.org/3/library/collections.html) - Container datatypes
- [Sorting HOW TO](https://docs.python.org/3/howto/sorting.html) - Sorting techniques in Python
- [Algorithm Complexity](https://wiki.python.org/moin/TimeComplexity) - Big O notation in Python

### AI Usage

**AI was not used in the development of the code** for this project. The implementations were developed from scratch following the 42 curriculum requirements and Python best practices.

However, **AI was used for documentation purposes**:
- Generating comprehensive README structure
- Creating exercise descriptions and learning objectives
- Formatting code examples and explanations
- Organizing resources and references
- Documenting learning progression

---

## Technical Decisions

### 1. Python Version
The project uses Python 3.x (not Python 2.x) because:
- Python 2 is end-of-life as of January 2020
- Python 3 is the industry standard
- Better syntax and libraries
- Modern language features

### 2. Type Hints
Functions include type hints (`-> None`, `-> int`, etc.) for:
- Better code documentation
- IDE autocompletion support
- Static type checking capabilities
- Professional code standards

### 3. Modular Structure
Each exercise is in its own directory to:
- Keep code organized and scannable
- Allow independent testing and evaluation
- Facilitate progressive learning
- Maintain clean separation of concerns

### 4. Function Naming Conventions
Functions follow the `ft_` prefix (from 42 C tradition) and use snake_case to:
- Maintain consistency with 42 curriculum
- Follow Python PEP 8 conventions
- Make it clear these are learning exercises

### 5. Incremental Difficulty
Exercises progress from simple to complex to:
- Build confidence early
- Establish solid foundations
- Introduce concepts gradually
- Allow for self-paced learning

---

## Getting Help

### Debugging Tips

1. **Use `print()` statements** to trace execution
2. **Read error messages carefully** - they tell you what went wrong
3. **Test small pieces** before combining them
4. **Use the Python REPL** to test code snippets
5. **Check your indentation** - Python is whitespace-sensitive

### Common Issues

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Ensure you're running from the correct directory |
| `IndentationError` | Check that all code blocks are properly indented |
| `TypeError` | Verify you're using the correct data types |
| `KeyError` | Make sure dictionary keys exist before accessing them |

### Getting More Help

- 42 Intra community forums
- Python Stack Overflow questions
- Python Discord communities
- Official Python documentation

---

## Author

**Pau Narváez Roy**

42 Madrid Student | [GitHub Profile](https://github.com/Pau-Narvaez-Roy)

---

## License

This project is part of the 42 school curriculum.

---

## Curriculum Path

This is the beginning of the Python learning pathway:

```
Python_00 (Fundamentals) → Python_01 (Intermediate) → Python_02 (Advanced)
```

After completing Python_00, you'll have the foundation to tackle more complex Python projects and explore specialized domains like web development, data science, and automation.

---

**Last Updated**: July 29, 2026
