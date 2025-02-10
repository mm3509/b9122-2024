# How can I disable AI completion?



# Installing PyCharm

After discussing with students in Office Hours, I have decided to support only one IDE (Integrated Development Environment), PyCharm. We already have a range of prior experience and operating systems, so supporting different IDEs could add additional and unnecessary complexity. I ask that all students install PyCharm (unlike what I wrote in lecture 1).

## installation steps

### Step 1: download

Please download PyCharm from [here](https://www.jetbrains.com/pycharm/download/) and run it (accept terms and conditions and stay with all default settings).

### Step 2 (optional): get a license

Optionally, you can get a license for education from [here](https://www.jetbrains.com/community/education/#students/), or you can wait for the end of the 30-day free trial.

### Step 3: new project

Open PyCharm, open a new project (call it "B9122", for example).

### Step 4: connect PyCharm to Anaconda Python

Even if PyCharm detects Python, make sure that it's connected to **Anaconda Python** and not to system Python.

#### Step 4.1 on macOS

Start a new shell. You should see `(base)` in it. If not check that you have conda:

```
which conda
```

If you have Conda, but do not see `(base)` when you start a shell, you'll have to run `conda activate` every time you start a shell. You can follow the installation steps again so that your shell activates conda every time.

If you don't have Conda, please install it, then try this again.

In a shell that shows `(base)`, run this:

```
which python
```

Copy that path to the clipboard, and go to Step 4.2

#### Step 4.1 on Windows

Start an **Anaconda Command Shell** (not git bash, or CMD, or PowerShell), and type:

``` python
where python
```

Copy the path you get from there.

#### Step 4.2: configure Python interpreter

Open PyCharm. You should see "Configure Python Interpreter" at the top right, then on "Add New Interpreter", then on "Add Local Interpreter". In Environment, "New" is selected, but click on "Existing". Click on the three dots at the right. Paste the path you got from Anaconda Command Shell. Click OK, then OK.

You succeeded if you no longer see "Configure Python Interpreter".

## Steps to create, run, and debug a file

Click on File > New Scratch File > Python file, and type:

``` python
a = "Hello world"
print(a)
```

At the top right, click on the button with the Play symbol to run it:

<img src="images/play_button.png" />

Under the file name "scratch.py", you have line numbers for the lines you typed; click on the number 2. A red circle should appear and indicates a breakpoint: Python will execute code and stop at this point:

<img src="images/debug_button.png" />

Click on the bug symbol next to the Play button:

<img src="images/play_button.png" />

The first line gets highlighted and execution stopped at your breakpoint. You are now inside the debugger:

<img src="images/debugger.png" />

In the bottom left of the program, there is a window called "Threads & Variables":

<img src="images/variables.png" />

Click on the box that says "Evaluate expression", then type and run this code: `a = None`.

<img src="images/inside_debugger.png" />

Hit the button "Play" at the left, which means "Continue execution":

<img src="images/continue.png" />

Switch to the console tab, to the right of "Threads & Variables":

<img src="images/debugging_result.png" />

You should now see that the Python program printed "None" instead of "Hello world".

That is: you changed a variable "on-the-fly", from inside the debugger, and concluded this part of the assignment.

## FAQ and Troubleshooting

### My PyCharm stopped working, what can I do?

Please try these steps, one at a time, and see if it solves your problem:

- restart the program / app

- restart the computer

- reinstall the program / app.

This simple procedure solves 90% of PyCharm problems, and indeed most computer problems.
