# Assignment #2 for B9122, Computing for Business Research

Out on Sep 30th, due on Tuesday Oct 8th, © 2024 Miguel Morin

Please note:

- This is a group assignment, with groups allocated randomly within sections.

- Now that we use GradeScope for automated grading, you should NOT add your UNI as a prefix to the code files you submit. Just edit the files and submit them as they are.

- Section "common errors" at the end of this assignment may change, as I get feedback on your different systems.

## Exercise 1: Interest rates, recursive (30 points)

This exercise is similar to assignment 1, but now I ask that you write a recursive function and more doc-tests.

### 1.1 Recursive function (10 points)

Complete the file `compound_interest.py` to compute the interest payment on the account with a recursive function. It's similar to Assignment 1, exercise 1.1, but with a recursive function.

Also complete the `calculate_interest()` function to call your recursive function. This is called a "helper" or "wrapper" function.

Note: you should NOT import the function you wrote for Assignment 1. You have to define a brand new function, from scratch.

Submit the file on GradeScope without changing the name.

### 1.2 Differential interest rates, recursive (10 points)

Complete the file `compound_interest_differential.py` to compute the interest payment on the account, taking into account baseline and bonus interest rates. It's similar to Assignment 1, exercise 1.2, but with a recursive function.

Remember that modules are just files, so you should `import` a function that you defined in question 1.1 to answer the current question.

Submit the file on GradeScope without changing the name.

### 1.3 Robustness (10 points)

Complete the file `compound_interest_differential_robust.py` to take
into account all the possible edge and corner cases you can think
of. Write these corner cases as doc-tests, then implement the code
that handles those edge cases.

Remember that modules are just files, so you should `import` a function that you defined in question 1.2 to answer the current question.

Submit the file on GradeScope without changing the name.

## Exercise 2: OCR and debugging (40 points)

TODO: move data source to Sci-Kit Learn, not Tensorflow.

### 2.1 Debugging (20 points)

The file `knn.py` implements the OCR system we mentioned in lecture 1. Install the required dependencies and check that you can run the code `knn.py`. The function `kNN()` in the general case is for your reference of how to implement k-Nearest Neighbors in the general case and you can ignore it.

This Python file has a bug. Find and correct it.

Note: this file has no doc-tests, so I give no indication of where the bug is.

(Hint: visually compare an image from the test data to its nearest neighbor from the training data.)

Submit the file on GradeScope without changing the name. Also submit at least 5 screenshots of your debugging steps, in PNG format, with names starting with `knn`, for example `knn1.png`, `knn2.png`.

### 2.2 Accuracy (15 points)

The file `knn_accuracy.py` imports the file above (whether or not you found the bug). Complete the function in the file to compute the accuracy of 1-nearest neighbor as an OCR system.

That is, run the algorithm on images from the test data (`test_x`), compare the algorithm's prediction to the true value (`test_y`), and report the percentage of images where the algorithm found the right answer.

Submit the file on GradeScope without changing the name.

### 2.3 Speed (5 points)

How long did your code take to compute the accuracy? Why do you think the Python code took that amount of time?

Submit your answer on GradeScope as a text file with `knn3.txt`.

### 2.4 Improvements (bonus, 5 points)

Inspect some of the images that the algorithm got wrong. Why did that happen? How could another algorithm solve it?

Submit your answer on GradeScope as a text file with `knn4.txt`.

## Exercise 3: System administration (30 points)

You installed my attendance software by pull the source code as text files; installing software this way is called "**from source**." When you installed Anaconda or PyCharm, you used an installer (a file with extension `.dmg` on `macOS` and `.exe` on `Windows`), which is a binary file (not a text file); installing software this way is called "**from binary**." Although it may have been frustrating, this question will show you some advantages of installing software this way.

Imagine that you attended a presentation and were given the video file with the recording. The file is 2 GB and contains nothing but slides. Unfortunately, the presenter did not give you the slides. You want to extract the slides as a PDF file so you can add your own notes, and also to save space (the PDF file could be 2 MB, instead of 2 GB for the video file).

