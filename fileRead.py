# r-read,w-write,a-append,r+-read and write
file_contents = open("readme.txt", "r")
file_contents = open(
    "D:\\Program_installation_files\\xampp_install\\htdocs\\aframe\\assigment\\solar-system\\index.html", "r")

# checking if file is readable
# print(file_contents.readable())
# print(file_contents.readline())-first line
# print(file_contents.readlines())-reads data into array
# print(file_contents.read())

for i in file_contents.readlines():
    print(i)


file_contents.close()

