# Python 620 Program Practice Plan: Zero to Hero Roadmap

This plan is structured into 57 days, with 10 to 12 programs per day, categorized for maximum learning efficiency. Each program is described clearly and assigned a unique filename.

---
## Day 1: Python Basics & Simple Math (11 Programs)
Focus: Input/Output, Arithmetic, and Basic Variable Manipulation.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **1** | Swap the values of two variables (using temporary variable AND Python tuple unpacking). | A. Basics | <a href="/Programs/620 Program Practice/Day 01 Python Basics and Simple Math (11 Programs)/A01_swap_values.py">A01_swap_values.py</a> |
| **2** | Calculate the sum of the first and last digit of a 4-digit integer. | A. Basics | <a href="620 Program Practice/Day 01 Python Basics and Simple Math (11 Programs)/A02_digit_sum.py">A02_digit_sum.py</a> |
| **3** | Convert distance in Kilometers (km) to Centimeters (cm), Meters, Feet, and Inches. | A. Basics | <a href="620 Program Practice/Day 01 Python Basics and Simple Math (11 Programs)/A03_unit_convert.py">A03_unit_convert.py</a> |
| **4** | Implement a simple calculator: take two numbers and an operator (+, -, \*, /) as input and display the result. | A. Basics | `A04_simple_calc.py` |
| **5** | Calculate the **Simple Interest (SI)** given Principal, Rate, and Time. | A. Math | `A05_simple_interest.py` |
| **6** | Calculate the **Compound Interest (CI)** given Principal, Rate, and Time. | A. Math | `A06_compound_interest.py` |
| **7** | Calculate the **Area of a Circle** given its radius ($A = \pi r^2$). | A. Math | `A07_circle_area.py` |
| **8** | Calculate the **Perimeter of a Rectangle** given its length and breadth. | A. Math | `A08_rect_perimeter.py` |
| **9** | Calculate the **Cube** of a number ($n^3$) input by the user. | A. Math | `A09_cube_number.py` |
| **10** | Calculate the **Average** of three numbers. | A. Math | `A10_average_three.py` |
| **11** | Convert temperature from **Fahrenheit to Celsius** (using the formula: $C = (F - 32) \times 5/9$). | A. Math | `A11_f_to_c.py` |

---
## Day 2: Conditional Logic & Decision Making (11 Programs)
Focus: `if`, `elif`, `else` blocks, Boolean logic, and comparison.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **12** | Determine if a user is **eligible to vote** (age $\ge 18$) and display an appropriate message. | B. Conditionals | `B01_vote_eligibility.py` |
| **13** | Determine if a number is **positive, negative, or zero**. | B. Conditionals | `B02_pos_neg_zero.py` |
| **14** | Determine if a number is **Even or Odd**. | B. Conditionals | `B03_even_odd.py` |
| **15** | Find the **Largest of Three** input numbers. | B. Conditionals | `B04_max_of_three.py` |
| **16** | Determine a person's life stage (Kid, Teenager, Adult, Senior Citizen) based on input age using tiered `elif` checks. | B. Conditionals | `B05_life_stage.py` |
| **17** | Calculate student **Total, Percentage, Result (Pass/Fail)**, and **Grade** for 5 subjects. Must be marked **Fail** if any subject mark is below 40. | B. Logic | `B06_student_grade.py` |
| **18** | Determine if a given year is a **Leap Year** (divisible by 4, except for years divisible by 100 but not by 400). | B. Logic | `B07_leap_year.py` |
| **19** | Check if a single input character is a **vowel** (`a, e, i, o, u`) or not. | B. Logic | `B08_is_vowel.py` |
| **20** | Convert an input character to **lowercase** if it's uppercase, and vice-versa. | B. Logic | `B09_toggle_case.py` |
| **21** | **Advanced Discount Logic:** Calculate bill payment with a tiered discount based on purchase amount (e.g., $<1000$: 5%, $>5000$: 20%). | B. Logic | `B10_bill_discount_tiered.py` |
| **22** | **Taxable Income Check:** Determine if income is taxable based on gender (Male > 700000, Female > 500000). | B. Logic | `B11_tax_check.py` |

---
## Day 3: Loops & Iteration (Part 1) (11 Programs)
Focus: `for` and `while` loops, basic counting, and tables.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **23** | Print numbers from 1 to 10 using a **`while`** loop. | C. Loops | `C01_while_1_to_10.py` |
| **24** | Print numbers from 1 to 10 using a **`for`** loop and the `range()` function. | C. Loops | `C02_for_1_to_10.py` |
| **25** | Print all **even numbers** up to a user-defined limit ($N$) using a `while` loop. | C. Loops | `C03_while_even_n.py` |
| **26** | Print all **odd numbers** from 1 to a user-defined limit ($N$) using a `for` loop. | C. Loops | `C04_for_odd_n.py` |
| **27** | Print the **multiplication table** of a given number ($N$) using a **`for`** loop. | C. Loops | `C05_table_for.py` |
| **28** | Print the multiplication table of a given number ($N$) using a **`while`** loop. | C. Loops | `C06_table_while.py` |
| **29** | Print numbers in **reverse order** from 100 down to 90 using `range()`. | C. Loops | `C07_for_100_90.py` |
| **30** | Find all numbers between 2000 and 3200 (inclusive) which are **divisible by 7 but NOT a multiple of 5**. | C. Loops | `C08_range_filter.py` |
| **31** | Calculate the **Factorial** of a number ($N!$) using iteration (loop). | C. Math | `C09_factorial_iter.py` |
| **32** | Print the first 10 natural numbers along with their **squares and cubes** in a tabular format. | C. Loops | `C10_sq_cube_table.py` |
| **33** | Print all numbers that are **divisible by 7** between 1 and 200. | C. Loops | `C11_divisible_by_7.py` |

---
## Day 4: Loops & Iteration (Part 2) (11 Programs)
Focus: Digit manipulation, sequences, and advanced loop usage.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **34** | Calculate the **sum of digits** of a given integer number ($N$). | C. Math | `C12_sum_of_digits.py` |
| **35** | **Reverse** a given integer number ($N$). | C. Math | `C13_reverse_number.py` |
| **36** | Check if a given number is a **Palindrome** (reads the same forwards and backwards). | C. Logic | `C14_palindrome_num.py` |
| **37** | Check if a given number is an **Armstrong Number** (sum of cubes of digits equals the number). | C. Logic | `C15_armstrong.py` |
| **38** | Generate the **Fibonacci series** up to $N$ terms. | C. Sequence | `C16_fibonacci.py` |
| **39** | Find all **Prime Numbers** up to a user-defined limit ($N$). | C. Sequence | `C17_primes_in_range.py` |
| **40** | Print characters from an input string that are present at **even index** positions using a loop. | C. String | `C18_string_even_index.py` |
| **41** | Use the `else` block with a **`for`** loop to display a message ("Loop completed successfully") only when the loop finishes without a `break`. | C. Advanced | `C19_for_else.py` |
| **42** | Use a loop to display elements from a given list that are present at **odd index** positions. | C. List | `C20_list_odd_index.py` |
| **43** | Find the total **number of words** in an input string. | C. String | `C21_count_words.py` |
| **44** | Count the **number of times a specific word** appears in a given string. | C. String | `C22_count_word_freq.py` |

---
## Day 5: Functions & Modularization (11 Programs)
Focus: Defining functions, return values, basic math, and arguments.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **45** | Create a function `calculate_area_circle(radius)` to calculate and return the area of a circle. | D. Function | `D01_func_area_circle.py` |
| **46** | Create two separate functions, `square(n)` and `cube(n)`, that return the square and cube of a number, respectively. | D. Function | `D02_func_sq_cube.py` |
| **47** | Create a function `calculate_simple_interest(P, R, T)` to calculate simple interest. | D. Function | `D03_func_si.py` |
| **48** | Create a function `is_prime(n)` that checks if a number is prime and returns a Boolean (`True` or `False`). | D. Function | `D04_func_is_prime.py` |
| **49** | Create a function `string_length(s)` that returns the length of a string without using the built-in `len()`. | D. Function | `D05_func_str_len.py` |
| **50** | Create a function `factorial_rec(n)` that calculates the factorial of a number using **recursion**. | D. Recursion | `D06_func_factorial_rec.py` |
| **51** | Create a function `encrypt_string(s)` that replaces all vowels (`a, e, i, o, u`) with 'x'. | D. Function | `D07_func_encrypt_vowel.py` |
| **52** | Implement the **recursive Fibonacci sequence** function. | D. Recursion | `D08_func_fib_rec.py` |
| **53** | Implement the **Tower of Hanoi** problem using recursion. | D. Recursion | `D09_func_hanoi.py` |
| **54** | Write a program to demonstrate the four ways to pass arguments to a function: **Required, Keyword, Default, and Variable-length (`*args`, `**kwargs`)**. | D. Arguments | `D10_func_arg_types.py` |
| **55** | Create a single function that accepts 3 arguments (2 numbers and 1 arithmetic operator string) and uses an `if/elif/else` structure to return the calculated result. | D. Function | `D11_func_op_calc.py` |

---
## Day 6: Data Structures (Lists & Tuples) (11 Programs)
Focus: List manipulation, comprehensions, and tuple basics.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **56** | Accept a sequence of **comma-separated numbers** from the user and generate a **list** and a **tuple** of those numbers. | E. List/Tuple | `E01_list_tuple_from_csv.py` |
| **57** | Display the **first and last elements** from a predefined list (e.g., a color list). | E. List | `E02_list_first_last.py` |
| **58** | Create a dynamic list by repeatedly taking elements from the user until a sentinel value is entered, then display the final list. | E. List | `E03_dynamic_list.py` |
| **59** | Write a program to find the **maximum, minimum, and length** of a list using **user-defined functions**. | E. List | `E04_list_min_max_func.py` |
| **60** | Create a new list using a **List Comprehension** that stores the squares of numbers from 1 to $N$. | E. List Comp | `E05_list_squares_comp.py` |
| **61** | Implement the **Two Sum Problem**: Given a list of numbers and a target, find the indices of the two numbers that add up to the target. | E. Algorithm | `E06_two_sum.py` |
| **62** | **Move Zeroes**: Move all zeroes in a list to the end while maintaining the relative order of the non-zero elements. | E. List Ops | `E07_move_zeroes.py` |
| **63** | **Merge Sorted Lists**: Merge two already sorted lists into a single sorted list. | E. List Ops | `E08_merge_sorted_lists.py` |
| **64** | Find all **Duplicate Elements** in a given list. | E. List Ops | `E09_find_duplicates.py` |
| **65** | **Rotate an Array**: Rotate a list of $N$ elements to the right by $K$ steps. | E. List Ops | `E10_rotate_array.py` |
| **66** | **Product of Array Except Self**: Compute a new list where each element is the product of all elements in the original list except the element at the current index. | E. Advanced | `E11_product_except_self.py` |

---
## Day 7: String Manipulation (11 Programs)
Focus: String methods, character-level logic, and basic search.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **67** | **Reverse an input string** without using slicing (`[::-1]`) or the `reversed()` function (use a loop). | F. String Ops | `F01_str_reverse_manual.py` |
| **68** | Check if an input string is a **Palindrome** (reads the same forwards and backwards). | F. String Logic | `F02_str_palindrome.py` |
| **69** | Convert an input string entirely to **uppercase** letters. | F. String Ops | `F03_str_to_upper.py` |
| **70** | Convert an input string entirely to **lowercase** letters. | F. String Ops | `F04_str_to_lower.py` |
| **71** | **Concatenate** two input strings. | F. String Ops | `F05_str_concatenate.py` |
| **72** | **Compare two strings** to check if they are exactly the same (case-sensitive and case-insensitive check). | F. String Logic | `F06_str_compare.py` |
| **73** | Find the number of **spaces and vowels** in an input string. | F. String Logic | `F07_str_vowels_spaces.py` |
| **74** | Check if two strings are **Anagrams** of each other (contain the same characters in a different order). | F. String Logic | `F08_check_anagram.py` |
| **75** | Find the **First Non-Repeating Character** in a string. | F. String Logic | `F09_first_unique_char.py` |
| **76** | **Remove all blank spaces** from an input string. | F. String Ops | `F10_remove_spaces.py` |
| **77** | Find the **Highest Frequency Character** (the one that occurs most frequently) in a string. | F. String Logic | `F11_highest_freq_char.py` |

---
## Day 8: Dictionaries, Sets, and Comprehension (12 Programs)
Focus: Advanced collection manipulation using Pythonic syntax.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **78** | Create a dictionary where keys are numbers from 1 to $N$ and values are their **squares** using a **Dictionary Comprehension**. | G. Dict Comp | `G01_dict_squares_comp.py` |
| **79** | Create a dictionary from a string, where keys are characters and values are their **frequencies** (occurrences). | G. Dictionary | `G02_dict_char_freq.py` |
| **80** | **Merge two dictionaries** into a single dictionary. Handle key conflicts by using values from the second dictionary. | G. Dictionary | `G03_dict_merge.py` |
| **81** | **Filter a dictionary** to include only items where the value is greater than a specified threshold. | G. Dict Comp | `G04_dict_filter_value.py` |
| **82** | **Invert a dictionary**: swap keys and values. Handle cases where multiple keys map to the same value (values become lists of keys). | G. Dictionary | `G05_dict_invert.py` |
| **83** | **Access nested data**: From a sample JSON API response (dictionary), extract a specific nested field (e.g., city name). | G. Dictionary | `G06_dict_nested_access.py` |
| **84** | Create a **Set** from a list to automatically **remove duplicate** elements. | G. Sets | `G07_set_remove_duplicates.py` |
| **85** | Perform **Set Operations**: Union, Intersection, and Difference between two sets of numbers. | G. Sets | `G08_set_operations.py` |
| **86** | Use a **Set Comprehension** to create a set of unique square roots of numbers from a list. | G. Set Comp | `G09_set_root_comp.py` |
| **87** | **List Comprehension with Conditional:** Create a new list containing only the even numbers from an existing list. | G. List Comp | `G10_list_comp_if.py` |
| **88** | **Nested List Comprehension:** Flatten a list of lists (a 2D structure) into a single 1D list. | G. List Comp | `G11_list_comp_nested.py` |
| **89** | Use a **Dictionary Comprehension** to swap the positions of keys and values for selected pairs in a dictionary. | G. Dict Comp | `G12_dict_comp_swap_filter.py` |

