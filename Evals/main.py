import sqlite3

mydb = sqlite3.connect("record.db")
cursor_obj = mydb.cursor()

name = "Student"
roll = 2

if name == "Student":
    cursor_obj.execute(
        "select * from table where roll == %s && date >= CURDATE() order by date" % roll)
    companies = cursor_obj.fetchall()

name = "TA"
number_of_students = 2
if name == "TA":
    no = number_of_students
    roll_nos = ["roll numbers of Students"]
    starting_time = "0"
    ending_time = "0"
    duration = 10 # In min

import pandas as pd

l = (pd.DataFrame(columns=['NULL'],
                  index=pd.date_range('2016-09-02T17:30:00Z', '2016-09-04T21:00:00Z',
                                      freq='15T'))
     .between_time('07:00', '21:00')
     .index.strftime('%Y-%m-%dT%H:%M:%SZ')
     .tolist()
     )
print(l)