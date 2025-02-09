# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 16:04:46 2024

@author: module teachers - CRUD Project
"""
import json 

# global variable for teachers
teachers = []
'''teachers = [
    {
      "id": 2001,
      "name": "John",
      "surname": "Brown",
      "fathers_name": "Michael",
      "age": 29,
      "class": 6,
      "id_number_t": "AN151515"    
      },
    {
      "id": 2002,
      "name": "Eleni",
      "surname": "Aggelopoulou",
      "fathers_name": "Menelaos",
      "age": 58,
      "class": 1,
      "id_number_t": "AO071388"    
      },
    {
      "id": 2003,
      "name": "Charis",
      "surname": "Romas",
      "fathers_name": "Isidoros",
      "age": 50,
      "class": 4,
      "id_number_t": "AI171717"    
      },
    {
      "id": 2004,
      "name": "Artemis",
      "surname": "Pavlidou",
      "fathers_name": "Alexandros",
      "age": 40,
      "class": 4,
      "id_number_t": "AI555566"    
      },
    ]'''

# functions for teachers
def create_teacher():
    # teacher = {}  
    name = input("Give the name of the teacher: ").capitalize().strip()
    if name.isalpha():
        pass
    else:
        print("Error! Give the name only in letters!")
        name = input("Give the name of the teacher: ").capitalize().strip()
    
    surname = input("Give the surname of the teacher: ").capitalize()
    while not surname.isalpha():
        print("Error! Give the surname only in letters!")
        surname = input("Give the surname of the teacher: ").capitalize()
        
    fathers_name = input("Give the father's name of the teacher: ").capitalize()
    while not fathers_name.isalpha():
        print("Error! Give the father's name only in letters!")
        fathers_name = input("Give the father's name of the teacher: ").capitalize()
    
    # Check if the teacher already exists at teachers list
    for p in teachers:
        if name == p["name"] and surname == p["surname"] and fathers_name == p["fathers_name"]:
            print("This teacher already exists.")
            ch = input("Do you want to continue? Enter (y-yes, n-no): ")
            if ch == 'n':
                return None # breaks the execute of the function - no object
    
    age = input("Give the age of the teacher: ")
    while (int(age) <= 25 or int(age) >= 65) or (not age.isdigit()):
        print("Give a proper age number only between {25-65}")
        age = input("Give a proper age number between {25-65}: ")
        
    classroom = input('Give the class of the teacher (1-6): ')
    while (int(classroom) < 1 or int(classroom) > 6) or (not classroom.isdigit()):
        print('Give only digits between (1-6)')
        classroom = input('Give the class of the teacher between (1-6): ')
            
    id_card = int(input("Does he/she has an id card: (1=True, 0-False): "))
    # while id_card != 1 or id_card != 0:
    #     print('Error! Give a valid input.')
    #     id_card = int(input("Does he/she has an id card: (1=True, 0-False): "))
    if id_card == 1:
        id_number_t = input("Give id card number: ")
        while not id_number_t.isalnum() or not id_number_t.isupper():
            print('Give only capital letters and/or digits!')
            id_number_t = input("Give a valid id card number: ")
            continue
    else:
        id_number_t = 'N/A'
    
    teacher = {
            "id": next_id(),
            "name": name,
            "surname": surname,
            "fathers_name": fathers_name,
            "age": age,
            "class": classroom,
            "id_number_t": id_number_t,
            }
    
    teachers.append(teacher)
    return teacher


def print_teacher(teacher):
    # teacher = {}
    print(f"The id of the new teacher is           : {teacher['id']}")
    print(f"The name of the new teacher is         : {teacher['name']}")
    print(f"The surname of the new teacher is      : {teacher['surname']}")
    print(f"The father's name of the new teacher is: {teacher['fathers_name']}")
    print(f"The age of the new teacher is          : {teacher['age']}")
    print(f"The class of the new teacher is        : {teacher['class']}")
    if "id_number_t" in teacher:
        print(f"The id_number of the new teacher is: {teacher['id_number_t']}")
    
def next_id():
    ids = [0]
    for p in teachers:
        ids.append(p["id"]) # ids = [2001, 2002, 2003, 2004]
    return max(ids) + 1
 

def init_teachers_data():
    global teachers
    try:
        with open("teachers.json") as f:
            teachers = json.load(f)
    except FileNotFoundError:
        teachers = []
    

def save_teachers_data():
    with open("teachers.json", "w") as g:
        json.dump(teachers, g)

def read_teacher(teacher_id):
    for teacher in teachers:
        if teacher_id == teacher["id"]:
            return teacher
    else:
        return None

def update_teacher(teacher_id, key, value):
    for teacher in teachers:
        if teacher_id == teacher["id"]:
            teacher[key] = value
            return


def delete_teacher(id_no):
    for i in range(len(teachers)+1):
        if id_no == teachers[i]["id"]:
            teachers.pop(i)
            return # or break
