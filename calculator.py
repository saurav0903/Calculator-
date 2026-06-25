# input we need from the user
#Total rent 
# Total food order fro snccking 
# charge per unit 
# person who is paying the bill
# output
# Total amount you've to pay is

rent = int(input("Enter flat rent: "))
food_order = int(input("Enter total food order for snacking: ")) 
electricity_charge = int(input("Enter electricity charge per unit: "))
charge_per_unit = int(input("Enter charge per unit: "))
person_paying = int(input("Enter the number of people sharing the bill: "))
total_bill = electricity_charge + charge_per_unit
output = (food_order + rent + total_bill) // person_paying 
print("Each person has to pay: ", output)

                                                          