📚 CF9 Python Learning Repository: From Core Syntax to OOP, Caching & File Handling 🐍

  

Overview 🌟

Welcome to my Python learning repository from Coding Factory 9. This is a hands-on collection of scripts, examples, and mini-lessons I'm building as I learn Python. The repository starts with core syntax and data structures, then gradually moves into functions, object behavior, recursion, lambda expressions, functional programming tools, memoization, decorators, generators, object-oriented programming, logging, and file handling.

About the Repository 📖

This repo takes a practical approach to learning Python, working through core language features one small, focused example at a time. Each lesson lives in its own folder with source code and a detailed README explaining the concept, the code, expected output, and a few exercises.

What You Will Practice 🧠

This repository is designed as a gradual learning path:

Python basics: values, strings, numbers, input, and formatting.

Control flow: conditions, loops, truthy/falsy logic, and short-circuit behavior.

Collections: lists, tuples, sets, dictionaries, nested lists, and stack behavior.

Functions: parameters, return values, optional arguments, *args, **kwargs, and scope.

Object behavior: identity, mutability, shallow copies, and references.

Functional tools: lambda expressions, map(), filter(), and reduce().

Performance & caching: memoization, lru_cache, timing functions, and decorators.

Generators & iterators: yield, infinite generators, custom iterators, and iterator protocol.

Introductory OOP: simple classes, properties, inheritance, encapsulation, hashability, abstract classes, and duck typing.

Files & logging: logging configuration, error tracing, and basic file CRUD operations.

Repository Contents 📂

Practical Applications 🛠️

Data Manipulation 🔢

User Interaction ⌨️

Basic Algorithms 🔄

Mathematical Demonstrations 📏

Function Design ⚙️

Recursion & Iteration 🔁

Functional Programming Tools 🧩

Performance & Caching ⚡

OOP, Protocols & Abstractions 🧱

Logging & File Handling 🪵

🐍 Python - Chapter01

<table>
  <tr>
    <td>01. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/01.%20Primitive%20Data%20Types" title="Introduces the basic data types in Python. Fundamental for beginners to understand how data is stored and manipulated.">Primitive Data Types</a></td>
    <td>02. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/02.%20Using%20Literals" title="Focuses on the different types of literals in Python and their usage, including number bases and string forms.">Using Literals</a></td>
    <td>03. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/03.%20Print%20Statements" title="Demonstrates various ways to use the print function, including the sep and end arguments.">Print Statements</a></td>
  </tr>
  <tr>
    <td>04. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/04.%20Mathematical%20Operations" title="Covers string formatting and the math module, providing a foundation for computational tasks.">Mathematical Operations</a></td>
    <td>05. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/05.%20Handling%20User%20Input" title="Teaches how to capture and convert user input, a key skill for interactive programs.">Handling User Input</a></td>
    <td>06. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/06.%20More%20on%20User%20Input" title="Expands on user input by turning answers into booleans and branching with if/else.">More on User Input</a></td>
  </tr>
  <tr>
    <td>07. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/07.%20Integer%20Functions" title="Explores integer behavior and operator methods like __add__ behind the + operator.">Integer Functions</a></td>
    <td>08. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/08.%20Working%20with%20Time" title="Converts a total number of seconds into days, hours, minutes and seconds using // and %.">Working with Time</a></td>
    <td>09. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/09.%20Limits%20of%20Integer" title="Explores sys.maxsize and the fact that Python integers have arbitrary precision (no fixed min/max).">Limits of Integer</a></td>
  </tr>
  <tr>
    <td>10. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/10.%20Float%20Operations" title="Focuses on floats, the type() function, and scientific notation.">Float Operations</a></td>
    <td>11. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/11.%20Floating%20Point%20Interest" title="Demonstrates numeric underscores and currency formatting with :,.2f in an interest calculation.">Floating Point Interest</a></td>
    <td>12. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/12.%20Boolean%20Values%20and%20Expressions" title="Explores boolean logic and how True/False behave as integers (1 and 0).">Boolean Values and Expressions</a></td>
  </tr>
  <tr>
    <td>13. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/13.%20Short%20Circuit%20Evaluation" title="A guide to Python's short-circuit behavior in logical operations with or and and.">Short Circuit Evaluation</a></td>
    <td>14. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/14.%20Short%20Circuit%20Application" title="Practical application of short-circuit evaluation to build messages and supply defaults.">Short Circuit Application</a></td>
    <td>15. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/15.%20Defining%20Strings" title="Demonstrates defining strings with single, double, and triple quotes, including multi-line text.">Defining Strings</a></td>
  </tr>
  <tr>
    <td>16. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/16.%20String%20Operations" title="Covers string concatenation (+) and repetition (*).">String Operations</a></td>
    <td>17. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/17.%20Character%20and%20String%20Interaction" title="Explains that Python has no separate char type; a single character is just a str.">Character and String Interaction</a></td>
    <td>18. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/18.%20String%20Indexing%20and%20Traversal" title="Access and traverse strings through indexing, len(), and for loops.">String Indexing and Traversal</a></td>
  </tr>
  <tr>
    <td>19. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/19.%20Generating%20Odd%20Numbers" title="Generate odd numbers within a range using loops, the modulo operator, and list comprehensions.">Generating Odd Numbers</a></td>
    <td>20. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/20.%20String%20Challenges" title="String pattern challenges using loops and repetition to build staircases and right-aligned triangles.">String Challenges</a></td>
    <td>21. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter01/21.%20String%20Slicing%20Techniques" title="String slicing with [start:stop:step] — indexing, negative indices, stepping, and reversing.">String Slicing Techniques</a></td>
  </tr>
