# FAQ

## I cannot install Tensorflow, or the assignment's requirements

Make sure that PyCharm is connected to Anaconda Python, i.e. follow this guide to change the interpreter in the PyCharm settings:

https://github.com/mm3509/b9122/blob/main/guides/PyCharm.md

Then start a shell.

If you don't see `(base)`, then your shell is not connected to Anaconda Python either, and please follow this guide to connect it:

https://github.com/mm3509/b9122/blob/main/guides/attendance-over-email.md

If you see `(base)`, then you are inside Anaconda. and you can install the assignment's requirements with:

```bash
pip install -r requirements.py
```

Then PyCharm should find tensorflow and the other required packages.

## Autograder doesn't complete or grade my homework

If the Autograder is not running for you, or does not finish in the required time, the TAs or I will fix your submission so it works. If it's something obvious, you may lose a few points on delivery. If it's something very tricky, you will not lose points.