---
## Day 9: File Handling (Text I/O) (11 Programs)
Focus: Reading, writing, and basic analysis of text files.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **90** | **Write and create a text file** and input multi-line text into it from the user. | H. File I/O | `H01_file_write_text.py` |
| **91** | **Read a text file line by line** and print the content to the console. | H. File I/O | `H02_file_read_line.py` |
| **92** | **Count Characters, Spaces, and Lines** in a given text file. | H. File Analysis | `H03_file_analyze_char.py` |
| **93** | **Copy the content** of one text file into a brand new duplicate file. | H. File I/O | `H04_file_copy.py` |
| **94** | **Append new content** to the end of an existing text file. | H. File I/O | `H05_file_append.py` |
| **95** | Read a file containing numbers (one per line) and display the **total sum and average**. | H. File Analysis | `H06_file_sum_avg_numbers.py` |
| **96** | Read a file and replace all occurrences of a specific character (e.g., 'a') with another (e.g., 'x'). | H. File Update | `H07_file_replace_char.py` |
| **97** | **Filter file content:** Read a file with numbers (1 to 10), and write odd numbers to `ODD.txt` and even numbers to `EVEN.txt`. | H. File Filter | `H08_file_filter_odd_even.py` |
| **98** | Read a text file and count the number of **uppercase, lowercase, and digit characters**. | H. File Analysis | `H09_file_count_case.py` |
| **99** | Find the **size of a file in bytes** without reading its entire content (using `os` module). | H. File Analysis | `H10_file_size.py` |
| **100** | Read two filenames as command-line arguments and **copy the content** of the first file into the second. | H. Advanced | `H11_file_cli_copy.py` |

---
## Day 10: Advanced File Handling & String Analysis (12 Programs)
Focus: Word analysis, serialization, and advanced string problems.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **101** | **Word Frequency Counter:** Read a text file and compute the frequency of each word, displaying the output sorted alphabetically. | I. Text Analysis | `I01_file_word_frequency.py` |
| **102** | Read a file and store all found **special characters** (symbols) into a separate file. | I. Text Analysis | `I02_file_extract_symbols.py` |
| **103** | Read a file and find the **employee who earns the highest salary** based on a structured record (name, salary). | I. Text Analysis | `I03_file_highest_salary.py` |
| **104** | **Binary File:** Write structured data (e.g., a simple record) into a binary file using the `pickle` module. | I. Binary I/O | `I04_file_write_binary.py` |
| **105** | **Binary File:** Read the structured data written in the previous program from the binary file using `pickle`. | I. Binary I/O | `I05_file_read_binary.py` |
| **106** | **Positioning:** Demonstrate the use of `seek()`, `tell()`, and `truncate()` functions for file pointer management. | I. Advanced | `I06_file_seek_tell.py` |
| **107** | Read a list of names from the keyboard and **store them into a text file**. | I. File I/O | `I07_file_store_names.py` |
| **108** | **Caesar Cipher Encryption:** Implement the Caesar Cipher to encrypt an input string with a given shift key. | I. String Crypto | `I08_caesar_cipher_enc.py` |
| **109** | **Caesar Cipher Decryption:** Implement the Caesar Cipher to decrypt a given encrypted string with the known shift key. | I. String Crypto | `I09_caesar_cipher_dec.py` |
| **110** | **Brackets/Parentheses Checker:** Check if a string containing parentheses, braces, and brackets is **balanced and properly nested**. | I. Data Struct | `I10_balanced_brackets.py` |
| **111** | **String to Integer (atoi):** Implement a function to convert a string representation of an integer to its actual integer value, handling potential overflow, sign, and non-digit characters. | I. Advanced | `I11_string_to_int.py` |
| **112** | **Validate an IP Address:** Create a function to check if a given string is a valid IPv4 address. | I. Advanced | `I12_validate_ip.py` |

---
## Day 11: Exception Handling (11 Programs)
Focus: Robust code, error types, and custom exceptions.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **113** | Implement a basic `try...except` block to **handle a `ZeroDivisionError`**. | J. Exception | `J01_except_zero_division.py` |
| **114** | Implement a `try...except` block to **handle a `ValueError`** when converting a non-numeric input string to an integer. | J. Exception | `J02_except_value_error.py` |
| **115** | Use **Multiple `except` blocks** to handle different types of exceptions (`TypeError`, `IndexError`) in a single `try` block. | J. Exception | `J03_except_multiple.py` |
| **116** | Demonstrate the use of the **`finally` block** to execute cleanup code regardless of whether an exception occurred or not. | J. Exception | `J04_except_finally.py` |
| **117** | Use a `try...except...else` structure. The `else` block should execute only if **no exception** is raised. | J. Exception | `J05_except_else.py` |
| **118** | **Safely Read Configuration File:** Implement robust code using `try...except` to read a configuration file (`config.txt`) and handle `FileNotFoundError`. | J. Robustness | `J06_except_file_not_found.py` |
| **119** | **Raise a custom exception** (`InvalidAgeError`) using the `raise` keyword when the input age is negative or unrealistically high. | J. Custom Except | `J07_except_raise_custom.py` |
| **120** | **Custom Exception Class:** Define and use a custom exception class, inheriting from `Exception`, to provide meaningful error messages. | J. Custom Except | `J08_except_custom_class.py` |
| **121** | **Handling API Errors (Mock):** Simulate a robust function that handles potential dictionary `KeyError` or network-related exceptions during a mock API request. | J. Robustness | `J09_except_api_robust.py` |
| **122** | **SSH Connection Failure (Mock):** Simulate handling connection-related exceptions (like `TimeoutError`) when trying to connect to a remote server. | J. Robustness | `J10_except_ssh_mock.py` |
| **123** | **Argument Validation:** Use `try...except` to validate that a script received the correct number and type of command-line arguments. | J. Robustness | `J11_except_validate_args.py` |

---
## Day 12: Object-Oriented Programming (OOP) - Fundamentals (12 Programs)
Focus: Classes, Objects, Methods, and Constructors.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **124** | Define a simple **Class and Object** (`Student` class with `name` and `roll_number` attributes) and create an instance. | K. OOP Basics | `K01_class_object.py` |
| **125** | Implement a **Constructor (`__init__`)** in a class (`Car`) to initialize object attributes (color, model). | K. OOP Basics | `K02_class_constructor.py` |
| **126** | Add a **Method** to the `Car` class (e.g., `start_engine()`) that prints a message and access an attribute. | K. OOP Basics | `K03_class_method.py` |
| **127** | Create a `Circle` class with radius as an attribute and methods to calculate the **Area and Circumference**. | K. OOP Basics | `K04_class_circle.py` |
| **128** | Create a `Bank` class with methods for `deposit` and `withdraw` money, tracking the balance attribute. | K. OOP Basics | `K05_class_bank_system.py` |
| **129** | Define a class method (`@classmethod`) to create a new object using an alternative constructor (e.g., creating a `Date` object from a string). | K. OOP Basics | `K06_class_classmethod.py` |
| **130** | Define a static method (`@staticmethod`) that performs a utility function related to the class but doesn't need `self` or `cls` (e.g., `is_working_day`). | K. OOP Basics | `K07_class_staticmethod.py` |
| **131** | Demonstrate the use of the `__str__` magic method for a user-friendly **string representation** of an object. | K. OOP Basics | `K08_class_str_repr.py` |
| **132** | Implement the **Vending Machine** as a class, managing inventory (dictionary) and handling user transactions. | K. OOP Project | `K09_class_vending_machine.py` |
| **133** | Create a `Student` class and use a **dictionary of objects** to store records for multiple students. | K. OOP Data | `K10_class_dict_of_objects.py` |
| **134** | Implement the **Binary Search** algorithm as a method within a dedicated `Search` class. | K. OOP Algo | `K11_class_binary_search.py` |
| **135** | **Overload comparison operators** (`__lt__`, `__gt__`, `__eq__`) in a class (e.g., comparing two `Point` objects based on distance from origin). | K. OOP Advanced | `K12_class_operator_overload.py` |

---
## Day 13: Object-Oriented Programming (OOP) - Inheritance & Polymorphism (11 Programs)
Focus: Inheritance types, method overriding, and abstraction.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **136** | Demonstrate **Single Inheritance**: Create a `Vehicle` base class and a `Car` derived class. | L. Inheritance | `L01_single_inheritance.py` |
| **137** | Demonstrate **Multilevel Inheritance**: `Animal` $\to$ `Dog` $\to$ `Puppy`. | L. Inheritance | `L02_multilevel_inheritance.py` |
| **138** | Demonstrate **Hierarchical Inheritance**: One base class (`Shape`) inherited by multiple derived classes (`Circle`, `Square`). | L. Inheritance | `L03_hierarchical_inheritance.py` |
| **139** | Demonstrate **Polymorphism** using **Method Overriding**: Base class `speak()` method is overridden in derived classes (`Dog`, `Cat`). | L. Polymorphism | `L04_method_overriding.py` |
| **140** | Demonstrate **Polymorphism** using **Duck Typing** (two unrelated classes having the same method name, `fly()`). | L. Polymorphism | `L05_duck_typing.py` |
| **141** | Simulate **Method Overloading** using default arguments or by checking argument types/counts within a single Python method. | L. Polymorphism | `L06_method_overloading.py` |
| **142** | Use the `super()` function in the derived class constructor (`__init__`) to call the parent class constructor. | L. Inheritance | `L07_super_function.py` |
| **143** | Implement an **Abstract Base Class (ABC)** (`Shape`) that defines an abstract method (`area()`) which must be implemented by subclasses. | L. Abstraction | `L08_abstract_class.py` |
| **144** | Demonstrate **Data Hiding/Encapsulation** using single (`_variable`) and double (`__variable`) leading underscores. | L. Encapsulation | `L09_data_encapsulation.py` |
| **145** | Create a **Mixin Class** (`LoggableMixin`) to add reusable logging functionality to multiple, unrelated classes. | L. OOP Advanced | `L10_mixin_class.py` |
| **146** | Implement a basic **Adapter Design Pattern** where an existing class's interface is converted to another one expected by a client. | L. OOP Design | `L11_adapter_pattern.py` |

---
## Day 14: Data Structures - Arrays/Lists (12 Programs)
Focus: Fundamental list operations and search algorithms.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **147** | Input $N$ elements into a list and print them, then implement a **Linear Search** to find a target value. | M. List Basics | `M01_list_linear_search.py` |
| **148** | Input $N$ elements and find the **sum and average** of all elements in the list. | M. List Basics | `M02_list_sum_avg.py` |
| **149** | Find the **Largest (Maximum) and Smallest (Minimum)** value from a list of $N$ elements. | M. List Basics | `M03_list_max_min.py` |
| **150** | Count how many elements in a list are **positive, negative, even, and odd**. | M. List Logic | `M04_list_count_stats.py` |
| **151** | **Copy the elements** of one list into a new list. (Shallow vs. Deep copy explanation in comments). | M. List Ops | `M05_list_copy_elements.py` |
| **152** | Arrange the elements of a list in **reverse order** (without using `list.reverse()` or slicing). | M. List Ops | `M06_list_reverse_manual.py` |
| **153** | **Insert an element** into the list at a user-defined position (index). | M. List Ops | `M07_list_insert_at_pos.py` |
| **154** | **Delete an element** from the list at a user-defined position (index). | M. List Ops | `M08_list_delete_at_pos.py` |
| **155** | **Merge two lists** ($A$ and $B$) into a third, combined list ($C$). | M. List Ops | `M09_list_merge_two.py` |
| **156** | Perform **vector addition** on two lists of equal size $C = A + B$. | M. List Ops | `M10_list_vector_add.py` |
| **157** | Implement the **Binary Search** algorithm **without using recursion**. | M. Search | `M11_binary_search_iter.py` |
| **158** | Implement the **Binary Search** algorithm **using recursion**. | M. Search | `M12_binary_search_rec.py` |

---
## Day 15: Matrices (2D Lists) (11 Programs)
Focus: Representing and manipulating 2D data structures.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **159** | Create and print a simple **$3 \times 3$ matrix** (nested list). | N. Matrix Basics | `N01_matrix_3x3_print.py` |
| **160** | **Add two matrices** (of the same dimensions, e.g., $3 \times 3$). | N. Matrix Ops | `N02_matrix_add.py` |
| **161** | **Subtract two matrices** (of the same dimensions). | N. Matrix Ops | `N03_matrix_subtract.py` |
| **162** | **Multiply two matrices** ($A \times B$). Include validation for compatible dimensions. | N. Matrix Ops | `N04_matrix_multiply.py` |
| **163** | Find the **Transpose** of a given matrix. | N. Matrix Ops | `N05_matrix_transpose.py` |
| **164** | Calculate the **Sum of all elements** in a matrix. | N. Matrix Ops | `N06_matrix_sum_elements.py` |
| **165** | Calculate the **Sum of elements** along the **main diagonal** of a square matrix. | N. Matrix Ops | `N07_matrix_diag_sum.py` |
| **166** | Create a function to **initialize a matrix with random values**. | N. Matrix Utility | `N08_matrix_random_init.py` |
| **167** | **Multiply two matrices** using list comprehensions for a more concise solution. | N. Matrix Comp | `N09_matrix_multiply_comp.py` |
| **168** | **Matrix Rotation:** Rotate a square matrix 90 degrees clockwise in place. | N. Matrix Advanced | `N10_matrix_rotate_90.py` |
| **169** | **Saddle Point:** Find a Saddle Point in a matrix (an element that is the minimum in its row and maximum in its column). | N. Matrix Advanced | `N11_matrix_saddle_point.py` |

---
## Day 16: Sorting Algorithms (11 Programs)
Focus: Implementing classic sorting techniques from scratch.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **170** | Implement **Bubble Sort** to arrange a list in **ascending order**. | O. Sorting | `O01_sort_bubble_asc.py` |
| **171** | Implement **Bubble Sort** to arrange a list in **descending order**. | O. Sorting | `O02_sort_bubble_desc.py` |
| **172** | Implement **Selection Sort** to arrange a list in ascending order. | O. Sorting | `O03_sort_selection.py` |
| **173** | Implement **Insertion Sort** to arrange a list in ascending order. | O. Sorting | `O04_sort_insertion.py` |
| **174** | Implement **Quick Sort** (choose pivot, partition, recurse) to arrange a list in ascending order. | O. Sorting | `O05_sort_quick.py` |
| **175** | Implement **Merge Sort** (divide and conquer) to arrange a list in ascending order. | O. Sorting | `O06_sort_merge.py` |
| **176** | Implement **Shell Sort** to arrange a list in ascending order. | O. Sorting | `O07_sort_shell.py` |
| **177** | Sort a list of **strings** in **descending order** (lexicographically). | O. Sorting | `O08_sort_strings_desc.py` |
| **178** | **Counting Sort:** Implement a basic counting sort algorithm for a list of small positive integers. | O. Sorting | `O09_sort_counting.py` |
| **179** | **Radix Sort:** Implement Radix Sort for sorting a list of integers. | O. Sorting | `O10_sort_radix.py` |
| **180** | **Sort Objects:** Sort a list of custom objects (e.g., `Employee` objects) based on an attribute (e.g., salary) using the `key` argument. | O. Sorting | `O11_sort_objects_key.py` |