</table>

🐍 Python - Chapter02

<table>
  <tr>
    <td>01. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/01.%20List%20Populate%20and%20Traverse" title="Creating a list, populating it, and traversing its elements with a loop.">List Populate and Traverse</a></td>
    <td>02. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/02.%20Range%20Function%20Demonstration" title="Driving loops with range() and using the underscore (_) as a throwaway loop variable.">Range Function Demonstration</a></td>
    <td>03. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/03.%20For%20Loops%20with%20Sales%20Data" title="Iterating over sales data with for loops and conditional logic.">For Loops with Sales Data</a></td>
  </tr>
  <tr>
    <td>04. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/04.%20No%20Scopping" title="Python loops don't create their own scope — loop variables remain visible afterwards.">No Scoping</a></td>
    <td>05. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/05.%20Nested%20Lists" title="Lists within lists and accessing elements in a 2D structure.">Nested Lists</a></td>
    <td>06. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/06.%20List%20Manipulation" title="Core list operations: append, insert, remove, sort, slice and more.">List Manipulation</a></td>
  </tr>
  <tr>
    <td>07. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/07.%20Tuple%20Operations" title="Immutable tuples, packing and unpacking multiple values.">Tuple Operations</a></td>
    <td>08. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/08.%20Set%20Operations" title="Sets and their operations: union, intersection and difference.">Set Operations</a></td>
    <td>09. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/09.%20Dictionary%20Operations" title="Key-value dictionaries and iterating over keys, values and items.">Dictionary Operations</a></td>
  </tr>
  <tr>
    <td>10. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/10.%20Frozen%20Set%20a%20Dict%20Key" title="Using an immutable frozenset as a dictionary key.">Frozen Set as a Dict Key</a></td>
    <td>11. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/11.%20Greeting%20Function" title="Defining your first function with parameters and a return value.">Greeting Function</a></td>
    <td>12. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/12.%20Comprehensive%20Application%20Style" title="Structuring a small multi-file application (app.py plus a helper module).">Comprehensive Application Style</a></td>
  </tr>
  <tr>
    <td>13. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/13.%20Truthy%20Falsy%20Values%20Operators%20and%20Challenge" title="Truthy/falsy values, empty dict vs set, and chained comparisons.">Truthy & Falsy Values</a></td>
    <td>14. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/14.%20Optional%20Parameters%20in%20Functions" title="Default parameter values and positional vs keyword arguments.">Optional Parameters in Functions</a></td>
    <td>15. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/15.%20Variable%20Arguments%20in%20Functions" title="Accepting any number of positional arguments with *args.">Variable Arguments (*args)</a></td>
  </tr>
  <tr>
    <td>16. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/16.%20Printing%20Cities" title="Combining *args with a keyword-only separator parameter, like print's sep.">Printing Cities</a></td>
    <td>17. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/17.%20Variable%20Arguments%20Average%20Calculation" title="Averaging an arbitrary number of values and unpacking a list into *args.">Variable Arguments Average</a></td>
    <td>18. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/18.%20Stack%20Implementation" title="A menu-driven LIFO stack with regex input validation and a match/case dispatcher.">Stack Implementation</a></td>
  </tr>
  <tr>
    <td>19. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/19.%20Or%20and%20In%20Operators" title="Three ways to test membership: or, .upper(), and the Pythonic in operator.">Or and In Operators</a></td>
    <td>20. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/20.%20Student%20Class" title="Your first class: __init__, self, and instance attributes.">Student Class</a></td>
    <td>21. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/21.%20Point%20Class" title="A 2D Point with __str__ and a distance method using the math module.">Point Class</a></td>
  </tr>
  <tr>
    <td>22. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/22.%20Point%20Class%20with%20Properties" title="Encapsulation, dunder methods, a classmethod instance counter, and properties.">Point Class with Properties</a></td>
    <td>23. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter02/23.%20Class%20Inheritance" title="Inheritance, super(), and public/protected/private with name mangling.">Class Inheritance</a></td>
    <td></td>
  </tr>
