rivers=[
    {"name": "Nile", "length":4157},
    {"name": "Yangtze", "length":3434},
    {"name": "Murray", "length":2310},
    {"name": "Volga", "length":2290},
    {"name": "Missisipi", "length":2540},
    {"name": "Amazon", "length":3915}
]
# print river names
for river in rivers:
    print (river["name"])

total_length = 0

for river in rivers:
    total_length=total_length + river["length"]

print(f"\n Total river lenght : {total_length}")