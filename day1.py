# print("Hello World")
# print("Python has 3 numeric types: int , float and complex")
# myvalue=[1,'a',3.0,'apple',5768546785,6j,True]
# for i in range(len(myvalue)):
#     print(str(myvalue[i]) + "is datatype of  ",type(myvalue[i]))


# mystring = "This is aws restart python class"
# print(str(mystring) + "is of type " +str(type(mystring)))

# firststring = 1
# secondstring = 2
# thirdString = firststring - secondstring
# print(str(thirdString) + "  is of type",type(thirdString))

# name = input("what is your name? ")
# lname = input("what is your lname? ")

# print(f"Hello ,{name} {lname}")

# mylist = ("Banana","Apple","Grapes","Guva","mango")
# # mylist[1] = "sewau"
# print(type(mylist))

# myDistionary = {
#   "student1":{
#       "Name" :"Anup Kafle",
#       "Age" : "40",
#       "address":{
#           "city" : "bhaktapur",
#           "country" : "nepal"

#       }   
#   }
# }
# print(myDistionary["student1"]["address"]["city"])





# myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
# for item in range(len(myMixedTypeList)):
#     print(myMixedTypeList[item])
import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

myInventoryList = []

with open('data.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    # print(f'Processed {lineCount} lines.')
currentVehicle = copy.deepcopy(myVehicle)
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")
    