</table>

🐍 Python - Chapter03

<table>
  <tr>
    <td>01. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/01.%20Immutable%20ID%20Demo" title="Explores object identity with id(), immutability, small integer caching, and string interning.">Immutable ID Demo</a></td>
    <td>02. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/02.%20Modifiable%20Objects%20Demo" title="Demonstrates mutable objects, object references, and how changes can affect the original object.">Modifiable Objects Demo</a></td>
    <td>03. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/03.%20Rectangle%20and%20Square%20Check" title="Uses conditional logic to check whether given dimensions form a rectangle or a square.">Rectangle and Square Check</a></td>
  </tr>
  <tr>
    <td>04. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/04.%20List%20Comparison" title="Compares lists by value and identity, reinforcing the difference between == and is.">List Comparison</a></td>
    <td>05. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/05.%20Ternary%20Operator%20Demo" title="Introduces Python's conditional expression for compact if/else assignments.">Ternary Operator Demo</a></td>
    <td>06. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/06.%20Character%20to%20ASCII%20Conversion" title="Converts characters to ASCII / Unicode code points using ord().">Character to ASCII Conversion</a></td>
  </tr>
  <tr>
    <td>07. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/07.%20Number%20Guessing%20Game" title="A small interactive guessing game using loops, random numbers, and user input.">Number Guessing Game</a></td>
    <td>08. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/08.%20Armstrong%20Number%20Checker" title="Checks whether a number is an Armstrong number using digit processing and arithmetic.">Armstrong Number Checker</a></td>
    <td>09. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/09.%20Sum%20and%20Product%20Calculator" title="Calculates the sum and product of values, reinforcing accumulators and arithmetic logic.">Sum and Product Calculator</a></td>
  </tr>
  <tr>
    <td>10. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/10.%20Factorial%20Calculator" title="Calculates factorial values using loops or function logic.">Factorial Calculator</a></td>
    <td>11. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/11.%20Fibonacci%20Calculator" title="Generates Fibonacci values and practices sequence-based thinking.">Fibonacci Calculator</a></td>
    <td>12. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/12.%20Fibonacci%20Improvement" title="Improves the Fibonacci example with cleaner or more efficient implementation ideas.">Fibonacci Improvement</a></td>
  </tr>
  <tr>
    <td>13. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/13.%20Name%20Spacing%20Demo" title="Uses string joining, stripping, and validation to print a name with custom spacing.">Name Spacing Demo</a></td>
    <td>14. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/14.%20Decrypt%20Message" title="Filters digits out of a string to reveal a hidden message.">Decrypt Message</a></td>
    <td>15. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/15.%20Break%20Scheduler%20App" title="Demonstrates searching, break, and Python's for/else structure.">Break Scheduler App</a></td>
  </tr>
  <tr>
    <td>16. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/16.%20HTTP%20Error%20Handler" title="Uses match/case to return messages for common HTTP status codes.">HTTP Error Handler</a></td>
    <td>17. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/17.%20HTTP%20Error%20Handler%20with%20Dictionary" title="Uses dictionary lookup with .get() as an alternative to match/case.">HTTP Error Handler with Dictionary</a></td>
    <td>18. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter03/18.%20Password%20Generator" title="Generates random passwords using random and string utilities.">Password Generator</a></td>
  </tr>
