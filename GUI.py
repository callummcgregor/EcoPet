from tkinter import *
from threading import Thread
from time import sleep
import math


class Menu(Frame):
	def __init__(self, master, child):
		super(Menu, self).__init__(master)
		self.grid()
		self.createWidgets(master, child)


	def update(self, child):
		"""
		Threading function to update stats periodically
		"""
		while 1:
			try:
				sleep(0.1)
				child.updateStats()
				self.updateLabels(child, labels)
			except:
				pass


	def updateDialogue(self, child, action):
		"""
		Updates the dialogue label
		"""
		label.config(text=child.doAction(action))


	def updateLabels(self, child, labels):
		"""
		Updates the stats labels
		"""
		labels[0].config(text="Energy: "+str(int(child.energy)))
		labels[1].config(text="Hunger: "+str(int((child.hunger))))
		labels[2].config(text="Hygiene: "+str(math.ceil(child.hygiene)))
		labels[3].config(text="Sleep: "+str(math.ceil(child.sleep)))
		labels[4].config(text="Last Time: "+str(int(child.lastTime)))
		labels[5].config(text="Points: "+str(child.points))


	def createWidgets(self, master, child):
		"""
		Creates main root and frame and populates with widgets
		Globals are used so page can be loaded
			multiple times
		"""
		global labels, label, entry
		#Sets stats on the labels
		Ltext=("Energy: "+str(int(child.energy)),"Hunger: "+str(int(child.hunger)),
			   "Hygiene: "+str(math.ceil(child.hygiene)),"Sleep: "+str(math.ceil(child.sleep)),
			   "Last Time: "+str(int(child.lastTime)),"Points: "+str(child.points), "Welcome back!")
		Btext=("Feed","Wash","Sleep","Play","Logout","Recycle","Shop","Submit")
		#Sets grid positions for labels and buttons
		Lrow=(0,1,2,3,4,3,4)
		Lcolumn=(0,0,0,0,0,3,1)
		Brow=(6,6,6,6,0,1,2,5)
		Bcolumn=(0,1,2,3,3,3,3,3)
		#Sets up commands for buttons
		commands=(lambda:self.updateDialogue(child, "feed"), lambda:self.updateDialogue(child, "wash"),
				  lambda:self.updateDialogue(child, "sleep"), lambda:self.updateDialogue(child, "play"),
				  logout, recycling, shop, submit)
		#Defines the labels
		labels=[]
		for i in range(len(Ltext)):
			label=Label(self,text=Ltext[i],width=20,anchor="c")
			label.grid(row=Lrow[i],column=Lcolumn[i],padx=5,pady=5)
			labels.append(label)
			if i == 6:
				label.config(anchor="w")
				label.grid(columnspan=2)
				labels.remove(label)
		#Defines the buttons
		for i in range(len(Btext)):
			button=Button(self,text=Btext[i],width=10,anchor="c",command=commands[i])
			button.grid(row=Brow[i],column=Bcolumn[i],padx=5,pady=5,ipadx=5)
		#Defines the entry
		entry=Entry(self)
		entry.grid(row=5,column=1,columnspan=2)
		entry.bind("<Return>", submit)
		#Starts thread for updates
		t=Thread(None, self.update(child))
		t.start()


def logout():
	pass

def recycling():
	pass

def shop():
	pass

def submit():
	pass