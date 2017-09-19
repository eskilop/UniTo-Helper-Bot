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

    def get_cursor(self):
        return self.c

    def get_connection(self):
        return self.conn