</table>

🐍 Python - Chapter04

<table>
  <tr>
    <td>01. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/01.%20Type%20Annotation" title="Function annotations, docstrings, runtime type checks, and function metadata.">Type Annotation</a></td>
    <td>02. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/02.%20Generic%20Function" title="Generic functions with TypeVar, Sequence, Any, and Optional.">Generic Function</a></td>
    <td>03. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/03.%20Function%20Scope" title="Shows local scope, global variables, and parameter reassignment inside functions.">Function Scope</a></td>
  </tr>
  <tr>
    <td>04. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/04.%20List%20Demo" title="Demonstrates list mutation by passing a list into a function and appending values.">List Demo</a></td>
    <td>05. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/05.%20List%20Duplicate" title="Explores duplicated lists and shared references inside nested lists.">List Duplicate</a></td>
    <td>06. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/06.%20List%20Shallow%20Copy" title="Explains shallow copies with slicing and why nested lists may still be shared.">List Shallow Copy</a></td>
  </tr>
  <tr>
    <td>07. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/07.%20Optional%20Parameters" title="Default parameter values, required parameters, and keyword arguments.">Optional Parameters</a></td>
    <td>08. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/08.%20Variable%20Length%20Arguments" title="Uses *args to accept a variable number of positional arguments.">Variable-Length Arguments</a></td>
    <td>09. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/09.%20List%20Unpacking" title="Unpacks list values into variables using normal and starred assignment.">List Unpacking</a></td>
  </tr>
  <tr>
    <td>10. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/10.%20Keyword%20Args" title="Filters product data using **kwargs, dictionary unpacking, and list comprehensions.">Keyword Args</a></td>
    <td>11. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/11.%20Factorial%20Recursion%20Demo" title="Calculates factorial values using recursion and base cases.">Factorial Recursion Demo</a></td>
    <td>12. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/12.%20Fibonacci%20Recursion" title="Implements a simple recursive Fibonacci function.">Fibonacci Recursion</a></td>
  </tr>
  <tr>
    <td>13. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/13.%20Lambda%20Demo" title="Introduces lambda functions with a power calculation example.">Lambda Demo</a></td>
    <td>14. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/14.%20Filter%20Even%20Numbers" title="Uses filter() and lambda to keep only even numbers from a list.">Filter Even Numbers</a></td>
    <td>15. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/15.%20Map%20Demo" title="Uses map() and lambda to transform city names into title case.">Map Demo</a></td>
  </tr>
  <tr>
    <td>16. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/16.%20Map%20Filter%20Lambda" title="Combines filter(), map(), and lambda to process city names.">Map Filter Lambda</a></td>
    <td>17. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/17.%20Reduce%20Demo" title="Uses functools.reduce() to calculate factorial values and print intermediate steps.">Reduce Demo</a></td>
    <td>18. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter04/18.%20Reduce%20Factorial%20Wow" title="Expands the reduce factorial example with step-by-step output.">Reduce Factorial Wow</a></td>
  </tr>
