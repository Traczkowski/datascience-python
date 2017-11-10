# Assessment #1

Welcome to your first assessment.  This assessment does not count towards your course performance, it is only used by your instructor team to gauge your strengths and weaknesses so they can provide you a better learning experience throughout the immersive program.

You will have 120 minutes to complete the two part assessment, after which you will submit a pull request which we will use to find and assess your work.

* Time: 120 minutes
* Open book
* Individual

## Instructions

The first step in taking this assessment (and all those to follow later) is to **fork this repository to your own github account**.  Your fork will retain private status, and be visible only to you through your account.

**After forking this repository to your own account** clone your copy using the git client in your terminal.  For example, when cloning a forked copy of this assessment, user `madrury` used the command:

```
git clone https://github.com/madrury/dsi-assessment-day1.git
```

This will copy the repository on your computer so that you can edit the files.  When you are finished with the assessment, **add** the `assessment.py` and `math_assessment.txt` to your git staging area, **commit** them, and then **push** them up to your Github account.  Finally, when you can see your modified files on your Github page, issue a **pull request** on Github to merge them into the gSchool repo (so we can see and grade them).  The git commands will look like this:  
```
git add src/assessment.py math/math_assessment.txt
git commit -m "<Your Name> Assessment 1 solutions"
git push origin master
```
Please ask for help from an instructor if you need help forking on Github, cloning and pushing with git from terminal, or issuing a pull request on Github.  

### Python version
Take this assessment in **Python 3**.  To check which version of Python is installed natively, type `python --version` in the terminal.  If it's Python 2, activate the Python 3 environment you made in the Precourse or Week 0:  
```
source activate py3
```
If you're running Anaconda's distribution of Python 2 natively and haven't made this environment before, it's easy to do though the download takes a few minutes.  In terminal type:
```
conda create -n py3 python=3 anaconda
```        
Only create the Python 3 environment if you **don't** have Python 3 installed.

## Assignment

The repository has the following folder structure:

    assessment-day1
    ├── Makefile
    ├── README.md
    ├── src
    │   ├── __init__.py
    │   ├── assessment.py
    ├── data
    │   ├── alice.txt
    │   ├── markets.sql
    ├── test
    │   ├── __init__.py
    │   └── unittests.py
    └── math
        ├── math_assessment.pdf
        └── math_assessment.txt

The goal of this assignment is to fill in each function stub to make the associated test pass.

There are 21 questions over these topics in this order:
* general Python (4 questions)
* probability (1 question)
* numpy (2 questions)
* pandas (2 questions)
* SQL (3 questions)
* Math (9 questions)

**There are two parts to this assessment!  Please complete both!**

1. `src/assessment.py` contains function stubs for you to fill in. The goal is to make the tests pass. There are 12 problems in the file.

 * **Running Unit Tests**

 * This section (`src/assessment.py`) can be tested using the unit tests. You can run the tests with this command from the root directory (dsi-assessment-day1/):    

    `make test`

 * If you do not have py.test, you may see Import errors. Run the following commands in case you see such errors:    

    `pip install pytest`     

 * `.` refers to passing test, `E` is an error in the code and `F` is a failure. So something that looks like this: `....EFFFFFF` means 4 tests passed, one has an error and 6-11 fail.
 * It can be helpful to press enter a bunch of times between each time you run the test so that it's easy to find the beginning of your most recent results.    


2. The questions for the math portion of the assessment are in
  `math/math_assessment.pdf`. Put your answers in `math_assessment.txt`.
  There are no automated tests for this portion of the assessment.

* At the end of 120 minutes, submit a pull request.

**Feel free to use any online resources like python documentation and tutorials, your notes, readings and exercises.**

Good luck!
