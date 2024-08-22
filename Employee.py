# CRUDS operation on domain "Company".

dataFile = "Employees.dat"
employeesData = {}
isEmployeeFound = 0

def printEmployeeNotFound():
	print("No employee found with id " + givenId + ".\n")

def printSuccessMessage(operationName):
	print("operation " + operationName + " successfull.\n")

def search():
	global isEmployeeFound
	isEmployeeFound = 0
	for employeeId, data in employeesData.items():
		if givenId == employeeId:
			isEmployeeFound = 1
			break

def getId(operationName):
	global givenId
	givenId = input("Enter employee Id to " + operationName + ": ")

def loadEmployees():
	global employeesData
	oDataFile = open(dataFile, "r")
	employeesData = eval(oDataFile.read())
	oDataFile.close()
	saveEmployees()

def saveEmployees():
	oDataFile = open(dataFile, "w")
	oDataFile.write(str(employeesData))
	oDataFile.close()

def addEmployee():
	global employeesData
	employeeId = input("Employee ID: ")
	employeesData[employeeId] = [input("Employee name: "), input("Employee salary: ")]
	saveEmployees()

def readEmployees():
	for employeeId, data in employeesData.items():
		print("\nEmployee ID = " + employeeId + "\nEmployee name = " + data[0] + "\nEmployee salary = " + data[1])

def searchEmployee():
	getId("search")
	search()
	if isEmployeeFound == 1:
		print("Employee details found.")
		print("Id:", givenId, "\nName:", employeesData[givenId][0], "\nSalary:", employeesData[givenId][1], "\n")
	else:
		printEmployeeNotFound()

def updateEmployee():
	global employeesData
	getId("update")
	search()
	if isEmployeeFound == 1:
		option = int(input("1) Update employee name\n2) Update employee salary\nEnter choice: "))
		if option == 1:
			employeesData[givenId][0] = input("Enter new employee name: ")
		elif option == 2:
			employeesData[givenId][1] = input("Enter new employee salary: ")
		else:
			print("Invalid choice.\n")
			printSuccessMessage("update")
	else:
		printEmployeeNotFound()
		saveEmployees()

def deleteEmployee():
	global employeesData
	getId("delete")
	search()
	if isEmployeeFound == 1:
		employeesData.pop(givenId)
		printSuccessMessage("delete")
		saveEmployees()
	else:
		printEmployeeNotFound()

def showMenu():
	loadEmployees()
	while True:
		operationList = [addEmployee, readEmployees, searchEmployee, updateEmployee, deleteEmployee, exit]
		operationList[int(input("1) Add employee\n2) Read employee\n3) Search employee\n4) Update employee\n5) Delete employee\n6) Exit\nEnter your choice: ")) - 1]()

showMenu()