---
## Day 17: Data Structures - Stack (12 Programs)
Focus: LIFO principle and classic Stack applications.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **181** | Implement a **Stack** using a Python `list` with basic `push`, `pop`, and `display` operations. | P. Stack | `P01_stack_basic_list.py` |
| **182** | Add **`peek`** (view top element without removal) and **`is_empty`** methods to the Stack implementation. | P. Stack | `P02_stack_peek_empty.py` |
| **183** | Write a program to **reverse a string** using a Stack data structure. | P. Stack App | `P03_stack_reverse_string.py` |
| **184** | Use a Stack to check if a sequence of parentheses/brackets is **Balanced**. (Revisiting I10 with Stack implementation). | P. Stack App | `P04_stack_balanced_brackets.py` |
| **185** | Calculate the **Factorial** of a number using the Stack concept (simulating recursion/call stack). | P. Stack App | `P05_stack_factorial.py` |
| **186** | Calculate the **Power of a Number** ($x^y$) using the Stack concept. | P. Stack App | `P06_stack_power_of_num.py` |
| **187** | Convert an **Infix** expression to a **Postfix** expression using a Stack. | P. Stack Adv | `P07_stack_infix_to_postfix.py` |
| **188** | Evaluate a **Postfix** expression using a Stack. | P. Stack Adv | `P08_stack_evaluate_postfix.py` |
| **189** | Find the **Next Greater Element** for every element in a list using a Stack. | P. Stack Adv | `P09_stack_next_greater.py` |
| **190** | Implement a Stack that supports `push`, `pop`, and also a method `getMin()` that returns the **minimum element** in $O(1)$ time. | P. Stack Adv | `P10_stack_get_min_O1.py` |
| **191** | Implement a Stack using the `collections.deque` module for **faster** append/pop operations. | P. Stack Impl | `P11_stack_deque.py` |
| **192** | Implement a **Limited-Size Stack** that raises an exception when trying to push onto a full stack. | P. Stack Impl | `P12_stack_limited_size.py` |

---
## Day 18: Data Structures - Queue (11 Programs)
Focus: FIFO principle, deque, and advanced Queue types.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **193** | Implement a simple **Queue** using a Python `list` with `insert` (enqueue) and `delete` (dequeue) operations. | Q. Queue | `Q01_queue_basic_list.py` |
| **194** | Implement a Queue using the **`collections.deque`** for efficient FIFO operations. | Q. Queue Impl | `Q02_queue_deque.py` |
| **195** | Implement a **Simple Queue** using a Python `class` structure with methods: `insert()`, `delete()`, `display()`, and `is_empty()`. | Q. Queue | `Q03_queue_class.py` |
| **196** | Implement a **Circular Queue** using a list and indices to handle wraparound. | Q. Queue Adv | `Q04_queue_circular.py` |
| **197** | Implement a **Priority Queue** using the `heapq` module. Insert elements with priorities and extract the highest priority element. | Q. Queue Adv | `Q05_queue_priority_heapq.py` |
| **198** | Use a Queue to perform **Breadth-First Search (BFS)** on a simple mock graph (adjacency list). | Q. Queue App | `Q06_queue_bfs_mock.py` |
| **199** | Implement a **Double-Ended Queue (Deque)** using `collections.deque` and demonstrate adding/removing from both ends. | Q. Queue Adv | `Q07_queue_deque_all_ops.py` |
| **200** | **Queue from Stacks:** Implement a Queue data structure using two Stacks. | Q. Queue Impl | `Q08_queue_from_stacks.py` |
| **201** | **Circular Tour Problem:** Given a list of petrol pumps, find the starting point of a circular tour using a Queue/loop. | Q. Queue Adv | `Q09_queue_circular_tour.py` |
| **202** | **First Non-Repeating Character in a Stream:** Use a Queue to efficiently find the first non-repeating character in a mock stream of characters. | Q. Queue Adv | `Q10_queue_first_non_repeat.py` |
| **203** | Use the `multiprocessing.Queue` to demonstrate **safe inter-process communication** between a producer and a consumer function. | Q. Queue Adv | `Q11_queue_multiprocessing.py` |

---
## Day 19: Data Structures - Singly Linked List (12 Programs)
Focus: Node structures, traversal, and core list manipulations.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **204** | Define a `Node` class and a basic `SinglyLinkedList` class to **create and display** a linked list. | R. SLL Basics | `R01_sll_create_display.py` |
| **205** | Implement **insertion at the beginning** (`insert_at_start`) of the Singly Linked List. | R. SLL Ops | `R02_sll_insert_start.py` |
| **206** | Implement **insertion at the end** (`insert_at_end`) of the Singly Linked List. | R. SLL Ops | `R03_sll_insert_end.py` |
| **207** | Implement **insertion after a specific node** (`insert_after_node`). | R. SLL Ops | `R04_sll_insert_after.py` |
| **208** | Implement **deletion of the first node** (`delete_start`). | R. SLL Ops | `R05_sll_delete_start.py` |
| **209** | Implement **deletion of the last node** (`delete_end`). | R. SLL Ops | `R06_sll_delete_end.py` |
| **210** | Implement **deletion of a node by value** (`delete_by_value`). | R. SLL Ops | `R07_sll_delete_by_value.py` |
| **211** | **Count the number of nodes** available in the linked list. | R. SLL Utility | `R08_sll_count_nodes.py` |
| **212** | **Reverse the Singly Linked List** (iterative approach). | R. SLL Adv | `R09_sll_reverse.py` |
| **213** | **Find the Middle Node** of the linked list in a single pass. | R. SLL Adv | `R10_sll_find_middle.py` |
| **214** | Detect if the linked list contains a **Cycle** (loop) using Floyd's Tortoise and Hare algorithm. | R. SLL Adv | `R11_sll_detect_cycle.py` |
| **215** | Given two non-empty linked lists representing two non-negative integers (digits stored in reverse order), **add the two numbers** and return the sum as a new linked list. | R. SLL Leet | `R12_sll_add_two_numbers.py` |

---
## Day 20: Data Structures - Doubly and Circular Linked Lists (11 Programs)
Focus: Two-way traversal and circular connections.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **216** | Define a `DoublyNode` class and a basic `DoublyLinkedList` class to **create and display** a Doubly Linked List (DLL). | S. DLL Basics | `S01_dll_create_display.py` |
| **217** | Implement **insertion at the beginning** (`insert_at_start`) of the DLL. | S. DLL Ops | `S02_dll_insert_start.py` |
| **218** | Implement **insertion at the end** (`insert_at_end`) of the DLL. | S. DLL Ops | `S03_dll_insert_end.py` |
| **219** | Implement **insertion before a specific node** (`insert_before_node`) in the DLL. | S. DLL Ops | `S04_dll_insert_before.py` |
| **220** | Implement **deletion of a node by value** in the DLL. | S. DLL Ops | `S05_dll_delete_by_value.py` |
| **221** | Define a `CircularSinglyLinkedList` (CSLL) to **create and display** a circular linked list. | S. CLL Basics | `S06_csll_create_display.py` |
| **222** | Implement **insertion at the beginning** of the CSLL. | S. CLL Ops | `S07_csll_insert_start.py` |
| **223** | Implement **insertion at the end** of the CSLL. | S. CLL Ops | `S08_csll_insert_end.py` |
| **224** | Implement **insertion after a specific node** in the CSLL. | S. CLL Ops | `S09_csll_insert_after.py` |
| **225** | Implement **deletion of a node by value** in the CSLL. | S. CLL Ops | `S10_csll_delete_by_value.py` |
| **226** | **Traverse the DLL in reverse order** starting from the tail node. | S. DLL Utility | `S11_dll_reverse_traverse.py` |

---
## Day 21: Data Structures - Trees (11 Programs)
Focus: Binary Tree structure and various traversal algorithms.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **227** | Define a `Node` class and a basic `BinaryTree` class to **create a simple binary tree**. | T. Tree Basics | `T01_tree_create_basic.py` |
| **228** | Implement **In-order Traversal** (Left $\to$ Root $\to$ Right) on a Binary Tree (recursive). | T. Tree Traversal | `T02_tree_traverse_inorder.py` |
| **229** | Implement **Pre-order Traversal** (Root $\to$ Left $\to$ Right) on a Binary Tree (recursive). | T. Tree Traversal | `T03_tree_traverse_preorder.py` |
| **230** | Implement **Post-order Traversal** (Left $\to$ Right $\to$ Root) on a Binary Tree (recursive). | T. Tree Traversal | `T04_tree_traverse_postorder.py` |
| **231** | Implement **Level-order Traversal** (Breadth-First) on a Binary Tree using a Queue. | T. Tree Traversal | `T05_tree_traverse_level.py` |
| **232** | Implement the **insertion of a node** into a **Binary Search Tree (BST)**. | T. BST Ops | `T06_bst_insert_node.py` |
| **233** | Implement the **search** for a specific value in a BST. | T. BST Ops | `T07_bst_search_value.py` |
| **234** | Implement the calculation of the **Height of the Tree** (maximum depth). | T. Tree Utility | `T08_tree_calculate_height.py` |
| **235** | Implement the calculation of the **Total Number of Nodes** in the Tree. | T. Tree Utility | `T09_tree_count_nodes.py` |
| **236** | Implement the **deletion of a node** from a BST, handling 0, 1, and 2 children cases. | T. BST Adv | `T10_bst_delete_node.py` |
| **237** | Check if a given Binary Tree is a valid **Binary Search Tree (BST)**. | T. Tree Adv | `T11_tree_is_bst.py` |

---
## Day 22: Advanced Algorithms & Math (11 Programs)
Focus: Fundamental mathematical algorithms and classic coding problems.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **238** | Find the **Greatest Common Divisor (GCD)** of two numbers using the Euclidean algorithm (recursive). | U. Math | `U01_math_gcd_recursive.py` |
| **239** | Find the **Greatest Common Divisor (GCD)** of two numbers using an iterative approach. | U. Math | `U02_math_gcd_iterative.py` |
| **240** | Find the **Least Common Multiple (LCM)** of two numbers. | U. Math | `U03_math_lcm.py` |
| **241** | Find the **Smallest Common Divisor (SCD)** for a given number (this is essentially the smallest prime factor, or 1 if prime). | U. Math | `U04_math_smallest_divisor.py` |
| **242** | Check if a given number is a **Perfect Number** (sum of its proper positive divisors is equal to the number itself). | U. Math | `U05_math_perfect_number.py` |
| **243** | Find the **Missing Number** in a sequence of $N$ consecutive numbers (e.g., in `[1, 2, 4, 5]`, find 3). | U. Algo | `U06_algo_missing_number.py` |
| **244** | Find the **Kth Largest Element** in a list (without sorting the entire list). | U. Algo | `U07_algo_kth_largest.py` |
| **245** | Find the **Majority Element** in a list (the one that appears more than $\lfloor n/2 \rfloor$ times). | U. Algo | `U08_algo_majority_element.py` |
| **246** | Implement **Climbing Stairs**: Given $N$ stairs, find the number of distinct ways to climb to the top if you can take 1 or 2 steps at a time. | U. Algo | `U09_algo_climbing_stairs.py` |
| **247** | Implement the **Coin Change Problem**: Given a set of coin denominations and a total amount, find the minimum number of coins needed to make up that amount (Dynamic Programming approach). | U. Algo Adv | `U10_algo_coin_change.py` |
| **248** | **Container With Most Water:** Find two lines in a list that, along with the x-axis, form a container that holds the most water. | U. Algo Adv | `U11_algo_container_water.py` |

---
## Day 23: Recursion and Backtracking (11 Programs)
Focus: Recursive thinking and exploration algorithms.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **249** | Find the **maximum and minimum** number from a list using **recursion**. | V. Recursion | `V01_rec_max_min_list.py` |
| **250** | Calculate the **power of a number** ($x^y$) using recursion. | V. Recursion | `V02_rec_power_of_num.py` |
| **251** | **Reverse a given integer** using recursion (digit manipulation). | V. Recursion | `V03_rec_reverse_integer.py` |
| **252** | **Reverse a string** using recursion. | V. Recursion | `V04_rec_reverse_string.py` |
| **253** | **Check for Palindrome** (string) using recursion. | V. Recursion | `V05_rec_palindrome_check.py` |
| **254** | **Generate All Permutations** of a list of unique numbers using backtracking. | V. Backtracking | `V06_back_generate_permutations.py` |
| **255** | **Generate All Subsets** (Power Set) of a list of numbers using backtracking. | V. Backtracking | `V07_back_generate_subsets.py` |
| **256** | Implement the **N-Queens Problem** using backtracking to find all safe placements of $N$ queens on an $N \times N$ chessboard. | V. Backtracking | `V08_back_n_queens.py` |
| **257** | Implement a basic **Sudoku Solver** using backtracking. | V. Backtracking | `V09_back_sudoku_solver.py` |
| **258** | **Letter Combinations of a Phone Number:** Given a string containing digits from 2-9, return all possible letter combinations that the number could represent. | V. Backtracking | `V10_back_phone_combinations.py` |
| **259** | Implement **Depth-First Search (DFS)** traversal on a simple graph using recursion. | V. Recursion App | `V11_rec_dfs_mock.py` |

---
## Day 24: Project 1: Command Line Interface (CLI) Games (11 Programs)
Focus: Applying basic logic to build fun, interactive terminal applications.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **260** | **Band Name Generator:** CLI script that asks for a city name and a pet name, then combines them to suggest a band name. | W. CLI Project | `W01_cli_band_name_gen.py` |
| **261** | **Tip Calculator:** CLI script that takes total bill, tip percentage, and number of people, then calculates how much each person pays. | W. CLI Project | `W02_cli_tip_calculator.py` |
| **262** | **Rock, Paper, Scissors:** A CLI game where the user plays against the computer. | W. CLI Game | `W03_cli_rock_paper_scissors.py` |
| **263** | **Treasure Island - Choose Your Own Adventure:** A simple interactive story game using conditional logic and user input. | W. CLI Game | `W04_cli_treasure_island.py` |
| **264** | **PyPassword Generator:** CLI script that generates a random, strong password based on user-specified length and inclusion of letters, symbols, and numbers. | W. CLI Project | `W05_cli_password_generator.py` |
| **265** | **Number Guessing Game:** CLI game where the computer selects a random number and the user has limited attempts to guess it. | W. CLI Game | `W06_cli_number_guesser.py` |
| **266** | **Blackjack (Simplified):** A text-based, simplified version of the card game Blackjack. | W. CLI Game | `W07_cli_blackjack_simple.py` |
| **267** | **Higher Lower Game:** CLI game where the user guesses which of two entities has a higher attribute (e.g., follower count). | W. CLI Game | `W08_cli_higher_lower.py` |
| **268** | **Text-Based Tic Tac Toe:** A simple 3x3 grid game played between two human players in the terminal. | W. CLI Game | `W09_cli_tictactoe.py` |
| **269** | **Secret Auction:** CLI script that uses a dictionary to track bids and finds the highest bidder (blind auction). | W. CLI Project | `W10_cli_secret_auction.py` |
| **270** | **Text to Morse Code Converter:** A script that takes a string input and converts it to Morse code using a dictionary lookup. | W. CLI Project | `W11_cli_morse_converter.py` |

