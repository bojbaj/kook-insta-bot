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

    def set_insta_user(self, csrf, insta_id):
        db, db_c = self.open()
        query = "INSERT INTO tInstaUsers(csrf, insta_id, active)\n"
        query += "VALUES('{0}', '{1}', 1)\n"
        query += "ON DUPLICATE KEY UPDATE csrf='{0}'\n"
        query = query.format(csrf, insta_id)
        db_c.execute(query)
        db.commit()
        db.close()

    def set_insta_target(self, insta_id, target_hashtags, ignore_hashtags,
                       target_accounts, ignore_accounts):
        db, db_c = self.open()
        query = "INSERT INTO tInstaTarget(insta_id, target_hashtags, ignore_hashtags, target_accounts, ignore_accounts)\n"
        query += "VALUES('{0}', N'{1}', N'{2}', N'{3}', N'{4}')\n"
        query += "ON DUPLICATE KEY UPDATE target_hashtags=N'{1}', ignore_hashtags=N'{2}', target_accounts=N'{3}', ignore_accounts=N'{4}' \n"
        query = query.format(insta_id, target_hashtags, ignore_hashtags,
                             target_accounts, ignore_accounts)
        db_c.execute(query)
        db.commit()
        db.close()
