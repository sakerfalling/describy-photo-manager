import sqlite3

class PhotoDB:
	def __init__(self, db_file): 
		self.connect_to_db(db_file)
		
		self.create_table()
		self.insert_photo("what", "world")
		self.update_photo("what", "gosh")

		self.complete()

	def connect_to_db(self, db_file):
		self.conn = sqlite3.connect(db_file)
		self.cur = self.conn.cursor()

	def create_table(self):
		self.cur.execute("CREATE TABLE sample (filename TEXT PRIMARY KEY, description TEXT)")

	def insert_photo(self, filename, description):
		self.cur.execute("INSERT INTO sample (filename, description) VALUES (\"" + filename + "\", \"" + description + "\")")

	def update_photo(self, filename, description):
		self.cur.execute("UPDATE sample SET description=\"" + description + "\" WHERE filename=\"" + filename + "\"")
		
	def complete(self):
		self.conn.commit()
		self.conn.close()