---
## Day 25: Project 2: Command Line Interface (CLI) Applications (11 Programs)
Focus: Building utility scripts and refactoring with OOP principles.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **271** | **Calculator (Advanced CLI):** A script that implements recursive calculation capabilities (allows continuous operations). | X. CLI App | `X01_cli_calculator_adv.py` |
| **272** | **The Coffee Machine (CLI):** A simulation of a coffee machine that manages resources (water, milk, coffee) and handles transactions. | X. CLI App | `X02_cli_coffee_machine.py` |
| **273** | **OOP Version of the Coffee Machine:** Reimplement the coffee machine using Classes and Objects for better structure and state management. | X. OOP App | `X03_oop_coffee_machine.py` |
| **274** | **The Quiz Game (CLI/OOP):** An OOP-based true/false quiz game that loads questions from a list and tracks the user's score. | X. OOP App | `X04_oop_quiz_game.py` |
| **275** | **Disappearing Text Writing App (CLI concept):** A function that starts a timer; if the user stops typing for 5 seconds, all current text is cleared. | X. CLI App | `X05_cli_disappearing_text.py` |
| **276** | **Automated Folder Backup (Basic `os`):** A script using the `os` module to copy a source directory's files to a destination directory. | X. System Tool | `X06_tool_folder_backup.py` |
| **277** | **System Monitoring Mock:** A script that periodically checks mock server health statuses (OK/Error) and logs the output. | X. System Tool | `X07_tool_system_monitor_mock.py` |
| **278** | **Cleaning Up Old Log Files:** A script using the `os` and `datetime` modules to delete files in a specified directory that are older than 30 days. | X. System Tool | `X08_tool_clean_old_logs.py` |
| **279** | **Automating Git Status Check:** A script that iterates through a list of directories and uses the `subprocess` module to run `git status` in each. | X. System Tool | `X09_tool_git_status.py` |
| **280** | **Validate YAML/JSON Configuration:** A script that uses the `json` module to load and validate the syntax of a given JSON file. | X. System Tool | `X10_tool_validate_json.py` |
| **281** | **Calculate File Checksum (SHA-256):** A script using the `hashlib` module to calculate and print the SHA-256 hash of a specified file. | X. System Tool | `X11_tool_file_checksum.py` |

---
## Day 26: Project 3: GUI Development with Tkinter (12 Programs)
Focus: Building desktop apps with simple graphical user interfaces.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **282** | **Mile to Kilometer Converter:** A simple Tkinter GUI with an input box, a button, and a label to perform the conversion. | Y. Tkinter GUI | `Y01_tk_mile_to_km_converter.py` |
| **283** | **Simple GUI Window:** Create a basic Tkinter window with a title, size, and a central label. | Y. Tkinter GUI | `Y02_tk_basic_window.py` |
| **284** | **Button and Event Handling:** Create a button that changes a label's text when clicked. | Y. Tkinter GUI | `Y03_tk_button_event.py` |
| **285** | **Input/Entry Widget:** Create a Tkinter entry field and retrieve the text entered by the user. | Y. Tkinter GUI | `Y04_tk_entry_input.py` |
| **286** | **Grid Layout Manager:** Arrange widgets (labels, buttons, inputs) in a responsive grid structure. | Y. Tkinter GUI | `Y05_tk_grid_layout.py` |
| **287** | **Pomodoro Timer (Basic):** A Tkinter app with a Start/Stop button and a timer display (no breaks yet). | Y. Tkinter Project | `Y06_tk_pomodoro_basic.py` |
| **288** | **Pomodoro Timer (Advanced):** Add functionality for Work, Short Break, and Long Break periods. | Y. Tkinter Project | `Y07_tk_pomodoro_adv.py` |
| **289** | **Password Manager (Data Entry):** Tkinter app that collects website, email, and password, and prints the data to the console. | Y. Tkinter Project | `Y08_tk_password_manager_entry.py` |
| **290** | **Password Manager (JSON Storage):** Update the manager to save credentials securely to a JSON file. | Y. Tkinter Project | `Y09_tk_password_manager_json.py` |
| **291** | **Password Manager (Search):** Add a search button to retrieve and display credentials for a given website from the JSON file. | Y. Tkinter Project | `Y10_tk_password_manager_search.py` |
| **292** | **Flash Card App (GUI Logic):** Tkinter app that displays a word on the front, flips to show the translation after a delay, and presents the next card. | Y. Tkinter Project | `Y11_tk_flash_card_logic.py` |
| **293** | **Image Watermarking App (Basic):** Tkinter app that allows a user to upload an image and add a simple text watermark to it. | Y. Tkinter Project | `Y12_tk_image_watermarker.py` |

---
## Day 27: Project 4: Turtle Graphics (11 Programs)
Focus: Using the Turtle library for drawing, animations, and game development.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **294** | **Basic Turtle Drawing:** Create a turtle window and draw a simple square shape. | Z. Turtle Graphics | `Z01_turtle_draw_square.py` |
| **295** | **Drawing Dashed Line:** Use the `penup()` and `pendown()` methods to draw a dashed line. | Z. Turtle Graphics | `Z02_turtle_dashed_line.py` |
| **296** | **Drawing Geometric Shapes:** Use a loop to draw an equilateral triangle, square, pentagon, hexagon, etc., up to a decagon. | Z. Turtle Graphics | `Z03_turtle_geometric_shapes.py` |
| **297** | **Random Walk:** Make the turtle move in random directions and draw with random colors. | Z. Turtle Graphics | `Z04_turtle_random_walk.py` |
| **298** | **Spirograph/Hirst Painting:** Draw a series of interlocking circles with varying colors to create a complex pattern (like a Hirst spot painting). | Z. Turtle Graphics | `Z05_turtle_spirograph.py` |
| **299** | **Turtle Racing Game (Setup):** Create multiple turtle objects, assign them random colors, and set them up at a starting line. | Z. Turtle Project | `Z06_turtle_race_setup.py` |
| **300** | **Turtle Racing Game (Logic):** Implement the race logic where each turtle moves a random distance per turn, and declare the winner. | Z. Turtle Project | `Z07_turtle_race_logic.py` |
| **301** | **Snake Game (Part 1 - Head & Movement):** Create the snake's head and implement basic forward movement and turning controls (keyboard input). | Z. Turtle Project | `Z08_turtle_snake_part1.py` |
| **302** | **Snake Game (Part 2 - Body & Food):** Add the body segments, segment following logic, and create food that the snake can consume. | Z. Turtle Project | `Z09_turtle_snake_part2.py` |
| **303** | **Pong Game (Setup):** Create the screen, paddles, ball, and scoreboards. | Z. Turtle Project | `Z10_turtle_pong_setup.py` |
| **304** | **Pong Game (Physics):** Implement ball movement, wall collision detection, and paddle collision detection. | Z. Turtle Project | `Z11_turtle_pong_physics.py` |

---
## Day 28: Project 5: CSV and Data Analysis Basics (11 Programs)
Focus: Handling structured data using the `csv` module and introducing `pandas`.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **305** | **Reading a CSV File:** Use Python's built-in `csv` module to read data from a CSV file. | AA. CSV | `AA01_csv_read_basic.py` |
| **306** | **Reading CSV with `pandas`:** Use the `pandas` library to read and display the head of a CSV file (e.g., weather data). | AA. Pandas | `AA02_pd_read_csv.py` |
| **307** | **Data Series Access:** Using Pandas, access and print a single column (Series) from the loaded data. | AA. Pandas | `AA03_pd_access_series.py` |
| **308** | **Data Filtering:** Use Pandas to filter the DataFrame based on a condition (e.g., all rows where temperature is above 20 degrees). | AA. Pandas | `AA04_pd_filter_data.py` |
| **309** | **Data Conversion:** Use Pandas to calculate the mean (average) of a numeric column. | AA. Pandas | `AA05_pd_calculate_mean.py` |
| **310** | **Creating a DataFrame:** Create a Pandas DataFrame from a Python dictionary and save it to a new CSV file. | AA. Pandas | `AA06_pd_create_save_csv.py` |
| **311** | **US States Game (Data Prep):** Load the US states CSV and create a dictionary mapping state names to their coordinates. | AA. Project | `AA07_us_states_data_prep.py` |
| **312** | **US States Game (Turtle Integration):** Use the Turtle library to display the map image and place the user's correct guess name at the correct coordinate. | AA. Project | `AA08_us_states_turtle_draw.py` |
| **313** | **NATO Phonetic Alphabet Generator (Setup):** Load a CSV file containing letter-to-code mapping and create a dictionary from it. | AA. Project | `AA09_nato_data_load.py` |
| **314** | **NATO Phonetic Alphabet Generator (Logic):** Take a word input from the user and convert it into a list of NATO phonetic codes (e.g., "W-H-I-S-K-E-Y"). | AA. Project | `AA10_nato_generator.py` |
| **315** | **Error Handling in Pandas:** Use `try...except` to handle a `KeyError` when trying to access a non-existent column in a DataFrame. | AA. Pandas | `AA11_pd_except_keyerror.py` |

---
## Day 29: Project 6: Automated Email and HTTP Requests (12 Programs)
Focus: Networking, sending emails (`smtplib`), and making HTTP requests (`requests`).

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **316** | **Basic Email Sending (`smtplib`):** Use `smtplib` to connect to an SMTP server (e.g., Gmail) and send a simple plain-text email. | BB. Networking | `BB01_smtp_send_basic_email.py` |
| **317** | **Automated Birthday Wisher (Data Load):** Use Pandas to load a CSV of names and birthdays. | BB. Email App | `BB02_bday_wisher_data.py` |
| **318** | **Automated Birthday Wisher (Logic):** Check if today matches any birthday in the data and send a personalized email using a random quote/template. | BB. Email App | `BB03_bday_wisher_logic.py` |
| **319** | **Basic GET Request (`requests`):** Use the `requests` library to make a simple GET request to a public API (e.g., JSON Placeholder) and print the status code and text. | BB. Requests | `BB04_req_basic_get.py` |
| **320** | **ISS Overhead Notifier (API Call):** Query the ISS position API to get the current location and next overhead time for a given latitude/longitude. | BB. Requests App | `BB05_req_iss_api.py` |
| **321** | **ISS Overhead Notifier (Full App):** Combine the API call with `smtplib` to send an email notification when the ISS is overhead and it is dark outside. | BB. Requests App | `BB06_req_iss_notifier.py` |
| **322** | **Quizzler App (API Fetch):** Use `requests` to fetch 10 random True/False questions from the Open Trivia Database API. | BB. Requests App | `BB07_req_trivia_fetch.py` |
| **323** | **Rain Alert App (One Call API):** Use a weather API (mock) to check the forecast for the next 12 hours. | BB. Requests App | `BB08_req_weather_api.py` |
| **324** | **Rain Alert App (Twilio SMS Mock):** If rain is predicted, use Twilio (mock) to send an SMS alert (or print the message to console). | BB. Requests App | `BB09_req_twilio_mock.py` |
| **325** | **Checking the Health of a Web Service:** Use `requests` to make a GET request and check if the HTTP status code is 200 (OK). | BB. DevOps | `BB10_req_check_service_health.py` |
| **326** | **Automating GitHub: Creating a New Repository (Mock):** Simulate a POST request to the GitHub API to create a new repo. | BB. Requests Adv | `BB11_req_github_mock_post.py` |
| **327** | **Sending Notifications to Slack via Webhooks (Mock):** Use `requests` to send a formatted JSON payload to a mock Slack webhook URL. | BB. DevOps | `BB12_req_slack_webhook.py` |

---
## Day 30: Project 7: Web Scraping - BeautifulSoup (11 Programs)
Focus: Parsing HTML content to extract meaningful data.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **328** | **Basic HTML Parsing (`bs4`):** Use `BeautifulSoup` to parse a local HTML file (mock content) and print the title tag. | CC. Web Scraping | `CC01_bs4_basic_parse.py` |
| **329** | **Find Element by Tag:** Use `find()` to locate and print the content of the first `<p>` tag in a mock HTML page. | CC. Web Scraping | `CC02_bs4_find_tag.py` |
| **330** | **Find All Elements:** Use `find_all()` to extract all anchor tags (`<a>`) and print their text content and `href` attributes. | CC. Web Scraping | `CC03_bs4_find_all_links.py` |
| **331** | **Find Element by Class/ID:** Use selectors to find an element with a specific CSS class or ID. | CC. Web Scraping | `CC04_bs4_find_by_selector.py` |
| **332** | **CSS Selector (Advanced):** Use the `select()` method to find all elements matching a complex CSS selector (e.g., `div > p.highlight`). | CC. Web Scraping | `CC05_bs4_css_selector.py` |
| **333** | **Top 100 Movies Scraper (Data Fetch):** Use `requests` to fetch the HTML content of a public list of top 100 movies. | CC. Project | `CC06_bs4_movies_fetch.py` |
| **334** | **Top 100 Movies Scraper (Data Extract):** Use `BeautifulSoup` to extract the title and year of all 100 movies. | CC. Project | `CC07_bs4_movies_extract.py` |
| **335** | **Amazon Price Tracker (Setup):** Scrape the current price of a single product page (mock data) and convert the string price to a float. | CC. Project | `CC08_bs4_price_tracker_extract.py` |
| **336** | **Amazon Price Tracker (Alert Logic):** If the scraped price is below a target price, send an email alert using `smtplib` (mock). | CC. Project | `CC09_bs4_price_tracker_alert.py` |
| **337** | **Extracting Table Data:** Scrape a mock HTML table and extract the content row by row into a list of lists. | CC. Web Scraping | `CC10_bs4_extract_table.py` |
| **338** | **Handling Empty/Missing Tags:** Implement robust error handling (e.g., checking if the result of `find()` is `None`) when scraping elements that might not exist. | CC. Web Scraping | `CC11_bs4_robust_handling.py` |

