# dictionary
# key value pairs
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    'Mar': "March"
}

# print(monthConversions["Jan"])
# print(monthConversions.get("Feb", "not a valid key"))
# print data type
# delete value
del monthConversions["Jan"]
monthConversions.popitem()
item = 'Phone'
for key,values in monthConversions.items():
   print(i)

customer={
    "name":"jack slik",
    "age":"18",
    "email":"reander@gmail.com"
}
customer.get("name")


phone=input("Phone: ")

digit_mapping={
    "1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"seven","8":"eight","9":"nine" }

output=""
for i in phone:
   output +=digit_mapping.get(i,"!")
   
print(output)