# tuple is imutable
# use fir constant data values
coordinates = (2, 4), (3, 5)
# print(coordinates[0])


# # for loop
# for i in "password":
#     print(i)

# age=9

temp=int(input("Enter temp : "))
unit=str(input("Unit being used \n 1.Kelvin \n 2.Celsius\n"))

if unit=="1":
        converted=temp-273
        print(f"Converted : {converted} K")
elif unit=="2":
        converted=temp+273
        print(f"Converted : {converted} C")
else:
        print("invalid unit")