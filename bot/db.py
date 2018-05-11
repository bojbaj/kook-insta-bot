# import sqlite3
import MySQLdb
import ConfigParser
import json


def open_conn(self):
    config = ConfigParser.ConfigParser()
    config.readfp(open(r'./bot/config.inc'))
    host = config.get('DB', 'host')
    db_name = config.get('DB', 'db')
    user = config.get('DB', 'user')
    pwd = config.get('DB', 'pass')
    db = MySQLdb.connect(host=host, user=user, passwd=pwd,
                         db=db_name, charset='utf8')
    return db, db.cursor()


def set_insta_user(self, csrf, insta_id):
    db, db_c = open_conn(self)
    query = "INSERT INTO tInstaUsers(csrf, insta_id, active)\n"
    query += "VALUES('{0}', '{1}', 1)\n"
    query += "ON DUPLICATE KEY UPDATE csrf='{0}'\n"
    query = query.format(csrf, insta_id)
    db_c.execute(query)
    db.commit()
    db.close()


def set_insta_target(self, insta_id, target_hashtags, ignore_hashtags,
                     target_accounts, ignore_accounts):
    db, db_c = open_conn(self)
    query = "INSERT INTO tInstaTarget(insta_id, target_hashtags, ignore_hashtags, target_accounts, ignore_accounts)\n"
    query += "VALUES('{0}', N'{1}', N'{2}', N'{3}', N'{4}')\n"
    query += "ON DUPLICATE KEY UPDATE target_hashtags=N'{1}', ignore_hashtags=N'{2}', target_accounts=N'{3}', ignore_accounts=N'{4}' \n"
    query = query.format(insta_id, target_hashtags, ignore_hashtags,
                         target_accounts, ignore_accounts)
    db_c.execute(query)
    db.commit()
    db.close()


def set_insta_media_by_hashtag(self, target_hashtag, medias):
    db, db_c = open_conn(self)
    sp_name = 'spAddHashtag'
    args = (target_hashtag, "@Result")
    db_c.callproc(sp_name, args)
    query = "SELECT @_spAddHashtag_1;"
    db_c.execute(query)
    result = db_c.fetchall()
    hashtag_id = result[0][0]
    db.commit()

    for media in medias:
        query = "CALL spAddMediaByHashtag ({0}, '{1}', '{2}', '{3}', {4}, {5});\n"
        query = query.format(
            hashtag_id, media['node']['id'], media['node']['shortcode'], media['node']['owner']['id'], media['node']['taken_at_timestamp'], media['node']['is_video'])
        db_c.execute(query)
    db.commit()
    db.close()
