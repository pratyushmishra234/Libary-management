import datetime
import random
import time
from tkinter import *
from tkinter import messagebox, ttk
import tkinter
import mysql.connector


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1540x800+0+0")

        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()



        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1540,height=400)

        Dataframeleft=LabelFrame(frame,text="Library Membership Information",fg="black",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        Dataframeleft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(Dataframeleft,text="Member Type",font=("arial",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(Dataframeleft,font=("arial",12,"bold"),width=27,textvariable=self.member_var,state="readonly")
        comMember['value']=("Admin Staf","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(Dataframeleft,text="PRN.No:",font=("arial",12,"bold"),padx=2)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_No.grid(row=1,column=1)

        
        lblTitle=Label(Dataframeleft,font=("arial",12,"bold"),text="ID No:",padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(Dataframeleft,font=("arial",12,"bold"),text="Firstname:",padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(Dataframeleft,font=("arial",12,"bold"),text="Lastname:",padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(Dataframeleft,font=("arial",12,"bold"),text="Address1:",padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(Dataframeleft,font=("arial",12,"bold"),text="Address2:",padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostcode=Label(Dataframeleft,font=("arial",12,"bold"),text="Postcode:",padx=2,pady=6)
        lblPostcode.grid(row=7,column=0,sticky=W)
        txtPostcode=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostcode.grid(row=7,column=1)
        
        lblMobileNo=Label(Dataframeleft,font=("arial",12,"bold"),text="Mobile No:",padx=2,pady=6)
        lblMobileNo.grid(row=8,column=0,sticky=W)
        txtMobileNo=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobileNo.grid(row=8,column=1)

        lblBookId=Label(Dataframeleft,font=("arial",12,"bold"),text="Book ID:",padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(Dataframeleft,font=("arial",12,"bold"),text="Book Title:",padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuther=Label(Dataframeleft,font=("arial",12,"bold"),text="Auther:",padx=2,pady=6)
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.auther_var,width=29)
        txtAuther.grid(row=2,column=3)

        lblDateBorrowed=Label(Dataframeleft,font=("arial",12,"bold"),text="Date Borrowed:",padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(Dataframeleft,font=("arial",12,"bold"),text="Date Due:",padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(Dataframeleft,font=("arial",12,"bold"),text="Days On Book:",padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.daysonbook_var,width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(Dataframeleft,font=("arial",12,"bold"),text="Late Return Fine:",padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.latereturnfine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverDue=Label(Dataframeleft,font=("arial",12,"bold"),text="Date Over Due:",padx=2,pady=6)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtDateOverDue.grid(row=7,column=3)

        lblActualPrice=Label(Dataframeleft,font=("arial",12,"bold"),text="Actual Price:",padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.finalprice_var,width=29)
        txtActualPrice.grid(row=8,column=3)



        Dataframeright=LabelFrame(frame,text="Book Details",fg="black",bd=12,relief=RIDGE,font=("arial",12,"bold"))
        Dataframeright.place(x=910,y=5,width=580,height=350)

        self.txtBox=Text(Dataframeright,font=("arial",12,"bold"),width=37,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(Dataframeright)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=["Head Firt Book","Learn Python The Hard Way","Python Programming","Secrete Rahshy","Python CookBook","Into Machine tecno","My Python","Joss Ellif guru","Elite Jungle python","Jungli Python'Machine python","Advance Python","Inton Python","RedChilli Python","Ishq Python","Python Learning","Codeing Guide","Light Java","Info State"]

        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Head Firt Book"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.788")

            elif (x=="Learn Python The Hard Way"):
                self.bookid_var.set("BKID5567")
                self.booktitle_var.set("Basic Of Python")
                self.auther_var.set("ZED A.SHAW")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.755")
                
            elif (x=="Python Programming"):
                self.bookid_var.set("BKID3665")
                self.booktitle_var.set("Into The Python Comp Science")
                self.auther_var.set("John Zhelie")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.500")

            elif (x=="Secrete Rahshy"):
                self.bookid_var.set("BKID7577")
                self.booktitle_var.set("Basic Python")
                self.auther_var.set("Ref.kapil Kamble")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.285")

            elif (x=="Python CookBook"):
                self.bookid_var.set("BKID6367")
                self.booktitle_var.set("Python CookBook")
                self.auther_var.set("Brian Jones")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.354")
            
            elif (x=="Into Machine Learning"):
                self.bookid_var.set("BKID8657")
                self.booktitle_var.set("Into Machine Learning")
                self.auther_var.set("Sarah Guaido")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.466")

            elif (x=="My Python"):
                self.bookid_var.set("BKID3767")
                self.booktitle_var.set("My Python")
                self.auther_var.set("Smith Jonse")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.866")

            elif (x=="Joss Ellif guru"):
                self.bookid_var.set("BKID1197")
                self.booktitle_var.set("Joss Ellif guru")
                self.auther_var.set("Sarah Jone")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.400")
               




            

        
        listBox=Listbox(Dataframeright,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)
    

        framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        framebutton.place(x=0,y=530,width=1540,height=70)

        botnAddData=Button(framebutton,text="Add Data",font=("arial",12,"bold"),command=self.add_data,width=23,bg="blue",fg="white")
        botnAddData.grid(row=0,column=0)

        botnAddData=Button(framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        botnAddData.grid(row=0,column=1)

        botnAddData=Button(framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        botnAddData.grid(row=0,column=2)

        botnAddData=Button(framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        botnAddData.grid(row=0,column=3)

        botnAddData=Button(framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        botnAddData.grid(row=0,column=4)

        botnAddData=Button(framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        botnAddData.grid(row=0,column=5)

        Framedetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framedetails.place(x=0,y=600,width=1540,height=195)

        tableframe=Frame(Framedetails,bd=6,relief=RIDGE,bg="powder blue")
        tableframe.place(x=0,y=2,width=1460,height=170)

        xscroll=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(tableframe,orient=VERTICAL)

        self.libary_table=ttk.Treeview(tableframe,column=("membertype","prnno","title","firstname","lastname","address1","address2","postid","mobile","bookid","booktitle","auther","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.libary_table.xview)
        yscroll.config(command=self.libary_table.yview)


        self.libary_table.heading("membertype",text="Member Type")
        self.libary_table.heading("prnno",text="PRN No.")
        self.libary_table.heading("title",text="ID.NO")
        self.libary_table.heading("firstname",text="First Name")
        self.libary_table.heading("lastname",text="Last Name")
        self.libary_table.heading("address1",text="Address1")
        self.libary_table.heading("address2",text="Address2")
        self.libary_table.heading("postid",text="Post ID")
        self.libary_table.heading("mobile",text="Mobile No.")
        self.libary_table.heading("bookid",text="Book ID")
        self.libary_table.heading("booktitle",text="Book Title")
        self.libary_table.heading("auther",text="Auther")
        self.libary_table.heading("dateborrowed",text="Date Of Borrowerd")
        self.libary_table.heading("datedue",text="Date Due")
        self.libary_table.heading("days",text="DaysOnBook")
        self.libary_table.heading("latereturnfine",text="LateReturnFine")
        self.libary_table.heading("dateoverdue",text="DateOverDue")
        self.libary_table.heading("finalprice",text="Final Price")
        
        
        
        
        
        self.libary_table["show"]="headings"
        self.libary_table.pack(fill=BOTH,expand=1)

        self.libary_table.column("membertype",width=100)
        self.libary_table.column("prnno",width=100)
        self.libary_table.column("title",width=100)
        self.libary_table.column("firstname",width=100)
        self.libary_table.column("lastname",width=100)
        self.libary_table.column("address1",width=100)
        self.libary_table.column("address2",width=100)
        self.libary_table.column("postid",width=100)
        self.libary_table.column("mobile",width=100)
        self.libary_table.column("bookid",width=100)
        self.libary_table.column("booktitle",width=100)
        self.libary_table.column("auther",width=100)
        self.libary_table.column("dateborrowed",width=100)
        self.libary_table.column("datedue",width=100)
        self.libary_table.column("days",width=100)
        self.libary_table.column("latereturnfine",width=100)
        self.libary_table.column("dateoverdue",width=100)
        self.libary_table.column("finalprice",width=100)

        self.fatch_data()
        self.libary_table.bind("<ButtonRelease-1>",self.get_cursor)
                                                                                                   
       
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@Cool2rajat",database="master")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.auther_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.latereturnfine_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.finalprice_var.get()
                                                                                                                ))
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")
    


    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@Cool2rajat",database="master")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostId=%s,Mobile=%s,BookId=%s,BookTitle=%s,Auther=%s,Dateborrowed=%s,DateDue=%s,DayOnBook=%s,LaterReturnFine=%s,DateOverDue=%s,FinalPrice=%s where PRN_NO=%s",(
                                                                                                                                                                                                                                                                               self.member_var.get(),
                                                                                                                                                                                                                                                                               self.id_var.get(),
                                                                                                                                                                                                                                                                               self.firstname_var.get(),
                                                                                                                                                                                                                                                                               self.lastname_var.get(),
                                                                                                                                                                                                                                                                               self.address1_var.get(),
                                                                                                                                                                                                                                                                               self.address2_var.get(),
                                                                                                                                                                                                                                                                               self.postcode_var.get(),
                                                                                                                                                                                                                                                                               self.mobile_var.get(),
                                                                                                                                                                                                                                                                               self.bookid_var.get(),
                                                                                                                                                                                                                                                                               self.booktitle_var.get(),
                                                                                                                                                                                                                                                                               self.auther_var.get(),
                                                                                                                                                                                                                                                                               self.dateborrowed_var.get(),
                                                                                                                                                                                                                                                                               self.datedue_var.get(),
                                                                                                                                                                                                                                                                               self.daysonbook_var.get(),
                                                                                                                                                                                                                                                                               self.latereturnfine_var.get(),
                                                                                                                                                                                                                                                                               self.dateoverdue_var.get(),
                                                                                                                                                                                                                                                                               self.finalprice_var.get(),
                                                                                                                                                                                                                                                                               self.prn_var.get()
                                                                                                                                                                                                                                                                               ))
                                                                                                                                                                                                                                                                                           

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been Updated")
 
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@Cool2rajat",database="master")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.libary_table.delete(*self.libary_table.get_children())
            for i in rows:
                self.libary_table.insert("",END,values=i)
                conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.libary_table.focus()
        content=self.libary_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])

    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN No:\t\t\t"+self.prn_var.get()+"\n")
        self.txtBox.insert(END,"ID No:\t\t\t"+self.id_var.get()+"\n")
        self.txtBox.insert(END,"Firstname:\t\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"Lastname:\t\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address1:\t\t\t"+self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2:\t\t\t"+self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Post Code:\t\t\t"+self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No:\t\t\t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book No:\t\t\t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title:\t\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Auther:\t\t\t"+self.auther_var.get()+"\n")
        self.txtBox.insert(END,"Date Borrowed:\t\t\t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"Date Due\t\t\t"+self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"Days On Book:\t\t\t"+self.daysonbook_var.get()+"\n")
        self.txtBox.insert(END,"Late Return Fine:\t\t\t"+self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END,"Date Over Due:\t\t\t"+self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"Actual Price:\t\t\t"+self.finalprice_var.get()+"\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return
    
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@Cool2rajat",database="master")
            my_cursor=conn.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been Deleted")        


if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()