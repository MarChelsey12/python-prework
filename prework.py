# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the funtion. The first line of the code has been defined as below.
def hello_name(user_name):
    print(f"Hello, {user_name}! This was all written using Python coding. ")

def name_request():
    print("Please enter in your USERNAME: ")

def end_interaction():
    print(f"Thanks for reviewing my code. \nSee you on the first day of class!")

while True:
    response = input("Welcome! Would you like to continue? For YES type [y], for NO type [n] ")
    if response.lower() == 'y':
        user_name= input("Please enter in your USERNAME: ")
        hello_name(user_name)
    elif response.lower() == 'n':
        end_interaction()
        break
    else:
        print("Invalid input. Please try again.")

# Question 2
# Write a Python function, first_odds that prints the odd numbers from 1-100 and returns nothing.
def first_odds():
    first_odds = list(range(1,101,2))
    print(first_odds)

print(first_odds()) 
 
# Question 3
# Please write a Python function, max_num_list to return the max number of a given list. The first line of code has been defined as below.
def max_num_in_list(a_list):
    print(f"The max number of Snow White's dwarfs is {a_list}.")

dwarfs = ["doc", "happy", "sleepy", "sneezy", "grumpy", "bashful", "dopey"]    
max_num_in_list(a_list = len(dwarfs))  

# Question 4 
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be a boolean type (true/false).
def is_leap_year(a_year):


# Question 5
# Write a function to check to see if all numbers in a list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be a boolean type.
def is_consecutive(a_list):