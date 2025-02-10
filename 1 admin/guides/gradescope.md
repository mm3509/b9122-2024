# Gradescope

We use GradeScope for submissions.

## Submission checklist

Please ensure that you run these checks locally, on your computer, before uploading to Gradescope.

### Delivery: Your file is valid code

Make sure that your file is valid Python. For example, for a file called `exercise1.py`, run this in a shell:

``` bash
python exercise1.py
```

And solve any `SyntaxError` or `IndentationError` that you see.

Your Python file should follow this structure (without my comments):

```python
# Imports at the top
import sklearn


# Global variables next, uppercase
NEIGHBORS_KNN = 2


# Functions come next.
def square(num):
    """
    This is a doc-string. It's the triple-quoted string right after a function
    definition. It contains doc-tests. For now, you don't to write anything here
    other than doc-tests.
    
    These are doc-tests, starting with triple angled brackets and a space.
    The line after the triple-quoted bracket is the expected result.
    Corner cases should use the syntax below for the "traceback" of the error.
    >>> square(2)
    4
    >>> square("2")
    Traceback (most recent call last):
    ...
    ValueError: argument must be a number
    """
    
    if not isinstance(width, (int, float)):
        raise ValueError("argument must be a number")
        
    return num ** 2
    

# Classes come next, if any.
class MyClass(object):
    pass


# A main function comes next, if any.
def main():
    pass


# Finally, if you want to run code when the file is run but not when it's imported,
# use the "dunder" variable `__name__`, which is then equal to "__main__":
if __name__ == "__main__":
    main()
```

### Doc-tests: Your file passes your doc-tests

You should write at least 3 doc-tests for each of your functions, unless the assessment says otherwise. Doc-tests are inside the doc-string (which is the first string after the function name), and are anything that starts with `>>> `. They always follow this pattern: code to execute after `>>> `, and the result expected in the next line. Here is an example that you should copy for your doc-tests:

``` python
def compute_square(num):
    """
    >>> compute_square(2)
    4
    >>> compute_square(1.1)
    1.21
    >>> compute_square("2")
    Traceback (most recent call last):
    ...
    ValueError: argument must be a number
    """
    if not isinstance(num, (int, float)):
        raise ValueError("argument must be a number")
        
    return num ** 2
```

Make sure that your file passes your doc-tests. For example, for a file called `exercise1.py`, you would run this:

``` bash
python -m doctest exercise1.py
```

If you see nothing, your file either has no doc-tests or they all pass. If you want to see the full output of the test, add the `-v` switch (v for "verbose"):

``` bash
python -m doctest -v exercise1.py
```

Alternatively, you can add this "boilerplate" code at the bottom of your scripts so PyCharm runs your doc-tests:

``` python
import doctest

if __name__ == "__main__":
    tests_failed, tests_run = doctest.testmod(optionflags=doctest.ELLIPSIS)
    if 0 == tests_run:
        print("Unable to run doc-tests")
    elif 0 != tests_failed:
        print("Some doc-tests failed")
    else:
        print("Your doc-tests pass, congratulations!")
```

## Comments from TAs

If a TA deducted points from your submission, you can see the exact reason why and improve your code. For example, in this question, the student lost 0.5 points for bad variable naming:

![](../../.images/TA-comments3.png)

Sometimes the TA's add specific comments to help you improve. On Gradescope, click on your submission, then on "code" at the top right, and you'll see a "speech bubble" with comments the TA left for you, as in this picture:

![](../../.images/TA-comments1.png)

If you click on the exercise and scroll down, you'll see the comment that the TA left for you:

![](../../.images/TA-comments2.png)

## FAQ

### How to create an account

Click on "Gradescope" on the left bar on Canvas and use your Columbia email.

### How to upload a submission

[Here](https://courseworks2.columbia.edu/files/21823761/download?download_frd=1) is a screencast from Canvas on how to upload a submission.

### Autograder is unresponsive, what do I do?

Gradescope seems to have a bug and shows a page saying `The autograder hasn't finished running yet.` well after the 10 minute timeout:

![](../../.images/Gradescope_unresponsive.png)

In this case, please submit again and Gradescope will try to grade again.

### How do I upload a PDF file?

Click "Submit" or "Resubmit", then just drag-and-drop a PDF file onto the window.

### I got an encoding error, asking me to submit as ASCII or UTF-8. How do I fix it?

A file encoding translates bits (0-1 on the hard drive) into text
characters. Different countries need different characters: the US does not need accents, so it uses a simple encoding system that uses one byte (8 bits, 256 possible values) into characters: 26 uppercase letters, 26 lowercase letters, and other symbols. It's called ASCII (American Standard Code for Information Interchange).

European countries need accents on vowels ("être" in French, "tchüss" in German), diacritcs on consonants ("niño" in Spanish) and so need considerably more than 256 possible values. The solution was to still use bytes, but to have multiple bytes for a single character (for example, "ê" in French is first the accent "^" and then the letter "e"). It's called Unicode, or UTF-8 (for Unicode Transformation Format – 8-bit). The UTF-8 is the standard in Python: all strings are UTF-8 strings.

This can accommodate most Chinese and Korean characters, but not all. So there is another standard, UTF-16 (for 16 bits) that encodes all possible characters from all possible alphabets, and also encodes emojis.

Gradescope only supports ASCII and UTF-8 files. If you click on "Code" in your submission, you'll see that Autograder cannot display your text files.

Please search online for how to save files in UTF-8 or ASCII. For example, if you use Notepad, search for "how to save notepad file in ASCII". Alternatively, please come to office hours.
