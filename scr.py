from main import *
'''Добавление в базу'''
i = 1
mycursor.execute("SELECT ftype FROM formst ORDER BY ftype DESC LIMIT 1")
for row in mycursor.fetchone():
    a = row
while i <= a:
    with open("Type Name "+str(i)+".csv", encoding='utf-8') as file:
        mycursor.execute("SELECT ftype FROM formst WHERE type_name='"+file.name+"'")
        for row in mycursor.fetchone():
            ftype=row
        csv_check(file,ftype)
    i+=1
'''Обновление базы'''
mycursor.execute("SELECT ind FROM mailt ORDER BY ind DESC LIMIT 1")
for row in mycursor.fetchone():
    a=row
while(index<=a):
    try:
        mycursor.execute("SELECT data FROM mailt WHERE ind="+str(index))
        for row in mycursor.fetchone():
            data=row
        data=datetime.datetime.strptime(data,'%Y-%m-%d %H:%M:%S')
        data=datetime.datetime.now()-data
        if(data.days>=7):
            mycursor.execute("SELECT mail FROM mailt WHERE ind="+str(index))
            for row in mycursor.fetchone():
                b=row
            updsendlist(b,index)
        '''
        mycursor.execute("SELECT mail FROM mailt WHERE ind="+str(index))
        for row in mycursor.fetchone():
            b=row
        updsendlist(b,index)
        index+=1'''
    except:
        print('Some error in update')
        index+=1
