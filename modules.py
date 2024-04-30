import modules1
import pydoc
# gives acces to file and its methods

print(modules1.roll(43))

name="mango morales"
strip=name[::-1]
indexO=name.index('o')
cha=name.count('m')

myString="how ,are, you"
lister=myString.split(',') # , is the delimeter
newString=''.join(lister) #concatenating the elements in the list

school="UMaT"
faculty="Computer Science"
position="Student"
cwa = 92.232
age=23
#formatting
# sentence="the variable is %s" % faculty
# sentence="the variable is %d" % age
# sentence="the variable is %.2f" % cwa 
sentence="the variable is {} in {} as {}".format(school,faculty,position)
sentence=f"the variable is {school} in {faculty} as {position}"





print(sentence)
