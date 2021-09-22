import os
import shutil
import time

def getFileAge(path):

	
	ctime = os.stat(path).st_ctime


	return ctime


def program():
	path=input('Give The Name Of  The File In Which You Want To Delete Files Which are Stored More Than 30 Days : ')

	


	

	days = 2
	listFiles=os.listdir()

	
	seconds = time.time() - (days * 24 * 60 * 60)

	
	if os.path.exists(path):
		
	
		for subFolder, folders, files in os.walk(path):

		
			if seconds >= getFileAge(subFolder):

				
				removeFolder(subFolder)
			

			else:

				
				for folder in folders:

					
					folderPath = os.path.join(subFolder, folder)

				
					if seconds >= getFileAge(folderPath):

						
						removeFolder(folderPath)
						


				
				for file in files:

					
					filePath = os.path.join(subFolder, file)

					
					if seconds >= getFileAge(filePath):

						
						removeFile(filePath)
					
					else:
							if seconds >= getFileAge(path):
								removeFile(path)
				

	else:

	
		print(f'"{path}" is not found')
		

	


def removeFolder(path):

	
	if not shutil.rmtree(path):

	
		print(f"{path} is removed successfully")

	else:

	
		print(f"Unable to delete the {path}")



def removeFile(path):

	
	if not os.remove(path):

		
		print(f"{path} is removed successfully")

	else:

		
		print(f"Unable to delete the {path}")





program()