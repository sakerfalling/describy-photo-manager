import os

class Folder:
	def __init__(self, folder):
		self.folder = folder

	def get_all_pics(self): 
		contents = os.listdir("./" + self.folder)

		count = 1
		for content in contents:
			print str(count) + ":" + content
			count += 1
	
	def get_described_pics(): pass

	def get_undescribed_pics(): pass