</table>

🐍 Python - Chapter05

<table>
  <tr>
    <td>01. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/01.%20List%20Comprehension%20Map%20Demo" title="Compares list comprehensions with map(), filter(), lambda, and named functions.">List Comprehension, Map & Filter Demo</a></td>
    <td>02. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/02.%20Inner%20Functions" title="Calculates weighted grades using nested helper functions and tuple returns.">Inner Functions</a></td>
    <td>03. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/03.%20Function%20Arguments" title="Demonstrates positional arguments, optional parameters, *args, and **kwargs.">Function Arguments</a></td>
  </tr>
  <tr>
    <td>04. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/04.%20Closure%20Demo" title="Uses closures and nonlocal state to create department ID generators.">Closure Demo</a></td>
    <td>05. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/05.%20Student%20Enrollment" title="Uses *students, keyword-only parameters, defaults, and **kwargs.">Student Enrollment</a></td>
    <td>06. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/06.%20Average%20Calculator" title="Calculates averages with *args and a ternary expression.">Average Calculator</a></td>
  </tr>
  <tr>
    <td>07. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/07.%20Calculator%202" title="Menu-driven calculator with inner functions, reduce(), and match/case.">Calculator 2</a></td>
    <td>08. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/08.%20Event%20Logger" title="Logs events with datetime timestamps and flexible **kwargs metadata.">Event Logger</a></td>
    <td>09. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/09.%20Garage%20Demo" title="Simulates a garage queue using deque, append(), popleft(), and match/case.">Garage Demo</a></td>
  </tr>
  <tr>
    <td>10. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/10.%20Functions%20as%20Arguments" title="Passes arithmetic functions as arguments to a reusable calculator.">Functions as Arguments</a></td>
    <td>11. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/11.%20Grade%20Transformations" title="Groups grade upscaling, filtering, categorization, and average calculations.">Grade Transformations</a></td>
    <td>12. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/12.%20Iterators" title="Explains iter(), next(), StopIteration, and custom iterator classes.">Iterators</a></td>
  </tr>
  <tr>
    <td>13. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/13.%20Factorial%20Iterator" title="Custom iterator that produces factorial values from 0! to n!.">Factorial Iterator</a></td>
    <td>14. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/14.%20Simple%20Generator" title="Introduces yield, generator objects, next(), and preserved generator state.">Simple Generator</a></td>
    <td>15. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/15.%20Generators" title="Common README for factorial and Fibonacci infinite generators.">Generators</a></td>
  </tr>
  <tr>
    <td>16. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/16.%20Timing%20Function" title="Measures execution time using time.perf_counter().">Timing Function</a></td>
    <td>17. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/17.%20Time%20Decorator" title="Builds a reusable decorator that measures function execution time.">Time Decorator</a></td>
    <td>18. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/18.%20Logging%20Apps" title="Common README for basic and improved logging examples.">Logging Apps</a></td>
  </tr>
  <tr>
    <td>19. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/19.%20Demo%20of%20Copies" title="Compares shallow copy techniques with copy.deepcopy().">Demo of Copies</a></td>
    <td>20. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/20.%20Set%20Operations" title="Demonstrates intersection, union, difference, and symmetric difference.">Set Operations</a></td>
    <td>21. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/21.%20Memoization%20Fibonacci" title="Uses custom memoization decorators and cache statistics for Fibonacci.">Memoization Fibonacci</a></td>
  </tr>
  <tr>
    <td>22. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/22.%20LRU%20Cache%20Demo" title="Uses functools.lru_cache to optimize recursive Fibonacci.">LRU Cache Demo</a></td>
    <td>23. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/23.%20Multiple%20Decorators" title="Combines logging and timing decorators and explains execution order.">Multiple Decorators</a></td>
    <td>24. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/24.%20Unmodifiable%20Tuples" title="Shows tuple immutability and mutable elements inside tuples.">Unmodifiable Tuples</a></td>
  </tr>
  <tr>
    <td>25. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/25.%20Dictionary%20Comprehensions" title="Creates dictionaries with calculated values and optional filtering.">Dictionary Comprehensions</a></td>
    <td>26. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/26.%20Count%20Frequencies" title="Counts item frequencies with dicts, get(), manual loops, and Counter.">Count Frequencies</a></td>
    <td>27. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/27.%20Student%20Grades" title="Filters students by average grade using dictionary comprehension.">Student Grades</a></td>
  </tr>
  <tr>
    <td>28. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/28.%20Find%20Min%20Value" title="Uses min() with key functions on dictionary data.">Find Min Value</a></td>
    <td>29. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/29.%20Sales%20Analysis" title="Analyzes monthly sales with dictionaries, comprehensions, totals, averages, max, and min.">Sales Analysis</a></td>
    <td>30. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/30.%20Property%20Function" title="Creates managed attributes with getter, setter, deleter, and property().">Property Function</a></td>
  </tr>
  <tr>
    <td>31. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/31.%20Point%20Class" title="2D Point class with properties, validation, movement, and computed distance.">Point Class</a></td>
    <td>32. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/32.%20Hashable%20Point" title="Implements __eq__(), __hash__(), and __repr__() for dictionary keys.">Hashable Point</a></td>
    <td>33. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/33.%20Iterable%20Data%20Class" title="Custom collection supporting iteration, indexing, slicing, len(), and unpacking.">Iterable Data Class</a></td>
  </tr>
  <tr>
    <td>34. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/34.%20Abstract%20Class" title="Uses ABC and abstractmethod for DAO and inventory interfaces.">Abstract Class</a></td>
    <td>35. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/35.%20Duck%20Typing" title="Demonstrates behavior-based polymorphism with drive() methods.">Duck Typing</a></td>
    <td>36. <a href="https://github.com/jroumpekas/cf9-python/tree/main/chapter05/36.%20File%20Operations" title="Performs file create, read, update, and delete operations with os and open().">File Operations</a></td>
  </tr>
