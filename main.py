from decimal import Decimal
import random


def example_a():
    print('\nExample A')
    print('~~~~~~~~~')

    drugs = input('How many drugs you want to buy?: ')

    # An integer "int" is any WHOLE number from -2,147,483,648 to 2,147,483,647
    # No decimal points like 1.5, 2.1, 3.0 etc.
    # Be aware that if you do not enter a number that can be converted to an integer, the program will crash.
    # That's ok for now. We will cover if/else statements and null checks soon
    num_of_drugs = int(drugs)

    print(f"This is a police sting operation, you are under arrest for buying {num_of_drugs} drugs. Naughty, Naughty!")


# Puzzle A - Maths Stuff
#
# Write a program that asks the user to input two numbers
# Add the numbers together and display the result
# Subtract the second number from the first number and show the result
# Multiply the two numbers together and show the result
# Divide the first number by the second number and get a fraction like 1.666
# Divide the first number by the second number. Show the answer - whole number AND the REMAINDER
# (look up divide // and % remainder )
def puzzle_a():
    print('\nPuzzle A')
    print('~~~~~~~~~')

    num1_input = input("Please enter a WHOLE number: ")
    num1 = int(num1_input)

    num2 = int(input("Please enter another WHOLE number: "))

    # Add
    add_result = num1 + num2
    print(f'{num1} + {num2} = {add_result}')

    # Subtract
    subtract_result = num1 - num2
    print(f'{num1} - {num2} = {subtract_result}')

    # Multiply
    multiply_result = num1 * num2
    print(f'{num1} * {num2} = {multiply_result}')

    # Divide
    divide_result = num1 / num2
    print(f"{num1} / {num2} = {divide_result}")

    divide_quotient = num1 // num2
    remainder = num1 % num2
    print(f"{num1} // {num2} = {divide_quotient} remainder {remainder}")


def example_b():
    print('\nExample B')
    print('~~~~~~~~~')

    print("Elon Musk is drunk again and he is giving away free money on social media")

    money = input("How much free money do you want?:")

    # float allows decimal points or "Floating points"
    # It fills up 8 bytes of memory (64-bit)
    # The number can be 15 decimal digits
    rounded_money = round(float(money), 2) # We can only have 2 decimals for cents. So round the value.

    print(f"Elon Musk sends you ${rounded_money} by bank transfer")


# Puzzle B - Money
#
# Decimal is usually used for money, not float. It's more accurate.
# In python, you need to import Decimal to use it, at the very top of the page:
#   from decimal import Decimal
# Write a program that asks for donations to a charity
# Get the user's donation amount as a decimal
# Elon Musk will match the amount the user enters
# Output the user's donation amount, and the total donation after Elon matches it.
def puzzle_b():
    print('\nPuzzle B')
    print('~~~~~~~~~')

    money_input = input("How much would you like to donate to Sex Addicts Anonymous?:")

    money = Decimal(money_input)
    rounded_money = round(money, 2)

    matched_total = rounded_money * 2

    print(f"You have donated ${rounded_money} to Sex Addicts Anonymous, and Elon Musk has matched the donation!")
    print(f"Total Donated: ${matched_total}")


def example_c():
    print('\nExample C')
    print('~~~~~~~~~~~')

    print("Rolling the dice....")

    # You need to "import random" at top of the page
    roll = random.randint(1, 6)

    print(f"You rolled a {roll}")


# Puzzle C - Death and Taxes
#
# Write a Tax Department program that asks the user to enter their yearly salary
# Randomly generate a percentage between 30% and 100% to tax them
# Calculate what they will pay in tax
# The tax department works using whole numbers, so if they enter a floating point number round it up to a whole number.
# Tell them the bad news. Let them know the tax percentage they are paying and how much they will pay in tax.
def puzzle_c():
    print('\nPuzzle C')
    print('~~~~~~~~~~~')

    print("Tax Department")
    salary_input = input("You must enter your yearly salary, or you will be arrested: ")

    salary = Decimal(salary_input)
    rounded_salary = round(salary, 0) # Tax dept usually just goes by whole numbers

    tax = random.randint(30, 100)

    tax_to_pay = rounded_salary * tax / 100

    print(f"You need to pay {tax}% tax, that's ${tax_to_pay} you owe us or else")



if __name__ == '__main__':

    # Run the puzzles

    # example_a()
    puzzle_a()

    # example_b()
    puzzle_b()

    # example_c()
    puzzle_c()