---
## Day 31: Project 8: Web Automation - Selenium (12 Programs)
Focus: Automating browser interaction for complex tasks.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **339** | **Basic WebDriver Setup:** Set up the Selenium WebDriver (mocking the driver manager) and open a website (e.g., Python.org). | DD. Selenium | `DD01_selenium_basic_setup.py` |
| **340** | **Find Element by ID:** Use `find_element(By.ID, ...)` to locate and print the text of an element on a mock page. | DD. Selenium | `DD02_selenium_find_by_id.py` |
| **341** | **Find Element by CSS Selector:** Use `find_element(By.CSS_SELECTOR, ...)` to locate an element using a CSS selector path. | DD. Selenium | `DD03_selenium_find_by_css.py` |
| **342** | **Find Elements by XPath:** Use `find_elements(By.XPATH, ...)` to locate multiple elements using an XPath expression. | DD. Selenium | `DD04_selenium_find_by_xpath.py` |
| **343** | **Clicking and Interacting:** Navigate to a mock login page, find the login button, and click it. | DD. Selenium | `DD05_selenium_click_button.py` |
| **344** | **Form Submission:** Locate a search bar/input field, type text into it (`send_keys`), and submit the form. | DD. Selenium | `DD06_selenium_form_submit.py` |
| **345** | **Automated Gym Booking Bot (Mock Login):** Simulate the process of logging into a system with credentials. | DD. Project | `DD07_selenium_gym_login_mock.py` |
| **346** | **Automated Gym Booking Bot (Booking Logic):** After logging in, navigate to a booking calendar and click a specific time slot button. | DD. Project | `DD08_selenium_gym_booking_logic.py` |
| **347** | **Auto Tinder Swiping Bot (Mock):** Simulate finding and clicking the 'like' or 'dislike' buttons repeatedly. | DD. Project | `DD09_selenium_tinder_swipe.py` |
| **348** | **Automated Internet Speed Complaint Bot:** Log in to a speed test site, find the current speeds, and fill out a complaint form if speeds are too low. | DD. Project | `DD10_selenium_speed_complaint.py` |
| **349** | **Automating the Google Dinosaur Game:** Use Selenium to detect obstacles and send a jump command (`spacebar`). | DD. Project | `DD11_selenium_dino_bot.py` |
| **350** | **Handling Waits:** Use **Explicit Waits** (`WebDriverWait`) to wait for a specific element to be clickable or visible before interacting with it. | DD. Selenium Adv | `DD12_selenium_explicit_wait.py` |

---
## Day 32: Project 9: Web Development - Flask Fundamentals (11 Programs)
Focus: Building small web applications and understanding routing and templates.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **351** | **First Flask Server:** Create a minimal Flask application that runs on `localhost:5000` and returns a simple "Hello World!" string. | EE. Flask Basics | `EE01_flask_hello_world.py` |
| **352** | **Basic HTML Response:** Modify the Flask route to return a full HTML page (basic structure with a header). | EE. Flask Basics | `EE02_flask_html_response.py` |
| **353** | **URL Variables:** Create a route that takes a variable (e.g., `name`) from the URL path (`/user/<name>`) and prints it on the page. | EE. Flask Basics | `EE03_flask_url_variable.py` |
| **354** | **HTML Templating (`render_template`):** Use the `render_template` function to display a separate HTML template file (mocking Jinja). | EE. Flask Templating | `EE04_flask_render_template.py` |
| **355** | **Higher or Lower Web Game (Setup):** Flask app that randomly generates a number (0-9) when the route is accessed. | EE. Flask Project | `EE05_flask_high_low_setup.py` |
| **356** | **Higher or Lower Web Game (Logic):** Add logic to the route to accept a user guess from the URL and compare it to the random number, providing feedback. | EE. Flask Project | `EE06_flask_high_low_logic.py` |
| **357** | **Digital Name Card:** A Flask route that renders a detailed HTML template to serve as a digital business card. | EE. Flask Project | `EE07_flask_name_card.py` |
| **358** | **Handling POST Requests:** Create a route that can handle a submitted HTML form using the `request.form` object. | EE. Flask Forms | `EE08_flask_handle_post.py` |
| **359** | **A Templated Blog (Data):** Create a Flask app that reads mock blog post data from a Python list of dictionaries and passes it to the template. | EE. Flask Project | `EE09_flask_templated_blog.py` |
| **360** | **Functional Blog Contact Form:** Create a Flask route that validates form data and "sends" a mock email when the contact form is submitted. | EE. Flask Forms | `EE10_flask_contact_form.py` |
| **361** | **Error Handling (404):** Implement a custom error handler for the HTTP 404 (Not Found) status code. | EE. Flask Adv | `EE11_flask_error_handler.py` |

---
## Day 33: Project 10: Flask - Database & Advanced Features (11 Programs)
Focus: Implementing CRUD operations and user authentication with Flask extensions.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **362** | **Virtual Bookshelf (Setup - Flask-SQLAlchemy):** Configure Flask-SQLAlchemy and define a simple `Book` model with `id` and `title`. | FF. Flask DB | `FF01_flask_db_setup.py` |
| **363** | **Create/Read (CRUD - Add):** Implement a route to **Add (Create)** a new book entry to the SQLite database. | FF. Flask DB | `FF02_flask_db_crud_create.py` |
| **364** | **Create/Read (CRUD - View):** Implement a route to **View (Read)** all books from the database. | FF. Flask DB | `FF03_flask_db_crud_read.py` |
| **365** | **Update (CRUD - Edit):** Implement a route to **Edit (Update)** the title of an existing book by its ID. | FF. Flask DB | `FF04_flask_db_crud_update.py` |
| **366** | **Delete (CRUD - Remove):** Implement a route to **Delete** a book entry by its ID. | FF. Flask DB | `FF05_flask_db_crud_delete.py` |
| **367** | **Top Movies Website (Full CRUD):** Design a single-page Flask app with a form and list to manage a list of favorite movies. | FF. Flask Project | `FF06_flask_crud_movies.py` |
| **368** | **Cafe & Wifi API (Setup):** Flask app that returns a simple list of mock cafes as JSON data when accessing a `/all` route. | FF. Flask API | `FF07_flask_api_read.py` |
| **369** | **Cafe & Wifi API (Search):** Implement a `/search` route that accepts a query parameter (e.g., `location`) and returns matching cafe data. | FF. Flask API | `FF08_flask_api_search.py` |
| **370** | **Authentication with Flask-Login (Setup):** Configure Flask-Login and create a simple `User` class for basic user management. | FF. Flask Auth | `FF09_flask_auth_setup.py` |
| **371** | **Authentication with Flask-Login (Login/Logout):** Implement `/login` and `/logout` routes using Flask-Login functions. | FF. Flask Auth | `FF10_flask_auth_login.py` |
| **372** | **Authentication with Flask-Login (`@login_required`):** Protect a sensitive route using the `@login_required` decorator. | FF. Flask Auth | `FF11_flask_auth_protect.py` |

---
## Day 34: Data Analysis - Pandas & Matplotlib (12 Programs)
Focus: Manipulating structured data and visualizing results.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **373** | **Pandas Basics:** Create a DataFrame from a dictionary and inspect its column data types (`.dtypes`). | GG. Pandas Basics | `GG01_pd_create_and_inspect.py` |
| **374** | **Data Cleaning:** Handle **Missing Data** (`NaN` values) by dropping rows with `dropna()` or filling them with `fillna()`. | GG. Data Prep | `GG02_pd_handle_missing_data.py` |
| **375** | **Data Aggregation:** Use `.groupby()` to group data by a category column and calculate the sum of another column for each group. | GG. Data Analysis | `GG03_pd_groupby_aggregate.py` |
| **376** | **Merging DataFrames:** Merge two DataFrames based on a common key (e.g., merging student records with grades). | GG. Data Analysis | `GG04_pd_merge_dataframes.py` |
| **377** | **Time-Series Data:** Load time-series data and convert a date column to the proper datetime format. | GG. Time Series | `GG05_pd_time_series_prep.py` |
| **378** | **Basic Line Plot (`Matplotlib`):** Create a simple line plot to visualize a single column of data over time. | GG. Visualization | `GG06_plt_basic_line_plot.py` |
| **379** | **Bar Chart:** Create a bar chart using Matplotlib to visualize the counts of categorical data. | GG. Visualization | `GG07_plt_basic_bar_chart.py` |
| **380** | **Scatter Plot:** Create a scatter plot to visualize the relationship between two numeric variables. | GG. Visualization | `GG08_plt_basic_scatter.py` |
| **381** | **LEGO Dataset Analysis (Count):** Load a mock LEGO dataset and find the total number of themes and sets. | GG. Project | `GG09_pd_lego_count.py` |
| **382** | **LEGO Dataset Analysis (By Year):** Use Pandas to count the number of LEGO sets released each year and plot it. | GG. Project | `GG10_pd_lego_sets_by_year.py` |
| **383** | **Noble Prize Winners Analysis (Gender):** Load a mock Nobel Prize dataset and find the percentage of male vs. female winners. | GG. Project | `GG11_pd_nobel_gender.py` |
| **384** | **Noble Prize Winners Analysis (By Age):** Calculate the average age of Nobel winners by filtering and aggregation. | GG. Project | `GG12_pd_nobel_avg_age.py` |

---
## Day 35: Data Analysis - NumPy & Linear Regression (11 Programs)
Focus: Numerical computing fundamentals and introduction to Machine Learning models.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **385** | **NumPy Array Creation:** Create a 1D, 2D, and 3D NumPy array and print their shapes. | HH. NumPy | `HH01_np_array_creation.py` |
| **386** | **NumPy Arithmetic:** Perform basic element-wise arithmetic (addition, multiplication) on two NumPy arrays. | HH. NumPy | `HH02_np_arithmetic.py` |
| **387** | **NumPy Indexing/Slicing:** Demonstrate advanced indexing and slicing (e.g., selecting all rows where a condition is met). | HH. NumPy | `HH03_np_indexing_slicing.py` |
| **388** | **NumPy Linear Algebra:** Perform matrix multiplication (`np.dot`) on two NumPy 2D arrays. | HH. NumPy Adv | `HH04_np_matrix_mult.py` |
| **389** | **NumPy Broadcasting:** Demonstrate how broadcasting works when adding a scalar to a 2D array. | HH. NumPy Adv | `HH05_np_broadcasting.py` |
| **390** | **Simple Linear Regression (Data Prep):** Use NumPy to create mock data ($X$ and $Y$ with a linear relationship + noise). | HH. ML Prep | `HH06_ml_linear_prep.py` |
| **391** | **Simple Linear Regression (Manual Fit):** Manually calculate the slope ($m$) and intercept ($c$) for the mock data using formulas. | HH. ML Algo | `HH07_ml_linear_manual_fit.py` |
| **392** | **Simple Linear Regression (Scikit-Learn):** Use `sklearn.linear_model.LinearRegression` to fit a model to the mock data. | HH. ML Scikit | `HH08_ml_linear_sklearn.py` |
| **393** | **Making Predictions:** Use the trained Scikit-Learn model to predict the $Y$ value for a new $X$ value. | HH. ML Scikit | `HH09_ml_linear_predict.py` |
| **394** | **Evaluating the Model:** Calculate the Mean Squared Error (MSE) and $R^2$ score for the linear regression model. | HH. ML Scikit | `HH10_ml_linear_evaluate.py` |
| **395** | **Visualizing the Fit:** Use Matplotlib/Seaborn to plot the original data points and the fitted regression line. | HH. Visualization | `HH11_ml_linear_visualize.py` |

---
## Day 36: Project 11: Stock Monitoring and Habit Tracking (12 Programs)
Focus: Combining APIs, logic, and networking for real-world automation tasks.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **396** | **Stock Monitoring (Price Check):** Use a mock API to get the closing price for a stock yesterday and the day before. | II. API Project | `II01_stock_price_check.py` |
| **397** | **Stock Monitoring (Volatility):** Calculate the percentage difference between the two closing prices. | II. API Project | `II02_stock_calculate_volatility.py` |
| **398** | **Stock Monitoring (News Fetch):** If the volatility exceeds a threshold (e.g., 5%), use a mock News API to fetch the top three articles related to the stock. | II. API Project | `II03_stock_news_fetch.py` |
| **399** | **Stock Monitoring (Twilio Alert):** Format the stock change and news into a concise message and send it via Twilio (mock/console print). | II. API Project | `II04_stock_twilio_alert.py` |
| **400** | **Habit Tracker (Pixela API - User):** Simulate a POST request to create a new user account on the Pixela API. | II. API Project | `II05_pixela_create_user.py` |
| **401** | **Habit Tracker (Pixela API - Graph):** Simulate a POST request to create a new, trackable graph (e.g., "coding-hours") for the user. | II. API Project | `II06_pixela_create_graph.py` |
| **402** | **Habit Tracker (Pixela API - Post Pixel):** Simulate a POST request to record a new pixel (value) for the graph today. | II. API Project | `II07_pixela_post_pixel.py` |
| **403** | **Habit Tracker (Pixela API - Update):** Simulate a PUT request to update the value of a pixel recorded on a specific date. | II. API Project | `II08_pixela_update_pixel.py` |
| **404** | **Workout Tracking Application (Setup):** Create a function that takes exercise, duration, and calories and stores it in a mock list of dictionaries. | II. API Project | `II09_workout_tracker_setup.py` |
| **405** | **Workout Tracking Application (Data Entry):** Simulate natural language input parsing (e.g., "I ran for 30 minutes and did 10 pushups") and save the structured data. | II. API Project | `II10_workout_tracker_parse.py` |
| **406** | **Workout Tracking Application (Sheet Mock):** Simulate using the data to make a POST request to a mock Google Sheet API to log the workout. | II. API Project | `II11_workout_tracker_sheet.py` |
| **407** | **Dotenv/Environment Variables:** Read a sensitive API key from an environment variable (mocking `.env` file loading). | II. DevOps | `II12_devops_dotenv.py` |

