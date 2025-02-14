# -*- coding: utf-8 -*-
"""ai_builder_intro_python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/vistec-AI/ai-builders/blob/main/notebooks/ai_builder_intro_python.ipynb

# Introduction to Python

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vistec-AI/ai-builders/blob/main/notebooks/ai_builder_intro_python.ipynb)

### But First, Learning Tips!

1. Before clicking \[ ▶ Run \] to see the result from running the code, **make a guess of what the final result would be** before actually running it.
2. **Do not be afraid to play around with code**: change them, re-run the code, and see if the new result meets your expectation.
3. Got error messages? Relax. Even experienced programmers got these so-called bugs! **Pause for a few seconds and see why the code produces such error.**

## 1. Basic Arithmetics

Python can run simple math expressions out of the box.
So expressions like `2 + 2` will produce the final result 4.

Try running the code below by hitting \[ ▶ Run \] button.
"""

2 + 2

"""Since there is no $\times$ (times) and $\div$ (divide) symbol on the keyword, we instead use symbols `*` and `/` instead."""

17 / 3

50 - 5 * 6

"""Notice that in the above code, multiplication `*` is evaluated before subtraction `-`. This is due to what is called the **order of precedence**.


So if we want to do subtraction first, we need a pair of parentheses, `(` and `)`, just like in math!
"""

(50 - 5) * 6

"""### Example: Temperature Conversion

Now for our very first application! Let’s say that a weather app tells us that the current weather in Galapagos Island is **100°F** (Farenheit). We want to know what is this temperature value in Celcius.

We will use the following identity to help us with unit conversion:

> $\dfrac{C}{5} = \dfrac{F - 32}{9} \quad\Longleftrightarrow\quad C = \dfrac{F - 32}{9} \times 5$

And below is the code to convert 100°F into °C.
"""

((100 - 32) / 9) * 5

"""Once you have got familiarity with the **order of precedence**, then you will notice that we can remove the redundant pair of parentheses:"""

(100 - 32) / 9 * 5

"""### Example: Compound Interest (Exponentiation)

Suppose that we have **THB 10,000** (Thai Baht) in a savings account. Every year we receive **3% interest**, which is then compounded into your account for the subsequent year. If we leave our account alone for **12 years**, how much total money would we have at the end?

The answer is THB $10000 \times 1.03^{12}$ (with some rounding errors). Translating this into the Python code as follows.
"""

10_000 * 1.03 * 1.03 * 1.03 * 1.03 * 1.03 * 1.03 * 1.03 * 1.03 * 1.03 * 1.03 * 1.03

"""You should have got approximately 14257.61 THB as the result (if not, check the work again).

Yes, the above code looks very tiring. Luckily, we can use the `**` operator to perform exponentiation for us.
"""

10_000 * 1.03 ** 12

"""**Tips:** The exponentiation also works for negative numbers. Do the results below surprise you?"""

5 ** -1

(-2) ** 0.5

"""### Aside: Real Division vs Integer Division

Recall that the result of `17 / 3` from above produces a real number result.  
But what if you want the final _without the fractional part_ (also called a **quotient**)?

The answer is to use the `//` operator.
"""

17 // 3

"""What about the **remainder** of the above division? Can we compute this value?

One way to look at this is to consider the equation $17 = 5 \times 3 + 2$, which gives us the remainder value 2.

Let’s work backward in order to obtain the formula that we can use in our code. Suppose that $A$ (_Thai._ ตังตั้ง) divided by $B$ (_Thai._ ตัวหาร) produces the **quotient** $Q$ (_Thai._ ผลหาร) and the **remainder** $R$ (_Thai._ เศษ). So we have the follow equation.

> $A = Q \times B + R \quad \Longleftrightarrow \quad R = A - Q \times B$

And here is the Python code to compute the remainder from dividing 17 by 3.
"""

