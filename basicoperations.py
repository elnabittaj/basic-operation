'''
Author:Elna Ann Bittaj
Date:19-10-2024
Description:Create, concatenate, and print a string and access a sub-string from a given string.
'''
Firstname=str(input("Enter your first name:"))
Lastname=str(input("Enter your last name:"))
Name=Firstname+" "+Lastname
#print(Name)
firstname_length=len(Firstname)
print(Name[firstname_length:])