---
## Day 37: Project 12: Flight Deal Finder (11 Programs)
Focus: Complex data fetching, comparison logic, and user notification systems.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **408** | **Flight Deal Finder (Data Structure):** Define the required data structure (list of dictionaries) to hold city, IATA code, lowest price, and departure date. | JJ. Flight Project | `JJ01_flight_data_structure.py` |
| **409** | **Flight Deal Finder (Sheety/DB Load):** Simulate loading the list of target cities from a mock Google Sheet API (via Sheety). | JJ. Flight Project | `JJ02_flight_load_cities.py` |
| **410** | **Flight Deal Finder (Teekila API - IATA Mock):** Simulate a GET request to a Teekila-like API to get the IATA code for a city name. | JJ. Flight Project | `JJ03_flight_iata_mock.py` |
| **411** | **Flight Deal Finder (Update Sheet with IATA):** Simulate a PUT request to update the mock Google Sheet with the fetched IATA codes for each city. | JJ. Flight Project | `JJ04_flight_update_iata.py` |
| **412** | **Flight Deal Finder (Search - Mock):** Simulate a GET request to search for the cheapest flight from a home airport to a target city within a given date range. | JJ. Flight Project | `JJ05_flight_search_mock.py` |
| **413** | **Flight Deal Finder (Deal Check):** Process the mock flight search response and determine if the current price is lower than the recorded lowest price. | JJ. Flight Project | `JJ06_flight_deal_check.py` |
| **414** | **Flight Deal Finder (Twilio Alert - Deal):** If a deal is found, send a descriptive SMS alert (mock/console print) with the price and dates. | JJ. Flight Project | `JJ07_flight_twilio_deal.py` |
| **415** | **Flight Deal Finder (Twilio Alert - Stopover):** If the cheapest deal involves a stopover, modify the SMS alert to include the stopover city. | JJ. Flight Project | `JJ08_flight_twilio_stopover.py` |
| **416** | **Flight Deal Finder (User Sign-up Mock):** Simulate adding new user emails to a mock database/sheet. | JJ. Flight Project | `JJ09_flight_user_signup.py` |
| **417** | **Flight Deal Finder (Email List):** If a deal is found, use `smtplib` to send an email to the entire list of subscribed users. | JJ. Flight Project | `JJ10_flight_email_list.py` |
| **418** | **Handling API Authorization:** Demonstrate using `requests.auth.HTTPBasicAuth` for a mock API request that requires username/password. | JJ. Requests Adv | `JJ11_req_http_auth.py` |

---
## Day 38: DevOps - `subprocess` and `os` Modules (12 Programs)
Focus: System-level automation, file management, and interacting with the command line.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **419** | **Execute a Simple Shell Command:** Use `subprocess.run()` to execute a basic command like `ls -l` and print the output. | KK. Subprocess | `KK01_sub_run_ls.py` |
| **420** | **Capture Command Output:** Use `subprocess.run()` with `capture_output=True` to get the output as a string and process it (e.g., count lines). | KK. Subprocess | `KK02_sub_capture_output.py` |
| **421** | **Handle Command Error:** Use `subprocess.run()` with `check=True` and a `try...except` block to catch a `CalledProcessError` for a failed command. | KK. Subprocess | `KK03_sub_handle_error.py` |
| **422** | **Automating Git Operations (Clone Mock):** Use `subprocess` to run a mock `git clone <repo_url>`. | KK. Subprocess App | `KK04_sub_git_clone_mock.py` |
| **423** | **Automating Git Operations (Commit/Push Mock):** Use a sequence of `subprocess` calls to simulate `git add .`, `git commit -m "update"`, and `git push`. | KK. Subprocess App | `KK05_sub_git_commit_push.py` |
| **424** | **Check Git Status Across Multiple Repositories:** Iterate over a list of directories and use `subprocess` to check the status of each Git repository. | KK. Subprocess App | `KK06_sub_check_multi_repo.py` |
| **425** | **List Files in a Directory:** Use `os.listdir()` to list all files and folders in the current working directory. | KK. OS Module | `KK07_os_list_dir.py` |
| **426** | **Creating and Deleting a Directory:** Use `os.mkdir()` and `os.rmdir()` to create and then safely remove a new folder. | KK. OS Module | `KK08_os_create_delete_dir.py` |
| **427** | **File Path Manipulation:** Use `os.path.join()` and `os.path.basename()` to create a platform-independent file path and extract the filename. | KK. OS Module | `KK09_os_path_manipulation.py` |
| **428** | **Walk a Directory Tree:** Use `os.walk()` to traverse a directory tree and print the file paths. | KK. OS Module | `KK10_os_walk_tree.py` |
| **429** | **Find Large Files:** Use `os.walk()` combined with `os.path.getsize` to find all files in a directory tree larger than 10MB. | KK. OS App | `KK11_os_find_large_files.py` |
| **430** | **Compare Two Directory Trees:** Compare the contents of two directories recursively to check if they are identical (file names and sizes). | KK. OS App | `KK12_os_compare_dirs.py` |

---
## Day 39: DevOps - `Boto3` (AWS SDK) (12 Programs)
Focus: Interacting with Amazon Web Services (AWS) using the Boto3 library.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **431** | **Boto3 Setup/Session:** Initialize a Boto3 session and mock the client connection to an AWS service (e.g., S3). | LL. Boto3 Basics | `LL01_boto3_setup_client.py` |
| **432** | **S3: List Buckets (Mock):** Use the S3 client to list all mock S3 buckets in the account. | LL. Boto3 S3 | `LL02_boto3_s3_list_buckets.py` |
| **433** | **S3: Create a Bucket (Mock):** Use the S3 client to create a new S3 bucket with a globally unique name. | LL. Boto3 S3 | `LL03_boto3_s3_create_bucket.py` |
| **434** | **S3: Upload a File (Mock):** Use the S3 client to upload a local file to a specified bucket and key. | LL. Boto3 S3 | `LL04_boto3_s3_upload_file.py` |
| **435** | **S3: Download a File (Mock):** Use the S3 client to download an object from S3 to a local file path. | LL. Boto3 S3 | `LL05_boto3_s3_download_file.py` |
| **436** | **S3: Delete an Object (Mock):** Use the S3 client to delete a specific object from a bucket. | LL. Boto3 S3 | `LL06_boto3_s3_delete_object.py` |
| **437** | **S3: Handling a Non-Existent Bucket:** Implement `try...except` to catch and handle the error when trying to access a bucket that doesn't exist. | LL. Boto3 Error | `LL07_boto3_s3_handle_not_found.py` |
| **438** | **EC2: List Instances (Mock):** Use the EC2 client to describe (list) all running instances, filtering by state. | LL. Boto3 EC2 | `LL08_boto3_ec2_list_instances.py` |
| **439** | **EC2: Start an Instance (Mock):** Use the EC2 client to start a specific instance by its ID. | LL. Boto3 EC2 | `LL09_boto3_ec2_start_instance.py` |
| **440** | **EC2: Stop an Instance (Mock):** Use the EC2 client to gracefully stop a specific instance by its ID. | LL. Boto3 EC2 | `LL10_boto3_ec2_stop_instance.py` |
| **441** | **IAM: List Users (Mock):** Use the IAM client to list all user accounts in the AWS account. | LL. Boto3 IAM | `LL11_boto3_iam_list_users.py` |
| **442** | **IAM: Create a User (Mock):** Use the IAM client to create a new user with a specific name. | LL. Boto3 IAM | `LL12_boto3_iam_create_user.py` |

---
## Day 40: DevOps - `Paramiko` (SSH) (11 Programs)
Focus: Securely connecting to and executing commands on remote Linux servers.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **443** | **Paramiko Setup:** Create a `SSHClient` object and set the policy to automatically add the host key. | MM. Paramiko | `MM01_pmk_ssh_setup.py` |
| **444** | **Basic Connection (Mock Password):** Simulate connecting to a remote server using a username and password. | MM. Paramiko | `MM02_pmk_connect_password_mock.py` |
| **445** | **Secure Connection (Mock Key):** Simulate connecting using an SSH private key file path. | MM. Paramiko | `MM03_pmk_connect_key_mock.py` |
| **446** | **Execute Remote Command:** Connect to a mock server and execute a single remote command (e.g., `uptime`) and print stdout/stderr. | MM. Paramiko | `MM04_pmk_execute_command.py` |
| **447** | **Execute Command with Input (Mock SUDO):** Send input to the remote command (e.g., sending a password to a `sudo` prompt). | MM. Paramiko Adv | `MM05_pmk_execute_with_input.py` |
| **448** | **Handle Connection Errors:** Implement `try...except` to handle common connection failures like `AuthenticationException` or `NoValidConnectionsError`. | MM. Paramiko Error | `MM06_pmk_handle_errors.py` |
| **449** | **SFTP: Upload a File:** Use `SFTPClient` to upload a local file to a specified path on the remote server. | MM. Paramiko SFTP | `MM07_pmk_sftp_upload.py` |
| **450** | **SFTP: Download a File:** Use `SFTPClient` to download a file from the remote server to a local path. | MM. Paramiko SFTP | `MM08_pmk_sftp_download.py` |
| **451** | **SFTP: List Remote Directory:** Use `SFTPClient` to list the contents of a directory on the remote machine. | MM. Paramiko SFTP | `MM09_pmk_sftp_list_dir.py` |
| **452** | **Advanced Script Execution:** Write a Python function that executes a multi-line shell script remotely and collects all outputs. | MM. Paramiko Adv | `MM10_pmk_execute_script.py` |
| **453** | **Checking Remote File Existence:** Use `SFTPClient` to check if a specific file exists on the remote server before attempting to download. | MM. Paramiko Adv | `MM11_pmk_check_file_exists.py` |

---
## Day 41: DevOps - `Docker SDK` (11 Programs)
Focus: Programmatically controlling and automating Docker containers and images.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **454** | **Docker Client Setup:** Initialize the Docker client connection. | NN. Docker SDK | `NN01_docker_client_setup.py` |
| **455** | **List Running Containers:** Use the client to list all currently running Docker containers. | NN. Docker Containers | `NN02_docker_list_containers.py` |
| **456** | **List All Images:** Use the client to list all Docker images available locally. | NN. Docker Images | `NN03_docker_list_images.py` |
| **457** | **Pull an Image (Mock):** Use the client to pull a specified Docker image from a registry (e.g., `nginx:latest`). | NN. Docker Images | `NN04_docker_pull_image.py` |
| **458** | **Run a Container (Simple):** Use the client to run a simple, detached container (e.g., running `hello-world`). | NN. Docker Containers | `NN05_docker_run_simple.py` |
| **459** | **Stop and Remove a Container:** Find a container by name/ID, stop it, and remove it (`remove=True`). | NN. Docker Containers | `NN06_docker_stop_remove.py` |
| **460** | **Build an Image from a Dockerfile (Mock):** Use the client to build an image given a path to a `Dockerfile`. | NN. Docker Images | `NN07_docker_build_image.py` |
| **461** | **A CI/CD Script to Build and Push an Image (Mock):** Combine build, tag, and push operations (simulated) for a CI workflow. | NN. Docker App | `NN08_docker_ci_push_mock.py` |
| **462** | **Container Health Check:** Inspect a running container's status to check if it's "running" or "exited." | NN. Docker Containers | `NN09_docker_health_check.py` |
| **463** | **Docker System Cleanup Script:** Use `client.containers.prune()` and `client.images.prune()` to clean up unused resources. | NN. Docker App | `NN10_docker_cleanup_script.py` |
| **464** | **Handling Common Docker Exceptions:** Implement `try...except` to handle exceptions like `ImageNotFound` or `NotFound` (for containers). | NN. Docker Error | `NN11_docker_handle_exceptions.py` |

---
## Day 42: DevOps - `Kubernetes SDK` (12 Programs)
Focus: Managing and monitoring Kubernetes clusters and resources.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **465** | **Kubernetes Config Setup:** Load the Kube config file from its default location. | OO. K8s SDK | `OO01_k8s_config_load.py` |
| **466** | **List Pods in a Namespace:** Use the `CoreV1Api` to list all Pods in the 'default' namespace. | OO. K8s Core | `OO02_k8s_list_pods.py` |
| **467** | **Create a Namespace:** Use the `CoreV1Api` to programmatically create a new namespace. | OO. K8s Core | `OO03_k8s_create_namespace.py` |
| **468** | **Monitoring Pod Health:** List pods and check their `status.phase` (e.g., 'Running', 'Pending', 'Failed') to monitor health. | OO. K8s App | `OO04_k8s_monitor_pod_health.py` |
| **469** | **Create a Deployment:** Use the `AppsV1Api` to create a new deployment (specifying image, replicas). | OO. K8s Apps | `OO05_k8s_create_deployment.py` |
| **470** | **Get Deployment Status:** Check the status of a specific deployment (e.g., checking `readyReplicas`). | OO. K8s Apps | `OO06_k8s_get_deployment_status.py` |
| **471** | **Create a Service:** Use the `CoreV1Api` to create a `NodePort` or `LoadBalancer` Service that exposes the deployment. | OO. K8s Core | `OO07_k8s_create_service.py` |
| **472** | **Automating a Rolling Update:** Use the `AppsV1Api` to patch a deployment's image version to trigger a rolling update. | OO. K8s App | `OO08_k8s_rolling_update.py` |
| **473** | **Running and Monitoring a Job:** Create a simple batch `Job` and use a loop to wait for the job to complete successfully. | OO. K8s Batch | `OO09_k8s_run_monitor_job.py` |
| **474** | **Scale a Deployment:** Use the `AppsV1Api` to scale the number of replicas for an existing deployment. | OO. K8s Apps | `OO10_k8s_scale_deployment.py` |
| **475** | **Delete a Deployment:** Use the `AppsV1Api` to delete a deployment by its name. | OO. K8s Apps | `OO11_k8s_delete_deployment.py` |
| **476** | **Handling Kubernetes API Exceptions:** Implement `try...except` blocks to handle generic API exceptions (`ApiException`) during operations. | OO. K8s Error | `OO12_k8s_handle_api_errors.py` |

---
## Day 43: Advanced String & Regex (11 Programs)
Focus: Complex string processing, sub-problems, and pattern matching.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **477** | **Find Longest Substring Without Repeating Characters:** Find the length of the longest substring without any repeating characters. | PP. String Adv | `PP01_str_longest_substring.py` |
| **478** | **Find All Substrings:** Generate and print all possible substrings of a given input string. | PP. String Adv | `PP02_str_find_all_substrings.py` |
| **479** | **Group Anagrams:** Given a list of words, group the anagrams together. | PP. String Adv | `PP03_str_group_anagrams.py` |
| **480** | **Reverse Words and Swap Cases:** Reverse the order of words in a sentence and swap the case of all letters (e.g., "Hello World" $\to$ "wORLD hELLO"). | PP. String Adv | `PP04_str_reverse_swap_case.py` |
| **481** | **Excel Column Title to Number:** Convert an Excel column title string (e.g., 'A', 'AB', 'ZY') to its corresponding column number. | PP. String Adv | `PP05_str_excel_col_to_num.py` |
| **482** | **Regex: Basic Search:** Use `re.search()` to find the first occurrence of a pattern (e.g., a number) in a string. | PP. Regex | `PP06_regex_basic_search.py` |
| **483** | **Regex: Find All Matches:** Use `re.findall()` to extract all email addresses from a sample text block. | PP. Regex | `PP07_regex_find_all_emails.py` |
| **484** | **Regex: Substitution:** Use `re.sub()` to replace all instances of a pattern (e.g., all whitespace) with a different character (e.g., a hyphen). | PP. Regex | `PP08_regex_substitution.py` |
| **485** | **Find Most Frequent IP in a Log File:** Use regex (`re.match` or `re.search`) to extract IPs from a mock log file and count the most frequent one. | PP. Regex App | `PP09_regex_frequent_ip_log.py` |
| **486** | **Parsing a Log File for Error Lines:** Use regex to specifically identify and extract lines containing the word "ERROR" and the timestamp associated with it. | PP. Regex App | `PP10_regex_parse_error_log.py` |
| **487** | **Creating a Set of Unique User Roles from a Config:** Use regex to extract all unique user roles mentioned across a mock config file. | PP. Regex App | `PP11_regex_extract_roles.py` |

