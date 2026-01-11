print("heyy, welcome to the tip calculator")
bill=input("what's your total bill ")
tip=input("how much tip you wanna give 10% , 12% , 15% ")
share=input("how many people to split the bill in ? ") 
tip_amount=float(bill)*(int(tip)/100)
total_bill=float(bill)+tip_amount
amount_payable=total_bill/int(share)
print("each person has to pay :", amount_payable)