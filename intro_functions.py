# 1a) Copy and paste the function definition from the markdown file below. This block of code defines a function called hello(). However, you haven't used the
#function yet! In order to do this, you must type out hello() and run your program. Do this below, and comment an observation about what you see.






# 1b) Practice your looping skills! Write a function called hello2 that does the same thing as the original hello function, but replace the body of the function
#(print("Hello World!\n"*10)) with either a for loop or while loop that does the same thing. Run your hello2() function to see it work.







# 2a)If you haven't noticed, none of the functions you've created so far have parameters. In other words, there is nothing inside the parentheses of the function definition.
#Parameters help make our function reusable, because we are able to give it different information each time we use it. The code below defines a function that has one parameter:

def hello_name(name):
  print("Hello, " + name)


#Use the function below, and remember to give it an argument. In this case, you would want to put a string in the parentheses when you call this function.






# 2b) Redefine the function hello_name so that it takes two parameters: firstName and lastName. Then in the body of the function, print a statement that uses both.
#HINT: You can separate parameters inside the parentheses of your function definition with commas.








# 3a) The parameters that you use in your function definition are local variables. That is, they only work within the context of your function. They represent the
#values, or arguments, that you pass into your function when you use it. Let's look at another example of a function that adds 10 to whatever number you type in,
#and then prints the answer to the console:

def add_ten(y):
  print(y+10)
  
#Call the function add_ten below, making sure to give it an argument



#Uncomment the line of code below and run it. Comment on why you get an error, based on the information provided to you in question 3:
#print(y)







# 3b) While variables declared inside your function cannot be used outside of your function, variables declared outside of your function (global variables) can be
#used inside your function. For example:

h = 10
def add_ten(y):
  print(y+h)


#Use this function below (remember to give it an argument). Did it give an error? Describe what happened in a comment below.









# 4a) Let's say we wanted our function to do some math and return a value. We can use the return statement. Let's say I wrote a function that adds two number together.
# I can use the return statement so my function both makes the calculation and returns a value. Observe below:

def add_two_numbers(num1, num2):
  return num1 + num2
  
#Use the function add_two_numbers below, remembering to pass it two arguments num1 and num2. What happens when you run this? Comment below.






# 4b) Return isn't a print statement, so even though your function makes a calculation, there's no code telling Python to show us the result of what that calculation is.
#If you wrap your function call in a print statement, then we can visualize the result of the calculation. Likewise, you can save your function call as a variable
#and print that variable to the console. Try doing one of these below:







# 5)Write a function below that squares a number, and then use that function to square a number of your choice
#HINT: You should give your function an informative name, you should use a return statement, and your function definition should have one parameter!










#####--------------BONUS QUESTIONS-----------------######

# 1) Write a function that takes user input for their name, and then prints "Hi" and says the name that was user-inputted








# 2) Let's say you want to create a function to calculate how much money you have at the end of each month. The amount of money you have is dependent on your three
#variables: Your monthly_income, tax_rate, and expenses. Write a function that returns the value of this calculation. Make sure it is reusable, so I can use it for any value
#income, tax_rate and expenses.








# 3) Write a function that uses either a while loop or a for loop to print every odd number between a minimum and maximum that you determine when you call your function.













