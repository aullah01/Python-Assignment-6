
# Class Task 1:
# for i in range(1,11):
#     output = 3 * i
#     print("3 x", i, "=", output)

# Class Task 2:
# list = ["red", "green", "yellow", "blue", "black"]
# for i in list:
#     print("index: ", list.index(i), "item: ", i)
    
# list = ["red", "green", "yellow", "blue", "black"]
# for i in range(len(list)):
#     print("index: ", i, "item: ", list[i])
    
    
# Class Task3:
# cold_drinks = ["pepsi", "marinda","pakola"]
# for i in cold_drinks:
#     if i == "pakola":
#         print("pokala is there")

# cold_drinks = ["pepsi", "marinda","pakola","sprite", "7up", "dew"]
# for i in cold_drinks:
#     print("finding pakola")
#     if i == "pakola":
#         print("pokala is there")
#         print("pokala has been found")
#         break
#     print("not found")
#     print("move to the next item")



# arr = [1,2,3,4,5,6,7,8,9,10]
# for item in arr:
#     if item % 2 == 0:
#         continue
#     print(item)


# class Task 4:
# emails = ["user_1@gmail.com", "user_2@gmail.com", "user_3@gmail.com", "user_4@gmail.com", "admin@gmail.com", "user_5@gmail.com", "user_6@gmail.com"]
# for i in emails:
#     if i.find("@") < 0:
#         continue
#     print("sending email to user", i)
    
# for i in emails:
#     if i == "admin@gmail.com":
#         print("sending email to user", i)
#         break
    
# for item in emails:
#     # if item.find("@") == -1:
#     #     continue
#     if "@" not in item:
#         continue
#     print(item)

# for item in emails:
#     if item.find("admin") > -1:
#         print("Sending email to admin", item)
#         break
  


# Data structure Dictionary

# student_data = ["ameen", 30, True, 40.3, None]

# student_data = {
#     "name": "ameen",
#     "age": 30,
#     "is_employed": True,
#     "weight": 40.3,
#     "is_student": None
# }
# student_data["weight"] = 50.5
# # print(student_data)

# student_data["have_car"] = True
# print(student_data)



# student_data = {
#     "name": "ameen",
#     "age": 30,
#     "is_employed": True,
#     "weight": 40.3,
#     "is_student": None,
#     "siblings": ["fahad", "ameen", "bajwa"],
#     "employee_detail": {
#         "id": 200,
#         "salary": 5000,
#         "department": "IT",
#         "manager_of": ["shahzaib", "abdullah", "amin"]
#     }
# }

# print(student_data["siblings"][0])

# siblings = student_data["siblings"]
# print(siblings[0])

# print("Emplyee Salary is: ",student_data["employee_detail"]["salary"])

# emp_det = student_data["employee_detail"]
# print("Employee salary is: ",emp_det["salary"])

# print("manager is: ", student_data["employee_detail"]["manager_of"][1])


# employees = [
#     {
#         "name": "Alice",
#         "projects": ["ProjectA", "ProjectB", "ProjectC"],
#         "salaries": [70000, 72000, 75000],
#         "Department": "HR"
#     },
#     {
#         "name": "Bob",
#         "projects": ["ProjectD", "ProjectE", "ProjectF"],
#         "salaries": [65000, 67000, 70000],
#         "Department": "Finance"
#     },
#     {
#         "name": "Charlie",
#         "projects": ["ProjectG", "ProjectH", "ProjectI"],
#         "salaries": [80000, 82000, 85000],
#         "Department": "IT"
#     },
#     {
#         "name": "Diana",
#         "projects": ["ProjectJ", "ProjectK", "ProjectL"],
#         "salaries": [75000, 77000, 80000],
#         "Department": "Marketing"
#     },
#     {
#         "name": "John",
#         "projects": ["ProjectM", "ProjectN", "ProjectO"],
#         "salaries": [55000, 57000, 60000],
#         "Department": "Sales"
#     }
# ]

# alice = employees[0]["Department"]
# print(alice)

# for i in employees:
#     if i["name"] == "Charlie":
#         print(i["Department"])

# for i in range(len(employees)):
#     print(employees[i]["Department"])
    
