"""
Create a dictionary named student_scores with the following key-value pairs:
"Alice": 85
"Bob": 78
"Charlie": 92
"Diana": 88
"Evan": 76


1. Write a for loop to iterate through the student_scores dictionary and print each student's name and their score in the format: Student: [Name], Score: [Score].

2. Write a for loop to calculate the average score of the students. Print the average score.

3. Write a for loop to assign grades based on the following criteria:
Score >= 90: Grade A
Score >= 80 and < 90: Grade B
Score >= 70 and < 80: Grade C
Score < 70: Grade D
Store these grades in a new dictionary called student_grades.

4. Modify the student_scores dictionary by adding 5 bonus points to each student's score. 
Print the updated student_scores dictionary.
"""

# Solution 1:

# student_scores = {
#     "Alice": 85,
#     "Bob": 78,
#     "Charlie": 92,
#     "Diana": 88,
#     "Evan": 76
# }

# for i in student_scores:
#     print(f"Student: {i}, Score: {student_scores[i]}")


# Solution 2:

# student_scores = {
#     "Alice": 85,
#     "Bob": 78,
#     "Charlie": 92,
#     "Diana": 88,
#     "Evan": 76
# }

# for i in student_scores:
#     total_scores = sum(student_scores.values())
#     num_students = len(student_scores)
#     average_score = total_scores / num_students
# print(average_score)
    
    
# Solution 3:

# student_scores = {
#     "Alice": 85,
#     "Bob": 78,
#     "Charlie": 92,
#     "Diana": 88,
#     "Evan": 76
# }

# student_grades = {}

# for i in student_scores:
#     if student_scores[i] >= 90:
#         student_grades[i] = "A"
#     elif student_scores[i] >= 80 and student_scores[i] < 90:
#         student_grades[i] = "B"
#     elif student_scores[i] >= 70 and student_scores[i] < 80:
#         student_grades[i] = "C"
#     else:
#         student_grades[i] = "D"

# print("Student grasdes based on their score: ")
# for i in student_grades:
#     print(f"Student: {i}, Grade: {student_grades[i]}")
    

# Solution 4:

# student_scores = {
#     "Alice": 85,
#     "Bob": 78,
#     "Charlie": 92,
#     "Diana": 88,
#     "Evan": 76
# }

# for i in student_scores:
#     student_scores[i] += 5
# print(student_scores)



"""
Create a dictionary named employee_data with the following key-value pairs:
"John": 55000
"Emma": 60000
"Harry": 70000
"Sophia": 65000
"Mike": 48000

1. Write a for loop with an if statement to identify employees who earn more than $60,000. Print their names.
2. Write a for loop to increase the salary of each employee by 10%. Update the dictionary accordingly.

"""

# Solution 1:

# employee_data = {
#     "John": 55000,
#     "Emma": 60000,
#     "Harry": 70000,
#     "Sophia": 65000,
#     "Mike": 48000
# }

# for i in employee_data:
#     if employee_data[i] > 60000:
#         print("Employee who earns more than $60000: ",i)

# Solution 2:

# employee_data = {
#     "John": 55000,
#     "Emma": 60000,
#     "Harry": 70000,
#     "Sophia": 65000,
#     "Mike": 48000
# }

# for i in employee_data:
#     employee_data[i] = round(employee_data[i] * 1.10, 2)
# print(employee_data)


"""
Create a dictionary named library_books with the following key-value pairs:
"The Great Gatsby": 4
"1984": 6
"To Kill a Mockingbird": 3
"The Catcher in the Rye": 5
"Moby Dick": 2

1. Write a for loop to add 2 more copies to each book. Update the dictionary accordingly.
2. Write a for loop to calculate the total number of books in the library. Print the total count.
"""

# Solution 1:

# library_books = {
#     "The Great Gatsby": 4,
#     "1984": 6,
#     "To Kill a Mockingbird": 3,
#     "The Catcher in the Rye": 5,
#     "Moby Dick": 2
# }

# for i in library_books:
#     library_books[i] = library_books[i] + 2
# print(library_books)


