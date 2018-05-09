# import sqlite3
import MySQLdb
import ConfigParser

class DB:
    def __init__(self):
        self.config = ''

    def open(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open(r'./bot/config.inc'))
        host = config.get('DB', 'host')
        db_name = config.get('DB', 'db')
        user = config.get('DB', 'user')
        pwd = config.get('DB', 'pass')
        db = MySQLdb.connect(host=host, user=user, passwd=pwd, db=db_name)
        return db, db.cursor()

    def setInstaUser(self, csrf, insta_id):
        db, db_c = self.open()
        query = "INSERT INTO tInstaUsers(csrf, insta_id, active)\n"
        query += "VALUES('{0}', '{1}', 1)\n"
        query += "ON DUPLICATE KEY UPDATE csrf='{0}'\n"
        query = query.format(csrf, insta_id)
        r = db_c.execute(query)
        db.commit()
        db.close()
