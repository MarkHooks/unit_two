#mark hooks unit two assignment
#this program is to create a chatbot
import math

chatbot_number = 4
chatbot_name = "Not A.I Bot"
print("Hello! I am Not A.I Bot!")
users_name = input("What is your name")
print("What a lovely name!")
users_place_of_origin = input("Where are you from?")
print("What a lovely place to live!")
users_favorite_number = input("What is your favorite number?")

user_number_difference = float (users_favorite_number) * float (chatbot_number)
#need to put the variable in
print("your number multiplied by my number is", user_number_difference)
users_dream_car = input("What is your dream car?")
print("What a great car! I wish i had a car.")
users_car_cost = input("How much would your car cost?")
P = users_car_cost
users_loan = input("How many years would you need to take a loan out for?")
users_intrest = input("What would the anual intrest rate you would get on the car")
the_rate = float (users_intrest)/ 100
r = float (the_rate) / 12
n = float (P) / 12
monthly_payments = float (r) * float (P)/ (1- (1 + r) **-n)
print("you would pay", monthly_payments, "a month")

