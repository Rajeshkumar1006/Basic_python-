amount=float(input("Enter the amount of bill : "));
tip_amount=float(input("Enter the tip_percentage: "))/100
print(tip_amount);
tip=amount*tip_amount
total=amount+tip
print(f"the total amount ₹ {total}");