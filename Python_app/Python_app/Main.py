# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 22:12:10 2024

@author: CRUD Project - Professors (continued from 14_6)
"""
# 1st level = save data (files, DB, cloud), 
# 2nd level = application of data - real process, 
# 3rd = user interface UI - appearance
# we are going to handle the 2nd level

import mod_pupils
# from mod_pupils import * ## to import all
import mod_teachers
# from mod_teachers import *
        

# main function - Program
def main():
    
    mod_teachers.init_teachers_data()
    mod_pupils.init_pupils_data()
    
    while True:
        print("\n==============")
        print("      MENU      ")
        print("1 - Create Pupil")
        print("2 - Print")
        print("3 - Update Pupil")
        print("4 - Delete Pupil")
        print("5 - Create Teacher")
        print("6 - Read Teacher")
        print("7 - Update Teacher")
        print("8 - Delete Teacher")
        print("9 - Exit")
        choice = int(input("Pick one (1-2-3-4-5-6-7-8-9): "))
        while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6 and choice != 7 and choice != 8 and choice != 9:
            print('Give a valid input!')
            print("\n==============")
            print("      MENU      ")
            print("1 - Create Pupil")
            print("2 - Print")
            print("3 - Update Pupil")
            print("4 - Delete Pupil")
            print("5 - Create Teacher")
            print("6 - Read Teacher")
            print("7 - Update Teacher")
            print("8 - Delete Teacher")
            print("9 - Exit")
            choice = int(input("Pick one (1-2-3-4-5-6-7-8-9): "))
            continue            
        
        if choice == 1:
            print("NEW PUPIL")
            print("=========")
            mod_pupils.pupil = mod_pupils.create_pupil()
            if mod_pupils.pupil is None: # no pupil == None!
                continue
            else:
                print("NEW PUPIL")
                mod_pupils.print_pupil(mod_pupils.pupil)
            print(mod_pupils.pupils)
        
        elif choice == 2:
            print("\n==============")
            print("    SUB-MENU    ")
            print("1 - Print Pupil")
            print("2 - Print all pupils (details)")
            print("3 - Print all pupils (just the names)")
            print_choice = input("Give your choice (1-2-3): ")
            if print_choice.strip().isdigit():
                print_choice = int(print_choice)
            else:
                print("Wrong input!")
                continue
            
            if print_choice == 1:
                mod_pupils.pupil_id = int(input('Give the pupil id: '))
                mod_pupils.pupil = mod_pupils.search_pupil_by_id(mod_pupils.pupil_id)
                if mod_pupils.pupil is None:
                    print("This pupil does not exist (with this id).")
                else:
                    mod_pupils.print_pupil(mod_pupils.pupil)
                    
            elif print_choice == 2:
                mod_pupils.print_pupils_details()
                
            elif print_choice == 3:
                mod_pupils.print_pupils_names()
            
        elif choice == 3:
            print("\n==============")
            print("    SUB-MENU (UPDATE)    ")
            print("1 - Update Pupil (search by id)")
            print("2 - Update Pupil (search by surname)")
            update_choice = input("Give your choice (1-2): ")
            
            if update_choice.strip().isdigit():
                update_choice = int(update_choice)
            else:
                print("Wrong input!")
                continue
            
            if update_choice == 1:
                mod_pupils.pupil_id = int(input('Give id: '))
                mod_pupils.pupil = mod_pupils.search_pupil_by_id(mod_pupils.pupil_id)
                if mod_pupils.pupil is None:
                    print('Error! There is no pupil with this id number!')
                    continue
            elif update_choice == 2:
                pupil_surname = input('Give surname: ')
                mod_pupils.matching_pupils = mod_pupils.search_pupil_by_surname(pupil_surname)
                if not mod_pupils.matching_pupils: # empty list = False
                    print("No matching pupils with this surname!")
                    continue
                elif len(mod_pupils.matching_pupils) == 1:
                    pupil = mod_pupils.matching_pupils[0]
                else:
                    for p in mod_pupils.matching_pupils:
                        mod_pupils.print_pupil(p)
                        # print(f"id = {p['id']}")
                        print("-"*15)
                    pupil_id = input("Give id: ")
                    while not pupil_id.isdigit():
                        print("Error! Please give a valid id.")
                    else:
                        pupil_id_1 = int(pupil_id)
                    pupil = mod_pupils.search_pupil_by_id(pupil_id_1)
            
            mod_pupils.pupil_update(pupil) # call of the above function
        
        
        elif choice == 4:
            print("\n==============")
            print("    SUB-MENU (DELETE)    ")
            print("1 - Delete Pupil (search by id)")
            print("2 - Delete Pupil (search by surname)")
            delete_choice = input("Give your choice (1-2): ")
            
            if delete_choice.strip().isdigit():
                delete_choice = int(delete_choice)
            else:
                print("Wrong input!")
                continue
            
            if delete_choice == 1:
                pupil_id = int(input('Give id: '))
                pupil = mod_pupils.search_pupil_by_id(pupil_id)
                if pupil is None:
                    print('Error! There is no pupil with this id number!')
                    continue
            elif delete_choice == 2:
                pupil_surname = input('Give surname: ')
                mod_pupils.matching_pupils = mod_pupils.search_pupil_by_surname(pupil_surname)
                if not mod_pupils.matching_pupils: # empty list = False
                    print("No matching pupils with this surname!")
                    continue
                elif len(mod_pupils.matching_pupils) == 1:
                    pupil = mod_pupils.matching_pupils[0]
                else:
                    for p in mod_pupils.matching_pupils:
                        mod_pupils.print_pupil(p)
                        # print(f"id = {p['id']}")
                        print("-"*15)
                    pupil_id = input("Give id: ")
                    while not pupil_id.isdigit():
                        print("Error! Please give a valid id.")
                    else:
                        pupil_id_1 = int(pupil_id)
                    pupil = mod_pupils.search_pupil_by_id(pupil_id_1)
            
            # delete
            mod_pupils.delete_pupil_by_id(pupil["id"]) # call of the above function
        
        elif choice == 5:
            # first_name = input('Give name of the teacher: ')
            # surname = input('Give surname of the teacher: ')
            mod_teachers.create_teacher()
            print(mod_teachers.teachers)
        
        elif choice == 6:
            teacher_id = int(input('Give teacher id: '))
            teacher = mod_teachers.read_teacher(teacher_id)
            mod_teachers.print_teacher(teacher)
        
        elif choice == 7:
            teacher_id = int(input('Give the id of the teacher, who must be updated: '))
            teacher_key = input('Give the field that must be updated: id-name-surname-fathers_name-age-class-id_number_t: ')
            teacher_value = input('Give the new value: ')
            
            # teacher = {
            #  "id": 2001,
            #  "name": "John",
            #  "surname": "Brown",
            #  "fathers_name": "Michael",
            #  "age": 29,
            #  "class": 6,
            #  "id_number_t": "AN151515"    
            #  }
            
            mod_teachers.update_teacher(teacher_id, teacher_key, teacher_value)
            print(mod_teachers.teachers)
        
        elif choice == 8:
            id_no = int(input('Give the id no of the teachers, who must be deleted: '))
            mod_teachers.delete_teacher(id_no)
            print(mod_teachers.teachers)
            
        elif choice == 9:
            print("Bye bye!")
            mod_teachers.save_teachers_data()
            mod_pupils.save_pupils_data()

            break
#%%
main()


