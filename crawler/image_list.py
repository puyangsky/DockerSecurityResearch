import MySQLdb
import MySQLdb.cursors
from hashlib import md5

from MySQLdb.cursors import DictCursor
from DBUtils.PooledDB import PooledDB
import Config


class Mysql(object):
    __pool = None

    def __init__(self):

        self._conn = Mysql.__getConn()
        self._cursor = self._conn.cursor()

    @staticmethod
    def __getConn():

        if Mysql.__pool is None:
            __pool = PooledDB(creator=MySQLdb, mincached=1, maxcached=20,
                              host=Config.DBHOST, port=Config.DBPORT, user=Config.DBUSER, passwd=Config.DBPWD,
                              db=Config.DBNAME, use_unicode=False, charset=Config.DBCHAR, cursorclass=DictCursor)
        return __pool.connection()

    def getAll(self, sql, param=None):

        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchall()
        else:
            result = False
        return result

    def getOne(self, sql, param=None):

        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchone()
        else:
            result = False
        return result

    def getMany(self, sql, num, param=None):

        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchmany(num)
        else:
            result = False
        return result

    def insertOne(self, sql):

        self._cursor.execute(sql)
        return self.__getInsertId()

    def insertMany(self, sql, values):
        self._cursor.executemany(sql, values)

    #		except Exception,e:
    #           print e

    def __getInsertId(self):

        self._cursor.execute("SELECT @@IDENTITY AS id")
        result = self._cursor.fetchall()
        return result[0]['id']

    def __query(self, sql, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        return count

    def update(self, sql, param=None):

        return self.__query(sql, param)

    def delete(self, sql, param=None):

        return self.__query(sql, param)

    def begin(self):

        self._conn.autocommit(0)

    def end(self, option='commit'):

        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()

    def dispose(self, isEnd=1):

        if isEnd == 1:
            self.end('commit')
        else:
            self.end('rollback');
        self._cursor.close()
        self._conn.close()


def get_hash(string):
    return md5(string).hexdigest()


"""
def insert(name, url, author):
	hash_url = get_hash(url)
	db = MySQLdb.connect("192.168.200.125","root","123","docker")
	conn = db.cursor()
	conn.execute("select 1 from image WHERE hash = %r", hash_url)
	ret = conn.fetchone()
	print ret
	if ret != "":
		sql = "insert into image(name, url, hash, class, author) values('%s','%s','%s','%s','%s')" % (name, url, hash_url, "", author)
		print sql
		try:
			conn.execute(sql)
			db.commit()
		except Exception, e:
			print e
			db.rollback()
"""


def read():
    c = 1
    args = []

    db = MySQLdb.connect("192.168.27.130", "root", "123", "dockerhub")
    print "+++[connect db]"
    conn = db.cursor()
    for i in range(16, 26):
        filename = "sitemap_hub_" + str(i) + ".txt"
        print filename
        for line in open(filename, 'r'):
            if "com/r/" in line:
                c += 1
                # print line

                line = line.strip("\n")
                url = line
                hash_url = get_hash(url)
                items = line.split("/")
                if len(items) != 7:
                    continue
                author = items[-3]
                name = items[-2]
                # print author, name
                # insert(image_name, url, author)
                # pre_sql = "select 1 from image WHERE hash = %r" % hash_url
                # is_exist = mysql.getOne(pre_sql)
                if len(args) < 10:
                    temp_tuple = "('%s','%s','%s','%s','%s')" % (name, url, hash_url, "", author)
                    # print temp_tuple
                    # time.sleep(2)
                    args.append(temp_tuple)
                # sql = "insert into image(name, url, hash, class, author) values('%s','%s','%s','%s','%s')" % (name, url, hash_url, "", author)
                # id = mysql.insertOne(sql)
                # print "insert %d" % id
                else:
                    sql = "insert into image(name, url, hash, class, author) values " + ",".join(args)
                    # print sql
                    # time.sleep(0.1)
                    try:
                        conn.execute(sql)
                        db.commit()
                        # print id
                        print "[*] insert %d entries!" % len(args)
                        # clear
                        args = []
                    except Exception, e:
                        print e

        if args != []:
            sql = "insert into image(name, url, hash, class, author) values " + ",".join(args)
            try:
                conn.execute(sql)
                db.commit()
                # print id
                print "[*] insert %d entries!" % len(args)
                # clear
                args = []
            except Exception, e:
                print e


if __name__ == "__main__":
    read()
'''
	sql = "insert into image(name, url, hash, class, author) values ('inception_serving','https://hub.docker.com/r/mihaizn/inception_serving/','b8e1ddc104eefe912258f6dbd584b1d4','','mihaizn'),('portainer.test','https://hub.docker.com/r/bitti/portainer.test/','21b8395a7c4dbe638ccb5f98a773e678','','bitti'),('vdsm-centos','https://hub.docker.com/r/ovirtorg/vdsm-centos/','2d2e43a184ee4b12866ba3d84b308d74','','ovirtorg'),('docker-centos6-ansible','https://hub.docker.com/r/bmacauley/docker-centos6-ansible/','d469f4aaeaa5b430ec2a54bd22e7babe','','bmacauley'),('nginx-301-https','https://hub.docker.com/r/chauffer/nginx-301-https/','12dee2e58da62e4686a8cd626a40fffd','','chauffer'),('vdsm-fedora','https://hub.docker.com/r/ovirtorg/vdsm-fedora/','a9b29f8048339421b13e9e2167c46024','','ovirtorg'),('cypress-cli','https://hub.docker.com/r/chauffer/cypress-cli/','6e23761d18786e0bc78b3006afe130f9','','chauffer'),('bitlbee-steam','https://hub.docker.com/r/chauffer/bitlbee-steam/','ee5a382d6454ff7854e654d7c9ca17b6','','chauffer'),('egg_move_db','https://hub.docker.com/r/patoconnor43/egg_move_db/','3c619f0618a4bb8ed49761094f128c31','','patoconnor43'),('elastic-proxy','https://hub.docker.com/r/netcomposer/elastic-proxy/','59b21b63bababbd6e00df3caa675fb49','','netcomposer')"
	conn = MySQLdb.connect("192.168.27.130","root","123","dockerhub")
	print "+++[connect db]"
	cursor = conn.cursor()
	cursor.execute(sql)
	conn.commit()
	print "+++[insert 10]"
	conn.close()

'''
