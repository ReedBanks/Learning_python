# serialization => converting dictionary to json data
# deserialization => converting json data to dictionary
import json


package_info={
  "name": "node",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "dev": "nodemon index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.18.2",
    "nodemailer": "^6.9.4",
    "nodemon": "^3.0.1",
    "year":2002
  }
}

package_info_json=json.dumps(package_info,indent=4,sort_keys=True )#dumps the dictionary into a json format
# print(package_info_json)


# dumping dictionary into a json file
# with open("pkg_info.json","w") as f:
    # json.dump(package_info,f,indent=4)
    
# loading info from json data to dictionary
converted_json=json.loads(package_info_json)
# print(converted_json)

# loading info from json file to dictionary
with open('pkg_info.json', 'r') as f:
  converted_file_json=json.load(f)
  # print(converted_file_json)
  
# dealing with custiom objs
class User:
  def __init__(self,name,age):
    self.name = name
    self.age = age
    

user1=User("user1",23)

def encodeUser(e):
  # check if user is an instance of a class
  if isinstance(e,User):
    return {"name":e.name, "age":e.age,e.__class__.__name__:True}
  else:
    return TypeError("User must be an instance")

# implementation of a custom json encoder
from json import JSONEncoder

userJSON=json.dumps(user1,default=encodeUser) 
print(userJSON)

