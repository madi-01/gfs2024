import random
def lotto():
    numbers = random.sample(range(1, 50), 6)
    numbers.sort()
    return numbers

print("Herzlich willkommen beim Lotto 6 aus 49!")
user_numbers = []

for i in range(1, 7):
    number = int(input("Bitte geben Sie Ihre Zahl {} zwischen 1 und 49 ein: ".format(i)))
    user_numbers.append(number)

user_numbers.sort()
print("Ihre Zahlen lauten:", user_numbers)

winning_numbers = lotto()
print("Die Gewinnzahlen lauten:", winning_numbers)

correct_numbers = set(user_numbers).intersection(winning_numbers)
num_correct = len(correct_numbers)

if num_correct == 6:
    print("Herzlichen Glückwunsch! Sie haben den Jackpot geknackt!")
elif num_correct > 0:
    print("Sie haben {} Zahlen richtig getippt!".format(num_correct))
else:
    print("Leider haben Sie keine richtigen Zahlen getippt.")