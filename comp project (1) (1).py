
## ----------------------------------------------------------NOTE----------------------------------------------------- ##
##                                                                                                                     ##
## PRINT_TABLE               --->  Prints Sql record in table format as it is printed in sql                           ##
## Database                  --->  Checks if connection is establised with sql                                         ##
## Create_Table              --->  Checks if table exists in database, if not creates table                            ##
## Organ_Donate_Record_Add   --->  Adds Given records to Organ_Donate table in sql                                     ##
## Organ_Request_Record_Add  --->  Adds Given records to Organ_Request table in sql                                    ##
## Get_Fields                --->  Gets SQL Field Names                                                                ##
## Print_Record_Table_Form   --->  Prints Sql records in table format. Table name should be passed as argument         ##
## Print_Record_Line_Form    --->  Prints Sql records line by line. Table name should be passed as argument            ##
##                                                                                                                     ##
## ------------------------------------------------------------------------------------------------------------------- ##

#save lives organ donation.
import mysql.connector
def PRINT_TABLE(RECORDS , FIELDS) :
    try :
        FILE_DATA = []
        for RECORDS_DATA in RECORDS :
            RECORD_DATA = []
            for Data in RECORDS_DATA :
                RECORD_DATA.append(str(Data))
            FILE_DATA.append(RECORD_DATA)
        FIELDS = FIELDS
        Dash_Length_List = []
        Flag_Count = 0
        for Data in FILE_DATA :
            FLAG_List = []
            for Table_Length in Data :
                if Flag_Count == 0:
                    Dash_Length_List.append(len(str(Table_Length)))
                FLAG_List.append(len(str(Table_Length)))
            Flag_Count += 1
            for Index in range(len(Data)) :
                if Dash_Length_List[Index] < FLAG_List[Index] :
                    Dash_Length_List[Index] = FLAG_List[Index]
        for Index in range(len(FIELDS)) :
            if Dash_Length_List[Index] < len(FIELDS[Index]) :
                Dash_Length_List[Index] = len(FIELDS[Index])
        Table_Dash = []
        Table_Length_Contents = '|'
        Table_Length_Fields = '|'
        Table_Length_Dash = '+'
        for Dash_Length in Dash_Length_List :
            Dash_Length += 4
            Table_Dash.append('-'*Dash_Length)
            Table_Length_Contents += '{:<'+str(Dash_Length)+'}|'
            Table_Length_Fields += '{:^'+str(Dash_Length)+'}|'
            Table_Length_Dash += '{:^'+str(Dash_Length)+'}+'
        print(Table_Length_Dash.format(*Table_Dash))
        print(Table_Length_Fields.format(*FIELDS))
        print(Table_Length_Dash.format(*Table_Dash))
        for Print_Data in FILE_DATA :
            print(Table_Length_Contents.format(*Print_Data))
        print(Table_Length_Dash.format(*Table_Dash))
    except :
        print('NO RECORDS FOUND!')
def Database():
    host = 'localhost'
    user = 'root'
    password = 'Sasi@2003'
    database = 'project'
    try :
        mydb = mysql.connector.connect(host = host , user = user , password = password)
        print('Connected successfully to database \'' + str(database) + '\' at \'' + str(host) + '\' with user \'' + str(user)+'\'')
        return mydb
    except :
        print('Failed to connect to database \'' + str(database) + '\' at \'' + str(host) + '\' with user \'' + str(user)+'\'')
        return False
def Create_Table() :
    mydb = Database()
    if mydb == False :
        print("problem")
    else :
        mycur = mydb.cursor()
        mycur.execute("create database IF NOT EXISTS project")
        mycur.execute("use project")
        print('Checking for table \'ORGAN_DONATE\'')
        mycur.execute("CREATE TABLE IF NOT EXISTS ORGAN_DONATE(NAME VARCHAR(100),PARENT_GARDIEN VARCHAR(100),ADDRESS VARCHAR(200),CITY_DISTRICT VARCHAR(100),STATE VARCHAR(100),PIN_CODE INT ,PHONE_NUMBER BIGINT,OCCUPATION VARCHAR(200),EMAIL_ID VARCHAR(100),DOB DATE,AGE INT(5),SEX VARCHAR(100),BLOOD_GROUP VARCHAR(100),EMERGENCY_CONTACT_NUMBER BIGINT,EMERGENCY_CONTACT_ADDRESS VARCHAR(200),IDENTITY_PROOF VARCHAR(100),ORGAN VARCHAR(100))")
        print('Checking for table \'ORGAN_REQUEST\'')
        mycur.execute("CREATE TABLE IF NOT EXISTS ORGAN_REQUEST(NAME VARCHAR(100),AGE INT(5),CONTACT_NUMBER BIGINT, EMAIL_ID VARCHAR(100), HOSPITAL_NAME VARCHAR(100),BRANCH VARCHAR(100),HOSPITAL_NUMBER INT ,CITY_DISTRICT VARCHAR(100),STATE VARCHAR(100),BLOOD_GROUP VARCHAR(100),ORGAN_REQUIRED VARCHAR(100))")
        print('MySQL requirements met successfully')
def Organ_Donate_Record_Add(NAME, PARENT_GARDIEN, ADDRESS, CITY_DISTRICT, STATE, PIN_CODE, PHONE_NUMBER, OCCUPATION, EMAIL_ID, DOB, AGE, SEX, BLOOD_GROUP, EMERGENCY_CONTACT_NUMBER, EMERGENCY_CONTACT_ADDRESS, IDENTITY_PROOF, ORGAN) :
    mydb = Database()
    if mydb == False :
        pass
    else :
        mycur = mydb.cursor()
        mycur.execute("use project")
        que="INSERT INTO ORGAN_DONATE VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(NAME, PARENT_GARDIEN, ADDRESS, CITY_DISTRICT, STATE, PIN_CODE, PHONE_NUMBER, OCCUPATION, EMAIL_ID, DOB, AGE, SEX, BLOOD_GROUP, EMERGENCY_CONTACT_NUMBER, EMERGENCY_CONTACT_ADDRESS, IDENTITY_PROOF, ORGAN)
        mycur.execute(que)
        mydb.commit()
        print('Record added successfully')