---
## Day 44: Project 13: Web Scraping/Automation (11 Programs)
Focus: Scraper robustness, pagination, and advanced automation tasks.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **488** | **Scraper: Extracting Specific Data:** Scrape a mock sports results page and extract the final score for a specific team. | QQ. Web Scraping | `QQ01_scrape_sports_score.py` |
| **489** | **Scraper: Pagination (Mock):** Create a function that iterates through mock page numbers in a URL to scrape data from multiple pages. | QQ. Web Scraping | `QQ02_scrape_pagination.py` |
| **490** | **Scraper: Custom Web Scraper for Top 100 Books (Full):** Fetch a mock top book list, extract the title, author, and price, and store it in a Pandas DataFrame. | QQ. Project | `QQ03_scrape_top_books_full.py` |
| **491** | **Selenium: Instagram Follower Bot (Mock Follow):** Use Selenium to log in and simulate finding a target user's profile and clicking the 'Follow' button. | QQ. Project | `QQ04_selenium_ig_follow_mock.py` |
| **492** | **Selenium: Data Entry Automation (Form):** Scrape data from one source (mock) and use Selenium to automatically fill out a separate web form with that data. | QQ. Project | `QQ05_selenium_data_entry_form.py` |
| **493** | **Selenium: Data Entry Automation (Capcha Mock):** Implement a necessary wait and mock logic for handling a CAPTCHA or reCAPTCHA page element. | QQ. Project | `QQ06_selenium_captcha_mock.py` |
| **494** | **Selenium: Handling Alerts (Pop-ups):** Use `driver.switch_to.alert` to accept or dismiss a JavaScript alert box. | QQ. Selenium Adv | `QQ07_selenium_handle_alert.py` |
| **495** | **Selenium: Screenshot Capture:** Take a screenshot of the current page and save it to a local file. | QQ. Selenium Adv | `QQ08_selenium_capture_screenshot.py` |
| **496** | **Selenium: Downloads Folder Organizer (Setup):** Create a script that watches a mock downloads folder and automatically moves files based on extension (`.pdf`, `.jpg`) into category folders. | QQ. Project | `QQ09_selenium_downloads_organizer.py` |
| **497** | **Selenium: Headless Browser Mode:** Configure the WebDriver to run in headless mode (without opening a visible browser window). | QQ. Selenium Adv | `QQ10_selenium_headless_mode.py` |
| **498** | **Scraper: Extracting and Parsing Dates:** Scrape a mock event list and parse the date strings into Python `datetime` objects. | QQ. Web Scraping | `QQ11_scrape_parse_dates.py` |

---
## Day 45: Project 14: Data Visualizations (12 Programs)
Focus: Using Matplotlib and Seaborn to create insightful plots and charts.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **499** | **Matplotlib: Subplots:** Create a figure with two side-by-side subplots (e.g., a line plot and a scatter plot). | RR. Matplotlib | `RR01_plt_subplots.py` |
| **500** | **Matplotlib: Histograms:** Create a histogram to visualize the distribution of a mock dataset (e.g., test scores). | RR. Matplotlib | `RR02_plt_histogram.py` |
| **501** | **Matplotlib: Pie Chart:** Create a pie chart to visualize the percentage breakdown of categorical data. | RR. Matplotlib | `RR03_plt_pie_chart.py` |
| **502** | **Matplotlib: Customization:** Add titles, axis labels, legends, and gridlines to a plot for better readability. | RR. Matplotlib | `RR04_plt_customization.py` |
| **503** | **Seaborn: Scatter Plot:** Use Seaborn to create a scatter plot of two variables and use a third variable to color the points (`hue`). | RR. Seaborn | `RR05_sns_scatter_hue.py` |
| **504** | **Seaborn: Box Plot:** Create a box plot to visualize the distribution and outliers of a numeric variable for different categories. | RR. Seaborn | `RR06_sns_box_plot.py` |
| **505** | **Space Race Analysis (Data Prep):** Load a mock space mission dataset and clean the 'Date' column for analysis. | RR. Project | `RR07_data_prep_space_race.py` |
| **506** | **Space Race Analysis (Visualization):** Use Matplotlib/Pandas to plot the cumulative number of missions over time. | RR. Project | `RR08_plt_space_race_cumulative.py` |
| **507** | **Deaths by Police Analysis (Visualization):** Use Seaborn to create a bar chart showing the count of incidents by race/ethnicity. | RR. Project | `RR09_sns_deaths_by_race.py` |
| **508** | **Deaths by Police Analysis (Trends):** Plot the incident count over the years (time series) to analyze trends. | RR. Project | `RR10_plt_deaths_over_time.py` |
| **509** | **Google Play Store App Analytics (Prep):** Load a mock app dataset, clean the 'Reviews' column, and filter for high-review apps. | RR. Project | `RR11_data_prep_app_analytics.py` |
| **510** | **Google Play Store App Analytics (Plotly Mock):** Use Plotly (mock) to create an interactive scatter plot of app size vs. installs. | RR. Project | `RR12_plt_app_size_vs_installs.py` |

---
## Day 46: Advanced Project Topics (12 Programs)
Focus: Utility development (audio, image), and high-level web app components.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **511** | **Text to Audiobook Converter (Setup):** Use a mock text-to-speech library to convert a simple string to an audio file. | SS. Project Adv | `SS01_tts_basic_convert.py` |
| **512** | **Text to Audiobook Converter (File Input):** Read the content of a `.txt` file and convert the entire content to speech. | SS. Project Adv | `SS02_tts_file_input.py` |
| **513** | **PDF to Audiobook Converter (Mock `PyPDF2`):** Mock reading text from a PDF file and passing it to the TTS function. | SS. Project Adv | `SS03_tts_pdf_mock.py` |
| **514** | **Image Color Palette Generator (Setup):** Use a mock image processing library (`Pillow`) to open an image file. | SS. Project Adv | `SS04_img_palette_setup.py` |
| **515** | **Image Color Palette Generator (Logic):** Extract the 10 most common colors (RGB/Hex) from the mock image data. | SS. Project Adv | `SS05_img_palette_logic.py` |
| **516** | **Custom API Based Website (Data):** Flask app that fetches data from an external mock API and renders it in a template. | SS. Flask API | `SS06_flask_custom_api_site.py` |
| **517** | **eCommerce Website (Product List):** Flask app that displays a list of mock products from a database. | SS. Flask Project | `SS07_flask_ecommerce_product.py` |
| **518** | **eCommerce Website (Shopping Cart Logic):** Implement session-based logic to add and display items in a shopping cart. | SS. Flask Project | `SS08_flask_ecommerce_cart.py` |
| **519** | **eCommerce Website (Payment Processing Mock):** Simulate the process of submitting payment information to a mock service (e.g., Stripe/PayPal). | SS. Flask Project | `SS09_flask_ecommerce_payment_mock.py` |
| **520** | **Simple Chat Application (Setup - Mock DB):** Create a basic Flask route to display the last 10 messages from a mock database. | SS. Project Adv | `SS10_flask_chat_setup.py` |
| **521** | **Simple Chat Application (Post Message):** Implement a POST route to allow a user to submit a new message to the mock database. | SS. Project Adv | `SS11_flask_chat_post.py` |
| **522** | **Kanban-Style Todo List Website (CRUD):** Implement the core Flask-SQLAlchemy CRUD functions for managing a single list of todo items. | SS. Flask Project | `SS12_flask_todo_crud.py` |

---
## Day 47: Security & Cryptography (11 Programs)
Focus: Hashing, encryption concepts, and web security basics.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **523** | **SHA-256 Hashing:** Use `hashlib` to calculate the SHA-256 hash of an input string. | TT. Cryptography | `TT01_hash_sha256.py` |
| **524** | **MD5 Hashing:** Use `hashlib` to calculate the MD5 hash of an input string. | TT. Cryptography | `TT02_hash_md5.py` |
| **525** | **Password Hashing (`bcrypt` Mock):** Simulate the process of generating a salted hash for a user password using a modern library (e.g., `bcrypt`). | TT. Cryptography | `TT03_hash_password_bcrypt_mock.py` |
| **526** | **Password Verification (`bcrypt` Mock):** Simulate verifying a user-provided password against the stored hash. | TT. Cryptography | `TT04_hash_password_verify_mock.py` |
| **527** | **RSA: Key Generation (Mock):** Simulate the generation of public and private RSA keys. | TT. Cryptography | `TT05_crypto_rsa_key_gen_mock.py` |
| **528** | **RSA: Encryption (Mock):** Simulate encrypting a short message using the RSA public key. | TT. Cryptography | `TT06_crypto_rsa_encrypt_mock.py` |
| **529** | **RSA: Decryption (Mock):** Simulate decrypting the message using the RSA private key. | TT. Cryptography | `TT07_crypto_rsa_decrypt_mock.py` |
| **530** | **Diffie-Hellman Key Exchange (Mock):** Simulate the steps for two parties (Alice and Bob) to securely agree on a shared secret key. | TT. Cryptography | `TT08_crypto_diffie_hellman_mock.py` |
| **531** | **URL Encoding/Decoding:** Use the `urllib.parse` module to encode and decode a URL string (e.g., handling spaces and special characters). | TT. Web Security | `TT09_web_url_encoding.py` |
| **532** | **Sanitizing User Input:** Create a function to remove common exploit characters (e.g., `<script>`, `&`) from user input before display. | TT. Web Security | `TT10_web_input_sanitization.py` |
| **533** | **Basic XSS Filter:** Implement a simple regex-based filter to detect and neutralize basic Cross-Site Scripting (XSS) payload attempts. | TT. Web Security | `TT11_web_xss_filter.py` |

---
## Day 48: Advanced OOP & Design Patterns (11 Programs)
Focus: Advanced Python features like decorators, generators, and design patterns.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **534** | **Iterator Pattern:** Implement a simple custom iterable class (e.g., `RangeIterator`) that supports the `__iter__` and `__next__` methods. | UU. Design Patterns | `UU01_design_iterator_pattern.py` |
| **535** | **Generator Function:** Write a simple Python generator function using `yield` (e.g., an infinite sequence generator). | UU. OOP Adv | `UU02_oop_generator_function.py` |
| **536** | **Context Manager (`with` statement):** Implement a custom class with `__enter__` and `__exit__` to create a context manager (e.g., for managing a file handle). | UU. OOP Adv | `UU03_oop_context_manager.py` |
| **537** | **Decorator (Basic):** Implement a simple Python decorator to time the execution of a function. | UU. OOP Adv | `UU04_oop_basic_decorator.py` |
| **538** | **Factory Method Pattern:** Implement a Factory Method to create different types of objects (e.g., `Car`, `Bike`) based on a single input string. | UU. Design Patterns | `UU05_design_factory_method.py` |
| **539** | **Singleton Pattern (Basic):** Implement the Singleton pattern to ensure that only one instance of a specific class exists. | UU. Design Patterns | `UU06_design_singleton.py` |
| **540** | **Observer Pattern (Basic):** Implement a simple Observer pattern where a Subject notifies multiple attached Observers of a state change. | UU. Design Patterns | `UU07_design_observer_pattern.py` |
| **541** | **Proxy Pattern:** Implement a Proxy class that acts as a placeholder for another object (e.g., controlling access or adding logging). | UU. Design Patterns | `UU08_design_proxy_pattern.py` |
| **542** | **Chaining Functions:** Demonstrate how to use methods in a class to allow method chaining (returning `self` after each operation). | UU. OOP Adv | `UU09_oop_method_chaining.py` |
| **543** | **Property Decorator (Getter/Setter):** Use the `@property` decorator to define getter and setter methods for a private attribute. | UU. OOP Adv | `UU10_oop_property_decorator.py` |
| **544** | **Dependency Injection (Simple):** Implement a class that uses a dependency passed into its constructor instead of creating it internally. | UU. OOP Adv | `UU11_oop_dependency_injection.py` |

