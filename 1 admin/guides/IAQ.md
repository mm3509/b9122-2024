# Infrequently Asked Questions

This document contains answers to questions infrequently asked, which I will answer here to keep the precious lecture time focused on the material.

## Lecture 6, morning

### Can I run code in PyCharm like I would in a Jupyter Notebook?

Yes, you can. Select the code you want to run, right-click on it, then choose `Execute Cell in Console`.

You will then see an interface similar to Jupyter.

## I don't see `Inspect Element` in Safari

You need to enable Developer tools to see the page source of a web page (detailed steps [here](https://www.howtogeek.com/721416/how-to-turn-on-the-develop-menu-in-safari-on-mac/)).

## Lecture 6, afternoon

### How does SciKit-Learn compare to the built-in Statistics module?

From the [documentation](https://docs.python.org/3/library/statistics.html):

> The module is not intended to be a competitor to third-party libraries such as NumPy, SciPy, or proprietary full-featured statistics packages aimed at professional statisticians such as Minitab, SAS and Matlab. It is aimed at the level of graphing and scientific calculators.

For example, you can compute means, standard deviations, and even a linear regression using the `statistics` module.

For more advanced models like logistic regression and k-Nearest Neighbors, we need SciKit-Learn. So we just use SciKit-Learn.

### Why is the identity matrix called `eye`?

In math, the identity matrix uses the single letter "I" and the "spelling name" for it is "eye" or "aye". For more details, or other spelling names, read [this thread](https://math.stackexchange.com/questions/3028394/what-is-the-motivation-behind-naming-identity-matrix-as-eye).

### Why is it called "saving to disk"?

Back in the day, hard drives were magnetic disks spinning around. Even though now our storage today is not on disks (we have "solid state drives" and "flash storage"), the expression stayed. The reason is similar to why the "save" icon is a [floppy disk](https://en.wikipedia.org/wiki/Diskette), or "diskette", even though we haven't used them for 20 years.

## Lecture 8, morning

### What's the equivalent of `pbcopy` for Windows?

You can use `clip`, or a custom function from [this thread](https://superuser.com/questions/472598/pbcopy-for-windows) to avoid the carriage return:

``` bash
function cpy {
while read data; do     # reads data piped in to cpy
    echo "$data" | cat > /dev/clipboard     # echos the data and writes that to /dev/clipboard
done
tr -d '\n' < /dev/clipboard > /dev/clipboard     # removes new lines from the clipboard
}
```

Save this text at the end of the file `$HOME/.bashrc`. You can then call it with `cpy`, for example by piping a command to it: `echo Hello world | cpy`.

### How can I use `more` in Git Bash on Windows?

Please use `less` instead, which works the same way.

### How can I use `man` in Git Bash on Windows?

Git Bash does not support `man` for the manual page, but you can use this instead: `command-name --help`, for example `less --help`.

### How can I produce a sequence with a step in curly brace expansion?

Add a third number in the curly expansion:

``` bash
echo {0..10..2}  # prints 0 2 4 6 8 10
```
