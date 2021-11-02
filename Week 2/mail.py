import os
from imbox import Imbox 
import traceback
import gridfs
import mysql.connector
import pymongo 

download_folder = "E:\Downloads"

mydb = mysql.connector.connect(
  host="localhost",
  user="root",            
  password="",
  database='maildb'
)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["mail_attach"]

if not os.path.isdir(download_folder):
    os.makedirs(download_folder, exist_ok=True)

with Imbox('imap.gmail.com',username='aryan.juyal@somaiya.edu',password='password',ssl=True,ssl_context=None,starttls=False) as imbox:
        inbox_messages_from = imbox.messages(sent_from='aryanjuyall12345@gmail.com',sent_to='aryan.juyal@somaiya.edu',unread=True)
        all_inbox_messages = imbox.messages()

        for uid, message in inbox_messages_from:
                    inbox_messages_from.mark_seen(uid)
                    message.body
                    mes=message.body['plain'][0]
                    mes=mes.split('\r\n\r\n')

                    company_name=mes[0]
                    m_date=mes[1].split(': ')[1]  
                    invoice_num=mes[2].split(': ')[1]
                    items=mes[3].split(': ')[1]
                    address=mes[4].split(': ')[1]

                    sql = "INSERT INTO Company VALUES (%s,%s,%s,%s,%s)"
                    val = (company_name,m_date,invoice_num,items,address)
                    mycursor = mydb.cursor()
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "record inserted.")

                    for idx, attachment in enumerate(message.attachments):
                      try:
                         att_fn = attachment.get('filename')
                         download_path = f"{download_folder}/{att_fn}"
                         print(download_path)

                         with open(download_path, "wb") as fp:
                              fp.write(attachment.get('content').read())

                         file_location=download_path 
                         file_data=open(file_location,"rb")
                         data=file_data.read()
                         fs=gridfs.GridFS(db)
                         fs.put(data,filename=att_fn)
                         print("upload to mongo done")

                      except:
                         print(traceback.print_exc())