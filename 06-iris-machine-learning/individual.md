# Python Review Case Study

To work on this assignment, you will need to fork and clone this repository according the the routine provided in Learn.

Create an individual branch and switch (checkout) to this branch before starting to work on the assignment.

When working on this assignment, regularly add/commit/push your code.


## General Guidelines

We're going to flash forward and implement our first machine learning algorithm. Don't panic, this is actually a python review assignment. We have picked the simplest algorithm for you to develop from scratch, using the python programming skills you have acquired in the previous lectures.

We'll also use that assigment to enforce some good practices of coding.


### Have a workflow ready to use

We advise you to do the following:

1. In atom, open the whole directory of the repository.

2. Have a git bash window to execute your code using `python`. Don't forget to switch to the right anaconda environment (`conda env list` to check your existing environments).


### Test Driven Development

During this assignment, you will have to modify 3 files. Each of these files has been specifically written to reflect best practices in programming. In particular:

- each function has a **docstring** showing explicitely how to use the function, what it does, and what are the expected results from it.
- each file has a "main block" that executes the functions of that file and tries it against some test cases.

This is typical of a Test Driven Development workflow: you are provided empty functions. You have the description of behavior, and tests to execute your code against. Your mission is to develop each function to pass all the given tests.

To try to pass the tests, you can do two things:

1. you can execute each file, and use its provided main block, for instance:

  ```
  python etl.py
  ```

2. even better, you can use 'doctest' to execute the tests specified in the docstrings:

  ```
  python -m doctest etl.py
  ```

  For that `etl.py` file, **if you successfully pass all tests, this should not display anything**.

  In the current state of the code provided, this is what it will return:

  ```
  **********************************************************************
  2 items had failures:
     2 of   2 in etl.read_iris_file
     2 of   2 in etl.read_iris_line
  ***Test Failed*** 4 failures.
  ```

  Showing that all 4 tests have failed.


## Assignment


### Part 1 - `etl.py`

This script is dedicated to loading a dataset from a file. It will parse the content of the "iris.csv" file. We have separated that into 2 functions.

The first function, `read_iris_line()`, will "parse" one line given as a string.

The second function, `read_iris_file()`, will open the file and for each line call `read_iris_line()`, and collect the results in a list.

1. Open the file `iris.csv` in atom. Look at a few example lines (see below):

  ```
  sepal_length,sepal_width,petal_length,petal_width,species
  5.1,3.5,1.4,0.2,setosa
  4.9,3,1.4,0.2,setosa
  4.7,3.2,1.3,0.2,setosa
  4.6,3.1,1.5,0.2,setosa
  5,3.6,1.4,0.2,setosa
  5.4,3.9,1.7,0.4,setosa
  ```

  This is a dataset provided in a format called **Comma Separated Values**. The first line gives the name of the "columns" or "fields" of this dataset.

  Each line described one **example**, composed of 5 **fields**:
  - 4 numeric values (floats) we'll call the **attributes**,
  - one string we'll call the **class**.

2. Now open the python file `etl.py` in atom.

3. Browse that file and look up three things:
  - the function `read_iris_line()`
  - the function `read_iris_file()`
  - the "main block" at the end, starting with `if __name__ == '__main__':`

4. Implement function `read_iris_line()` according to its docstring. This function should take one line of this file and return a tuple corresponding to its fields.

  For instance, for the first line:

  ```
  5.1,3.5,1.4,0.2,setosa
  ```

  The function should return the tuple: `(5.1, 3.5, 1.4, 0.2, 'setosa')`.

  Look at the docstring of `read_iris_line()`, this is what is specified in the "Examples".

  Every time you think you have a working function, try it against the tests.

  You can try using:

  ```
  python etl.py
  ```

  And using:
  ```
  python -m doctest etl.py
  ```

  Note: this will execute all the tests, for all the functions in there. Watch out for the tests specific to the function `read_iris_line()`.