---
## Day 49: Advanced Data Structures & Algorithms (11 Programs)
Focus: Heaps, Graphs, and Dynamic Programming concepts.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **545** | **Heap/Priority Queue:** Use the `heapq` module to implement a Min-Heap and demonstrate pushing and popping elements. | VV. Data Struct | `VV01_ds_min_heap_heapq.py` |
| **546** | **Graph Traversal (Adjacency List):** Represent a simple directed graph using an adjacency list (dictionary of lists). | VV. Graph | `VV02_graph_adjacency_list.py` |
| **547** | **Graph: Breadth-First Search (BFS):** Implement the BFS algorithm on the mock graph. | VV. Graph | `VV03_graph_bfs.py` |
| **548** | **Graph: Depth-First Search (DFS):** Implement the DFS algorithm (iterative using a stack) on the mock graph. | VV. Graph | `VV04_graph_dfs_iterative.py` |
| **549** | **Shortest Path (Dijkstra's Algorithm):** Implement Dijkstra's algorithm to find the shortest path between two nodes in a weighted graph. | VV. Graph Adv | `VV05_graph_dijkstra.py` |
| **550** | **Graph: Kruskal's Algorithm:** Implement Kruskal's algorithm to find the Minimum Spanning Tree (MST) of a connected, undirected graph. | VV. Graph Adv | `VV06_graph_kruskal.py` |
| **551** | **Graph: Prim's Algorithm:** Implement Prim's algorithm to find the Minimum Spanning Tree (MST) using a Priority Queue. | VV. Graph Adv | `VV07_graph_prim.py` |
| **552** | **Dynamic Programming: Fibonacci:** Implement the Fibonacci sequence using memoization (top-down DP) for optimal performance. | VV. DP | `VV08_dp_fibonacci_memo.py` |
| **553** | **Dynamic Programming: Knapsack (0/1):** Implement the 0/1 Knapsack problem using a bottom-up DP approach. | VV. DP | `VV09_dp_knapsack.py` |
| **554** | **Dynamic Programming: Longest Common Subsequence (LCS):** Implement the LCS problem using a DP table. | VV. DP | `VV10_dp_lcs.py` |
| **555** | **Dynamic Programming: Edit Distance:** Implement the Edit Distance (Levenshtein distance) calculation using DP. | VV. DP | `VV11_dp_edit_distance.py` |

---
## Day 50: Advanced Data Analytics & ML (11 Programs)
Focus: Data transformations, advanced ML models, and predictive modeling.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **556** | **Multi-Variable Regression (Data Prep):** Load mock housing price data with multiple features ($X_1, X_2, \dots$) and a target variable ($Y$). | WW. ML Adv | `WW01_ml_multi_var_prep.py` |
| **557** | **Multi-Variable Regression (Sklearn Fit):** Use `sklearn.linear_model.LinearRegression` to fit a model with multiple independent variables. | WW. ML Adv | `WW02_ml_multi_var_fit.py` |
| **558** | **Classification (Logistic Regression):** Use Scikit-Learn to implement a Logistic Regression model for a binary classification problem (mock data). | WW. ML Adv | `WW03_ml_logistic_regression.py` |
| **559** | **Classification (Decision Tree):** Implement a Decision Tree Classifier for a categorical dataset (mock data). | WW. ML Adv | `WW04_ml_decision_tree.py` |
| **560** | **Clustering (K-Means):** Use Scikit-Learn to implement K-Means clustering on an unlabeled dataset (mock data). | WW. ML Adv | `WW05_ml_k_means_clustering.py` |
| **561** | **Model Evaluation:** Calculate the **Confusion Matrix** and **Classification Report** (precision, recall, F1-score) for a classification model. | WW. ML Adv | `WW06_ml_confusion_matrix.py` |
| **562** | **Feature Scaling:** Implement **Min-Max Scaling** (normalization) on a mock numeric column using Pandas/NumPy. | WW. Data Prep | `WW07_data_feature_scaling.py` |
| **563** | **One-Hot Encoding:** Convert a categorical column in a Pandas DataFrame into numeric format using One-Hot Encoding. | WW. Data Prep | `WW08_data_one_hot_encode.py` |
| **564** | **Time Series: Moving Average:** Calculate the 7-day **Moving Average** for a mock time-series column in Pandas. | WW. Data Analysis | `WW09_data_moving_average.py` |
| **565** | **Data Detective Story (Mock Data):** Load a mock dataset on historical events, clean it, and aggregate data to find trends based on a hypothesis. | WW. Data Analysis | `WW10_data_detective_story.py` |
| **566** | **Pandas: Apply/Lambda:** Use the `.apply()` method with a lambda function to create a new column based on complex logic involving multiple existing columns. | WW. Data Analysis | `WW11_data_pandas_apply.py` |

---
## Day 51: Databases - SQL/MySQL Mock (12 Programs)
Focus: Connecting and interacting with relational databases using Python's DB API.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **567** | **DB Connection Setup (Mock `mysql.connector`):** Set up a mock database connection and cursor object. | XX. DB Basics | `XX01_db_connect_mock.py` |
| **568** | **SQL: Create Table (Mock):** Execute a mock SQL command to **CREATE** a new table (`Products`). | XX. DB CRUD | `XX02_db_sql_create_table.py` |
| **569** | **SQL: Insert Data (Mock):** Execute a mock SQL command to **INSERT** a single record into the table. | XX. DB CRUD | `XX03_db_sql_insert_one.py` |
| **570** | **SQL: Insert Multiple Data (Mock):** Use `cursor.executemany()` to **INSERT** multiple records from a Python list into the table efficiently. | XX. DB CRUD | `XX04_db_sql_insert_many.py` |
| **571** | **SQL: Select All Data (Mock):** Execute a mock `SELECT *` query and fetch all results using `cursor.fetchall()`. | XX. DB CRUD | `XX05_db_sql_select_all.py` |
| **572** | **SQL: Select Filtered Data (Mock):** Execute a mock `SELECT` query with a **`WHERE` clause** to filter results (e.g., price > 100). | XX. DB CRUD | `XX06_db_sql_select_where.py` |
| **573** | **SQL: Update Data (Mock):** Execute a mock SQL command to **UPDATE** a specific record. | XX. DB CRUD | `XX07_db_sql_update.py` |
| **574** | **SQL: Delete Data (Mock):** Execute a mock SQL command to **DELETE** a record based on a condition. | XX. DB CRUD | `XX08_db_sql_delete.py` |
| **575** | **SQL: Prepared Statements (Mock):** Use parameterized queries (prepared statements) to execute a mock SELECT query safely. | XX. DB Security | `XX09_db_sql_prepared_stmt.py` |
| **576** | **SQL: Join Operation (Mock):** Execute a mock SQL query to perform a **`LEFT JOIN`** between two tables (`Orders` and `Customers`). | XX. DB Advanced | `XX10_db_sql_left_join.py` |
| **577** | **SQL: Aggregate Functions (Mock):** Execute a mock query using `GROUP BY` and an aggregate function like `SUM()` or `COUNT()`. | XX. DB Advanced | `XX11_db_sql_aggregate.py` |
| **578** | **SQL: Stored Procedures (Mock Callable Statement):** Simulate calling a stored procedure using a database API (mock `callproc`). | XX. DB Advanced | `XX12_db_sql_stored_proc.py` |

---
## Day 52: Databases - NoSQL/MongoDB Mock (11 Programs)
Focus: Connecting and interacting with document databases using Python's driver.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **579** | **MongoDB Connection Setup (Mock `pymongo`):** Set up a mock client connection to a MongoDB instance/database. | YY. MongoDB Basics | `YY01_mongo_connect_mock.py` |
| **580** | **MongoDB: Insert One Document (Mock):** Insert a single JSON-like document into a mock collection. | YY. MongoDB CRUD | `YY02_mongo_insert_one.py` |
| **581** | **MongoDB: Insert Many Documents (Mock):** Insert a list of documents into a mock collection. | YY. MongoDB CRUD | `YY03_mongo_insert_many.py` |
| **582** | **MongoDB: Find All Documents (Mock):** Retrieve and print all documents from a collection. | YY. MongoDB CRUD | `YY04_mongo_find_all.py` |
| **583** | **MongoDB: Find Filtered Documents (Mock):** Query documents using a filter criteria (e.g., `{'status': 'pending'}`). | YY. MongoDB CRUD | `YY05_mongo_find_filter.py` |
| **584** | **MongoDB: Find with Projection (Mock):** Query documents but only retrieve specific fields (projection) to limit data transfer. | YY. MongoDB CRUD | `YY06_mongo_find_projection.py` |
| **585** | **MongoDB: Update One Document (Mock):** Use `$set` operator to update a specific field in one document. | YY. MongoDB CRUD | `YY07_mongo_update_one.py` |
| **586** | **MongoDB: Update Many Documents (Mock):** Update a specific field for multiple documents matching a criteria. | YY. MongoDB CRUD | `YY08_mongo_update_many.py` |
| **587** | **MongoDB: Delete One Document (Mock):** Delete a single document matching a specific criteria. | YY. MongoDB CRUD | `YY09_mongo_delete_one.py` |
| **588** | **MongoDB: Aggregation Pipeline (Mock):** Simulate a basic aggregation pipeline using `$match` and `$group` operators. | YY. MongoDB Adv | `YY10_mongo_aggregate.py` |
| **589** | **MongoDB: Indexing (Mock):** Simulate creating an index on a specific field to improve query performance. | YY. MongoDB Adv | `YY11_mongo_create_index.py` |

---
## Day 53: Patterns, Utility & System (12 Programs)
Focus: Practical system utilities and advanced Python language features.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **590** | **URL Shortener (Logic):** Implement a simple base-62 encoding scheme to convert a sequential integer ID into a short, unique code (mock URL). | ZZ. Utility | `ZZ01_utility_url_shortener.py` |
| **591** | **Downloads Folder Organizer (Full Logic):** Implement the core logic to categorize and move files based on their extensions using `shutil` (mock). | ZZ. Utility | `ZZ02_utility_folder_organizer.py` |
| **592** | **Image Resizer (Mock):** Use a mock imaging library to resize a batch of images in a folder to a specific dimension. | ZZ. Utility | `ZZ03_utility_image_resizer.py` |
| **593** | **CSV to JSON Converter:** Write a script that reads data from a CSV file and converts the entire dataset into a JSON file format. | ZZ. Data Format | `ZZ04_utility_csv_to_json.py` |
| **594** | **JSON to XML Converter (Mock):** Write a function that takes a nested Python dictionary (JSON data) and converts it to a basic XML structure. | ZZ. Data Format | `ZZ05_utility_json_to_xml.py` |
| **595** | **Logging Configuration:** Configure Python's standard `logging` module to log messages of different levels (INFO, WARNING, ERROR) to both the console and a file. | ZZ. System | `ZZ06_system_logging_config.py` |
| **596** | **Argument Parsing (`argparse`):** Write a script that uses the `argparse` module to handle command-line arguments and flags efficiently. | ZZ. System | `ZZ07_system_argparse.py` |
| **597** | **Memory Usage Tracker:** Use the `psutil` library (mock) to check and report the current CPU and memory usage of the running script/system. | ZZ. System | `ZZ08_system_resource_monitor.py` |
| **598** | **Multithreading (Basic):** Use the `threading` module to run two simple functions concurrently to demonstrate multithreading. | ZZ. System Adv | `ZZ09_system_multithreading.py` |
| **599** | **Multiprocessing (Basic):** Use the `multiprocessing` module to run two simple functions in parallel processes. | ZZ. System Adv | `ZZ10_system_multiprocessing.py` |
| **600** | **Producer-Consumer Pattern:** Implement the Producer-Consumer pattern using a Queue for thread-safe data exchange between two threads. | ZZ. System Adv | `ZZ11_system_producer_consumer.py` |
| **601** | **Basic Unit Testing (`unittest`):** Write a simple function and create a unit test case for it using Python's built-in `unittest` module. | ZZ. System Adv | `ZZ12_system_unit_testing.py` |

---
## Day 54: Advanced Web Projects & DevOps (11 Programs)
Focus: Finalizing web apps, advanced Flask features, and API design.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **602** | **Full CRUD Blog (Database Setup):** Implement the full database model for a blog that includes `User`, `Post`, and `Comment` tables (mock). | AAA. Flask Adv | `AAA01_flask_blog_db_model.py` |
| **603** | **Full CRUD Blog (Commenting):** Implement the Flask route and database logic to allow a logged-in user to add a comment to a post. | AAA. Flask Adv | `AAA02_flask_blog_comment.py` |
| **604** | **Full CRUD Blog (Post Deletion):** Implement a secure route for deleting a post, ensuring only the original author or an admin can delete it. | AAA. Flask Adv | `AAA03_flask_blog_post_delete.py` |
| **605** | **Flask CLI Commands:** Define a custom command using Flask's CLI (`@app.cli.command()`) for tasks like setting up the database. | AAA. Flask Adv | `AAA04_flask_cli_command.py` |
| **606** | **Rate Limiting (Mock):** Implement a mock rate-limiting mechanism in a Flask route to prevent users from hitting an API endpoint too frequently. | AAA. Flask API | `AAA05_flask_api_rate_limit.py` |
| **607** | **Microservices: Inter-Service Communication (Mock):** Simulate a Flask service making an API call to another mock Flask service. | AAA. DevOps | `AAA06_devops_microservice_call.py` |
| **608** | **Environment Check Script:** Write a Python script to check for the required Python version, necessary system dependencies (mock), and environment variables before deployment. | AAA. DevOps | `AAA07_devops_env_check.py` |
| **609** | **Flask: API to Manage Server List:** Create a Flask API that uses a mock database to manage a list of server hostnames and their statuses (Read/Write). | AAA. DevOps | `AAA08_flask_server_list_api.py` |
| **610** | **Monitoring Web App (Health Check Endpoint):** Create a basic Flask app with a `/health` endpoint that returns JSON status information (e.g., uptime, DB status mock). | AAA. DevOps | `AAA09_flask_health_endpoint.py` |
| **611** | **Data Pipeline Mock (ETL):** Write a function simulating an ETL (Extract, Transform, Load) process using Pandas for the transform stage. | AAA. DevOps | `AAA10_devops_etl_mock.py` |
| **612** | **Version Control Fundamentals (`GitPython` Mock):** Use a mock `GitPython` client to programmatically commit files and check repository status. | AAA. DevOps | `AAA11_devops_gitpython_mock.py` |

---
## Day 55: Final Capstone Projects (12 Programs)
Focus: Bringing together multiple concepts in large application scenarios.

| \# | Program Description (Focus) | Category | Filename |
| :-: | :--- | :--- | :--- |
| **613** | **Blackjack Game (Full OOP):** Fully object-oriented implementation of the card game with `Deck`, `Card`, and `Player` classes. | BBB. Capstone | `BBB01_capstone_blackjack_oop.py` |
| **614** | **Space Invaders Game (Basic Logic):** Implement the core game loop, player movement, and bullet firing logic (using a game library mock). | BBB. Capstone | `BBB02_capstone_space_invaders.py` |
| **615** | **Breakout Game (Collision Logic):** Implement ball movement and collision detection logic with paddles and blocks. | BBB. Capstone | `BBB03_capstone_breakout_collision.py` |
| **616** | **Disappearing Text Writing App (Tkinter/Timer):** Implement the full Tkinter GUI with the timer and auto-clear functionality. | BBB. Capstone | `BBB04_capstone_disappearing_text_gui.py` |
| **617** | **Personal Portfolio Website (Flask/Templates):** Build a multi-page Flask application using templates to display portfolio sections (Home, About, Projects). | BBB. Capstone | `BBB05_capstone_portfolio_flask.py` |
| **618** | **Typing Speed Test Desktop App (Tkinter/Logic):** Implement the Tkinter interface, text display, and typing speed calculation logic. | BBB. Capstone | `BBB06_capstone_typing_speed_test.py` |
| **619** | **Cafe & Wifi Website (Kanban CRUD):** Implement the full web application for the Kanban/Todo list, allowing items to be moved between status columns (mock DB). | BBB. Capstone | `BBB07_capstone_kanban_web.py` |
| **620** | **Virtual Bookshelf (Advanced UI/Authentication):** Combine user authentication (`Flask-Login`) with the CRUD database for a personalized bookshelf experience. | BBB. Capstone | `BBB08_capstone_bookshelf_auth.py` |
| **621** | **Deployment: Dockerizing a Flask App:** Create a `Dockerfile` and a simple entry point script (`app.py`) for a Flask application. | CCC. Deployment | `CCC01_deployment_dockerfile.py` |
| **622** | **Deployment: Gunicorn/WSGI Server:** Write a simple startup script to run the Flask application using Gunicorn (mock). | CCC. Deployment | `CCC02_deployment_gunicorn.py` |
| **623** | **Deployment: CI/CD Pipeline Mock (GitHub Actions):** Write a YAML structure that simulates a CI/CD pipeline using GitHub Actions to build, test, and deploy (mock stages). | CCC. Deployment | `CCC03_deployment_github_actions.py` |
| **624** | **Deployment: Serverless Function (Mock Lambda):** Write a Python function structured to run in an AWS Lambda or Google Cloud Function environment (event handler). | CCC. Deployment | `CCC04_deployment_serverless_mock.py` |
