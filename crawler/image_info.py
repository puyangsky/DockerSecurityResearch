import MySQLdb
import MySQLdb.cursors
import requests
import threading
import time


IP         = "192.168.27.130"
DBUSERNAME = "root"
DBPWD      = "123"
DBNAME     = "dockerhub"
index      = 1
lock       = threading.Lock()
MAX        = 411548

class Task(threading.Thread):
	"""docstring for Task"""
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		global index, lock, MAX
		while index <= MAX:
			#time.sleep(1)
			if lock.acquire():
				print "+++The %d time..." % index
				name = getImageName(index)
				print "+++" + name
				if name == "#error#":
					print ">>>>>>error"
				getInfo(name)
				index += 1
				lock.release()

		


def getImageName(_index):
	global MAX
	if _index > MAX:
		return "-1"

	conn = MySQLdb.connect(IP, DBUSERNAME, DBPWD, DBNAME)
	cursor = conn.cursor()
	sql = "select url from image where id = %d" % _index
	cursor.execute(sql)
	url = cursor.fetchone()
	print url
	if url != None:
		url = str(url[0])
		items = url.split('/')
		if len(items) != 7:
			return "#error#"
		name = items[-3] + '/' + items[-2]
		return name
	else:
		print "+++None return"
		return "#error#"

	conn.close()

 

def getInfo(name):
	if name != "":
		url = "https://hub.docker.com/v2/search/repositories/?page=1&page_size=100&query=%s" % name
		conn = requests.get(url)
		info = conn.text
		info = str(info)
		print info


if __name__ == '__main__':
	#getInfo()
	#getImageName()
	for i in range(5):
		task = Task()
		task.start()