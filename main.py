import mysql.connector
import csv
import datetime
from emailSender import *

mdb=mysql.connector.connect(
    host='localhost',
    user='',
    password='',
    database="u",
    charset='utf8')
mycursor=mdb.cursor()
index=1
def addp(mail,name,data,ftype):
    try:
        mycursor.execute("SELECT ind FROM mailt ORDER BY ind DESC LIMIT 1")
        for row in mycursor.fetchone():
            index=row+1
    except:
        print('no data in table')
        index=1
    mycursor.execute("INSERT INTO mailt (ind,mail,name,ftype,sendlist,data) VALUES (%s,%s,%s,%s,%s,%s)",(index,mail,name,ftype,'',data))
    mdb.commit()
    index+=1
    return
def updsendlist(mail,ind):
    mycursor.execute("SELECT ftype FROM mailt WHERE mail='"+mail+"' AND ind="+str(ind))
    for row in mycursor.fetchone():
        ftype=row
    mycursor.execute("SELECT sendlist FROM mailt WHERE mail='"+mail+"' AND ind="+str(ind))
    for row in mycursor.fetchone():
        sendlist=row
    mycursor.execute("SELECT sendlist FROM sendlistt WHERE ftype="+str(ftype))
    for row in mycursor.fetchone():
        a=row
    mycursor.execute("SELECT name FROM mailt WHERE mail='"+mail+"' AND ind="+str(ind))
    for row in mycursor.fetchone():
        name=row
    if(len(a)==len(sendlist)):
        return
    if(sendlist==''):
        b=''
        for i in a:
            if(i!=';'):
                b+=i
            else:
                break
        sendlist=sendlist+b
    else:
        b=''
        c=a[len(sendlist)+1:]
        for i in c:
            if(i!=';'):
                b+=i
            else:
                break
        sendlist=sendlist+';'+b
    mycursor.execute("SELECT msub FROM textt WHERE mindex="+b)
    for row in mycursor.fetchone():
        sub=row
    '''
    print(name,mail,sub,int(b))
    mycursor.execute("UPDATE mailt SET data='"+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"' WHERE mail='"+mail+"' AND ind="+str(ind))
    mycursor.execute("UPDATE mailt SET sendlist='"+str(sendlist)+"' WHERE mail='"+mail+"' AND ind="+str(ind))
    mdb.commit()
    '''
    error=emailSenderFunction(name,mail,sub,int(b))
    if(error==0):
        mycursor.execute("UPDATE mailt SET data='"+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"' WHERE mail='"+mail+"' AND ind="+str(ind))
        mycursor.execute("UPDATE mailt SET sendlist='"+str(sendlist)+"' WHERE mail='"+mail+"' AND ind="+str(ind))
        mdb.commit()
    else:
        mycursor.execute("INSERT INTO errort (mail,error,data) VALUES (%s,%s,%s)",(str(mail),str(error),(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))))
        mdb.commit()
    return
def csv_check(file,ftype):
    try:
        for line in csv.DictReader(file):
            line["Submitted"]=line["Submitted"][:19]
            mycursor.execute("SELECT ind FROM mailt WHERE mail='"+line["your-email"]+"' AND ftype="+str(ftype))
            if(mycursor.fetchone()==None):
                addp(line["your-email"],line["your-name"],line["Submitted"],str(ftype))
    except:
        print('Some error in csv_check, Maybe person already in this ftype')
        return