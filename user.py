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
    def __init__(self, userid, username, user_name, year, course):
        self.userid = userid
        self.username = username
        self.user_name = user_name
        self.year = year
        self.course = course
        self.dbh = DBHelper(db_name)

	# Saving new user values
    def save_user(self):
        self.dbh.newUser(self)

	# Updating new user values
    def update_user(self, what, update, uid):
        self.dbh.updateUser(what, update, uid)

	# Check if user exists
    def check(self):
        return self.dbh.do_check(self.userid)

	# Get name of the user
    def getName(self):
        return self.dbh.getName(self.userid)

	# Get username of the user
    def getUname(self):
        return self.dbh.getUname(self.userid)

	# Get id of the user
    def getID(self):
        return self.dbh.getID(self.userid)

	# Get the year of the user
    def getYear(self):
        return self.dbh.getYear(self.userid)

	# Get the course of the user
    def getCourseLetter(self):
        return self.dbh.getCourseLetter(self.userid)
