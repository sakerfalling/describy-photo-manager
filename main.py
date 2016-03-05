import os
import flask

from Database import PhotoDB
from Folder import Folder

def main(): pass
	# db = PhotoDB("sample.sqlite")
	#folder_choice = get_folder_choice()
	#folder = Folder(folder_choice)	
	#folder.get_all_pics()

def get_folder_choice():
	subdirs = []

	folder_contents = os.listdir(".")

	for content in folder_contents:
		if os.path.isdir(content):
			subdirs.append(content)

	count = 0
	for subdir in subdirs:
		print str(count) + ":" + subdir
		count += 1

	print "Enter folder choice: "
	choice = raw_input()
	print "You chose " + subdirs[int(choice)]

	return subdirs[int(choice)]

if __name__ == "__main__":
	main()
