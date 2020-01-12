import mysql.connector
from main import *
mdb=mysql.connector.connect(host='localhost',user='root',password='',database="main")
mycursor=mdb.cursor()
#def crpool():
#    i=1
#    global pool
#    pool=[]
#        pool.append(i)
#        i+=1
#    return
#crpool()
#def delind(index):
# global pool
 #if(index in pool):
 #    pool.remove(index)
 #return
#def addind(ind):
#    global pool
#    if(ind not in pool):
#        pool.insert(ind-1,ind)
#    return
#def delp(mail):
#    mycursor.execute("SELECT ind FROM mailt WHERE mail='"+mail+"'")
#    for row in mycursor.fetchone():
#        ind=row
#    addind(ind)
#    mycursor.execute("DELETE FROM mailt WHERE mail='"+mail+"'")
#    mdb.commit()
#    return
#for j in pool:
 #       if(index>j):
#            delind(j)
#            mycursor.execute("INSERT INTO mailt (ind,mail,name,ftype,sendlist,data) VALUES (%s,%s,%s,%s,%s,%s)",(j,mail,name,ftype,'',''))
#            mdb.commit()
#            return
#    delind(index)
#mycursor.execute("CREATE DATABASE main")
#mycursor.execute("SHOW TABLES")
#for tb in mycursor:
#    print(tb)
#for db in mycursor:
  #  print(db)
#mycursor.execute("CREATE TABLE formst (ftype INTEGER(10), type_name VARCHAR(1024))")
#tableadd="INSERT INTO sendlistt(ftype,sendlist) VALUES (%s, %s)"
#a=[(1, "1,2,3"),(2, "2,3,1"),(3, "3,1,2"),(4, "3,2,1")]
#mycursor.executemany(tableadd, a)
############################################## Убрать человека из рассылки #######################################################################################
#mycursor.execute("UPDATE mailt SET ind=0 WHERE mail='' AND ftype=1")
###############################################################################################################################################################
#mycursor.execute("CREATE TABLE textt (mindex INTEGER(255), msub VARCHAR(255), mtext VARCHAR(255))")
#mycursor.execute("DROP TABLE textt")
#i=0
#while i<6:
#    mycursor.execute("INSERT INTO textt (mindex,msub,mtext) VALUES (%s,%s,%s)",(i,'Subject'+str(i),'Text of message'+str(i)))
#    mdb.commit()
#    i+=1

#mycursor.execute("INSERT INTO formst (ftype,type_name) VALUES (%s,%s)",(3,'Type Name 3'))
#mycursor.execute("SELECT ftype FROM mailt WHERE mail='1mail@gmail.com' AND ind=2")
#for row in mycursor.fetchone():
#        ftype=row
#print(ftype)
#mycursor.execute("SELECT * FROM mailt WHERE mail='"+mail+"'")
################################################################################################################################################
mycursor.execute("DELETE FROM mailt WHERE ftype=4")
#################################################################################################################################
#mycursor.execute("DELETE FROM mailt WHERE name='User4'")
#mycursor.execute("SELECT ind FROM mailt ORDER BY ind DESC LIMIT 1")
#for row in mycursor.fetchone():
#    a=row
#print(a)
#addp("mail@gmail.com","User",0,"")
mdb.commit()
#addp(str(k)+"mail@gmail.com","User"+str(k),"",3)
#k=1
#while (k<11):
#    addp(str(k)+"mail@gmail.com","User"+str(k),"",3)
#    k+=1
#updsendlist("1mail@gmail.com")
