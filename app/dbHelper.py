import MySQLdb
import os

class dbHelper:
	"""This class queries data from a SQL DB using an input as the filter for the desired value in the DB."""
	def __init__(self):
		# Initialization
		self.db = ""
		self.sqlHost = os.environ['HOST']
		self.sqlUser = os.environ['USER']
		self.sqlPass = os.environ['PASS']
		
		self.sqlDatabase = "Products"
		self.sqlTable = "Products"
		self.sqlColumn = "Name"

	def initConnection(self):
		try:
			self.db = MySQLdb.connect(host=self.sqlHost, user=self.sqlUser, passwd=self.sqlPass, db=self.sqlDatabase)
			cur = self.db.cursor()
			cur.execute("SELECT VERSION()")
			results = cur.fetchone()
			# Check if anything at all is returned
			if results:
				print("SQL Version: " + str(results) + "Connection is Valid!!")
				return True
			else:
				print("Things were not returned. Connection Valid?")
				return False
		except MySQLdb.Error:
			print("ERROR IN CONNECTION")
			return False

	def queryDB(self, filter=''):
			cur = self.db.cursor()
			sql = "SELECT * FROM " + self.sqlTable + " WHERE " + self.sqlColumn + " LIKE '%" + filter + "%';"
			print(sql)
			try: 
				cur.execute(sql)
				data = cur.fetchall()
				cur.close
				return data
			except: 
				print("Failed to return values from DB")
				cur.close

	def formatData(self, data):
			prettyData = []
			for item in data:
				prettyData.append(item[0])
			return prettyData



