def helloworld():
    print("hello world")


ismale =""
tall = ""
if ismale or tall:
    print("male or tall")
elif ismale != True or tall != True:
    print("female or not tall")
elif ismale and tall:
    print("male and tall")
elif ismale != True and tall != True:
    print("female and not tall")

else:
    print("invalid")

# positional arguments
def newmax(val1, val2, val3):
    if val1 >= val2 and val1 >= val3:
        print(val1, " is the maximum")
    elif val2 >= val1 and val2 >= val3:
        print(val2, " is the maximum")
    else:
        print(val3, " is the maximum")


# newmax(1, 22, 1)

# keyword arguments
# for this position doesn't matter
def greetings(firstname, lastname):
    print(f'hello, {firstname} {lastname} \n how are you?')


def square(val1):
    return pow(val1,2)

print(f'square : {square(2)}')
print(greetings("another","emailer"))
print(greetings(lastname="another",firstname="emailer"))