5. Now, implement function `read_iris_file()` using the I/O functions seen during the lecture. This function should discard the header line and call the previous function for every line. Implement it according to the docstring.

  Every time you think you have a working function, try it against the tests.

  You can try using:

  ```
  python etl.py
  ```

  And using:
  ```
  python -m doctest etl.py
  ```

  Note: this will execute all the tests, for all the functions in there. Watch out for the tests specific to the function `read_iris_file()`.


### Part 2 - `classification.py`

In a second part, we will create an algorithm called **k-Nearest Neighbors** in its simplest form.

The idea is simple:
- on one side we have a dataset full of **examples** of flowers, each has its own **class** (either `setosa`, `virginica` or `versicolor`).
- on the other you have a given example, and you don't know its class.
- to determine (**predict**) the class of the unknown example, we will compare it to all the available **examples**, we will pick the closest one in terms of the distance computed on the **attributes**, and we'll just say that this probably has the same class.

This is a simple way of reporting an unknown case to a dataset of known cases, and to determine that the unknown class should be the one from the case that is the most similar to the unknown case.

To do that, we have separated this algorithm into three functions:

- the function `distance()` computes the distance between two examples based on all 4 **attributes**,
- the function `closest()` finds the example within a dataset of `examples` which is a closest from a given `example_x` (using `distance()`),
- the function `classify()` returns, for a given `example_x` and a dataset of `examples` given as a list, the class from the closest example (using `closest()`).


1. Open the python file `classification.py` in atom.

2. Browse that file and look up four things:
  - the function `distance()`
  - the function `closest()`
  - the function `classify()`
  - the "main block" at the end, starting with `if __name__ == '__main__':`

  For the following steps, you just have to do what you now know how to do: implement each function according to its docstring. The test cases provided in the "main block" are real test cases from which we have hidden the class (replacing it by `None`).

3. Implement function `distance()` according to its docstring. Test it using `python` or `python -m doctest`.

4. Implement function `closest()` according to its docstring. Test it using `python` or `python -m doctest`.

5. Implement function `classify()` according to its docstring. Test it using `python` or `python -m doctest`.


### Part 3 - `validation.py`

Now, you may have noticed something weird. The examples we have picked in `classification.py` to test the `classify()` function are actual examples drawn from the dataset. It is not surprising that we are able to "detect" the class of an "unknown example" because it's not entirely unknown. We have seen the same case before.

What would be really useful would be to try an example that we have **never seen** before, something that is **not simple one of the examples**. We are going to do what we call splitting our dataset into a "training set" and a "testing set".

What we'll call the "training set" will be a sublist of the examples we'll give to the algorithm you coded in `classify.py`, but not the full dataset, only 70% of it.

What we'll call the "testing set" will be a sublist of the examples that we'll not give to the algorithm. Instead, we're going to see if the algorithm can correctly classify each example from this testing set. This testing set will be the remaining 30% of our original dataset.

1. Open file `validation.py`.

2. Browse that file and look up three things:
  - the function `examples_split()`
  - the function `compute_score()`
  - the "main block" at the end, starting with `if __name__ == '__main__':`

  For the following steps, you just have to do what you now know how to do: implement each function according to its docstring.

3. Implement function `examples_split()`. This function "splits" our original set of examples (150) into two parts, according to a given `ratio`. If ratio is `0.7`, it will put 70% of those 150 into a `train` list, and the remaining 30% into a `test` list. And it will return both.

  _Note: to be solid, this methodology requires you to shuffle your examples. Use the following example:_

  ```python
  import random

  numbers = [1,2,3,4,5]
  print(random.shuffle(numbers))
  ```

4. Implement function `compute_score()` according to its docstring. This one doesn't have tests.

  Run the function and observe the result. For a 70% split ratio, the score you obtain should be around 95-97%.

  Wow! Using that simple algorithm, you have created a program that can automatically detect the kind of an iris!

5. Just for fun, try to reduce the `ratio`. What proportion of training examples do you need in order to achieve an acceptable score? What's an acceptable score by the way?
