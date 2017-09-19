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

from dbhelper import DBHelper
from options import *

class User:

	# builder
    def __init__(self, userid, username, user_name):
        self.userid = userid
        self.username = username
        self.user_name = user_name

        # database utils
        self.dbh = DBHelper(db_name)

	# Saving new user values
    def save(self):
        self.dbh.get_cursor().execute("INSERT INTO data VALUES (?, ?, ?, ?, ?)", (self.userid, self.username, self.user_name, self.year, self.course))
        self.dbh.get_connection().commit()
        print("user {} was saved".format(str(self.userid)))

	# Updating new user values
    def update(self, what, update):
        self.dbh.get_cursor().execute("UPDATE data SET {} =? WHERE userid=?".format(what), (update, self.userid))
        self.dbh.get_connection().commit()
        print("user {} has been updated".format(str(self.userid)))

	# Check if user exists
    def exists(self):
        self.dbh.get_cursor().execute('SELECT userid FROM data WHERE userid=?', (self.userid,))
        self.dbh.get_connection().commit()
        data = self.dbh.get_cursor().fetchone()
        if data is None:
            return False
        elif len(data) > 0:
            return True
        else:
        	return False

	# Get name of the user
    def get_name(self):
        self.dbh.get_cursor().execute('SELECT name FROM data WHERE userid=?', (self.userid,))
        self.dbh.get_connection().commit()
        warn = self.dbh.get_cursor().fetchone()[0]
        print(warn)
        return str(warn)

	# Get username of the user
    def get_uname(self):
        self.dbh.get_cursor().execute('SELECT year FROM data WHERE userid=?', (self.userid,))
        self.dbh.get_connection().commit()
        return str(self.dbh.get_cursor().fetchone()[0])

	# Get id of the user
    def get_id(self):
        self.dbh.get_cursor().execute('SELECT userid FROM data WHERE userid=?', (self.userid,))
        self.dbh.get_connection().commit()
        return str(self.dbh.get_cursor().fetchone()[0])

	# Get the year of the user
    def get_year(self):
        self.dbh.get_cursor().execute('SELECT year FROM data WHERE userid=?', (self.userid,))
        self.dbh.get_connection().commit()
        t = self.dbh.get_cursor().fetchone()
        if(t != None):
            return int(t[0])
        else:
            return 6

	# Get the course of the user
    def get_course(self):
        self.dbh.get_cursor().execute('SELECT course FROM data WHERE userid=?', (self.userid,))
        self.dbh.get_connection().commit()
        return str(self.dbh.get_cursor().fetchone()[0])

    def set_year(self, year):
        self.dbh.get_cursor().execute('UPDATE user SET year={} WHERE userid=?'.format(year), (self.userid))
        self.dbh.get_connection().commit()
        # todo: check that update has completed

    def set_course(self, course):
        self.dbh.get_cursor().execute('UPDATE user SET course={} WHERE userid=?'.format(course), (self.userid))
        self.dbh.get_connection().commit()
        # todo: check that update has completed
