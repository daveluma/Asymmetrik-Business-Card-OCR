#This program takes in a business card file(txt) and outputs the name, number, and email based on the respective card information
from tkinter import *
import tkinter as tk
from tkinter import simpledialog
import re

name_list = []
tel_list = []
email = ""
tel = ""
name = ""

#Choose if you're using a file or a string 
usin = input("are you using a string or a text file?\n(s for string, t for text file: ")

if (str(usin) == "t"):
  #opens the file
  while True:
    try:
      doc = input("give the name of the file: ")
      f = open(doc, "r")
      break
      print(f)
    except:
      print("Error trying to open file. Try again")
else:
  f = input("input your string: ")
i = 1
j = 1

#Seperate the business card into pieces (by newline)
if usin == "s":
  print(f)
  f = f.split("\\n")
  print(f)
#opens the file

def BusinessCardParser(f):
  i = 1
  j = 1

  for x in f:
      #if input from line matches "firstname lastname" format add to list
      name_match = re.search(r'\b([A-Z]+[a-z]+)\b \b([A-Z]+[a-z]+)\b', x)
      if name_match:
          name_list.append(str(i) + ") " + name_match.group(0))
          i += 1
      tel_match = re.search(r'(\(*\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$', x)
      #If input from line matches telephone format then add it to list
      if tel_match:
          tel_list.append(str(j) + ") " + tel_match.group(0))
          j += 1
      #if input from line matches email format then store it as the email
      email_match = re.search(r'.*[@].*', x)
      if email_match:
          email = email_match.group(0)
  i = 0
  while i < len(tel_list):
      tel_list[i] = tel_list[i][:-1]
      i += 1

  if len(tel_list) == 1:
      tel = tel_list[0]
  print(tel_list)
  ROOT = tk.Tk()

  ROOT.withdraw()

  #ask user which is the correct name
  USER_INP = simpledialog.askstring(title="Name",prompt="Which of these are your name?:" + "\n" + str(name_list) + "\n(Select a number):")

  #select choice from the user
  name = name_list[int(USER_INP)-1]
  #crop out the number in the name
  name = name[2:]

  print(tel_list)
  if(len(tel_list) > 1):
    USER_INP = simpledialog.askstring(title="Name",prompt="Which of these are your telephone number?:" + "\n" + str(tel_list) + "\n(Select a number):")
    tel = tel_list[int(USER_INP)-1]
    tel = tel[2:]
  else:
    tel = tel[2:]

  root = tk.Tk()

  #output the name, phone number, and email
  msg = tk.Message(root, text = ("Name: " + str(name) + "\n" + "Phone: " + str(tel) + "\n" + "Email: " + str(email)), width = 1000)
  msg.config(font=("times",24))
  msg.pack()
  root.mainloop()

BusinessCardParser(f)

#if needed this outputs to the console
def getName():
  return name
def getPhoneNumber():
  return tel
def getEmail():
  return email
