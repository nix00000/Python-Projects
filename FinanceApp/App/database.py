import sqlite3
import csv
import sys



conn = sqlite3.connect('comp.db')
c = conn.cursor()

# c.execute("""
#     CREATE TABLE companies (
#     inds text,
#     name text)
# """)
# data = open("comapniesBS.csv", "r")
# normal = []
# for d in data.readlines():
#     p,r = d.split("\n")
#     normal.append(p)
# print(normal)
#
# for n in normal:
#     a,b = n.split('/')
#     print(a)
#     c.execute("""INSERT INTO companies(inds, name)
#                VALUES (?,?);""", (a, b))


c.execute("""SELECT inds FROM companies WHERE name = 'Accenture plc' """)
data = c.fetchone()
print(data[0])

conn.commit()
conn.close()