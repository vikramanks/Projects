#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Version 1 with cred file updation
import psycopg2
import csv
import sys
import os
import configparser
import smtplib 
import imghdr
from email.message import EmailMessage

config = configparser.ConfigParser()

config.read('E:\Test\Cred\\cred.cred')

hostname = config['Postegres_Connection']['hostname']
database = config['Postegres_Connection']['database']
username = config['Postegres_Connection']['username']
pwd      = config['Postegres_Connection']['pwd']
port_id  = config['Postegres_Connection']['port_id']

conn = psycopg2.connect(
                host     = hostname,
                dbname   = database,
                user     = username,
                password = pwd,
                port     = port_id)
    
cur=conn.cursor()
    
sql = '''SELECT bookid, facid, memid, DATE(starttime), slots 
         FROM cd.bookings;'''

csv_file_path = 'E:\Test\Weekly_Report.csv'

try:
    cur.execute(sql)
    rows = cur.fetchall()
finally:
    conn.close()

# Continue only if there are rows returned.
if rows:
    # New empty list called 'result'. This will be written to a file.
    result = list()

    # The row name is the first entry for each entity in the description tuple.
    column_names = list()
    for i in cur.description:
        column_names.append(i[0])

    result.append(column_names)
    for row in rows:
        result.append(row)

    # Write result to file.
    with open(csv_file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in result:
            csvwriter.writerow(row)
else:
    sys.exit("No rows found for query: {}".format(sql))
    

EMAIL_ADDRESS  = config['Email']['Emailid']
EMAIL_PASSWORD = config['Email']['Password']

contact = ['vikramandon5401@gmail.com','subbushaolin1306@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Weekly Report'
msg['From']    =  EMAIL_ADDRESS
msg['To']      =  contact
msg.set_content ('Please find the weekly report attached.')

with open ('E:\Test\\Weekly_Report.csv', 'rb') as f:
    file_data = f.read()
    #file_type = imghdr.what(f.name)
    file_name = 'Weekly_Report.csv'
    
msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename = file_name )
    
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    smtp.send_message(msg)


# In[ ]:




