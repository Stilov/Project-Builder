#imports
import os

#functions

#creates a folder and takes the path of the folder as an argument
def dirMaker(path):
	os.makedirs(projectPath + path)

#Creates a file and takes the path of the file as an argument
def fileMaker(path):
	open(projectPath + path,"w")



#used to check if the directory already exists
usableName = 0

#Loops until a valid project name is given
while usableName == 0:

	#The name of the project
	projectName = input("What do you want to name your project?\n")

	#The path of the project
	projectPath = "./" + projectName + "/"

	#Checks if the folder already exists and creates it if it doesn't and ends the loop
	if os.path.exists(projectPath):
		print("A folder named", projectName, "already exists in this directory, please choose a new name for your project.\n")
	else:
		os.makedirs(projectPath)
		usableName = 1
#Types of projects:
#web = HTML/CSS/JS
#more coming soon

y = 0
while y == 0:
	#The user chooses what kind of project to create
	projectType = input("What kind of project do you want to create? (Check README)\n")

	#Coverts answer to lowercase
	projectType = projectType.lower()
	

	#Checks if the type is valid, more types will be added
	if projectType == "web":

		#creates files and folders
		
        #Creating folders
		dirMaker("JS")
		dirMaker("CSS")
		dirMaker("Res")

		#Creating files
		fileMaker("index.html")
		fileMaker("JS/main.js")
		fileMaker("CSS/style.css")
		fileMaker("Res/delete.me")
		y = 1


	#elif projectType == "python":

	else:
		print("That kind of project is not available, check the README and github page for more info. \n Please choose another project type.")
		continue
		

