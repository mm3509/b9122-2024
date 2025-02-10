# Assignment 1

Out on Sep 20th, due on Tuesday Oct 1st (not Sep 30th!), © 2024 Miguel Morin

Bonus questions are optional, but will increase your grade up to a maximum of 100 points.

Note 1: the rubric on speed and efficiency will NOT be used to grade this assignment.

## Clarifications from student questions

- Please see the Canvas discussion for any clarifications on or after Sunday, September 29th, 2024.

- PyCharm may not run the doctests, depending on your configuration (I can fix it for you in Office Hours). To be sure that your function passes the doc-tests, please run the Python file from a shell ("python3 compound_interest.py"), which is sure to run the doc-tests (if you see a message “Unable to run doc-tests”, please come to Office Hours).

- In exercise 1, assume that the input list is sorted in ascending order (as implied by one of the doc-tests).

- Exercises 2.3 and 2.4 require answers in plain English, not in code. Please write your answers in a TXT file and submit that. Please do NOT submit a Word document, which has extension .doc or .docx and not .txt (plus, I do not even have Microsoft Word installed!).

- If you have issues in the doc-tests of exercise 2, it may be because the doc-tests assume that days are zero-indexed. That is, a transaction with details (5, 500) actually happens on the 6th of the month.

- I added doc-tests to all coding exercises, and added more doc-tests to cover the questions I have been getting. The new files are now in the GitHub repository and no longer on Canvas. To get the files, you can run “cd; cd b9122; git pull” or go to this link: [https://github.com/mm3509/b9122/tree/main/assignment1] .

- You can see the differences in the files for assignment 1 with [https://github.com/mm3509/b9122/compare/132e7fc..3828a87#diff-bf15504ed1c9da355ea405b11c0a90ef1ae13d66956d6db6f67113a3ad0ea6f8||this link], or by running this command in the console “cd; cd b9122/assignment1; git diff 132e7fc HEAD *” (each red line starts with - and has the lines I removed; each green line starts with + and has the lines I added).

- There are no trick doc-tests. That is, I do not expect you to anticipate corner cases in exercise 2 (you have to do so in exercise 1, but for exercise 2 I prefer that you focus on the logic).

- I delayed the due date of this assignment by 1 day, so you can come to my office hours on Tuesday (and other assignments will also be due on a Tuesday).

- If your code does not pass the doc-tests, please use the PyCharm debugger to run through the doc-test case where it fails. That is: copy the test case from the doc-test to the bottom of the file, remove the leading angled brackeds on each line (`>>> `), insert a breakpoint in the call to the function, run the debugger, and step into the function to find your bug.

- In exercise 2, the interest rate has to compound daily.

- I changed the name of the file to be submitted in exercise 2.2: it's now “<your-uni>_compound_interest2.py”.

- Your answers with Python code must be submitted as Python files (with extension .py) instead of Jupyter notebooks (with extension .ipynb). The reason is that we will use automated grading tools to run, test, and grade your Python code.

- In exercise 2.2, the chosen rate, either baseline or bonus, applies to the whole month.

- During Office Hours, students found one edge case I had not considered, so I added doc-tests to the function of exercise 2.1. The new file is on Canvas.

- I didn't add doc-tests to question 2.2 to help you check if your code was right, so I uploaded the new file on Canvas.

- Bonus questions are optional: you don't have to complete them.

- What I mentioned in class (about MSFE students having an extra exercise) is void. Instead, I changed the assignment to be suitable to all students. All students must complete both exercises 1 and 2 in this assignment (but bonus questions are optional).

- For bonus question 2.3: if your bank does not provide a traditional bank statement, you can instead upload a screenshot of your transaction history that clearly shows the interest payments and the principal.

- The file `compound_interest.py` is on Canvas, under "assignment1" (which I had forgotten to publish on Friday, so I apologize for that).

- You can import libraries to complete the assignment, e.g. \texttt{numpy}.

- Where I do not provide a file with doc-tests, you have to write the tests yourself to get full credit for the exercise (see the grading rubric in the syllabus).

- For questions 2.3 and 2.4, I expect a verbal answer, not Python code. I ask for it as a text file (“.txt”) to run comparison and similarity checks.

- The file “compound_interest.py” had a typo, which is now fixed (“interest == calculate” changed to “interest = calculate”).

- I ask for text file submissions so we can run code comparisons and similarity checks.

- When testing that code passes the doc-tests, I recommend using the shell, which is more reliable. Jupyter doesn't always find and run the doc-tests (in lecture 3, only one student had a configuration that worked). You don't need to open a new shell each time you change code and want to test it: you can keep the same shell open, in the same directory, and just run the doc-tests when you change code.

- Regarding comments, adding a comment on every single line will cause you to lose points. Please follow the guidance from the assigned reading so you use comments wisely and sparingly: [https://stackoverflow.blog/2021/12/23/best-practices-for-writing-code-comments/||link here].

- I cannot comment on the correctness of anyone's code, because it would be unfair on the others, but I am trying to implement a solution with Gradescope that allows you to check the correctness of your code and get an indication of your grade.

## 1 Unique elements (30 points)

This question is inspired by the book "A practical guide to quantitative finance interviews", so it's a question you could really be facing in interviews.

Download the file `unique_elements.py` from this GitHub repository.

Complete the function so that it takes a sorted list of numbers in ascending order and extracts the unique elements from it. For example, if the list is `[2, 2, 4, 4, 6, 8, 9, 10, 10]`, it should return a list with `[2, 4, 6, 8, 9, 10]`. The returned list should still be ordered. Make sure that your function passes all the doc-tests.

Submit your file as `unique_elements.py`.

## 2 Compound interest (70 points)

Some savings accounts compute interest rates daily and pay it monthly (e.g., this one by [HSBC UK](https://www.hsbc.co.uk/savings/products/online-bonus-saver/). That is, if the account receives money, for example $100 on the 3rd of the month, the bank pays daily interest on that amount from day 3 onwards.

### 2.1 Simple function (35 points)

Download the file `compound_interest.py` from this GitHub repository.

Complete the Python function that computes the interest that the bank has to pay into the account at the end of the month.

The function takes as arguments:

- the initial balance

- the yearly interest rate

- the transactions on the savings account, in the format of a list of tuples: [(day, amount), ...]

Assume that a transaction always happens at the start of the day, i.e. a credit starts accumulating interest on that day. Make sure that your function passes all the doc-tests.

Submit your code as a file: `compound_interest1.py`.

### 2.2 Differential interest rates (35 points)

HSBC actually pays a bonus interest rate in case the account has no debits (currently 4%, as opposed to 2% if an account has debits). This rate, either baseline or bonus, applies to the whole month.

Download the file `compound_interest_differential.py` from this GitHub repository. Complete the function so that it takes this difference into account. The function takes as arguments:

- the initial balance

- the yearly baseline interest rate (e.g., 0.02 for 2%)

- the yearly bonus interest rate (e.g., 0.04 for 4%)

- the transactions on the savings account, in the same format as before.

Submit your code as a file: `compound_interest2.py`. Make sure that your function passes all the doc-tests.

### 2.3 Bonus: real-life bank statements (5 points)

If you have a bank account that pays interest, get a statement for one month (or a quarter, or a year), and type the values (balance, interest rate, transaction list) ready for your function. Run your function to compute the interest payable. Compare the value of the interest you computed to the one you received. Do you find a discrepancy? Why could that be?

Remove the personal information from your bank statement and upload the file as a PDF or an image.

Submit the answer as `compound_interest3.txt`.
