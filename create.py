from flaskext.mysql import MySQL

def checkOrg (shortname,mysql):
    connection = mysql.connect()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM organizations WHERE shortname=%s",(shortname))
    count = cursor.fetchone()[0];
    print (count)
    if count >0:
        print ("Another entry found...")
        return True
    else:
        return False

def checkMem (shortname,mysql):
    connection = mysql.connect()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM members WHERE shortname=%s",(shortname))
    count = cursor.fetchone()[0];
    print (count)
    if count >0:
        print ("Another entry found...")
        return True
    else:
        return False


def createEntry(info,signuptype,mysql):
    if signuptype == "org":
        if checkOrg(str(info['shortname']),mysql):
            return False
    elif signuptype == "mem":
        if checkMem(str(info['shortname']),mysql):
            return False
    name = info['name']
    shortname = info['shortname']
    email = info['email']
    password = info['password']
    connection = mysql.connect()
    cursor = connection.cursor()
    if signuptype == "org":
        city = info['city']
        state = info['state']
        zipcode = info['zipcode']
        add_entry = ("INSERT INTO organizations"
            "(name,shortname,city,state,zipcode,email,password)"
            "VALUES (%s,%s,%s,%s,%s,%s,%s)")
        data_entry = (name,shortname,city,state,zipcode,email,password)
    elif signuptype == "mem":
        cursor.execute("SELECT orgid FROM organization WHERE shortname == %s",info['school'])
        s_id = cursor.fetchone()[0]
        add_entry = ("INSERT INTO members"
            "(name,shortname,school,email,password)"
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
        data_entry = (name,shortname,s_id,email,password)
    else:
        return False
    cursor.execute(add_entry,data_entry)
    connection.commit()
    cursor.close()
    connection.close()
    return True
