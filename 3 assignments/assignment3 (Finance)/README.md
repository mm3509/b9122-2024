---
title: 'Assignment 3 - B9122, PhD Computing for Business Research - morning section'
subtitle: 'Miguel Morin, (c) 2024'
geometry: margin=2cm
numbersections: true
colorlinks: true
header-includes:
- \pagenumbering{gobble}
- \setlength{\parskip}{\baselineskip}
- \usepackage{hyperref}
- \usepackage{xcolor}
- \newcommand{\link}[1]{{\color{blue}\underline{\href{#1}{#1}}}}
---

**Preliminaries**

Unlike previous assessments, this assignment is worth 140 points. All exercises are worth 10 points, except the last two, which are worth 20 points.

This assignment has a higher number of shorter questions. It should give you a lot of practice writing Python code and submitting it on Gradescope in preparation for the final.

For all these questions:

1. complete the Python function in the relevant file and submit it on Gradescope without changing file or function name;

2. do not use any modules or libraries, please write the functions from scratch (exceptions are `doctest`, `sys` and `os`, which you are allowed to import);

3. the exception to the above banning of modules is other files you wrote in this assignment: you should be importing to be DRY;

4. all your functions should have at least 3 doc-tests (unless stated otherwise) and apply defensive programming.

# Exercise 1: List manipulation

This function rotates a list to the right by a given number of steps. It should return a new list. It should also wrap around the initial list.

You can use "slicing" (define a list `a` and check what `a[:2]` and `a[2:]` do), and built-in operators.

# Exercise 2: List slicing

This function takes a list and a positive integer `n` and returns every `n`-th element from the list, starting from 0. For example, if `n` is 2, you should return elements at every even position, starting from 0. You can use slicing notation, i.e. if `a = list(range(10))`, then check what is `a[::3]`.

# Exercise 3: Dictionary manipulation

This function takes a string and counts the frequency of each character. It should return a dictionary with each character as the key and its frequency as the value.

A character is anything represented in a string: space, punctuation, numbers (in string format). An uppercase letter and the same letter in lowercase are different characters.

Do not use any built-in functions like `collections.Counter` .

# Exercise 4: Tuple manipulation

This function takes a tuple of integers and returns a new tuple containing only the unique integers from the original tuple, in the order they first appeared.

For speed, you can use the built-in function `set()`, which checks if an element is in a set. Run `pydoc set` from a shell or `help(set)` from a Python interpreter to read the documentation.

# Exercise 5: String manipulation

This function takes a string as input and returns a new string with all vowels removed, all other letters in lower case, and all other elements unchanged.

In English, the letter "y" is sometimes a vowel (as in "by") and sometimes a consonant (as in "yard"). For this exercise, it's considered a vowel.

# Exercise 6: Empty string

This function checks if a given string is a palindrome. A palindrome is a string that reads the same forwards and backwards. Case should not matter, i.e. `"Abba"` is a palindrome. The function should also handle the case of an empty string, i.e. `""` which is a string of length 0, and should also be considered a palindrome.

You can assume that the string has no spaces and Autograder will not pass a string with a space.

# Exercise 7: In-place

This function removes all occurrences at even indices from a list. To check if a number is even, use the modulo operator, `%`, which gives the remainder of an integer division, i.e. `5 % 2` gives 1. The function should work **"in-place"** and modify the original list.

Hint: if you are sure your function has the right logic but Gradescope gives you errors, read about "local scoping".

# Exercise 8: View vs. copy

This function takes a list of years and modifies it **in-place** removing all the numbers in the original list that are not leap years. (In-place means that it uses **a view and not a copy** of the original list.)

This question is tricky: if you iterate on the index of a list, find that index 0 has a leap year, and remove it, then the year at index 0 has now changed. There are a few ways to do this and you can choose any of them.

# Exercise 9: Copy / return (not "in-place")

These two functions do the same thing and reverse a list. One works in-place and is tricky to program. The other function does not work in-place and returns a new list.

This exercise is meant to teach that, in this case, "in-place" seems clunky and returning a new list is much easier.

Do not use the built-in list method `.reverse()`; you have to write the function from scratch.

# Exercise 10: debugging

This function removes all occurrences of an item from a list. It has a bug because it does not perform as we expected, and does not pass the doc-tests. Find the bug and fix it. (You do not need to add doc-tests.)

# Exercise 11: imports, system arguments, and dunder variables (20 points)

This function that checks whether two strings are anagrams. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. Case does not count (i.e., uppercase "A" is the same as lowercase "a") and spaces do not count: for example, "The Morse Code" is an anagram of "Here come dots". You should ignore punctuation like apostrophes and periods.

If this file is called directly, it should get the two arguments passed by the shell with `sys.argv[1]` and `sys.argv[2]`
(the first argument, `sys.argv[0]`, is the path to the Python file),
and print a Boolean for whether they are anagrams.

That is, if you run this in a shell:

```
python exercise11.py "The Morse Code" "Here come dots"
```

it should print

```
True
```

But, if you import this file somewhere else, it should not do anything. In particular, it should not throw an error.

Also, your code must handle the corner case where not exactly two arguments are passed to the function. Check this with `python exercise11.py 1` and `python exercise11.py 1 2 3`.

# Exercise 12: Prime numbers and the sieve of Erathostenes (20 points)

A prime number is a number that is only divisible by itself and the number 1. It has no other divisors. By convention, the number 1 is not a prime number.

The file has three functions:

- `is_prime(n)` should check if `n` is a prime number in the usual, slow way checking the remainder of integer division by numbers from 2 to `int(sqrt(n))`).

- `get_primes_slow(n)` should use the first function to return a list of prime numbers from `2` to `n`.

- `get_primes_fast(n)` should use change the algorithm design completely and use the ["Sieve of Erathostenes"](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) to return a list of prime numbers from `2` to `n`.

You are allowed to `import math` in order to use the square root function: `math.sqrt()`.

Complete the functions. Add a doc-tests to ensure that your fast function finds the same prime numbers as your slow function. Submit the file on Gradescope without changing the name.
