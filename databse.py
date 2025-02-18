import sqlite3 as s3


path="database.db"

#default function
def create_default():
    file=s3.connect(path)
    f=file.cursor()
    query1="create table if not exists registration([name]text,[mail]text,[password]text,[contact]text)"
    query2="create table if not exists projects([name]text,[domain]text,[teamsize]int,[techused]text,[breif]text,[user]text)"
    f.execute(query1)
    f.execute(query2)
    file.commit()
    file.close()
#user functions
def check_user(mail,password=0,login=False):
    file=s3.connect(path)
    f=file.cursor()
    query=f"""select mail,password from registration where mail='{mail}'"""
    f.execute(query)
    data=f.fetchall()
    file.commit()
    file.close()
    if not login and len(data)==0:
        return True
    elif login and len(data)!=0:
        if password ==data[0][1]:
            return True
    else:
        return False 

def add_user(data):
    name=data["name"]
    mail=data["mail"]
    password=data["password"]
    contact=data["contact"]
    file=s3.connect(path)
    f=file.cursor()
    verify=check_user(mail)
    if not verify:
        return False
    else:
        query=f"""insert into registration values("{name}","{mail}","{password}","{contact}")"""
        f.execute(query)
        file.commit()
        file.close()
        return True

#projects functions
def check_project(name):
    file=s3.connect(path)
    f=file.cursor()
    query=f"select * from projects where name='{name}'"
    f.execute(query)
    data=f.fetchall()
    file.commit()
    file.close()
    if len(data)==0:
        return True
    else:
        return False

def add_project(data):
    file=s3.connect(path)
    f=file.cursor()
    check=check_project(data[0])
    if not check:
        return False
    try:
        query=f"""insert into projects values('{data[0]}','{data[1]}','{data[2]}','{data[3]}','{data[4]}','{data[5]}')"""
        f.execute(query)
        file.commit()
        file.close()
        return True
    except:
        return False
    
def get_projects(mail,name=None,user=True):
    file=s3.connect(path)
    f=file.cursor()
    if user:
        if name is not None:
            query=f"""select * from projects where name='{name}'"""
        else:
            query=f"select * from projects where user ='{mail}'"
    
    else:
        query=f"select * from projects where user !='{mail}'"    
    f.execute(query)
    data=f.fetchall()
    file.commit()
    file.close()
    return data


def delete_project(name):
    file=s3.connect(path)
    f=file.cursor()
    query=f"delete from projects where name='{name}'"
    f.execute(query)
    file.commit()
    file.close()
    return True

def update_project(data):
    file=s3.connect(path)
    f=file.cursor()
    query=f"update projects set domain='{data[1]}',teamsize='{data[2]}',gitlink='{data[3]}', breif='{data[4]}' where name='{data[0]}'"
    f.execute(query)
    file.commit()
    file.close()
    return True


#update_project(["teammates","hfdh","3","hgfdhddfe","hello"])

#print(get_projects("yateeshec013@gmail.com",user=False))
#create_default()u
#print(add_user("hello","hello@gmail.com","123","8639661731"))
#print(check_user("hello@gmail.com",login=True))
#print(add_project(["p1","ec",3,"skills","hghdrtd","user"]))
#add_user("p1","yateeshec013@gmail.com","123","565987236")
#print(check_user("yateeshec013@gmail.com",login=True))
#print(get_projects("yateeshec013@gmail.com",name="p1"))