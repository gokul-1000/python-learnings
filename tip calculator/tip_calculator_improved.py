print("heyy, welcome to the tip calculator")

bill = float(input("what's your total bill "))
tip = int(input("how much tip you wanna give 10% , 12% , 15% "))
share = int(input("how many people to split the bill in ? "))

tip_amount = bill * (tip / 100)
total_bill = bill + tip_amount
amount_payable = total_bill / share

print("each person has to pay :", round(amount_payable, 2))
