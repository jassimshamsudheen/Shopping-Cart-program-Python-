#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: jassimshamsudheen
"""
import math # importing for the purpose to input math.floor function
"""CPS-109 Project"""

""" Weekly essential Shopping Cart Expense Tracker"""

""" We all have so called budget planning for our overall expense. An average household
canadian household savings rate is just below 7%. Most of us spend roughly 15 % of our income towards
the groceries and other essential goods and sometimes end up paying more for the non essentials.
Here we come up with a solution that can help you to create a cart before you go to the super store to track the spending towards the essentials weekly.
This would help us to stay top on budget and support us for the long term savings ."""

"""Budget Calculator """

print("Welcome to the essential shopping cart expense tracker\n")
# Lets start with Inserting the amount of income that you recieve weekly
Weekly_Income = int((input("enter your weekly income:$")))
print(f"Your Weekly_Income is ${Weekly_Income}")
# An Average canadians spend rougly 40 percentage of their income towards the bill payments. Using arithmetic operation to calculate the 
#amount of bill payment amount from the total income
Bill_payment = (Weekly_Income*0.4)
print(f"Money went towards Bill payment is ${Bill_payment}")
# Building a long term savings is a safety net for future . An average 30 percent of salary goes towards the emregency and long term savings account. Using arithmetic operation to calculate the 
#amount of savings from the weekly income
Saving_account = (Weekly_Income - Bill_payment) - (0.3 * Weekly_Income)
print(f"Money went towards Savings account is ${Saving_account}")
# Here comes our budget for the essential weekly shopping . Lets take 15 % of our salary as the weekly essential budget. Using arithmetic operation to calculate the 
#amount available for essential items from the total income
ess_budget =float((Weekly_Income - Bill_payment - Saving_account) - (0.15 * Weekly_Income)) 
# Lets keep the rest of funds as additional funds for added expense . Using arithmetic operation to find the remaining amount after all the expenses
add_expense = (Weekly_Income - Bill_payment - Saving_account - ess_budget)

print(f"Funds  available for additional expense is ${add_expense}\n")

print(f"Funds available to spend for essential weekly cart is ${ess_budget}\n")

total=0 # assigning variable to find the total cost in the shopping cart 
final_list = [] # assigning variable for appending at iteration in further lines
overall_list = [] # assigning variable to read the shopping cart in output file
price_list = []
 

while True: #this while loop will execute until you confirm your shopping cart
    food = input('Enter the essential that you like to buy:') # assign a variable to ask the input for the essential

    quantity = int(input(f'Enter the quantity of {food}:'))  # assign a variable to ask the input for the quantity
    price = float(input(f'Enter the price for the {food}:$'))  # assign a variable to ask the input for the price
    price_list.append(quantity*price)
    final_list.append(food) # appending the food input to the final list for the loop iteration in line 62
    overall_list.append((food,quantity, price)) # using overall list to show the shopping cart as outcome in output file
    print('\n')
    items_g = input('Would you like to add more items [yes/no]:') # prompt asking to exit or continue within the loop
    if items_g=='no':
        break
print('------------your cart------------')

for x in final_list: # for loop to iterate and view the shopping list that you currently planning to buy
    print(x, end='  ')
print('\n') # adding new line to customize the output
proceed = input('Would you like to proceed to see the total [yes/no]:')
if proceed=='no':
    print('If you are optimistic about the total, lets go and see how you did with your budget')
else:
    for y in price_list:
        total=total+y
    print(f'your total is ${total}')

def budget(a,b): # function to check the percentage of budget saved or overspend in your cart
    if a>b:
        percent_saved = math.floor(((ess_budget-total)/ess_budget)*100) # using math.floor to find the percentage saved from budget
        return(f'you saved {percent_saved}% of your budget')
    else:
        percent_saved = math.floor(((ess_budget-total)/ess_budget)*100) #using math.floor to find the percentage spend from budget
        return(f'you spend over budget by {abs(percent_saved)}% of your budget')

print('\n')
print('\n')
print('\n')

suggestion = input('Would you like to see how much percentage you saved or over spend from your budget [yes/no]:')
if suggestion=='yes': # Using if loop to confirm to proceed with suggest and returning the percentage of budget saved or overspend through the budget function that I created 
    advise = budget(ess_budget, total)
    print(advise)
else:
    print("Please try to see your improvement in saving from budget next time") 
if ess_budget>total and (suggestion=='yes'):
    ask = input('would you like to move this remaining funds to long term savings[yes/no]:')
    if ask =='yes':
        New_Saving_account = Saving_account+(ess_budget-total)
        print(f'your contribution for your future is updated to ${New_Saving_account}')
    if ask == 'no':
        print("you deserve some luxury this week for your hard work. Iam adding this to your non essential funds")
elif ess_budget<total and total>(ess_budget+add_expense) and (suggestion=='yes'):
    print("Unfortunately you cant afford this at this time, please reset your shopping cart")
else:
    print("lets take some money from non essential funds and manage our budget well for upcoming week")


  
def output_status(): # function to write budget status to an external text file
    with open("file_output.txt","w") as file_output:
        file_output.write(f"Your Weekly Income Total is ${Weekly_Income}\n")
        file_output.write(f"Your Weekly Bill Payment is ${Bill_payment}\n")
        file_output.write(f"Your Weekly Long-term Savings is ${Saving_account}\n")
        file_output.write(f"Your Additional non-essential funds is ${add_expense}\n")
        file_output.write(f"Your Funds available for essentials is ${ess_budget}\n")
        file_output.write(f"------Shopping Cart-------\n")
        for x in range(len(overall_list)):
            file_output.write(f" Items:{overall_list[x][0]}     Quantity:{overall_list[x][1]}     Price:{overall_list[x][2]} \n")
        file_output.write(f"Your essentials cart costis ${total}\n")
        if ess_budget>total:
            file_output.write(f"Your contribution to long term savings is updated to${New_Saving_account}\n")
            
        
                
output_status() # function to write the main outcomes from this program to the external file
        
        
        
        
        
        
        
        
        
    