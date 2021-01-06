'''
--------------------------
Name: problem2.py
Purpose: Calculates the number of chicken per student and the remainder for Fabroa.

Author: Brighton Zhang

Created: date 07/12/2020
--------------------------
'''

#User inputted number of students.
student = int(input("How many students are in the class?: "))
#User inputted number of chicken.
chicken = int(input("How many piece of chicken are there?: "))

#Printing calculated integer number of chicken per student.
print("The students will get", chicken // student, "pieces of chicken.")
#Printing calculated remaining number of chicken for Fabroa.
print("Fabroa will get", chicken % student, "pieces of chicken.")
