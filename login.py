from tkinter import *


def getUserData():
    while True:
        try:
            username = input("Enter username: ")
            file = open(username+".txt", "r").readlines()
            break
        except:
            print("User not found")
    data = []
    for line in file:
        data.append(line.strip())
    return data