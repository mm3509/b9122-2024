# Marking attendance over email

This file explains how to install and mark attendance. For PyCharm, please go [here](PyCharm.md).

## Step 1: Install software to mark attendance (one-off)

You only need to follow these steps once (or multiple times, if you choose to install manually instead of git). Each step ends with a validation for you to confirm that it succeeded

### Step 1.1: Install a bash shell

#### On Windows

Download and install Git for Windows from: [www.gitforwindows.org](https://gitforwindows.org). Say OK to all the default settings. Add the program to the task bar and you should see this symbol:

<img src="https://avatars.githubusercontent.com/u/4571183?s=200&amp;v=4" width="100" height="100" alt="@git-for-windows">

#### On MacOS

1. Search for `Terminal.app` on Spotlight. Launch it. Start a **new shell** with Command-N (N for new).

Go to the Dock, right-click on the Terminal application, click on "Options" and then on "Keep in Dock", so it's always there. You should see a program running with this symbol:

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Terminalicon2.png/120px-Terminalicon2.png">

#### Validation

Copy-paste this code and press ENTER:

``` bash
echo $HOME
```

You succeeded if you see the path to the home folder of your computer, e.g. `/Users/<your-username>` on macOS or `/c/Users/<your-username>` on Windows.

### Step 1.2: Clone this repository

Note: Ater lecture 4, manual download of this repository from GitHub is no longer supported. Only git and command shell are supported.

Start a **new shell** and copy-paste this code:

``` bash
cd; git clone https://github.com/mm3509/b9122
```

At the end, you should see something like this:

``` bash
Cloning into 'b9122'...
remote: Enumerating objects: 64, done.
remote: Counting objects: 100% (64/64), done.
remote: Compressing objects: 100% (41/41), done.
remote: Total 64 (delta 34), reused 46 (delta 19), pack-reused 0 (from 0)
Receiving objects: 100% (64/64), 9.39 KiB | 1.88 MiB/s, done.
Resolving deltas: 100% (34/34), done.
```

#### Common error 1

If you get an error that the repository already exists:

```
fatal: destination path 'b9122' already exists and is not an empty directory
```

then please run this code instead:

```
if [ -d ~/b9122 ]; then mv ~/b9122 ~/b9122_backup; fi
cd; git clone https://github.com/mm3509/b9122
if [ -d ~/b9122_backup ]; then mv ~/b9122_backup/\.*.txt ~/b9122/; rm -rf b9122_backup; fi
```

#### Common error 2

``` bash
Please commit your changes or stash them
Aborting...
```

then please copy-paste this code in a shell and press ENTER:

``` bash
cd; cd b9122; git stash; git pull
```

and then run:

``` bash
python3 -m pip install -r requirements.txt; python3 mark_attendance.py
```

#### Common error 3

On macOS, if you get this error:

```
xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
```

then install XCode command-line tools again with this command:

```
xcode-select --install
```

#### validation

Copy-paste this code in a shell:

``` bash
cd; cd b9122; ls mark*
```

You succeeded if you see this:

``` bash
mark_attendance.ipynb mark_attendance.py
```

### Step 1.3: Connect the shell to your installation of Python

#### On macOS

Normally, you don't need to do anything. Python is already installed on macOS, and if you installed Anaconda Python properly, every new shell starts in an Anaconda environment.

Please come see me if you have issues.

#### On Windows

1. Make sure you installed Anaconda Python from [here](https://www.anaconda.com/download/success).

2. Open a text editor, like Notepad:

<img src="https://play-lh.googleusercontent.com/jD8waDJPN1yv4OdcB6_ILw9M4kyNPdtgBYtoTiPrYhxA1l4FLSKXXe4kAcDCjmtZmQ4=w240-h480" />

3. Run an **ANACONDA COMMAND PROMPT SHELL** (it's different from a Git Bash shell!). To do so, in the Windows search box, search for "Anaconda prompt", look for it, and press Enter to run it.

4. Type this command (and notice it's **conda**, not **anaconda**):

``` bash
where conda
```

You should see a list of paths that start with "C:\Users\...". The first line ends with "conda.bat". Take the first line and copy it into Notepad. Remove the text starting from `\Library`, change the initial `C:\` to `/c/`, and change all backslashes to forward slashes, from `\` to `/`. You should see something like this in Notepad: "/c/Users/your-username/anaconda3".

<img src="https://play-lh.googleusercontent.com/jD8waDJPN1yv4OdcB6_ILw9M4kyNPdtgBYtoTiPrYhxA1l4FLSKXXe4kAcDCjmtZmQ4=w240-h480" />

Now add this text to the end of path on Notepad: "/etc/profile.d/conda.sh", so it becomes "/c/Users/your-username/anaconda3/etc/profile.d/conda.sh".

<img src="https://play-lh.googleusercontent.com/jD8waDJPN1yv4OdcB6_ILw9M4kyNPdtgBYtoTiPrYhxA1l4FLSKXXe4kAcDCjmtZmQ4=w240-h480" />

4. In a **Git Bash shell** (not a CMD shell, nor a Power Shell, nor an Anaconda shell), edit this code so the first line uses the path from Notepad in the step before (notice the space between the period and the path from Notepad), and press ENTER:

``` bash
echo ".    <the-path-from-notepad>" >> ~/.bash_profile
echo "conda activate" >> ~/.bash_profile
echo 'alias python3="python"' >> ~/.bash_profile
```

Note that the last line creates an alias to call `python` whenever you type `python3`. This is for compatibility with my material (because some computers have both `python` for Python 2 and `python3` for Python 3).

5. For these changes to take effect, close your shell and open a new one.

##### Errors

If Windows open the Microsoft Store when you run `python` in a shell, please remove the execution aliases. Go to Settings > Apps and features > App Execution Aliases and turn off the items called "App Installer" that start with `python` and end with `.exe`. See [this thread](https://superuser.com/questions/1437590/typing-python-on-windows-10-version-1903-command-prompt-opens-microsoft-stor/1461471#1461471) for details.

<img src="https://i.sstatic.net/cbdFj.png">

#### Validation

You succeeded if you can get the Python version from a shell (Terminal.app or Git Bash):

``` bash
python3 --version
```

You should see something like:

``` bash
Python 3.12.4
```

### Step 1.4: Install the requirements for this repository

1. Open a new shell (Terminal.app or Git Bash)

2. Copy-paste this code and press ENTER:

``` bash
cd; cd b9122; git pull; python3 -m pip install -r requirements.txt
```

You should see something like:

``` bash
Requirement already satisfied: requests in ...
```

#### Validation

You succeeded if you can type this in a shell (Terminal.app or Git Bash) and press ENTER:

``` bash
cd; cd b9122; python3 mark_attendance.py
```

and see this result:

``` bash
********************

Success! You did well. Software version: September 28th, 2024

********************
You have the right software and you can run this, but you'll need to be in class to validate it
...
```

### Step 1.5: Define a shortcut (alias) to run the code (optional)

#### On macOS

Start a new shell. We'll use the Nano text editor, which can be daunting at first, to edit a system file that macOS normally doesn't let us access:

``` bash
sudo nano ~/.zshrc
```

Enter your password

Use the down arrow key to get to the bottom of the file, then type this code AS-IS:

``` bash
alias miguel="cd; cd b9122; python3 -m pip install -r requirements.txt; python3 mark_attendance.py"
```

Hit Control-O to save the file, then ENTER to validate that save. Hit Control-X to exit the editor.

#### On Windows

Start a new shell, copy-paste this code, and press ENTER (it may ask for your password):

```
echo 'alias miguel="cd; cd b9122; python3 -m pip install -r requirements.txt; python3 mark_attendance.py"' >> ~/.bash_profile
```

#### Validation

Now you can mark attendance by simply running `miguel` in a shell.

Start a **new shell**, copy-paste this code, and type ENTER:

```
miguel
```

You succeeded if you see this result:

``` bash
********************

Success! You did well. Software version: September 28th, 2024

********************
You have the right software and you can run this, but you'll need to be in class to validate it
...
```

## Step 2: Update software to mark attendance (recurring)

I may update the software to fix bugs or to incorporate your feedback, so you'll have to update it as well.

After following the steps above to install the software, you can update it by starting a shell (Terminal.app on macOS or Git Bash on Windows), typing this code and running it:

``` bash
cd; cd b9122; git pull; python3 -m pip install -r requirements.txt; python3 mark_attendance.py
```

or simply calling the "alias" defined in the installation:

``` bash
miguel
```

### Common error

If you get an error such as:

``` bash
Please commit your changes or stash them before you merge
Aborting
```

then please copy-paste this code in a shell and press ENTER:

``` bash
cd; cd b9122; git stash; git pull
```

## Step 3: How to mark attendance

After following the steps below to install, here is how to mark attendance.

### Step 3.1: Mark attendance from the shell

Start a shell (`Terminal.app` on macOS, `git bash` on Windows) and run this command:

```bash
cd; cd b9122; git pull; python3 -m pip install -r requirements.txt; python mark_attendance.py
```

### Step 3.2: Run from PyCharm (or another IDE)

Start your favorite Integrated Development Environment (IDE), such as PyCharm. Open the file `b9122.py` in the IDE. Normally, this file is at `$HOME/b9122/b9122.py`, i.e. in the `b9122` folder that inside your Home folder (the Home folder is the folder one level up from Downloads, Desktop, etc). Run the file.

We only support PyCharm but you are free to run and debug from your own IDE.

For example: you can run from VS Code, but sometimes it does not work with my software, so please run from the shell instead.

## Notes for Windows users

1. You may run a Python command on git bash and it seems stuck: nothing happens, and the shell does not respond. That appears to be a bug, and git bash does not show output, even though it is running. If you hit Control-C (the universal keystroke to stop a program), you may see output. If you have this issue, I suggest running from PyCharm instead (and make sure PyCharm is connected to Anaconda Python, [per the guide](PyCharm.md)).

You can also it and run it again to see if that fixes your issue, or ask for my help.

1. Whenever you see a command like `python` or `python3` alone in my material, you have to add ` -i` to the command to run an interpreter. Otherwise, Python is running but you don't see it, and it seems like nothing happens. Close the window and start a new one.