def Organ_Request_Record_Add(NAME, AGE, CONTACT_NUMBER, EMAIL_ID, HOSPITAL_NAME, BRANCH, HOSPITAL_NUMBER, CITY_DISTRICT, STATE, BLOOD_GROUP, ORGAN_REQUIRED):
    mydb = Database()
    if mydb == False :
        pass
    else :
        print("addup")
        mycur = mydb.cursor()
        mycur.execute("use project")
        que="INSERT INTO ORGAN_REQUEST VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(NAME, AGE, CONTACT_NUMBER, EMAIL_ID, HOSPITAL_NAME, BRANCH, HOSPITAL_NUMBER, CITY_DISTRICT, STATE, BLOOD_GROUP, ORGAN_REQUIRED)
        mycur.execute(que)
        mydb.commit()
        print('Record added successfully')
def Get_Fields(Table_Name):
    mydb = Database()
    if mydb == False :
        pass
    else :
        mycur = mydb.cursor()
        mycur.execute("use project")
        mycur.execute("DESC {}".format(Table_Name))
        Data = mycur.fetchall()
        Fields = []
        for Record in Data :
            Fields.append(Record[0])
        return Fields
def Print_Record_Table_Form(Table_Name):
    mydb = Database()
    if mydb == False :
        pass
    else :
        mycur = mydb.cursor()
        mycur.execute("use project")
        mycur.execute("SELECT * FROM {}".format(Table_Name))
        Data = mycur.fetchall()
        PRINT_TABLE(Data,Get_Fields(Table_Name))
def Print_Record_Line_Form(Table_Name):
    mydb = Database()
    if mydb == False :
        pass
    else :
        mycur = mydb.cursor()
        mycur.execute("use project")
        mycur.execute("SELECT * FROM {}".format(Table_Name))
        Data = mycur.fetchall()
        Fields = Get_Fields(Table_Name)
        Count = 1
        print ("here",Fields)
        print(Data)
        for i in Data:
            print(i)
def mobile(g):
    if len(str(g))!=10:
        print("please enter a valid mobile number")
        g = input("phone number: ")
        mobile(g)
def hpn(x):
    if len(x) != 8:
        print("")
    elif len(x) == 11:
        print("")
    else:
        print("please enter a valid number")
        x = input("hospital phone number: ")
        hpn(x)
def age(k):
    if k >= 18:
        print("you are elegible for organ donation ")
        print(" please verify your details again")
        
    else:
        print("you are too young to donate an organ")
        print("But we appreciate your will to be a part of organ donation")
def donate():
    print("To become an organ donar please enter the following details")
    a = input("name of donar(full name): ")
    b = input("name of any one parent or gardien: ")
    c = input("enter your current address: ")
    d = input("enter city/ district: ")
    e = input("enter state: ")
    f = input("enter pin code: ")
    g = input(" phone number: ")
    mobile(g)
    h = input("occupation: ")
    i = input("email id: ")
    j = input("date of birth: ")
    k = int(input("age: "))
    l = input("sex: ")
    m = input("blood group: ")
    n = input("emergency contact number: ")
    mobile(n)
    o = input("emergency contact address: ")
    print("choose any one of the identity proofs'\n' 1.PAN card '\n' 2.voter id '\n' 3.Driving license '\n' 4.Aadhae card")
    p = input("enter identity proof: ")
    q = input("enter the above identity proof number: ")
    print("choose the organ u would like to donate : \n'all organs' \n 'corneas(eyes)'\n' kidneys'\n' heart'\n' lungs'\n' liver'\n' pancreas '\n 'small intestine'\n' skin'. ")
    r = input("enter the organ you would like to donate: ")
    age(k)
    print("hope you have verified your details \n")
    print(" IT TAKES A GREAT HEART TO BE AN ORGAN DONOR. \n WE SOLEMNLY WISH YOU GOOD")
    tname='ORGAN_DONATE'
    Organ_Donate_Record_Add(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,q,r)    
    Print_Record_Table_Form(tname)
def req():
    print(" please enter the following details of the patient correctly so that we can help ")
    tname="ORGAN_REQUEST"
    a = input("name of the person who requires an organ: ")
    b = int(input("age: "))
    c = input("contact number: ")
    mobile(c)
    d = input("email.id: ")
    h = input("name of the hospital: ")
    i = input("branch: ")
    j = input("hospital phone nnumber: ")
    hpn(j)
    e = input("city/district where the patient is admitted: ")
    f = input("state: ")
    g = input("blood group: ")
    k = input("please enter the name of the organ required: ")
    print("The patient details will be verified with hospital", ' \n ', "we will try our best to find a perfect donar and let you know please give us some time")
    Organ_Request_Record_Add(a,b,c,d,h,i,j,e,f,g,k)
    Print_Record_Table_Form(tname)
print("Hey!!! Welcome to SAVE LIVES ORGAN DONATION")
print("enter 'D' if you would like be an organ donar")
print("enter 'R' if there is an organ requirement")
#Database()
Create_Table()
t = input(" enter 'D'or 'R' :")
t=t.upper()
if t == 'D':
   donate()
elif t == 'R':
    req()
else:
    print("selection invalid \n please select D or R")
