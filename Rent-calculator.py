# calculating rent
rent=int(input("Enter your hostel/flat rent : "))
food=int(input("Enter the mount of food ordered : "))
electricity_spend=int(input("Enter the total electricity spend : "))
charges_per_unit=int(input("Enter the charge per unit : "))
persons= int(input("Enter the number of persons  living in room/flat : "))

total_bill=electricity_spend*charges_per_unit
output=(food+rent+total_bill)//persons
print("Each person will pay : ",output)