# Mark Hooks unit two assignment
# this program is to create a chatbot

chatbot_number = 4

chatbot_name = "Not A.I Bot"

print("Hello! I am Not A.I Bot!")

users_name = input("What is your name?")

print("What a lovely name!")

users_place_of_origin = input("Where are you from?")

print("What a lovely place to live!")

# this section below it to calculate the user's favorite number with the chatbot's number
users_favorite_number = input("What is your favorite number?")

user_number_difference = float(users_favorite_number) * float(chatbot_number)

# this section below is to calculate the monthly payment and the total cost of the users dream car.
print("Your number multiplied by my number is", user_number_difference)

users_dream_car = input("What is your dream car?")

print("What a great car! I wish I had a car.")

users_car_cost = input("How much would your car cost?")

P = float(users_car_cost)

users_interest = input("What would the annual interest rate be on that car?")

users_loan = input("How many years would you need to take out a loan for?")

r = float(users_interest) / 100 / 12

n = float(users_loan) * 12

monthly_payments = (r * P) / (1 - (1 + r) ** -n)

car_total = float(monthly_payments) * n

print("you would pay", monthly_payments, "a month. Thats a total of", car_total, "I hope you get the car!")

print("Sorry, something came up and I must go! Good bye!")
