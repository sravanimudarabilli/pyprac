import json
import jsonschema
from jsonschema import validate

employeeSchema={
    "type":"object",
    "properties":{
        "name":{"type":"string",
                "pattern":"[A-Za-z]",
                "minLength":1,
                "maxLength":7
                },
        "id":{"type":"integer",
              "minimum":4,
              "maximum":200

              },
        "mail":{
            "type":"string",
            "pattern":"^[A-Za-z0-9]*@gmail.com$"
        }


    },
    "required":["name","mail"]
}
#reading data from json file
with open('sample.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)


#validating one by one against schema
for x in json_object:
    def validateJson(x):
        try:
            validate(instance=x, schema=employeeSchema)
        except jsonschema.exceptions.ValidationError as err:
            print("invalid json", err)
            return False
        return True
#jsonData=json.loads('{"name":"SRAVANI","id":5,"mail":"srav91@gmail.com"}')
    isValid=validateJson(x)
    if isValid:
        print(x)
        print("given data is valid")
        with open('valid.json', 'a') as f:
            json.dump(x, f)
        print("*************************")
    else:
        print(x)
        with open('invalid.txt', 'a') as fi:
            json.dump(x, fi)
        print("given data is invalid")
        print("**************************")