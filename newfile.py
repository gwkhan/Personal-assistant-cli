import datetime
import csv
import random
def getdate():
	a = datetime.datetime.today()
	b = a.strftime("%Y:%m:%d\n%H:%M")
	
	print(b)
class notes:
	def addnote(note):
		with open("notes.txt","a",newline = "\n") as file:
			file.write(note + "\n")
	def getnote():
		with open("notes.txt","r")as file:
			a = file.read()
			print(a)
class contact:
	def savecontact(contact):
		with open("contacts.csv","a",newline="")as file:
			write = csv.writer(file)
			write.writerow([contact])
	def showcontact():
		with open("contacts.csv","r") as file:
			read = csv.reader(file)
			for row in read:
				print(row)
def showmotivation():
	mq = ['I have never let my schooling interfere with my education.',
	"done than regret the things I haven't done." ,
	"Either you run the day, or the day runs you.",
	"He who conquers himself is the mightiest warrior."]
	a = random.choice(mq)
	print(a)
def calculator():
	while True:
		a = input("what you wanna do like ( x + y,x - y):")
		b = a.split()
		if a == "exit":
			break
		if len(b) != 3:
			print("invalid format")
			continue
		num1 , operator , num2 = b
		c = float(num1)
		d = float(num2)
		if operator == '+':
			print(f"{num1} + {num2} is = ", c + d)
		if operator == '-':
			print(f"{num1} - {num2} is = ", c - d)
		if operator == '*':
			print(f"{num1} * {num2} is = ", c * d)
		if operator == '/':
			print(f"{num1} / {num2} is = ", c / d)

print("========= Personal Assistant =========")
while True:
	ask = input("choose one:\n1. Show current date & time\n2. Add a quick note\n3. View all notes\n4. Calculator\n5. Save new contact\n6. Show contact list\n7. Show motivational quote\n8. Exit\nenter:- ")
	if ask =="1":
		getdate()
	elif ask =="2":
		a = input("enter your note: ")
		notes.addnote(a)
	elif ask =="3":
		notes.getnote()
	elif ask =="4":
		calculator()
	elif ask =="5":
		b = input("enter (name:contact): ")
		contact.savecontact(b)
	elif ask =="6":
		contact.showcontact()
	elif ask =="7":
		showmotivation()
	elif ask =="8":
		print("thanku")
		break
	else:
		print("wrong input")