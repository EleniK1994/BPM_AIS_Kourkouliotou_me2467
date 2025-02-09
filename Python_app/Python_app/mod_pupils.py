# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 21:30:10 2024

@author: module pupils - CRUD Project
"""
import json

# global variable for pupils
pupils = []
'''pupils = [
    {
     "id": 1001,
     "name": "John",
     "surname": "Doe",
     "fathers_name": "Michael",
     "age": 11,
     "class": 6,
     "id_number": "AN123949"    
     },
    {
     "id": 1002,
     "name": "Eleni",
     "surname": "Kourkouliotou",
     "fathers_name": "Angelos",
     "age": 6,
     "class": 1,
     "id_number": "AO071381"    
     },
    {
     "id": 1003,
     "name": "Charis",
     "surname": "Thomas",
     "fathers_name": "Nikolaos",
     "age": 9,
     "class": 4,
     "id_number": "AM173950"    
     },
    {
     "id": 1004,
     "name": "Artemis",
     "surname": "Thomas",
     "fathers_name": "Themistoklis",
     "age": 10,
     "class": 4,
     "id_number": "AI173951"    
     },
    ]'''

# functions for pupils
def create_pupil():
    # pupil = {}  
    name = input("Give the name of the pupil: ").capitalize().strip()
    if name.isalpha():
        pass
    else:
        print("Error! Give the name only in letters!")
        name = input("Give the name of the pupil: ").capitalize().strip()
    
    surname = input("Give the surname of the pupil: ").capitalize()
    while not surname.isalpha():
        print("Error! Give the surname only in letters!")
        surname = input("Give the surname of the pupil: ").capitalize()
        
    fathers_name = input("Give the father's name of the pupil: ").capitalize()
    while not fathers_name.isalpha():
        print("Error! Give the father's name only in letters!")
        fathers_name = input("Give the father's name of the pupil: ").capitalize()
    
    # Check if the pupil already exists at pupils list
    for p in pupils:
        if name == p["name"] and surname == p["surname"] and fathers_name == p["fathers_name"]:
            print("This pupil already exists.")
            ch = input("Do you want to continue? Enter (y-yes, n-no): ")
            if ch == 'n':
                return None # breaks the execute of the function - no object
    
    age = input("Give the age of the pupil: ")
    while (int(age) <= 5 or int(age) >= 12) or (not age.isdigit()):
        print("Give a proper age number only between {6-11}")
        age = input("Give a proper age number between {6-11}: ")
        
    classroom = input('Give the class of the pupil (1-6): ')
    while (int(classroom) < 1 or int(classroom) > 6) or (not classroom.isdigit()):
        print('Give only digits between (1-6)')
        classroom = input('Give the class of the pupil between (1-6): ')
            
    id_card = int(input("Does he/she has an id card: (1=True, 0-False): "))
    # while id_card != 1 or id_card != 0:
    #     print('Error! Give a valid input.')
    #     id_card = int(input("Does he/she has an id card: (1=True, 0-False): "))
    if id_card == 1:
        id_number = input("Give id card number: ")
        while not id_number.isalnum() or not id_number.isupper():
            print('Give only capital letters and/or digits!')
            id_number = input("Give a valid id card number: ")
    else:
        id_number = 'N/A'
    
    # pupil["id"] = next_id()
    
    pupil = {
            "id": next_id(),
            "name": name,
            "surname": surname,
            "fathers_name": fathers_name,
            "age": age,
            "class": classroom,
            "id_number": id_number,
            }
    
    pupils.append(pupil)
    return pupil


def print_pupil(pupil):
    # pupil = {}
    print(f"The id of the new pupil is           : {pupil['id']}")
    print(f"The name of the new pupil is         : {pupil['name']}")
    print(f"The surname of the new pupil is      : {pupil['surname']}")
    print(f"The father's name of the new pupil is: {pupil['fathers_name']}")
    print(f"The age of the new pupil is          : {pupil['age']}")
    print(f"The class of the new pupil is        : {pupil['class']}")
    if "id_number" in pupil:
        print(f"The id_number of the new pupil is: {pupil['id_number']}")

    
def next_id():
    ids = [0]
    for p in pupils:
        ids.append(p["id"]) # ids = [1001, 1002, 1003]
    return max(ids) + 1
 

def init_pupils_data():
    global pupils
    try:
        with open("pupils.json") as f:
            pupils = json.load(f)
    except FileNotFoundError:
        pupils = []

def save_pupils_data():
    with open("pupils.json", "w") as g:
        json.dump(pupils, g)


def search_pupil_by_id(pupil_id):
    for pupil in pupils:
        if pupil_id == pupil["id"]:
            return pupil

def print_pupils_details():
    for pupil in pupils:
        print("="*15)
        print_pupil(pupil)

def print_pupils_names():
    for pupil in pupils:
        print(f"{pupil['name']}, {pupil['fathers_name'][0]}.{pupil['surname']}")

# for Choice == 3 UPDATE (section 12.6)
def search_pupil_by_surname(surname):
    match_pupils = []
    for pupil in pupils:
        if surname == pupil["surname"]:
            match_pupils.append(pupil)
    return match_pupils

def pupil_update(pupil):
    print_pupil(pupil)
    print(15*'=')
    print("1-name")
    print("2-surname")
    print("3-father's name")
    print("4-age")
    print("5-class")
    print("6-id number")
    print(15*"=")
    choice_to_update = input("Pick something to update (1-6): ")
    
    if int(choice_to_update).strip().isdigit():
        choice_to_update = int(choice_to_update)
    else:
        print("Wrong input!")
    
    if choice_to_update == 1:
        name_of_choice = input('Give the updated name: ')
        pupil["name"] = name_of_choice
    elif choice_to_update == 2:
        surname_of_choice = input('Give the updated surname: ')
        pupil["surname"] = surname_of_choice
    elif choice_to_update == 3:
        fathers_of_choice = input("Give the updated father's name: ")
        pupil["fathers_name"] = fathers_of_choice
    elif choice_to_update == 4:
        age_of_choice = input("Give the updated age: ")
        pupil["age"] = age_of_choice
    elif choice_to_update == 5:
        class_of_choice = input("Give the updated class: ")
        pupil["class"] = class_of_choice
    elif choice_to_update == 6:
        id_of_choice = input("Give the updated id: ")
        pupil["id_number"] = id_of_choice
    
    # "id": next_id(),
    # "name": name,
    # "surname": surname,
    # "fathers_name": fathers_name,
    # "age": age,
    # "class": classroom,
    # "id_number": id_number,
    
    print(15*"=")
    print_pupil(pupil)
    # print(pupils) # only for check
    print("The pupil is updated!")


def delete_pupil_by_id(id_no):
    for i in range(len(pupils)+1):
        if id_no == pupils[i]["id"]:
            pupils.pop(i)
            return # or break