This GitHub repository contains a Python tool to do that: [https://github.com/mm3509/video2pdf](https://github.com/mm3509/video2pdf) (adapted from the original at: [https://github.com/kaushikj/video2pdf](https://github.com/kaushikj/video2pdf) ).

### 3.1 Installation (10 points)

In a **new** shell, install this tool with `git` and `pip`, just like you did with my attendance code. See the end of this exercise for common issues.

Save the output from the shell as a text file and submit it on GradeScope as `system1.txt`.

### 3.2 Usage: presentation only (10 points)

I created a video file with the first 3 minutes of lecture 1 [here](https://www.dropbox.com/scl/fi/k97fjziyv60vs0f88aw0y/lecture_1_slides.mp4?rlkey=5r7sb7ddvkv7249mlzkdy49sf&st=b54y5gf3&dl=0). Download this video file (6 MB).

Use the installation from the previous step and run the tool on this file. Your output should contain between 3 and 6 images. I get 3 images when I run on my computer, the TAs got 5 images, you may get a different number and that is OK. Make sure your initial code captures all three slides at the start.

Submit these images on GradeScope without changing their name.

### 3.3 Usage: presentation + camera (10 points)

Sometimes, a video file has both the slides and a camera recording. In this case, the algorithm needs adjustment in order to detect the change in slides that is not from the change in the person's face.

I mixed the recording of the slides with the recording of the camera (if you're curious, I used FFMPEG: a cross-platform video editor that works from the shell!). Download this video file [here](https://www.dropbox.com/scl/fi/vol37jiyaogtzm36aiwlg/lecture_1_camera.mp4?rlkey=ahbqvy0stcmqhz2wo6e2mbzwh&st=m7hfdr5c&dl=0). If you run the tool on this file, it will save around 6 images when there are only 3 slides: it confuses the change in the camera recording as a possible change of slide.

Find the place in the source code where you can adjust the settings to ignore movement from the camera. Run the tool to extract the slides into image files. Check the files to confirm that you are not missing any slides. Your output should now contain a lower number of images with the camera (for example, on my computer it started at 6 and I got it down to 3). Your output should contain still contain all 3 slides.

Submit the edited file on Gradescope without changing its name: `video2pdfslides.py`.

Submit those files on GradeScope without changing their name.

### 3.4 PDF files (bonus, 5 points)

If you install an additional tool, `qpdf`, then you can convert these images into a PDF.

Install the tool. On macOS, if you don't have `brew` installed, you can install it with:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
echo 'export PATH="/usr/local/opt/python/libexec/bin:$PATH"' >> ~/.profile
source ~/.profile
```

You may get a warning that you need to add brew to your PATH. Please follow the steps in the "Next steps" section to get brew running. You succeed if you run:

``` bash
which brew
```

and you see something like this: `/usr/local/bin/brew`.

and then install `qpdf` with:

``` bash
brew install qpdf
```

You'll also need to install another required package that uses `qpdf`:

``` bash
python3 -m pip install img2pdf>=0.4.1
```

Run the tool again on the previous two questions (changing the setting as needed).

Submit the resulting PDF files with name `slides1.pdf` and `slides2.pdf`.

### 3.5 Advantages and disadvantages (bonus, 5 points)

What advantages do you see in installing software from source as opposed to binary? What disadvantages do you see?

Submit your answer in plain English (not code) as a text file: `system5.txt`.

### Common issues

#### `ModuleNotFoundError: No module named 'distutils.util'` or `error: subprocess-exited-with-error`

OpenCV (CV stands for "Computer Vision") has known issues with Python 3.12 on macOS. If you are running an earlier version and you see this error, please contact Miguel.

If you are running Python 3.12, you have three solutions:

1. Install OpenCV from a binary instead of from source. After cloning the repository, run this command:

``` bash
pip install -r requirements.txt --prefer-binary
```

Note the last flag, which indicates that PIP should not try to install the packages from source, using instead what someone else already built for your system.

2. Try other computers in your group to see if someone happens to be running a previous version.

3. Create a virtual environment with a previous version of Python with Anaconda. Run this command:

``` bash
conda create -n "envVideo2pdf" python=3.11 ipython
```

If that succeeds, activate the environment with:

``` bash
conda activate envVideo2pdf
```

and proceed with the assignment.

If you are comfortable with cloud computing (AWS, Google Cloud, or IBM Cloud), you can create a virtual machine on the cloud running Python 3.12 on Linux (which does not have these issues) to handle this task.
