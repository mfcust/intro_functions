# Functions

What is a function? Simply put, a function is a block of code that tells Python to carry out a task. Let's think about some functions that we've already used in Python. One function we commonly use is the print function shown below:
```
print("Hello World!")
```
What are the characteristics of the print function? It has an informative name, it takes an argument, and it's purpose is to print the thing inside the parentheses to the console. The argument in the example above is the string "Hello World!" The print function can print strings, but it can also print other data types such as integers, floats, lists, etc. A function doesn't need to take any arguments, or return any value, but most do at least one of these things.


A function is like an iceberg; you can only see the tip of the iceberg, but underneath the surface of the water it is much larger and more complex. When we use the print function, we are only seeing the "tip of the iceberg." There is a lot of code underneath the surface that makes the print function do what it does.

In Python, we can define our own functions so that we can use them later. Lots of people in the Python community make their own functions to complete specific tasks, and then make them available for everyone else to use. Let's say I wanted to make a function that prints "Hello World!" 10 times to the console. The syntax for defining such a function is provided below:
```
def hello():
  print("Hello World!\n"*10)
```
There are 4 parts that make up a function definition. First, you need to start with **def**, which stands for define. The second part is the name of the function. In the case above, we named our function **hello**. Third, is the parameters, which would be located inside the parentheses. For the function above, we do not have any parameters. Last is the body of the function, which is the indented code inside of it. We have successfully defined our function above, but we haven't yet used it. Navigate to the python file to learn more about functions!
