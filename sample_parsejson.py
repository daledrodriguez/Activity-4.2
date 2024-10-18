import json
import yaml

x = '{"name" : "John", "Age": "30", "City": "New York City"}'

y = json.loads(x)
print("The output of json file is: ",y)
print("Name:",y["name"])
print("Age:",y["Age"])
print("City:",y["City"])