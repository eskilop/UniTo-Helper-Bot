#!/usr/bin/python3

'''
   Copyright 2016-2017 Eskilop

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''

import sqlite3

class DBHelper:

	# Builder
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname, check_same_thread = False)
        self.c = self.conn.cursor()
        
    # Inline query the db
    def query(self, query, args):
        self.c.execute(query, args)
        self.conn.commit()
        data = self.c.fetchall()
        return data
        
    # Get count of the rows (number of users)
    def count(self):
        self.c.execute("SELECT COUNT(*) FROM data")
        self.conn.commit()
        data = self.c.fetchone()[0]
        return data

	# Checks if user exists
    def do_check(self, userid):
        self.c.execute('SELECT userid FROM data WHERE userid=?', (userid,))
        self.conn.commit()
        data = self.c.fetchone()
        if data is None:
            return False
        elif len(data) > 0:
            return True
        else:
        	# How is this even possible?
            print("WTF")

	# Gets user name
    def getName(self, userid):
        self.c.execute('SELECT name FROM data WHERE userid=?', (userid,))
        self.conn.commit()
        warn = self.c.fetchone()[0]
        print(warn)
        return str(warn)

	# Gets user year
    def getYear(self, userid):
        self.c.execute('SELECT year FROM data WHERE userid=?', (userid,))
        self.conn.commit()
        t = self.c.fetchone()
        if(t != None):
            return int(t[0])
        else:
            return 6

	# Gets user id
    def getID(self, userid):
        self.c.execute('SELECT userid FROM data WHERE userid=?', (userid,))
        self.conn.commit()
        return str(self.c.fetchone()[0])

	# Gets username
    def getUname(self, userid):
        self.c.execute('SELECT year FROM data WHERE userid=?', (userid,))
        self.conn.commit()
        return str(self.c.fetchone()[0])

	# Gets course
    def getCourseLetter(self, userid):
        self.c.execute('SELECT course FROM data WHERE userid=?', (userid,))
        self.conn.commit()
        return str(self.c.fetchone()[0])

	# Inserts new user
    def newUser(self, user):
        self.c.execute("INSERT INTO data VALUES (?, ?, ?, ?, ?)", (user.userid, user.username, user.user_name, user.year, user.course))
        self.conn.commit()
        print("A new user was saved")

	# Updates an user
    def updateUser(self, what, update, userid):
        self.c.execute("UPDATE data SET {} =? WHERE userid=?".format(what), (update, userid))
        self.conn.commit()
        print("An user has been updated")
