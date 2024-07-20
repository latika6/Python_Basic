#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.

bill = input()
bill_1 = int(bill)
total_bill = (bill_1 * 0.12) + bill_1
split_bill = round(total_bill/5, 2)
print(f"Each person should pay: {split_bill}")