# Solution 2:

# library_books = {
#     "The Great Gatsby": 4,
#     "1984": 6,
#     "To Kill a Mockingbird": 3,
#     "The Catcher in the Rye": 5,
#     "Moby Dick": 2
# }

# total_books = 0

# for books in library_books:
#     total_books += library_books[books]
# print(total_books)


"""
consider the list of dicts
book_list = [{"name": "The Great Gatsby", "quantity": 4}, {"name": "1984", "quantity": 6}, {"name": "To Kill a Mockingbird", "quantity": 3}, {"name": "Moby Dick", "quantity": 2}]
Write a for loop to assign one more detail "stock" based on the number of copies available:
Copies >= 5: "Popular"
Copies >= 3 and < 5: "Available"
Copies < 3: "Limited"
Store these stock categories in a same dict i.e book_list.
"""

# Solution:

# book_list = [
#     {"name": "The Great Gatsby", "quantity": 4}, 
#     {"name": "1984", "quantity": 6}, 
#     {"name": "To Kill a Mockingbird", "quantity": 3}, 
#     {"name": "Moby Dick", "quantity": 2}
#     ]

# for book in book_list:
#     quantity = book["quantity"]
#     if quantity >= 5:
#         book["stock"] = "Popular"
#     elif quantity >= 3 and quantity <= 5:
#         book["stock"] = "Available"
#     else:
#         book["stock"] = "Limited"
# print(book_list)


"""
Given the dict

students = {
    "Alice": {
                "Subjects": ["Math", "Science", "English"],
                "Scores": [85, 90, 78],
                "Class": 10
            },
    "Bob": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [75, 80, 88],
        "Class": 10
    },
    "Charlie": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [92, 89, 94],
        "Class": 11
    },
    "Diana": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [88, 76, 85],
        "Class": 11
    },
    "John": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [50, 60, 60],
        "Class": 11
    }
}


1. display Alice English Score
2. display Bob Class
3. display Charlie Math Score
4. display Diana's avg score
5. display John's all subject name and score with format: Student: [Name], Score: [Subject], Score: [Score].
6. Add new Student and its subject, score and class in same dict i.e students
7. add new subject and its score in John
"""

# students = {
#     "Alice": {
#                 "Subjects": ["Math", "Science", "English"],
#                 "Scores": [85, 90, 78],
#                 "Class": 10
#             },
#     "Bob": {
#         "Subjects": ["Math", "Science", "English"],
#         "Scores": [75, 80, 88],
#         "Class": 10
#     },
#     "Charlie": {
#         "Subjects": ["Math", "Science", "English"],
#         "Scores": [92, 89, 94],
#         "Class": 11
#     },
#     "Diana": {
#         "Subjects": ["Math", "Science", "English"],
#         "Scores": [88, 76, 85],
#         "Class": 11
#     },
#     "John": {
#         "Subjects": ["Math", "Science", "English"],
#         "Scores": [50, 60, 60],
#         "Class": 11
#     }
# }

# Solution 1:

# alice = students["Alice"]["Scores"][2]
# print(alice)

# Solution 2:

# bob = students["Bob"]["Class"]
# print(bob)

# Solution 3:

# charlie = students["Charlie"]["Scores"][0]
# print(charlie)

# Solution 4:

# diana = students["Diana"]["Scores"]
# avg = sum(diana)/len(diana)
# print(avg)

# Solution 5:

# john = students["John"]

# print(f"Student: John")
# num_sub = len(john["Subjects"])
# for i in range(num_sub):
#     subject = john["Subjects"][i]
#     score = john["Scores"][i]
#     print(f"Subjects: {subject}, Score: {score}")


# Solution 6:

# new_student = {
#     "Ameen": {
#         "Subjects": ["Math", "Physics", "Chemistry"],
#         "Scores": [95, 98, 92],
#         "Class": 12
#     }
# }
# students.update(new_student)
# print("Updated students dictionary with Ameen:")
# print(students)

# Solution 7:

# new_subject = "Physics"
# new_score = 75