17 - (17 // 3) * 3

"""Whew, that was a lot of work! Luckily, we can achieve the same result simply by using the **modulo** operator: `%`."""

17 % 3

"""_Did you notice a recurring theme?_ In Python (as well as other programming languages), we have all these handy operations at our disposal which help us shorten our workload. Later in this session, we will also learn how to create one ourselves, with functions.

Lastly, before we move on, what is the result of dividing -17 by 3? Make a guess before running the code.
"""

-17 // 3

-17 % 3

"""## 2. Variables

### Example: Quadratic Equation

Let’s consider a high school math problem. How do we solve for $x$ in the following quadratic equation.

> $ax^2 + bx + c = 0$

According to high school math, there are two solutions according to this formula:

> $x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$

**Question:** What are the solutions to the equation $2x^2 + 7x + 3 = 0$ 

We need two separate pieces of codes, one for $+\sqrt{b^2 - 4ac}$ and another for $-\sqrt{b^2 - 4ac}$.
"""

(-7 + (7**2 - 4*2*3) ** 0.5) / (2*2)

(-7 - (7**2 - 4*2*3) ** 0.5) / (2*2)

"""Did you see that we have to type almost the exact same code twice? If you think that this is troublesome, you are not alone. Programmers hate repeating themselves as much as you do.

We will divide our workload into smaller steps and avoid recomputing the same values as much as possible.

> $r = \sqrt{b^2 - 4ac}$  
> $x_1 = \dfrac{-b + r}{2a}$  
> $x_2 = \dfrac{-b - r}{2a}$  

In order to reuse intermediate result $k$ for subsequent computations, we need to use **variables**. The above steps can be translated into the following code.
"""

a = 2
b = 7
c = 3

r = (b**2 - 4*a*c) ** 0.5
x1 = (-b + r) / (2*a)
x2 = (-b - r) / (2*a)

print(x1, x2)

"""Not only we did introduce a variable for intermediate result `k`, we introduce a whole lot of variables for coefficients `a`, `b`, `c`, as well as for solutions `x1` and `x2`. What is nice about this approach is that, if you want to solve other quadratic equations of the same form, you can just simply change values for `a`, `b`, and `c`, and rerun the code.

Try playing around, changing values for `a`, `b`, and `c`.

---

There are a few things you must know.

- Python code generally runs from top to bottom. So shuffling lines of code may produce unintended consequences.
- The code `<variable> = <expression>` represents an assignment of values to the right of `=` symbol into a **variable** whose name is shown on the left. Swapping the location of these two things will produce an error (try for yourself).
- Expressions may refer to variables which have been assigned previously. For example, see how the assignment of `k` refers to `a`, `b`, `c` above it. Then, `x1` and `x2` both take turn to refer to `k`. As mentioned earlier, swapping these lines may break things.

Try executing the following code and see what kind of error it produces.

```python
area = width * height
height = 1080
width = 1080 * 16 / 9
print(area)
```
"""

area = width * height
height = 1080
width = 1080 * 16 / 9
print(area)

"""Fix the code above so that it runs correctly. In the end you should get the area of 2,073,600.

### Aside: Statements By Themselves Do Not Produce Value

We have already seen the assignment statements (of the form `<variable> = <expression>`). In the code above, if we remove the line `print(area)`, we will see no output. In Python specifically, there is a distinction between an **expression** and a **statement**. Expressions always produce value, but statements do not.

However, statements may partially contain expressions, just like what we have seen with assignment statements, but in this case, the value is stored into a variable and is not shown to us. _That_ is the reason why the code to compute `area` from multiplying `width` and `height` does not display any result if `print(area)` is absent; `print` tells python to display the content of `area`.

To be precise, `print(...)` will _print_ out anything it receives; whatever we put between the pair of parentheses is called **input arguments** to a function. So you can also print the following.
"""

print(1 + 2 + 3 + 4 + 5)

"""As a special case for Python Notebook (this piece of web application software we are currently using), an expression by itself will have its result be printed out as well. **Warning:** This is not true for general Python code."""

1 + 2 + 3 + 4 + 5

area

"""### Aside: Code Comments

We can provide additional notes to our code using what are called **comments**. In Python, a comment begins with `#` and the rest of the line will not be interpreted by Python. For example,
"""

# Computing the distance from the origin (0, 0) to (x, y)
x = 4
y = -3
distance_from_origin = ((x ** 2) + (y ** 2)) ** 0.5  # Pythagorean Theorem
print(distance_from_origin)

"""It is best to add comments to explain the logic behind the code if it would not be obvious by itself. You will thank yourself later.

## 3. Functions

### Example: Games With Random Loot

Now it’s time to talk about games with Random Number Generators (RNG). Let’s say that a certain rare item has a drop rate of 0.3% from a loot box (that is three in a thousand chance). What is the chance that we win at least one such item within 10 loot boxes?

Let’s write some code to find out.  
**Note:** `format(..., '%')` function turns numbers into percentage form when printed.
"""

drop_rate = 0.003
n_attempts = 10

fail_once_prob = 1 - drop_rate
fail_all_prob = fail_once_prob ** n_attempts
winning_prob = 1 - fail_all_prob

print(format(winning_prob, "%"))

"""Not bad. The probability jumps to almost around 3%. Well, how about 100 loot boxes?

We can just modify the previous code and set `n_attempts` to `100`, but then we will lose track of history of all previous computations. It would be nice to keep some previous results available for inspection.

**Did you know?** In scientific community, scientists maintain what is called a lab notebook, and it is considered unethical to make something disappear from lab notebooks. Do not worry, we are not doing something that serious here.

We instead will duplicate the code from above and modify the number to `n_attempts = 100`.
"""

drop_rate = 0.003
n_attempts = 100

fail_once_prob = 1 - drop_rate
fail_all_prob = fail_once_prob ** n_attempts
winning_prob = 1 - fail_all_prob

print(format(winning_prob, "%"))

"""What if we want to perform this computation again for other number of attempts? Are we _really_ going to copy this chuck of code again? One philosophy of programmers (or for any people who are sufficiently lazy) is to avoid repeating ourselves.

We will combine the entire chunk our code into a single unit of workload, by defining a **function**.

We begin first with our code:
"""

def compute_winning_prob(drop_rate, n_attempts):
    fail_once_prob = 1 - drop_rate
    fail_all_prob = fail_once_prob ** n_attempts
    winning_prob = 1 - fail_all_prob
    return winning_prob


# Making calls to the above function
winning_prob_10_attempts = compute_winning_prob(0.003, 10)
print(format(winning_prob_10_attempts, "%"))

# For better readability, input argument names can be specified too
winning_prob_100_attempts = compute_winning_prob(drop_rate=0.003, n_attempts=100)
print(format(winning_prob_100_attempts, "%"))

# The result of calling a function can be input to another function
print(format(compute_winning_prob(0.003, 1000), "%"))

"""Let’s look at the function definition:

```python
def compute_winning_prob(drop_rate, n_attempts):
    fail_once_prob = 1 - drop_rate
    fail_all_prob = fail_once_prob ** n_attempts
    winning_prob = 1 - fail_all_prob
    return winning_prob
```

It consists of the following:

- Function name, `compute_winning_prob`
- Input arguments, `drop_rate` and `n_attempts`
- Function body. In this case, they are all four lines of indented code.
- Output of the function is signified by the expression following the **`return`** keyword. (In cases where this return statement is missing from the function, `None` will be returned implicitly, a special constant value to indicate an absence of data.)

Here is the fundamental concepts of computation: a function consists of **inputs** and **outputs**  (it may also sometimes has side-effects, but let’s ignore this fact for the moment). The above function receives two inputs, `drop_rate` and `n_attempts`, and produces the winning probability as the output. The order of input arguments does matter. Make sure that the function call specifies these inputs in the same order as well.

#### Symmetry Between Function Definitions and Function Calls

Notice that the first line of function definition and the function call pattern looks similar. This is a conscious design decision intended by Python core developers.

```python
def compute_winning_prob(drop_rate, n_attempts):
```
```python
winning_prob = compute_winning_prob(drop_rate, n_attempts)
```

#### Function Docstring

It is considered good practice to explain what our functions do inside the source code itself. In Python, the practice is to use docstring syntax to do so, like in the following. Generally, this should provide a **contract** whoever is using our functions, such as what are valid inputs, and what is the guarantee about the output.

```python
def compute_winning_prob(drop_rate, n_attempts):
    '''Computes the probability of winning an item at least once
    given the drop rate of such item and the number of attempts.

    Arguments:
        drop_rate: Probability rate of item being drop,
            which must be a number within the range from 0.0 to 1.0
        n_attempts: Number of attempts to claim such item,
            which must be a positive integer.

    Returns:
        The probability of winning such item at least once.    
    '''
    fail_once_prob = 1 - drop_rate
    fail_all_prob = fail_once_prob ** n_attempts
    winning_prob = 1 - fail_all_prob
    return winning_prob
```

What’s more, you are unlikely to remember all code you have written after a day. Docstrings work just like post-it reminders.

### Exercise: Area of Triangle

Write a function that computes the area of a triangle from lengths of its three sides ($A$, $B$, and $C$). Here is the Heron’s formula to implement in code.

> $\mathrm{Area} = \sqrt{S(S-A)(S-B)(S-C)}$
> 
> $S = \dfrac{A + B + C}{2}$
"""

def area_of_triangle(a, b, c):
    """Computes the area of a triangle.

    Arguments:
        a: Non-negative length of the first side
        b: Non-negative length of the second side
        c: Non-negative length of the third side

    Returns:
        The area of the triangle whose side lengths are a, b, and c.
    """
    ... # your code here

print(area_of_triangle(3, 4, 5))  # expected 6
print(area_of_triangle(3, 3, 3))  # expected 3.8971
print(area_of_triangle(2, 3, 8))  # expected ??????

"""## 4. Conditionals

### Example: Phases of H₂O

We will write a function to determine the phase of H₂O at different temperatures. In a simplified model, at sea-level, water freezes (or ice melts) at 0°C whereas water evaporates (or steam condenses) at 100°C.

Our function should receive a single number, which is the temperature of H₂O at sea-level. It should return the phase of H₂0, `"ice"`, `"water"`, or `"steam"`.
"""

def h2o_phase(celcius):
    """Determines the phases of H₂O given its temperature in Celcius."""
    print("input temperature is", celcius)
    if celcius <= 0:
        print("    ice")
    if 0 <= celcius <= 100:
        print("    water")
    if celcius >= 100:
        print("    steam")


h2o_phase(25)
h2o_phase(-273.15)
h2o_phase(1948)
h2o_phase(100)
h2o_phase(0)

"""When did the message `"ice"` get printed? Answer: when inputs were `-273.15` and `0` (both are 0°C or lower). Likewise, `"water"` got printed when inputs were `25`, `100`, and `0` (all are within range from 0°C to 100°C). The same goes for `"steam"`.

You have probably noticed that the **if clause** the **condition** whether the body of the statement (the indented part under the if clause) should be executed.

### Aside: Strings

Strings are just textual data. In Python code, they mostly are written between a pair of **double quotes** `"`:

> e.g. `"hello"`, `"Humuhumunukunukuapua'a is a type of fish."`, and `""` (empty string)

or between a pair of **single quotes** `'`:

> e.g. `'กขคง'`, `'people say they know "blockchain"'`, and `'さよなら means goodbye'`
"""

print("hello")
print("Humuhumunukunukuapua'a is a type of fish.")
print("")
print('กขคง')
print('people say they know "blockchain"')
print('さよなら means goodbye')

"""Both double quotes and single quotes work fine, but we have to be consistent: the string must start and end with the same type of quotation characters.

Also, it is tricky for a text to include a double quote inside a string which begins and ends with double quotes (same goes for single quotes). To do so, we need what is called **character escaping**. Specifically, we will need to prepend the double quote with a backslash inside a string:
"""

print('Humuhumunukunukuapua\'a is a type of fish.')
print("people say they know \"blockchain\"")

"""### Example: Air Quality Index

For the past few years, we have experienced increasing air pollution. For this task, we will write a function to translate AQI integer values (input) into category colors (output). Here is the summary:

| AQI Values | Category | Colors |
|------------|----------|--------|
| 0 - 50 | Good | Green |
| 51 - 100 | Moderate | Yellow |
| 100 - 150 | Unhealthy For Sensitive Groups | Orange |
| 151 - 200 | Unhealthy | Red |
| 201 - 300 | Very Unhealthy | Purple |
| 301 - 500 | Hazardous | Maroon |

And here is how we could implement this function:
"""

def aqi_category_color(aqi_value):
    """Computes the category color of an AQI value.

    Arguments:
        aqi_value: Integer value of Air Quality Index
            within a range from 0 to 500

    Returns:
        A string representing the category color
    """
    if aqi_value <= 50:
        return 'green'
    elif aqi_value <= 100:
        return 'yellow'
    elif aqi_value <= 150:
        return 'orange'
    elif aqi_value <= 200:
        return 'red'
    elif aqi_value <= 300:
        return 'purple'
    else:
        return 'maroon'


print('Color status of AQI 25 is', aqi_category_color(25))
print('Color status of AQI 125 is', aqi_category_color(125))
print('Color status of AQI 225 is', aqi_category_color(225))
print('Color status of AQI 325 is', aqi_category_color(325))

"""This function differs from `phase_h2o` in a couple of ways:

- Function `aqi_category_color` itself does _not_ **`print`** any strings. It instead returns a string as output, which then got feeded into **`print`** function outside. This approach is generally preferable because the computational logic is separated from the presentation.
- Function `aqi_category_color` introduces sibling clauses **`elif`** and **`else`** to if statements. As you may have guessed, **`elif`** and **`else`** clauses are even considered at all when the previous clauses are false.

Let’s break down the code a bit further.
- AQI value 125 converts to `"yellow"` because `aqi_value <= 50` was false, but `aqi_value <= 100` was true.
- AQI value 325 converts to `"maroon"` because all previous **`if`** and **`elif`** clauses were false.

### Aside: Booleans

Boolean is a type of data that has two possible values, **`True`** and **`False`**. It is commonly used in predicate logic or for representing binary states (such as **on** or **off**).

We have dealt with boolean data before, but we have not inspected them closely. Take a look at a few bunch of the following inequalities.
"""

two = 2

print(1 < 2)  # less than (<)
print(2 + 2 == 4)  # equal (=)
print(-123 >= 123)  # greater or equal to (≥)
print(two > two)  # greater (>)
print(100 != two)  # not equal (≠)
print(3 <= 3)  # less than or equal to (≤)
print("x" in "styrofoam")
print("x" in "xylophone")

"""Remember Logic in high school math. Here is what you are waiting for."""

booleans = [True, False]

for x in booleans:
    for y in booleans:
        print(x, "and", y, "is", x and y)
        print(x, " or", y, "is", x or y)
        print()

for x in booleans:
    print("not", x, "is", not x)

"""## 5. Lists and For Loops

Imagine that we are given a sequence of values (e.g. numbers, strings, or even more complex data) and we want to learn something about this sequence. Tasks like this include:

- **Aggregations:** for the given list of values, compute their sum (or the maximum value, or count the number of unique values, or their average, etc.)
- **Sorting:** order the list according to its value (or based on its derivatives)
- **Filtering:** find which values in the list satisfy a given condition (usually called a predicate)
- and a whole lot others!

### Example: Computing Average

We begin with a list of `numbers` and we will compute their average (arithmetic mean).
"""

def compute_average(numbers):
    """Computes the average of a given list of numbers."""
    total = 0
    count = 0
    for n in numbers:
        total = total + n
        count = count + 1
    average = total / count
    return average


numbers = [34, 13, 62, 91, 87, 66, 29, 17, 83, 55, 44]
average_number = compute_average(numbers)
print("The average number is", format(average_number, '.3f'))

"""Let’s walk through this code together.

First of all, look at the first line of code. It declares a list of 11 integers, and stores into a variable called `numbers`.
```python
numbers = [34, 13, 62, 91, 87, 66, 29, 17, 83, 55, 44]
```

Next, skip the for clause for a moment and look at its **body** (the indented part of the for statement). Look at the assignment statements below.
```python
    total = total + value
    count = count + 1
```
What essentially happens here is that, variable `total` updates its value by an increment of `n`, whereas variable `count` bumps up its own value by `1`.

Now for the interpretation of the main **for clause**,
```python
for n in numbers:
```
It means that the body of the for statement has to be executed **once for each value** (called `n`) in the list of values (called `numbers`).

With `total` and `count` being initialized at 0, at the end,

- `total` will have accumulated the _total_ of numbers in the list, and 
- `count` will be the _count_ of numbers in the list (sometimes called the _length_).

And thus, we have all necessary data to compute the average as the final result.

---

By the way, there are Python built-in functions **`sum`** and **`len`** that would compute the total and the count of values in the list for us. In the future, there will also be other ways to compute the mean of a sequence of values in a single function.
"""

numbers = [34, 13, 62, 91, 87, 66, 29, 17, 83, 55, 44]
average = sum(numbers) / len(numbers)
print("The average number is", format(average, '.3f'))

"""### Mini Guessing Game

More guessing game! Look at each of the following code and guess what would happen once they are run.
"""

fruits = ["apple", "banana", "cherry", "orange"]
for f in fruits:
    print(f)

for char in "banana":
    print(char)

adjectives = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry", "orange"]

for a in adjectives:
    for f in fruits:
        print(a, f)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for d in digits:
    if 3 < d < 7:
        print(d)

for d in digits:
    if d % 2 == 0:
        print(d)

"""### More List Operations

Apart from iterating through each element in the list, we can operate on lists in a few diferent ways:

[Python Documentation on List](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

#### List Appending and Insertion
"""

selected_letters = []
for char in "mississippi":
    if char in 'pie':  # char must be 'p', 'i', or 'e'
      selected_letters.append(char)
print(selected_letters)

selected_letters = []
for char in "supercalifragilisticexpialidocious":
    if char < 'e' or char > 's':
        selected_letters.insert(0, char)  # insert at the beginning
print(selected_letters)

fruits = ["apple", "banana", "cherry", "orange"]
selected_fruits = []
for f in fruits:
    if 'e' in f:  # fruit (f) must contain letter 'e'
        selected_fruits.append(f)
print(selected_fruits)

"""#### List Concatenation and Multiplication"""

a = [1, 2, 3]
b = [4, 6, 8, 10]
print(a + b)
print(4 * a)

"""#### Accessing and Modifying List Elements"""

numbers = [34, 13, 62, 91, 87, 66, 29, 17, 83, 55, 44]

print(numbers[0])
print(numbers[1])
print(numbers[7])
print(numbers[-1])
print(numbers[-6])
print()

print(numbers[1:4])
print(numbers[2:-2])
print(numbers[3:3])
print(numbers[8:])
print(numbers[0:11])
print(numbers[2:] + numbers[:2])
print(numbers[::2])
print()

numbers[5] = 0
numbers[0] = numbers[0] ** 2
numbers[10] = -numbers[0]
print(numbers)

"""##### Some cheatsheets

- **Indexing a single element**
```
       0    1    2    3    4    5    6    7    8    9   10
L = | 34 | 13 | 62 | 91 | 87 | 66 | 29 | 17 | 83 | 55 | 44 |
     -11  -10   -9   -8   -7   -6   -5   -4   -3   -2   -1
```

- **Indexing a slice of elements**
```
    0    1    2    3    4    5    6    7    8    9   10   11
L = | 34 | 13 | 62 | 91 | 87 | 66 | 29 | 17 | 83 | 55 | 44 | 
  -11  -10   -9   -8   -7   -6   -5   -4   -3   -2   -1
```

By the way, indexing, slicings, and concatenation works on strings too.
"""

disease = "pneumonoultramicroscopicsilicovolcanoconiosis"

print(disease[0] + disease[-1])
print(disease[14])
print(disease[8:8+5])  # what is the word length?
print(disease[32:29:-1] + disease[2])
print(disease[-15:-15+7])  # what is the word length?

print("oh" + 3 * " no")

"""#### Sorting"""

numbers = [34, 13, 62, 91, 87, 66, 29, 17, 83, 55, 44]

print(sorted(numbers))
print(sorted(numbers, reverse=True))

def last_digit(n):
    """Get only the last digit of a number."""
    return abs(n) % 10


# Sorts the numbers based only on their last digits
print(sorted(numbers, key=last_digit))

"""### Aside: Utility Functions With For Loops

Allow us to introduce several built-in functions used in conjunction with for loop statements.

Function **`enumerate`** makes sure that each for loop iterates over a sequence of indices as well as original values.
"""

denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

for index, value in enumerate(denominations):
    print("at index", index, "value is", value, "which is equal to", denominations[index])

"""Function **`range`** allows for-loops to iterate over an arithmetic sequence of numbers."""

for number in range(5):
    print("next number is", number)

for number in range(3, 7):
    print(number)

word = "studying"
for start in range(4):
    print(word[start:])

"""Function **`zip`** groups multiple lists into a single list, element-by-element."""

for char, num in zip("heart", [1, 3, 5, 7, 9]):
    print(char * num)

for first_char, second_char in zip("kale", "broccoli"):
    print(first_char + second_char)

for x, y in zip(range(6), range(4, 8)):
    print(x, y, x + y)

for x, y, z in zip(range(0, 2), range(1, 3), range(2, 4)):
    print(x, y, z, x * y * z)

print("start")
for char, num in zip("this is a very long sentence", []):
    print(char * num)
print("end")

"""### Exercise: Letter Counting

Write a function to count number of specific letters in a word. The function receives two input arguments: a word string and a target letter to count. It should output the number of such target letters in the word.
"""

def count_letter(word, letter):
    ... # your code here


print(count_letter("mohorovičić", "o"))  # expected 3
print(count_letter("mohorovičić", "i"))  # expected 2
print(count_letter("mohorovičić", "c"))  # expected 0
print(count_letter("5555555555", "5"))  # expected 10 
print(count_letter("", "x"))  # expected 0

"""### Exercise: Prime Numbers

What is a prime number? A prime number is an integer $n$ whose factors are $1$ and $n$ itself. In other words, integers from $2$ to $n-1$ does _not_ divide $n$ for $n$ to be a prime.

Write a function to check whether a given integer is a prime number. It should receive an integer as input and should return a boolean (**`True`** or **`False`**) indicating whether the given input is prime or not.
"""

def is_prime(number):
    ...  # your code here (approx. 4 lines needed)


primes = [n for n in range(2, 100) if is_prime(n)]
print(primes)  # expected [2, 3, 5, 7, ..., 97]

"""## 6. Recursions

### Example: Factorial

Although there is a way to compute $n!$ (factorial) for an integer input $n$ using just for loops, we will instead apply one of the most fundamental magic of computer science: **recursion**.

Here is a common definition of factorial:

> $n! = 1 \times 2 \times 3 \times \ldots \times n$

However, we can rewrite the above equation as in the following.

> $n! = (n-1)! \times n \quad\text{where}\quad 0! = 1$
"""

def factorial(n):
    """Computes the factorial of n where
    n is a non-negative integer.
    """
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n

print(factorial(1))
print(factorial(3))
print(factorial(6))
print(factorial(10))

# Breaching the contract of the function
print(factorial(-1))

"""Ignore the last error for a second. It might seem strange at first as why the function makes a (_recursive_) call to itself. Let’s break down this process a bit for $n = 3$.

- Computing `factorial(3)` will return `factorial(2) * 3`
- Computing `factorial(2)` will, in turn, return `factorial(1) * 2`
- Computing `factorial(1)` will return `factorial(0) * 1`
- And computing `factorial(0)` will return `1`

By substitution, it is not difficult to see that `factorial(3)` would end up with the result `1 * 1 * 2 * 3`, which is 6.

---

Now, repeat the break-down process for $n = -1$. We will start to see that, the computation keeps going on forever, because computing `factorial(-1)` requires computing `factorial(-2)`, and that in turn, requires computing `factorial(-3)`, and so on, and so on. There is no end to it. However, the only reason that Python produces the error is that it ran out of memory.

### Mystery Function

Make a guess of what this function does.
"""

def mystery(numbers):
    if len(numbers) == 0:
        return []
    else:
      lowers = []
      equals = []
      uppers = []
      for n in numbers:
          if n < numbers[0]:
              lowers.append(n)
          elif n > numbers[0]:
              uppers.append(n)
          else:
              equals.append(n)
      return mystery(lowers) + equals + mystery(uppers)


print(mystery([6, 5, 4, 7, 2, 5, 3]))

"""## 7. Other Programmers Invented The Wheel For You So That You Don’t Need To

As discussed earlier, we programmers do not like to repeat themselves. If someone wrote a function you need, then good; you do not need to implement it by yourself. In terms of learning curve and economy, downloading, installing, importing, and using other people’s code is a smart choice.

However, do not fool yourself that you cannot write those magical functionalities yourself. You have ability to learn and accumulate experiences enough to implement difficult functionalities by yourself. Remember, your only good excuse is that you don’t have enough time to do just every single task. When time comes, you could join the forefront of the community and create new pieces of software for others to use.

With all that said, now let’s play around with other people’s code.

### Generating QR Code

Installing package: [qrcode](https://pypi.org/project/qrcode/).

We can generate QR code from any string.
"""

# This tells Colab to install a package from 
!pip install qrcode

import qrcode
image = qrcode.make("Hello, World!")
display(image)

"""Scan the QR code below with a phone to see an [interesting geographical feature](https://www.atlasobscura.com/places/subsubsub-island-on-victoria-island)."""

message = 'geo:69.7924,-108.2395'
image = qrcode.make(message)
display(image)

"""Advanced usage of QR code, generate WiFi access for visitors to your home."""

def generate_wifi_qrcode(ssid, password, auth_type='WPA'):
    """Generates a QR code image for WiFi access.

    Arguments:
        ssid: Name of the WiFi network
        password: WiFi password
        auth_type: Type of authentication (defaults to WPA)

    Returns:
        A Pillow image of the QR code (use display to show it)

    For more information, see 
    https://github.com/zxing/zxing/wiki/Barcode-Contents#wi-fi-network-config-android-ios-11 
    """
    message = 'WIFI:S:' + ssid + ';P:' + password + ';T:' + auth_type +';;'
    print("Encoded message:", repr(message))
    return qrcode.make(message)


display(generate_wifi_qrcode('WiFi name', '12345678'))

"""### Wikipedia

Installing package: [wikipedia](https://pypi.org/project/wikipedia/).

We can fetch Wikipedia pages through the web and display some content here.
"""

!pip install wikipedia

import textwrap
import wikipedia

result = wikipedia.page('3Blue1Brown')
print(textwrap.fill(result.summary, width=66))

"""### Math Functions

By the way, Python already comes with wide array of functionalities pre-installed. For example, [math](https://docs.python.org/3/library/math.html) package hosts a collection of with mathematical functions and constants (and similarly [cmath](https://docs.python.org/3/library/cmath.html) package to deal with complex numbers).
"""

import math

print(format(math.degrees(math.pi / 3), '.12f'))
print(format(math.cos(math.pi / 3), '.12f'))
print(math.gcd(1991, 2534))

"""### Randomization

Wanna test your luck, try [random](https://docs.python.org/3/library/random.html) package.
"""

import random

print(random.randint(0, 99))

foods = ['หมูกรอบ', 'ผัดกะเพรา', 'ชานมไข่มุก']
print(random.choice(foods))
print(random.choice(foods))
print(random.choice(foods))
print(random.choice(foods))
print(random.choice(foods))
print(random.choice(foods))

def drop_at_least_once(drop_rate, n_attempts):
    """Performs Bernoulli sampling and see if winning at least once.

    Arguments:
        drop_rate: Probability rate of item being drop,
            which must be a number within the range from 0.0 to 1.0
        n_attempts: Number of attempts to claim such item,
            which must be a positive integer.
 
    Returns:
        A boolean indicating whether such item is won at least once.
    """
    for _ in range(n_attempts):
        if random.random() < drop_rate:
            return True
    return False


for _ in range(10):
    print(drop_at_least_once(0.003, 100))

"""## Final Notes

We have covered about 20% of Python syntax. There is a lot more to pick up. [Check out Python tutorial on their website!](https://docs.python.org/3/tutorial/) Review chapters 3, 4, and 5 in particular. Some matertials were not covered here, but please do not be afraid to try out yourself.
"""