</table>

Educational Value 🎓

Small, focused scripts that each isolate one concept

Worked examples and exercises that build understanding step by step

Progressive coverage from beginner syntax to decorators, generators, OOP protocols, logging, and file operations

Well-Documented Code 📄

Each lesson folder includes a detailed README with objectives, key concepts, code demos, and exercises

Chapter Learning Path 🧭

Chapter01: Core syntax, primitive data types, literals, printing, arithmetic, strings, input, and basic expressions.

Chapter02: Collections, loops, dictionaries, truthy/falsy values, functions, stack implementation, and introductory OOP.

Chapter03: Object identity, mutability, conditionals, small algorithms, string processing, HTTP error handlers, and a password generator.

Chapter04: Function annotations, generics, scope, list copying, optional parameters, *args, **kwargs, recursion, lambda, map(), filter(), and reduce().

Chapter05: Advanced functions, closures, generators, decorators, memoization, dictionary comprehensions, OOP data model methods, abstract classes, duck typing, logging, and file operations.

Getting Started 🚀

No installation is required beyond Python itself:

Ensure Python 3.x is installed on your machine.

Clone the repository: git clone https://github.com/jroumpekas/cf9-python.git

Navigate to the lesson folder of interest inside chapter01, chapter02, chapter03, chapter04, or chapter05.

Open a terminal or command prompt.

Run a script with python <filename>.py, and read its README for an explanation.

📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

📄 License

🔐 This project is protected under the MIT License.

Contact 📧

Dimitris Roumpekas - jimroumpi@gmail.com

🔗 Note: This is a Python script and requires a Python interpreter to run.

<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/dimitris-roumpekas-24a81b17a/">Dimitris</a> (<a href="https://github.com/jroumpekas">GitHub</a>)
</p>