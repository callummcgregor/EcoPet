import login
import childPet
import GUI


if __name__ == "__main__":
	data = login.getUserData()			#loads user data
	child = childPet.ChildPet(*data)	#creates new instance of childPet with user data as attributes
	root = GUI.Tk()
	root.title(str(child.childName + " & " + child.petName))
	menu = GUI.Menu(root, child)
	menu.grid()
	GUI.mainloop()