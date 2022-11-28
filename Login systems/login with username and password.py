#password and usernames (If you put new ones in please edit line 14 with the new username and line 27 with the new password)
password = ("YOUR PASSWORD") 
username = ("YOUR USERNAME")
#Imports
password = input
import os
import time

print("Welcome!")

time.sleep(0.5)

trying = input("Please enter you're username. ")
if trying == "YOUR USERNAME":
    print("Username correct.")

else:
    os.system('cls')
    print("Wrong username. Try again.")
    time.sleep(1.2)
    exit()


time.sleep(0.5)

password = input("Please Enter you're password. ")
if password == "YOUR PASSWORD":
        print("Welcome!")

else:
    print("Wrong password. Try again.")
    time.sleep(1.2)
    exit()

print("hold")

#made by 353mss#0447