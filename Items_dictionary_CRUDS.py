# CRUD operations on Items domain, data value as lists and key as id in dictionary

import timeit

FileItemName = "Items.dat"
data = {}
isFound = 0

def LoadData():
	global data, FileItemName
	fItem = open(FileItemName, "r")
	data = fItem.read()
	data = eval(data)

def SaveData():
	global FileItemName
	fItem = open(FileItemName, "w")
	fItem.write(str(data))
	fItem.close()

def accountNotFoundMessage():
	print("Account not found.\n")

def SuccessfullMessage(operationItemName):
	print(operationItemName, "Successfull")

def AddItem():
	ItemId = input("Enter bank id: ")
	ItemName = input("Enter bank ItemName: ")
	Price = int(input("Enter Price: "))
	data[ItemId] = [ItemName, Price]
	SaveData()

def SearchItem():
	GetId("search")
	Search()
	if isFound == 1:
		print("Record found.\n")
		print("Item id: ", GivenId, "\nName: ", data[GivenId][0], "\nprice: ", data[GivenId][1])

	else:
		accountNotFoundMessage()

def Search():
	global isFound
	for key in data.keys():
		if key == GivenId:
			isFound = 1
			break

def GetId(operationItemName):
	global GivenId
	GivenId = input("Enter id to " + operationItemName + ": ")

def UpdateItem():
	GetId("Update")
	Search()
	if isFound == 1:
		choice = input("\n1) Update Account holder ItemName\n2) Update account Price\nEnter your choice: ")
		if choice == "1":
			data[GivenId][0] = input("Enter new ItemName: ")
		elif choice == "2":
			data[GivenId][1] = input("Enter new Price: ")
		else:
			print("Invalid choice.\n")
		SaveData()
		SuccessfullMessage("Update")
	else:
		accountNotFoundMessage()

def DeleteItem():
	GetId("Delete")
	Search()
	if isFound == 1:
		del data[GivenId]
		SaveData()
		SuccessfullMessage("Delete")
	else:
		accountNotFoundMessage()

def ReadItems():
	print()
	for keys, values in data.items():
		print("Item Id:", keys, "\nName:", values[0], "\nPrice:", values[1])

def ShowMenu():
	LoadData()
	while True:
		Menu = [AddItem, ReadItems, UpdateItem, DeleteItem, SearchItem, exit]
		Menu[int(input("\n1) Add Account\n2) Read Details\n3) Update details\n4) DeleteItem\n5) SearchItem\n6) Exit\nEnter your choice: ")) - 1]()

ShowMenu()