# students["John"]["Subjects"].append(new_subject)

# students["John"]["Scores"].append(new_score)

# print("Updated John dictionary with new subject and score:")

# print(students["John"])


"""
Givent the list of students
students = [
    {
        "name": "Alice",
        "subjects": ["Math", "Science", "English"],
        "scores": [85, 90, 78],
        "Class": 10
    },
    {
        "name": "Bob",
        "subjects": ["Math", "Science", "English"],
        "scores": [75, 80, 88],
        "Class": 10
    },
    {
        "name": "Charlie",
        "subjects": ["Math", "Science", "English"],
        "scores": [92, 89, 94],
        "Class": 11
    },
    {
        "name": "Diana",
        "subjects": ["Math", "Science", "English"],
        "scores": [88, 76, 85],
        "Class": 11
    }
]

1. display Alice English Score
2. display Bob Class
3. display Charlie Math Score
4. display Diana's avg score
5. display John's all subject name and score with format: Student: [Name], Score: [Subject], Score: [Score].
6. display which class obtained the higher marks
7. display the student name that obtain high marks in subject Math in class 10
8. Add new Student and its subject, score and class in same dict i.e students
"""

# students =[
#     {
#         "name": "Alice",
#         "subjects": ["Math", "Science", "English"],
#         "scores": [85, 90, 78],
#         "Class": 10
#     },
#     {
#         "name": "Bob",
#         "subjects": ["Math", "Science", "English"],
#         "scores": [75, 80, 88],
#         "Class": 10
#     },
#     {
#         "name": "Charlie",
#         "subjects": ["Math", "Science", "English"],
#         "scores": [92, 89, 94],
#         "Class": 11
#     },
#     {
#         "name": "Diana",
#         "subjects": ["Math", "Science", "English"],
#         "scores": [88, 76, 85],
#         "Class": 11
#     },
#     {
#         "name": "John",
#         "subjects": ["Math", "Science", "English"],
#         "scores": [50, 60, 60],
#         "Class": 11
#     }
# ]

# Solution 1:

# alice = students[0]["scores"][2]
# print(alice)

# Solution 2:

# bob = students[1]["Class"]
# print(bob)

# Solution 3:

# charlie = students[2]["scores"][0]
# print(charlie)

# Solution 4:

# diana = students[3]["scores"]
# avg = sum(diana)/ len(diana)
# print(avg)

# Solution 5:

# student_name = students[4]["name"]
# print(f"Student Name: {student_name}")

# john = students[4]
# num_subject = len(john["Subjects"])

# for i in range(num_subject):
#     subject = john["Subjects"][i]
#     score = john["Scores"][i]
#     print(f"Subject: {subject}, Score: {score}")


# Solution 6:

# total_score_Class_10 = 0
# total_score_Class_11 = 0

# for i in students:
#     if i["Class"] == 10:
#         total_score_Class_10 += sum(i["scores"])
#     elif i["Class"] == 11:
#         total_score_Class_11 += sum(i["scores"])
        
# if total_score_Class_10 > total_score_Class_11:
#     print("Class 10 obtained the higher marks.")
# elif total_score_Class_11 > total_score_Class_10:
#     print("Class 11 obtained the higher marks.")
# else:
#     print("Both classes obtained the same marks.")

# Solution 7:


# highest_math_score = -1
# top_math_student = None

# for student in students:
#     if student["Class"] == 10:
#         math_index = student["subjects"].index("Math")
#         math_score = student["scores"][math_index]
#         if math_score > highest_math_score:
#             highest_math_score = math_score
#             top_math_student = student["name"]

# if top_math_student:
#     print(f"Student with highest marks in Math in class 10: {top_math_student}")
# else:
#     print("No student found in class 10.")

# Solution 8:

# new_student = {
#     "Ameen": {
#         "Subjects": ["Math", "Physics", "Chemistry"],
#         "Scores": [95, 98, 92],
#         "Class": 12
#     }
# }
# students.append(new_student)
# print("Updated students dictionary with Ameen:")
# print(students)
