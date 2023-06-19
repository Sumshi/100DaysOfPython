#!/usr/bin/python3
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# 1 year = 365days
# 1 year = 52 weeks
#1 year = 12 months
age_a = int(age)
year_remaining = 90 - age_a
days_remaining = year_remaining * 365
weeks_remaining = year_remaining * 52
months_remainning = year_remaining * 12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remainning} months left.")
