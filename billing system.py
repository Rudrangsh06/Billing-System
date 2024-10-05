from tkinter import *
import random
import os
import sys
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#0A7CFF")
        self.root.title("Restaurant Billing System")
        title=Label(self.root,text="Restaurant Billing System",bd=12,relief=RIDGE,font=("Arial Black",20),bg="#A569BD",fg="white").pack(fill=X)
        #===================================variables=======================================================================================
        self.chilipotato=IntVar()
        self.sandwich=IntVar()
        self.malaichaap=IntVar()
        self.springroll=IntVar()
        self.cheesepakoda=IntVar()
        self.manchurian=IntVar()
        self.cheeseburger=IntVar()
        self.Chholebhature=IntVar()
        self.pasta=IntVar()
        self.pavbhaji=IntVar()
        self.malaikofta=IntVar()
        self.paneerlababdar=IntVar()
        self.daltadka=IntVar()
        self.kidneybeans=IntVar()
        self.samosa=IntVar()
        self.poha=IntVar()
        self.masaladosa=IntVar()
        self.idlisambhar=IntVar()
        self.dabeli=IntVar()
        self.kachori=IntVar()
        self.alootikki=IntVar()
        self.total_starter=StringVar()
        self.total_mac=StringVar()
        self.total_sna=StringVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()
        #==========================================customer details label frame=================================================
        details=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="#A569BD",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=80,relwidth=1)
        cust_name=Label(details,text="Customer Name",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=0,padx=15)

        cust_entry=Entry(details,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)

        contact_name=Label(details,text="Contact No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=2,padx=10)

        contact_entry=Entry(details,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)

        bill_name=Label(details,text="Bill.No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=4,padx=10)

        bill_entry=Entry(details,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)
        #=======================================Starters=================================================================
        starter=LabelFrame(self.root,text="Starter",font=("Arial Black",12),bg="#E5B4F3",fg="#6C3483",relief=GROOVE,bd=10)
        starter.place(x=5,y=180,height=380,width=325)

        item1=Label(starter,text="Chilli Potato",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item1_entry=Entry(starter,borderwidth=2,width=15,textvariable=self.chilipotato).grid(row=0,column=1,padx=10)

        item2=Label(starter,text="Sandwich",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item2_entry=Entry(starter,borderwidth=2,width=15,textvariable=self.sandwich).grid(row=1,column=1,padx=10)

        item3=Label(starter,text="Malaichaap",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item3_entry=Entry(starter,borderwidth=2,width=15,textvariable=self.malaichaap).grid(row=2,column=1,padx=10)

        item4=Label(starter,text="Springroll",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item4_entry=Entry(starter,borderwidth=2,width=15,textvariable=self.springroll).grid(row=3,column=1,padx=10)

        item5=Label(starter,text="Cheese Pakoda",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item5_entry=Entry(starter,borderwidth=2,width=15,textvariable=self.cheesepakoda).grid(row=4,column=1,padx=10)

        item6=Label(starter,text="Manchurian",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item6_entry=Entry(starter,borderwidth=2,width=15,textvariable=self.manchurian).grid(row=5,column=1,padx=10)

        item7=Label(starter,text="Cheese Burger",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item7_entry=Entry(starter,borderwidth=2,width=15,textvariable=self.cheeseburger).grid(row=6,column=1,padx=10)
        #=================================== Main Course =====================================================================================
        mainc=LabelFrame(self.root,text="Main Course",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        mainc.place(x=340,y=180,height=380,width=325)

        item8=Label(mainc,text="Chhole Bhature",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item8_entry=Entry(mainc,borderwidth=2,width=15,textvariable=self.Chholebhature).grid(row=0,column=1,padx=10)

        item9=Label(mainc,text="Pasta",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item9_entry=Entry(mainc,borderwidth=2,width=15,textvariable=self.pasta).grid(row=1,column=1,padx=10)

        item10=Label(mainc,text="Pav Bhaji",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item10_entry=Entry(mainc,borderwidth=2,width=15,textvariable=self.pavbhaji).grid(row=2,column=1,padx=10)

        item11=Label(mainc,text="Malaikofta",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item11_entry=Entry(mainc,borderwidth=2,width=15,textvariable=self.malaikofta).grid(row=3,column=1,padx=10)

        item12=Label(mainc,text="Paneer Lababdar",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item12_entry=Entry(mainc,borderwidth=2,width=15,textvariable=self.paneerlababdar).grid(row=4,column=1,padx=10)

        item13=Label(mainc,text="Dal Tadka",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item13_entry=Entry(mainc,borderwidth=2,width=15,textvariable=self.daltadka).grid(row=5,column=1,padx=10)

        item14=Label(mainc,text="Kidney Beans",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item14_entry=Entry(mainc,borderwidth=2,width=15,textvariable=self.kidneybeans).grid(row=6,column=1,padx=10)
        #========================================Snacks===============================================================================
        snacks=LabelFrame(self.root,text="Snacks",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        snacks.place(x=677,y=180,height=380,width=325)

        item15=Label(snacks,text="Samosa",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item15_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.samosa).grid(row=0,column=1,padx=10)

        item16=Label(snacks,text="Poha",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item16_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.poha).grid(row=1,column=1,padx=10)

        item17=Label(snacks,text="Masala Dosa",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item17_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.masaladosa).grid(row=2,column=1,padx=10)

        item18=Label(snacks,text="Idli Sambhar",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item18_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.idlisambhar).grid(row=3,column=1,padx=10)

        item19=Label(snacks,text="Dabeli",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item19_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.dabeli).grid(row=4,column=1,padx=10)

        item20=Label(snacks,text="Kachori",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item20_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.kachori).grid(row=5,column=1,padx=10)

        item21=Label(snacks,text="Aloo Tikki",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item21_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.alootikki).grid(row=6,column=1,padx=10)
        #=====================================================billarea==============================================================================
        billarea=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
        billarea.place(x=1010,y=188,width=330,height=372)

        bill_title=Label(billarea,text="Bill Area",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)

        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #=================================================billing menu=========================================================================================
        billing_menu=LabelFrame(self.root,text="Billing Summery",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#A569BD",fg="white")
        billing_menu.place(x=0,y=560,relwidth=1,height=137)

        total_starter=Label(billing_menu,text="Total Starter Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=0)
        total_starter_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_starter).grid(row=0,column=1,padx=10,pady=7)

        total_maincourse=Label(billing_menu,text="Total MainCourse Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=0)
        total_maincourse_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_mac).grid(row=1,column=1,padx=10,pady=7)


        total_snacks=Label(billing_menu,text="Total Snacks Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=2,column=0)
        total_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_sna).grid(row=2,column=1,padx=10,pady=7)

        tax_starter=Label(billing_menu,text="Starter Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=2)
        tax_starter_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.a).grid(row=0,column=3,padx=10,pady=7)

        tax_maincourse=Label(billing_menu,text="MainCourse Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=2)
        tax_maincourse_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.b).grid(row=1,column=3,padx=10,pady=7)


        tax_snacks=Label(billing_menu,text="SnacksTax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=2,column=2)
        tax_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.c).grid(row=2,column=3,padx=10,pady=7)

        button_frame=Frame(billing_menu,bd=7,relief=GROOVE,bg="#6C3483")
        button_frame.place(x=830,width=500,height=95)

        button_total=Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:total(self)).grid(row=0,column=0,padx=12)
        button_clear=Button(button_frame,text="Clear Field",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:clear(self)).grid(row=0,column=1,padx=10,pady=6)
        button_exit=Button(button_frame,text="Exit",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",width=8,command=lambda:exit1(self)).grid(row=0,column=2,padx=10,pady=6)
        intro(self)


def total(self):
    if (self.c_name.get=="" or self.phone.get()==""):
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.hp=self.chilipotato.get()*50
    self.sh=self.sandwich.get()*120
    self.mc=self.malaichaap.get()*110
    self.sr=self.springroll.get()*80
    self.cp=self.cheesepakoda.get()*30
    self.ma=self.manchurian.get()*70
    self.cb=self.cheeseburger.get()*40
    total_starter_price=(
                self.hp+
                self.sh+
                self.mc+
                self.sr+
                self.cp+
                self.ma+
                self.cb)
    self.total_starter.set(str(total_starter_price)+" Rs")
    self.a.set(str(round(total_starter_price*0.05,3))+" Rs")

    self.ch=self.Chholebhature.get()*180
    self.pa=self.pasta.get()*120
    self.pb=self.pavbhaji.get()*100
    self.mk=self.malaikofta.get()*160
    self.pl=self.paneerlababdar.get()*130
    self.dt=self.daltadka.get()*90
    self.kb=self.kidneybeans.get()*80
    total_mainco_price=(
        self.ch+
        self.pa+
        self.pb+
        self.mk+
        self.pl+
        self.dt+
        self.kb)

    self.total_mac.set(str(total_mainco_price)+" Rs")
    self.b.set(str(round(total_mainco_price*0.01,3))+" Rs")

    self.sa=self.samosa.get()*15
    self.ph=self.poha.get()*30
    self.md=self.masaladosa.get()*50
    self.ids=self.idlisambhar.get()*50
    self.da=self.dabeli.get()*85
    self.ka=self.kachori.get()*100
    self.at=self.alootikki.get()*40

    total_snacks_price=(
        self.sa+
        self.ph+
        self.md+
        self.ids+
        self.da+
        self.ka+
        self.at)

    self.total_sna.set(str(total_snacks_price)+" Rs")
    self.c.set(str(round(total_snacks_price*0.10,3))+" Rs")
    self.total_all_bill=(total_starter_price+
                total_mainco_price+
                total_snacks_price+
                (round(total_mainco_price*0.01,3))+
                (round(total_snacks_price*0.10,3))+
                (round(total_starter_price*0.05,3)))
    self.total_all_bil=str(self.total_all_bill)+" Rs"
    billarea(self)
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO BLUE HEAVEN\n\tPhone-No.7668716123")
    self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END,"\n====================================\n")
def billarea(self):
    intro(self)
    if self.chilipotato.get()!=0:
        self.txtarea.insert(END,f"ChilliPotato\t\t {self.chilipotato.get()}\t{self.cp}\n")
    if self.sandwich.get()!=0:
        self.txtarea.insert(END,f"Sandwich\t\t {self.sandwich.get()}\t{self.sh}\n")
    if self.malaichaap.get()!=0:
        self.txtarea.insert(END,f"Malaichaap\t\t {self.malaichaap.get()}\t{self.mc}\n")
    if self.springroll.get()!=0:
        self.txtarea.insert(END,f"Springroll\t\t {self.springroll.get()}\t{self.sr}\n")
    if self.cheesepakoda.get()!=0:
        self.txtarea.insert(END,f"Cheesepakoda\t\t {self.cheesepakoda.get()}\t{self.cp}\n")
    if self.manchurian.get()!=0:
        self.txtarea.insert(END,f"Manchurian\t\t {self.manchurian.get()}\t{self.ma}\n")
    if self.cheeseburger.get()!=0:
        self.txtarea.insert(END,f"Cheeseburger\t\t {self.cheeseburger.get()}\t{self.cb}\n")
    if self.Chholebhature.get()!=0:
        self.txtarea.insert(END,f"ChholeBhature\t\t {self.Chholebhature.get()}\t{self.ch}\n")
    if self.pasta.get()!=0:
        self.txtarea.insert(END,f"Pasta\t\t {self.pasta.get()}\t{self.pa}\n")
    if self.pavbhaji.get()!=0:
        self.txtarea.insert(END,f"PavBhaji\t\t {self.pavbhaji.get()}\t{self.pb}\n")
    if self.malaikofta.get()!=0:
        self.txtarea.insert(END,f"MalaiKofta\t\t {self.malaikofta.get()}\t{self.mk}\n")
    if self.paneerlababdar.get()!=0:
        self.txtarea.insert(END,f"PaneerLababadar\t\t {self.paneerlababdar.get()}\t{self.pl}\n")
    if self.daltadka.get()!=0:
        self.txtarea.insert(END,f"DalTadkal\t\t {self.daltadka.get()}\t{self.dt}\n")
    if self.kidneybeans.get()!=0:
        self.txtarea.insert(END,f"KidneyBeans\t\t {self.kidneybeans.get()}\t{self.kb}\n")
    if self.samosa.get()!=0:
        self.txtarea.insert(END,f"Samosa\t\t {self.samosa.get()}\t{self.sa}\n")
    if self.poha.get()!=0:
        self.txtarea.insert(END,f"Poha\t\t {self.poha.get()}\t{self.ph}\n")
    if self.masaladosa.get()!=0:
        self.txtarea.insert(END,f"Masaladosa\t\t {self.masaladosa.get()}\t{self.md}\n")
    if self.idlisambhar.get()!=0:
        self.txtarea.insert(END,f"IdliSambhar\t\t {self.idlisambhar.get()}\t{self.ids}\n")
    if self.dabeli.get()!=0:
        self.txtarea.insert(END,f"Dabeli\t\t {self.dabeli.get()}\t{self.da}\n")
    if self.kachori.get()!=0:
        self.txtarea.insert(END,f"Kachori\t\t {self.kachori.get()}\t{self.ka}\n")
    if self.alootikki.get()!=0:
        self.txtarea.insert(END,f"AlooTikki\t\t {self.alootikki.get()}\t{self.at}\n")

    self.txtarea.insert(END,f"------------------------------------\n")
    if self.a.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total StarterTax : {self.a.get()}\n")
    if self.b.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Main Course Tax : {self.b.get()}\n")
    if self.c.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Snacks Tax : {self.c.get()}\n")
    self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END,f"------------------------------------\n")
def clear(self):
        self.txtarea.delete(1.0,END)
        self.chilipotato.set(0)
        self.sandwich.set(0)
        self.malaichaap.set(0)
        self.springroll.set(0)
        self.cheesepakoda.set(0)
        self.manchurian.set(0)
        self.cheeseburger.set(0)
        self.Chholebhature.set(0)
        self.pasta.set(0)
        self.pavbhaji.set(0)
        self.malaikofta.set(0)
        self.paneerlababdar.set(0)
        self.daltadka.set(0)
        self.kidneybeans.set(0)
        self.samosa.set(0)
        self.poha.set(0)
        self.masaladosa.set(0)
        self.idlisambhar.set(0)
        self.dabeli.set(0)
        self.kachori.set(0)
        self.alootikki.set(0)
        self.total_starter.set(0)
        self.total_mac.set(0)
        self.total_sna.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)
def exit1(self):
    self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()
