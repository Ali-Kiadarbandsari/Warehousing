'''
Ali Kiadarbandsari
2023/04/2
'''
import sqlite3 as sql
import pandas as pd
from matplotlib import pyplot as plt
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import io
from tkinter import messagebox  
from tkcalendar import Calendar, DateEntry
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
main = Tk()
registration = Toplevel()
loginn = Toplevel()
Product = Toplevel()
User = Toplevel()
stock = Toplevel()
importt = Toplevel()
purchase = Toplevel()
departure = Toplevel()
history = Toplevel()
bill_main = Toplevel()
bill_detail = Toplevel()
bill = Toplevel()
class INTcheck:
    def __set_name__(self,instance,key):
        self.key = key
    
    def __get__(self,instance,owner):
        return  instance.__dict__[self.key]
    
    def __set__(self,instance,value):
        if value.isdigit():
             instance.__dict__[self.key]=value
        else:
            messagebox.showerror("error","لطفا عدد وارد کنید")  
            
    def __delete__(self,instance):
        del instance.__dict__[self.key]
class STRcheck:
    def __set_name__(self,instance,key):
        self.key = key
    
    def __get__(self,instance,owner):
        return  instance.__dict__[self.key]
    
    def __set__(self,instance,value):
        if value.isalpha():
             instance.__dict__[self.key]=value
        else:
            messagebox.showerror("error","لطفا حروف وارد کنید")  
            
    def __delete__(self,instance):
        del instance.__dict__[self.key]
class home:
    name = STRcheck()
    code = INTcheck()
    point = INTcheck()
    desc = STRcheck()

    UserN = STRcheck()
    UserL = STRcheck()
    UserC = INTcheck()

    
    def __init__(self,event = None) :
        main.state("withdrawn")
        registration.state("withdrawn")
        loginn.state("withdrawn")
        Product.state("withdrawn")
        User.state("withdrawn")
        stock.state("withdrawn")
        importt.state("withdrawn")
        purchase.state("withdrawn")
        departure.state("withdrawn")
        history.state("withdrawn")
        bill_main.state("withdrawn")
        bill_detail.state("withdrawn")
        bill.state("withdrawn")
        self.main_page()
        self.register()
        self.login()
        self.Product_registration()
        self.User_registration()
        self.warehouse_stock()
        self.import_product()
        self.purchase_request()
        self.departure_product()
        self.order_history()
        self.billing()
        self.bill_detaill()
        self.show_bill()

        self.check()

        self.create_tables()
        self.product_count = 0
        self.purchase_count = 0
        self.import_count = 0
        self.stock_count = 0
        self.user_count = 0
        self.bill_count = 0
        self.departure_count = 0
        self.history_count = 0
        self.kalalst = []
        self.valuelst = []
        self.his_lst = []
        self.stocklst = []
        self.his_lst = []   





    def create_tables(self) :
        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS login (name TEXT ,last TEXT,username TEXT,password TEXT)''')
        
        self.cur.execute('''CREATE TABLE IF NOT EXISTS kala (id   ,name TEXT ,point INTEGER,Description TEXT
        ,type TEXT,groupp TEXT,stock INTEGER,photoo BLOB)''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS user (name TEXT ,last_name TEXT,code TEXT
        ,gender TEXT,work_Pposition TEXT,photoo BLOB)''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS history (order_code TEXT , product_name TEXT,product_code TEXT,groupp TEXT
        ,type TEXT,stock INTEGER,user_name TEXT,user_code TEXT,user_gender TEXT,number TEXT,date TEXT,situation TEXT)''')
        self.con.commit()





    def register(self) :
        registration.state("withdraw")
        registration.geometry('900x500+510+290')
        registration.title('ثبت نام')
        self.register_image = PhotoImage(file = 'img/register_back.png')
        self.register_img = Label(registration,image = self.register_image )
        self.register_img.place(x = 0 , y = 0)

        self.name_lbl = Label(registration,text = ": نام",font = ('B Koodak' , 18),bg = '#F8F9FA',fg = '#707070')
        self.last_lbl = Label(registration,text = ": نام خانوادگی",font = ('B Koodak' , 18),bg = '#F8F9FA',fg = '#707070')
        self.user = Label(registration,text = ": نام کابری",font = ('B Koodak' , 18),bg = '#F8F9FA',fg = '#707070')
        self.passw = Label(registration,text = ": کلمه عبور",font = ('B Koodak' , 18),bg = '#F8F9FA',fg = '#707070')

        self.name_ent = Entry(registration, bg = '#adb5bd', width = 25 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#FFFFFF')
        self.last_ent = Entry(registration, bg = '#adb5bd', width = 25 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#FFFFFF')
        self.user_ent = Entry(registration, bg = '#adb5bd', width = 25 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#FFFFFF')
        self.passw_ent = Entry(registration, bg = '#adb5bd', width = 25 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#FFFFFF')

        self.name_lbl.place(x =750 , y = 90 )
        self.last_lbl.place(x =750 , y = 155 )
        self.user.place(x =750 , y = 220 )
        self.passw.place(x =750 , y = 283 )

        self.name_ent.place(x =500 , y = 100 )
        self.last_ent.place(x =500 , y = 165 )
        self.user_ent.place(x =500 , y = 230 )
        self.passw_ent.place(x =500, y = 293 )

        self.submit_btn = Button(registration,bg = "#495057" , text = "ثبت",font = ('B Koodak' , 14),width=10 ,relief="flat" , fg = "#FFFFFF")

        self.submit_btn.place(x = 611 ,y = 362)

        self.submit_btn.bind('<Button-1>',self.register_check)



    def login(self):
        loginn.state("withdraw")
        loginn.geometry('450x550+550+150')
        loginn.title('ورود')

        self.login_image = PhotoImage(file = 'img/login_back.png')
        self.login_img = Label(loginn,image = self.login_image ,relief="flat")
        self.login_img.place(x = 0 , y = 0)

        self.user = Label(loginn,text = ": نام کاربری",font = ('B Koodak' , 18),bg = '#495057',fg = '#F8F9FA')
        self.passw = Label(loginn,text = ": رمز عبور",font = ('B Koodak' , 18),bg = '#495057',fg = '#F8F9FA')
        self.user.place(x = 310 , y = 141)
        self.passw.place(x = 310 , y = 209)
        
        self.user_entt = Entry(loginn, bg = '#ced4da', width = 23 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
        self.passw_entt = Entry(loginn, bg = '#ced4da', width = 23 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057',show = "*")
        self.user_entt.place(x = 80 , y = 151)
        self.passw_entt.place(x = 80 , y = 219)

        self.baste_image = PhotoImage(file = 'img/baste.png')
        self.eye = Button(loginn,image = self.baste_image ,relief="flat" , bg = "#495057",activebackground = '#495057')
        self.eye.place(x = 35 , y = 219)

        self.submit_btn = Button(loginn,bg = "#6C757D" , text = "ثبت",font = ('B Koodak' , 14),width=13 ,relief="flat" , fg = "#FFFFFF")
        self.submit_btn.place(x = 148 , y = 336)

        self.eye.bind('<Button-1>',self.hide)
        self.eye.bind('<ButtonRelease>',self.hide)
        self.submit_btn.bind('<Button-1>',self.login_check)


    def check(self) :
        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        self.tables = self.cur.fetchall()
        if len(self.tables) == 0:
            registration.state("normal")
        else:
            loginn.state("normal")
        self.cur.close()
        self.con.close()
    def register_check(self,event = None): 
        self.name_v = self.name_ent.get()
        self.last_v = self.last_ent.get()
        self.user_v = self.user_ent.get()
        self.passw_v = self.passw_ent.get()

        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        self.data=(self.name_v,self.last_v,self.user_v,self.passw_v)
        self.cur.execute('''CREATE TABLE IF NOT EXISTS login (name TEXT ,last TEXT,username TEXT,password TEXT)''')
        self.cur.execute('INSERT INTO login(name,last,username,password) VALUES(?,?,?,?)',self.data)
        self.con.commit()

        registration.state('withdrawn')
        main.state('normal')
    def login_check(self,event = None) :
        con = sql.connect('mydb.db')
        cur = con.cursor()
        def sql_show():
            
            row = cur.execute('SELECT * FROM login')
            lst = list(row)
            return lst       
                
        lst = sql_show()
        if self.user_entt.get() == lst[0][2] and self.passw_entt.get() == lst[0][3] :
            loginn.state('withdrawn')
            main.state('normal')
    def hide(self,event = None):
        if self.passw_entt['show'] == '*' :
            self.passw_entt['show'] = ""
            self.baste_image['file'] = 'img/baz.png'
        elif self.passw_entt['show'] == "" :
            self.passw_entt['show'] = '*'
            self.baste_image['file'] = 'img/baste.png'






    def main_page(self) :
        main.state("withdraw")
        main.geometry('1200x680+360+200')
        main.title('صفحه اصلی')

        self.main_image = PhotoImage(file = 'img/main_back.png')
        self.main_img = Label(main,image = self.main_image ,relief="flat")
        self.main_img.place(x = 0 , y = 0)

        self.enter_img = PhotoImage(file = 'img/enter_btn.png')

        self.btn1 = Button(main,image = self.enter_img ,relief="flat" ,width = 160,fg = "#DEE2E6", bg = "#DEE2E6",activebackground = '#DEE2E6')
        self.btn2 = Button(main,image = self.enter_img ,relief="flat" ,width = 160,fg = "#DEE2E6", bg = "#DEE2E6",activebackground = '#DEE2E6')
        self.btn3 = Button(main,image = self.enter_img ,relief="flat" ,width = 160,fg = "#DEE2E6", bg = "#DEE2E6",activebackground = '#DEE2E6')
        self.btn4 = Button(main,image = self.enter_img ,relief="flat" ,width = 160,fg = "#DEE2E6", bg = "#DEE2E6",activebackground = '#DEE2E6')
        self.btn5 = Button(main,image = self.enter_img ,relief="flat" ,width = 160,fg = "#DEE2E6", bg = "#DEE2E6",activebackground = '#DEE2E6')
        self.btn6 = Button(main,image = self.enter_img ,relief="flat" ,width = 160,fg = "#DEE2E6", bg = "#DEE2E6",activebackground = '#DEE2E6')
        self.btn7 = Button(main,image = self.enter_img ,relief="flat" ,width = 160,fg = "#DEE2E6", bg = "#DEE2E6",activebackground = '#DEE2E6')
        self.btn8 = Button(main,image = self.enter_img ,relief="flat" ,width = 160,fg = "#DEE2E6", bg = "#DEE2E6",activebackground = '#DEE2E6')
        
        self.btn1.place(x = 87 , y = 248)
        self.btn2.place(x = 381 , y = 248)
        self.btn3.place(x = 671 , y = 248)
        self.btn4.place(x = 961 , y = 248)
        self.btn5.place(x = 87 , y = 558)
        self.btn6.place(x = 381 , y = 558)
        self.btn7.place(x = 671 , y = 558)
        self.btn8.place(x = 961 , y = 558)
        self.btn1.bind('<Button-1>',self.home_to_product)
        self.btn2.bind('<Button-1>',self.home_to_user)
        self.btn3.bind('<Button-1>',self.home_to_stock)
        self.btn4.bind('<Button-1>',self.home_to_import)
        self.btn5.bind('<Button-1>',self.home_to_purchse)
        self.btn6.bind('<Button-1>',self.home_to_departure)
        self.btn7.bind('<Button-1>',self.home_to_bill)
        self.btn8.bind('<Button-1>',self.home_to_history)






    def home_to_product(self,event = None) :
        main.state("withdrawn")
        Product.state("normal")
        self.product_data_to_treeview()
    def home_to_user(self,event = None) :
        main.state("withdrawn")
        User.state("normal")
        self.user_data_to_table()
    def home_to_stock(self,event = None) :
        main.state("withdrawn")
        stock.state("normal")
        self.data_to_stock()
    def home_to_import(self,event = None) :
        main.state("withdrawn")
        importt.state("normal")
        self.data_to_import_table()
    def home_to_purchse(self,event = None) :
        main.state("withdrawn")
        purchase.state("normal")
        self.data_to_purchase_table()
    def home_to_departure(self,event = None) :
        main.state("withdrawn")
        departure.state("normal")
        self.data_to_departure_table()  
    def home_to_bill(self,event = None) :
        main.state("withdrawn")
        bill_main.state("normal")
        self.data_to_bill_main()
    def home_to_history(self,event = None) :
        main.state("withdrawn")
        history.state("normal")
        self.history_table_by_Date()               

    def product_to_home(self,evnt = None) :
        Product.state("withdrawn")
        main.state("normal")
        for item in self.kala.get_children():
            self.kala.delete(item)
            print(item)
        self.product_type_combo.set("یک گزینه را انتخاب کنید")
        self.product_group_combo.set("یک گزینه را انتخاب کنید")
        self.product_code_ent.delete(0,END)
        self.product_name_ent.delete(0,END)
        self.point_purchase_ent.delete(0,END)
        self.Description_ent.delete(0,END)
        self.search_ent.delete(0,END)

        self.procuct_img = Image.open("img/empty.png")
        self.procuct_image = self.procuct_img.resize((220, 176))
        self.product_photo = ImageTk.PhotoImage(self.procuct_image)
        self.product_photo_label = Label(Product, image=self.product_photo, width=self.new_width, height=self.new_height)
        self.product_photo_label.place(x=125, y=153) 
    def user_to_home(self,event = None) :
        User.state("withdrawn")
        main.state("normal")  
        for item in self.user_table.get_children():
            self.user_table.delete(item)
        self.UserName_ent.delete(0,END)
        self.UserLast_ent.delete(0,END)
        self.UserCode_ent.delete(0,END)
        self.user_search_ent.delete(0,END)
        self.UserGender_combo.set("یک گزینه را انتخاب کنید")
        self.UserWorkPosition_combo.set("یک گزینه را انتخاب کنید")

        self.user_img = Image.open('img/empty.png')
        self.user_image = self.user_img.resize((220, 176))
        self.user_photo = ImageTk.PhotoImage(self.user_image)
        self.user_label = Label(User, image=self.user_photo, width=self.new_width, height=self.new_height)
        self.user_label.place(x = 197 , y = 148)
    def stock_to_home(self,event = None) :
        stock.state("withdrawn")
        main.state("normal")
        for item in self.stock_table.get_children():
            self.stock_table.delete(item)
        self.stock_search_ent.delete(0,END)
    def import_to_home(self,event = None) :
        importt.state("withdrawn")
        main.state("normal")
        for item in self.import_table.get_children():
            self.import_table.delete(item)
        self.us_name['text'] = ""
        self.us_gender['text'] = ""
        self.pr_name['text'] = ""
        self.pr_point['text'] = ""
        self.pr_type['text'] = ""
        self.pr_group['text'] = ""
        self.us_code_ent.delete(0,END)
        self.pr_code_ent.delete(0,END)
        self.number_ent.delete(0,END)
        self.date_cal.delete(0,END)
        self.import_order_code_ent.delete(0,END)

        self.impo_empty_img = Image.open('img/import_empty.png')
        self.impo_empty_image = self.impo_empty_img.resize((175, 124))
        self.impo_empty = ImageTk.PhotoImage(self.impo_empty_image)
        self.impo_empty_label = Label(importt, image=self.impo_empty)
        self.impo_empty_label.place(x = 115 , y = 260)
    def purchase_to_home(self,event = None) :
        purchase.state("withdrawn")
        main.state("normal")
        for item in self.purchase_table.get_children():
            self.purchase_table.delete(item)
    def departure_to_home(self,event = None) :
        departure.state("withdrawn")
        main.state("normal")
        for item in self.departure_table.get_children():
            self.departure_table.delete(item)
        self.departure_us_name['text'] = ""
        self.departure_us_last['text'] = ""
        self.departure_us_gender['text'] = ""
        self.departure_pr_name['text'] = ""
        self.departure_pr_number['text'] = ""
        self.departure_pr_type['text'] = ""
        self.departure_pr_group['text'] = ""
        self.departure_us_code_ent.delete(0,END)
        self.departure_pr_code_ent.delete(0,END)
        self.departure_number_ent.delete(0,END)
        self.departure_code_ent.delete(0,END)
        self.departure_date_cal.delete(0,END)

        self.departure_empty_img = Image.open('img/import_empty.png')
        self.departure_empty_image = self.departure_empty_img.resize((170, 160))
        self.departure_empty = ImageTk.PhotoImage(self.departure_empty_image)
        self.departure_empty_label = Label(departure, image=self.departure_empty)
        self.departure_empty_label.place(x = 367 , y = 239)
    def bill_to_home(self,event = None) :
        bill_main.state("withdrawn")
        main.state("normal")
        for item in self.bill_table.get_children():
            self.bill_table.delete(item)
    def history_to_home(self,event = None) :
        history.state("withdrawn")
        main.state("normal")
        for item in self.history_table.get_children():
            self.history_table.delete(item)
    def Dbill_to_Mbill(self,event = None) :
        bill_detail.state("withdrawn")
        bill_main.state("normal")
        for item in self.bill_detail_table.get_children():
            self.bill_detail_table.delete(item)
    def bill_to_Dbill(self,event = None) :
        bill.state("withdrawn")
        bill_detail.state("normal")
    def bill_to_main(self,evnt = None) :
        bill.state("withdrawn")
        main.state("normal")




    def Product_registration(self) :
        Product.state("withdraw")
        Product.geometry('1400x900+300+50')
        Product.title('ثبت کالای جدید')

        self.Product_registration_image = PhotoImage(file = 'img/Product-registration_back.png')
        self.Product_registration_img = Label(Product,image = self.Product_registration_image ,relief="flat")
        self.Product_registration_img.place(x = 0 , y = 0)

        self.produuct_serach_btn_img = PhotoImage(file = 'img/search_btn.png')
        self.search_btn = Button(Product,bg = "#495057" , image = self.produuct_serach_btn_img,width=150 ,relief="flat",activebackground = "#495057")
        self.search_ent = Entry(Product, bg = '#FFFFFF', width = 35 , font = ('B Koodak' , 14) , relief = 'flat' , justify = 'right',fg='#495057')
        self.search_btn.place(x = 85 , y = 33)
        self.search_ent.place(x = 266 , y = 40)
        
        self.product_name = Label(Product,text = ": نام کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.product_code = Label(Product,text = ": کد کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.point_purchase = Label(Product,text = ": نقطه خرید",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.Description = Label(Product,text = ": توضیحات کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.product_name.place(x = 1169 , y = 181)
        self.product_code.place(x = 1169 , y = 233)
        self.point_purchase.place(x = 1169 , y = 285)
        self.Description.place(x = 1169 , y = 337)

        self.product_name_ent = Entry(Product, bg = '#FFFFFF', width = 35 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
        self.product_code_ent = Entry(Product, bg = '#FFFFFF', width = 35 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
        self.point_purchase_ent = Entry(Product, bg = '#FFFFFF', width = 35 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
        self.Description_ent = Entry(Product, bg = '#FFFFFF', width = 35 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
        self.product_name_ent.place(x = 824 , y = 185)
        self.product_code_ent.place(x = 824 , y = 237)
        self.point_purchase_ent.place(x = 824 , y = 289)
        self.Description_ent.place(x = 824 , y = 341)

        self.produuct_upload_btn_img = PhotoImage(file = 'img/upload_btn.png')
        self.photo_submit = Button(Product,bg = "#DEE2E6",activebackground= "#DEE2E6" , image = self.produuct_upload_btn_img,width=178 ,relief="flat")
        self.photo_submit.place(x = 146 , y = 342)

        self.product_type = Label(Product,text = ": نوع کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.product_group = Label(Product,text = ": نام گروه کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.product_type.place(x = 607 , y = 189)
        self.product_group.place(x = 607 , y = 289)

        self.product_type_combo = ttk.Combobox(Product,width = 20 , font = ('B Koodak' , 12),justify = 'right',values=["مواد خام", "کالای خریداری شده", "کالای توید شده اولیه", "کالای تولید شده برای فروش"])
        self.product_group_combo = ttk.Combobox(Product,width = 20 , font = ('B Koodak' , 12),justify = 'right',values=["فلزات", "مواد غذایی"])
        self.product_type_combo.set("یک گزینه را انتخاب کنید")
        self.product_group_combo.set("یک گزینه را انتخاب کنید")
        self.product_type_combo.place(x=378, y=195)
        self.product_group_combo.place(x=378, y=295)

        self.product_submit_img = PhotoImage(file = 'img/submit_btn.png')
        self.product_edit_img = PhotoImage(file = 'img/edit_btn.png')
        self.product_delete_img = PhotoImage(file = 'img/delete_btn.png')
        self.product_home_img = PhotoImage(file = 'img/home_btn.png')
        self.Product_registration_submit = Button(Product,bg = "#FFFFFF",activebackground = "#FFFFFF" , image = self.product_submit_img,width=197 ,relief="flat" ) 
        self.Product_registration_edit = Button(Product,bg = "#FFFFFF" ,activebackground = "#FFFFFF", image = self.product_edit_img,width=197 ,relief="flat" ) 
        self.Product_registration_delete = Button(Product,bg = "#FFFFFF" ,activebackground = "#FFFFFF", image = self.product_delete_img,width=197 ,relief="flat" ) 
        self.Product_registration_exit = Button(Product,bg = "#FFFFFF" ,activebackground = "#FFFFFF", image = self.product_home_img,width=230 ,relief="flat" ) 
        self.Product_registration_submit.place(x=50, y=815)
        self.Product_registration_edit.place(x=262, y=815)    
        self.Product_registration_delete.place(x=473, y=815)    
        self.Product_registration_exit.place(x=1120, y=815)    
 
        self.kala = ttk.Treeview(Product,show='headings',height=7)
        self.kala['columns']=('group','Type','point','id','Name','row')
        self.kala.column('#0',width=0,stretch=NO)
        self.kala.column('group',width=220,anchor=E)
        self.kala.column('Type',width=220,anchor=E)
        self.kala.column('point',width=220,anchor=E)
        self.kala.column('id',width=200,anchor=E)
        self.kala.column('Name',width=220,anchor=E)
        self.kala.column('row',width=150,anchor=E)
        self.kala.heading('#0',text='',anchor=E)
        self.kala.heading('group',text='گروه کالا',anchor=E)
        self.kala.heading('Type',text='نوع کالا',anchor=E)
        self.kala.heading('point',text='نقطه خرید',anchor=E)
        self.kala.heading('id',text='کد کالا',anchor=E)
        self.kala.heading('Name',text='نام کالا',anchor=E)
        self.kala.heading('row',text='ردیف',anchor=E)
        ttk.Style().theme_use('clam')
        ttk.Style().configure("Treeview.Heading",font=('B koodak', 18),padding=[0, 5, 15, 5],background='#495057',foreground="white",bd=0,relief='flat')
        ttk.Style().map("Treeview.Heading",background=[('active','#495057')])
        ttk.Style().configure("Treeview", highlightthickness=0, height=150,bd=0, font=('AraFProgram', 16),background="white",foreground="black",rowheight = 35,fieldbackground="white")
        ttk.Style().map("Treeview",background=[('selected', '#DEE2E6')],foreground=[('selected', 'black')])
        
        self.kala.place(x = 75 , y = 477)

        self.photo_submit.bind('<Button-1>',self.change_image)
        self.Product_registration_submit.bind('<Button-1>',self.Product_registration_info)
        self.kala.bind('<Button-1>',self.show_info)
        self.kala.bind('<ButtonRelease-1>',self.show_info)
        self.search_btn.bind('<Button-1>',self.product_search)
        self.Product_registration_edit.bind('<Button-1>',self.edit)
        self.Product_registration_delete.bind('<Button-1>',self.product_delete)
        self.Product_registration_exit.bind('<Button-1>',self.product_to_home)

    def show_info(self,event = None) :
        self.product_type_combo.set("یک گزینه را انتخاب کنید")
        self.product_group_combo.set("یک گزینه را انتخاب کنید")
        self.product_code_ent.delete(0,END)
        self.product_name_ent.delete(0,END)
        self.point_purchase_ent.delete(0,END)
        self.Description_ent.delete(0,END)

        self.selected = self.kala.focus()
        self.values = self.kala.item(self.selected , "values")
        self.valuelst = self.product_sql_search(self.values[3])
        self.product_name_ent.insert(0,self.valuelst[0][1])
        self.product_code_ent.insert(0,self.valuelst[0][0])
        self.point_purchase_ent.insert(0,self.valuelst[0][2])
        self.Description_ent.insert(0,self.valuelst[0][3])
        self.product_type_combo.set(self.valuelst[0][4])
        self.product_group_combo.set(self.valuelst[0][5])

        con = sql.connect('mydb.db')
        cur = con.cursor()
        product_imh_cmd = "SELECT photoo FROM kala WHERE id = '{}'".format(self.values[3])
        cur.execute(product_imh_cmd)
        self.image_data = cur.fetchone()[0]
        self.procuct_img = Image.open(io.BytesIO(self.image_data))
        self.procuct_image = self.procuct_img.resize((220, 176))
        self.new_width = 220
        self.new_height = 175
        self.product_photo = ImageTk.PhotoImage(self.procuct_image)
        self.product_photo_label = Label(Product , image=self.product_photo)
        self.product_photo_label.place(x = 125 , y = 153)
    def edit(self,event = None):
        self.code = self.product_code_ent.get()
        self.name = self.product_name_ent.get()
        self.point = self.point_purchase_ent.get()
        self.desc = self.Description_ent.get()
        self.type = self.product_type_combo.get()
        self.group = self.product_group_combo.get()
        self.product_sql_update(self.values[3],self.code,self.name,self.point,self.desc,self.type,self.group)
        self.kala.item(self.selected ,values = (self.group,self.type,self.point,self.code,self.name,self.values[5])) 

        self.product_type_combo.set("یک گزینه را انتخاب کنید")
        self.product_group_combo.set("یک گزینه را انتخاب کنید")
        self.product_code_ent.delete(0,END)
        self.product_name_ent.delete(0,END)
        self.point_purchase_ent.delete(0,END)
        self.Description_ent.delete(0,END)

        self.procuct_img = Image.open("img/empty.png")
        self.procuct_image = self.procuct_img.resize((220, 176))
        self.product_photo = ImageTk.PhotoImage(self.procuct_image)
        self.product_photo_label = Label(Product, image=self.product_photo, width=self.new_width, height=self.new_height)
        self.product_photo_label.place(x=125, y=153) 
    def product_sql_update(self,id1,code1,name1,point1,Description1,type1,group1):
        con = sql.connect('mydb.db')
        cur = con.cursor()
        command = ' UPDATE kala SET id = "{}" , name = "{}", point = "{}", Description = "{}", type = "{}",groupp = "{}" WHERE id="{}" '.format(code1,name1,point1,Description1,type1,group1,id1)    
        cur.execute(command)    
        con.commit()
    def product_sql_search(self,id1):
        con = sql.connect('mydb.db')
        cur = con.cursor()
        row = cur.execute('SELECT * FROM kala WHERE id="{}"'.format(id1))    
        return list(row)

    def product_delete(self, event = None) :
        self.product_q = messagebox.askquestion("Confirm","آیا مطمئن هستید؟")  
        if self.product_q == "yes" :
            con = sql.connect('mydb.db')
            cur = con.cursor()

            def sql_delete(name):
                command = ' DELETE FROM kala WHERE id="{}" '.format(name)    
                cur.execute(command)    
                con.commit()
            sql_delete(self.values[3])
            self.deletee = self.kala.selection()[0]
            self.kala.delete(self.deletee)  

            self.product_type_combo.set("یک گزینه را انتخاب کنید")
            self.product_group_combo.set("یک گزینه را انتخاب کنید")
            self.product_code_ent.delete(0,END)
            self.product_name_ent.delete(0,END)
            self.point_purchase_ent.delete(0,END)
            self.Description_ent.delete(0,END)

            self.procuct_img = Image.open("img/empty.png")
            self.procuct_image = self.procuct_img.resize((220, 176))
            self.product_photo = ImageTk.PhotoImage(self.procuct_image)
            self.product_photo_label = Label(Product, image=self.product_photo, width=self.new_width, height=self.new_height)
            self.product_photo_label.place(x=125, y=153)


    def product_search(self,event = None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.idK=self.search_ent.get()
        self.product_count=0
        if self.idK !='':
            for i in self.kala.get_children():
                self.kala.delete(i)
            self.row=self.cur.execute('SELECT * FROM kala WHERE id="{}"'.format(self.idK))
            self.search_list=list(self.row)
            self.kala.insert(parent='',index='end',iid=self.product_count,text='',
            values=(self.search_list[0][5],self.search_list[0][4],self.search_list[0][2],
            self.search_list[0][0],self.search_list[0][1],str(self.product_count+1)))
        
        else:
            for item in self.kala.get_children():
                self.kala.delete(item)
                print(item)
            self.product_data_to_treeview()

    def product_data_to_treeview(self):
        self.kalalst = []
        self.product_count = 0
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        row=self.cur.execute('SELECT * FROM kala')
        for i in row :
            self.kalalst.append(i)
        for i in self.kalalst:
            self.kala.insert(parent='',index='end',iid=self.product_count,text='',
            values=(i[5],i[4],i[2],i[0],i[1],str(self.product_count+1)))
            self.product_count += 1
    def Product_registration_info(self,event = None) :
        self.code = self.product_code_ent.get()
        self.name = self.product_name_ent.get()
        self.point = self.point_purchase_ent.get()
        self.desc = self.Description_ent.get()
        self.type = self.product_type_combo.get()
        self.group = self.product_group_combo.get()
        self.photo = self.covert_to_binary_data(self.filename)

        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.data=(self.code,self.name,self.point,self.desc,self.type,0,self.group,self.photo)
        self.cur.execute('''CREATE TABLE IF NOT EXISTS kala (id   ,name TEXT ,point INTEGER,Description TEXT
        ,type TEXT,groupp TEXT,stock INTEGER,photoo BLOB)''')
        self.cur.execute('INSERT INTO kala(id,name,point,Description,type,stock,groupp,photoo) VALUES(?,?,?,?,?,?,?,?)',self.data)
        self.con.commit()

        self.product_type_combo.set("یک گزینه را انتخاب کنید")
        self.product_group_combo.set("یک گزینه را انتخاب کنید")
        self.product_code_ent.delete(0,END)
        self.product_name_ent.delete(0,END)
        self.point_purchase_ent.delete(0,END)
        self.Description_ent.delete(0,END)

        self.procuct_img = Image.open("img/empty.png")
        self.procuct_image = self.procuct_img.resize((220, 176))
        self.product_photo = ImageTk.PhotoImage(self.procuct_image)
        self.product_photo_label = Label(Product, image=self.product_photo, width=self.new_width, height=self.new_height)
        self.product_photo_label.place(x=125, y=153) 

        self.kala.insert(parent = '',index = 'end',text = 'parent',values = (self.group,self.type,self.point,self.code,self.name,self.product_count+1))
        self.product_count += 1
    def covert_to_binary_data(self,filename):
        with open (filename , 'rb') as f:
            blobdata = f.read()
        return blobdata

    def change_image(self,event = None) :
        self.filename = filedialog.askopenfilename()
        self.procuct_img = Image.open(self.filename)
        self.procuct_image = self.procuct_img.resize((220, 176))
        self.new_width = 220
        self.new_height = 175
        self.product_photo = ImageTk.PhotoImage(self.procuct_image)
        self.product_photo_label = Label(Product, image=self.product_photo, width=self.new_width, height=self.new_height)
        self.product_photo_label.place(x=125, y=153)   

        



    def User_registration(self) :
        User.state("withdraw")
        User.geometry('1400x900+300+50')
        User.title('ثبت کاربر جدید')

        self.User_registration_image = PhotoImage(file = 'img/User-registration_back.png')
        self.User_registration_img = Label(User,image = self.User_registration_image ,relief="flat")
        self.User_registration_img.place(x = 0 , y = 0)

        self.UserName = Label(User,text = ": نام",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.UserLast = Label(User,text = ": نام خانوادگی",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.UserCode = Label(User,text = ": کد ملی",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.UserGender = Label(User,text = ": جنسیت",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.UserWorkPosition = Label(User,text = ": سِمَت شغلی",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.UserName.place(x = 1177 , y = 170)
        self.UserLast.place(x = 1177 , y = 244)
        self.UserCode.place(x = 1177 , y = 318)
        self.UserGender.place(x = 824 , y = 170)
        self.UserWorkPosition.place(x = 824 , y = 245)

        self.UserName_ent = Entry(User, bg = '#FFFFFF', width = 23 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
        self.UserLast_ent = Entry(User, bg = '#FFFFFF', width = 23 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
        self.UserCode_ent = Entry(User, bg = '#FFFFFF', width = 23 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
        self.UserGender_combo = ttk.Combobox(User,width = 22 , font = ('B Koodak' , 12),justify = 'right',values=["مرد", "زن"])
        self.UserWorkPosition_combo = ttk.Combobox(User,width = 22 , font = ('B Koodak' , 12),justify = 'right',values=["فروشنده", "خریدار","کارمند","رئیس کارگاه"])
        self.UserName_ent.place(x = 945 , y = 175)
        self.UserLast_ent.place(x = 945 , y = 249)
        self.UserCode_ent.place(x = 945 , y = 323)
        self.UserGender_combo.place(x = 590 , y = 175)
        self.UserWorkPosition_combo.place(x = 590 , y = 249)
        self.UserGender_combo.set("یک گزینه را انتخاب کنید")
        self.UserWorkPosition_combo.set("یک گزینه را انتخاب کنید")

        self.user_upload_btn_img = PhotoImage(file = 'img/upload_btn.png')
        self.image_btn = Button(User,bg = "#DEE2E6",activebackground= "#DEE2E6" , image = self.user_upload_btn_img,width=178 ,relief="flat")
        self.image_btn.place(x = 217 , y = 341)

        self.user_serach_btn_img = PhotoImage(file = 'img/search_btn.png')
        self.user_search_btn = Button(User,bg = "#495057",activebackground= "#495057", image = self.user_serach_btn_img,width=150 ,relief="flat")
        self.user_search_ent = Entry(User, bg = '#FFFFFF', width = 35 , font = ('B Koodak' , 14) , relief = 'flat' , justify = 'right',fg='#495057')
        self.user_search_btn.place(x = 85 , y = 32)
        self.user_search_ent.place(x = 266 , y = 40)

        self.user_submit_img = PhotoImage(file = 'img/submit_btn.png')
        self.user_edit_img = PhotoImage(file = 'img/edit_btn.png')
        self.user_delete_img = PhotoImage(file = 'img/delete_btn.png')
        self.user_home_img = PhotoImage(file = 'img/home_btn.png')
        self.User_registration_submit = Button(User,bg = "#FFFFFF" , image = self.user_submit_img,width=197 ,relief="flat") 
        self.User_registration_edit = Button(User,bg = "#FFFFFF" , image = self.user_edit_img,width=197 ,relief="flat") 
        self.User_registration_delete = Button(User,bg = "#FFFFFF" , image = self.user_delete_img,width=197 ,relief="flat") 
        self.User_registration_exit = Button(User,bg = "#FFFFFF" , image = self.user_home_img,width=230 ,relief="flat") 
        self.User_registration_submit.place(x=50, y=815)
        self.User_registration_edit.place(x=262, y=815)    
        self.User_registration_delete.place(x=473, y=815)    
        self.User_registration_exit.place(x=1120, y=815) 

        self.user_table = ttk.Treeview(User,show='headings',height=7)
        self.user_table['columns']=('UserWorkPosition','gender','code','last','name','row')
        self.user_table.column('#0',width=0,stretch=NO)
        self.user_table.column('UserWorkPosition',width=220,anchor=E)
        self.user_table.column('gender',width=220,anchor=E)
        self.user_table.column('code',width=200,anchor=E)
        self.user_table.column('last',width=200,anchor=E)
        self.user_table.column('name',width=220,anchor=E)
        self.user_table.column('row',width=150,anchor=E)
        self.user_table.heading('#0',text='',anchor=E)
        self.user_table.heading('UserWorkPosition',text='سِمَت شغلی',anchor=E)
        self.user_table.heading('gender',text='جنسیت',anchor=E)
        self.user_table.heading('code',text='کد ملی',anchor=E)
        self.user_table.heading('last',text='نام خانوادگی',anchor=E)
        self.user_table.heading('name',text='نام',anchor=E)
        self.user_table.heading('row',text='ردیف',anchor=E)
        ttk.Style().theme_use('clam')
        ttk.Style().configure("Treeview.Heading",font=('B koodak', 18),padding=[0, 5, 15, 5],background='#495057',foreground="white",bd=0,relief='flat')
        ttk.Style().map("Treeview.Heading",background=[('active','#495057')])
        ttk.Style().configure("Treeview", highlightthickness=0, height=150,bd=0, font=('AraFProgram', 16),background="white",foreground="black",rowheight = 35,fieldbackground="white")
        ttk.Style().map("Treeview",background=[('selected', '#DEE2E6')],foreground=[('selected', 'black')])
        
        self.user_table.place(x = 75 , y = 477)

        self.image_btn.bind('<Button-1>',self.user_change_image)
        self.User_registration_submit.bind('<Button-1>',self.User_registration_info)
        self.user_table.bind('<Button-1>',self.user_show_info)
        self.user_table.bind('<ButtonRelease-1>',self.user_show_info)
        self.User_registration_edit.bind('<Button-1>',self.user_edit)
        self.User_registration_delete.bind('<Button-1>',self.user_delete)
        self.user_search_btn.bind('<Button-1>',self.user_search)
        self.User_registration_exit.bind('<Button-1>',self.user_to_home)


    def user_change_image(self,event = None) :
        self.filename = filedialog.askopenfilename()
        self.user_img = Image.open(self.filename)
        self.user_image = self.user_img.resize((220, 176))
        self.new_width = 220
        self.new_height = 175
        self.user_photo = ImageTk.PhotoImage(self.user_image)
        self.user_label = Label(User, image=self.user_photo, width=self.new_width, height=self.new_height)
        self.user_label.place(x = 197 , y = 148)

    def user_data_to_table(self):
        self.userlst = []
        self.user_count=0
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        row=self.cur.execute('SELECT * FROM user')
        for i in row :
            self.userlst.append(i)
        for i in self.userlst:
            self.user_table.insert(parent='',index='end',iid=self.user_count,text='',
            values=(i[4],i[3],i[2],i[1],i[0],str(self.user_count+1)))
            self.user_count += 1
    def User_registration_info(self,event = None) :
        self.UserN = self.UserName_ent.get()
        self.UserL = self.UserLast_ent.get()
        self.UserC = self.UserCode_ent.get()
        self.UserG = self.UserGender_combo.get()
        self.UserO = self.UserWorkPosition_combo.get()
        self.UserPhoto = self.covert_to_binary_data(self.filename)

        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.data=(self.UserN,self.UserL,self.UserC,self.UserG,self.UserO,self.UserPhoto)
        self.cur.execute('''CREATE TABLE IF NOT EXISTS user (name TEXT ,last_name TEXT,code TEXT
        ,gender TEXT,work_Pposition TEXT,photoo BLOB)''')
        self.cur.execute('INSERT INTO user(name,last_name,code,gender,work_Pposition,photoo) VALUES(?,?,?,?,?,?)',self.data)
        self.con.commit()

        self.UserName_ent.delete(0,END)
        self.UserLast_ent.delete(0,END)
        self.UserCode_ent.delete(0,END)
        self.UserGender_combo.set("یک گزینه را انتخاب کنید")
        self.UserWorkPosition_combo.set("یک گزینه را انتخاب کنید")

        self.user_img = Image.open('img/empty.png')
        self.user_image = self.user_img.resize((220, 176))
        self.new_width = 220
        self.new_height = 175
        self.user_photo = ImageTk.PhotoImage(self.user_image)
        self.user_label = Label(User, image=self.user_photo, width=self.new_width, height=self.new_height)
        self.user_label.place(x = 197 , y = 148)

        self.user_table.insert(parent = '',index = 'end',text = 'parent',values = (self.UserO,self.UserG,self.UserC,self.UserL,self.UserN,self.user_count+1))
    def covert_to_binary_data(self,filename):
        with open (filename , 'rb') as f:
            blobdata = f.read()
        return blobdata

    def user_show_info(self,event = None) :
        self.UserName_ent.delete(0,END)
        self.UserLast_ent.delete(0,END)
        self.UserCode_ent.delete(0,END)
        self.UserGender_combo.set("یک گزینه را انتخاب کنید")
        self.UserWorkPosition_combo.set("یک گزینه را انتخاب کنید")

        self.selected = self.user_table.focus()
        self.values = self.user_table.item(self.selected , "values")
        self.valuelst = self.user_sql_search(self.values[2])
        self.UserName_ent.insert(0,self.valuelst[0][0])
        self.UserLast_ent.insert(0,self.valuelst[0][1])
        self.UserCode_ent.insert(0,self.valuelst[0][2])
        self.UserGender_combo.set(self.valuelst[0][3])
        self.UserWorkPosition_combo.set(self.valuelst[0][4])

        con = sql.connect('mydb.db')
        cur = con.cursor()
        user_imh_cmd = "SELECT photoo FROM user WHERE code = '{}'".format(self.values[2])
        cur.execute(user_imh_cmd)
        self.user_image_data = cur.fetchone()[0]
        self.user_img = Image.open(io.BytesIO(self.user_image_data))
        self.user_image = self.user_img.resize((220, 176))
        self.user_photo = ImageTk.PhotoImage(self.user_image)
        self.user_photo_label = Label(User , image=self.user_photo)
        self.user_photo_label.place(x = 197 , y = 148)
    def user_edit(self,event = None):
        self.username = self.UserName_ent.get()
        self.userlast = self.UserLast_ent.get()
        self.usercode = self.UserCode_ent.get()
        self.usergender = self.UserGender_combo.get()
        self.userworkposition = self.UserWorkPosition_combo.get()
        self.user_sql_update(self.values[2],self.username,self.userlast,self.usercode,self.usergender,self.userworkposition)
        self.user_table.item(self.selected ,values = (self.userworkposition,self.usergender,self.usercode,self.userlast,self.username,self.values[5])) 

        self.UserName_ent.delete(0,END)
        self.UserLast_ent.delete(0,END)
        self.UserCode_ent.delete(0,END)
        self.UserGender_combo.set("یک گزینه را انتخاب کنید")
        self.UserWorkPosition_combo.set("یک گزینه را انتخاب کنید")
        
        self.user_img = Image.open('img/empty.png')
        self.user_image = self.user_img.resize((220, 176))
        self.user_photo = ImageTk.PhotoImage(self.user_image)
        self.user_label = Label(User, image=self.user_photo, width=self.new_width, height=self.new_height)
        self.user_label.place(x = 197 , y = 148)
    def user_sql_update(self,id1,name1,last1,code1,gender1,userworkposition1):
        con = sql.connect('mydb.db')
        cur = con.cursor()
        command = ' UPDATE user SET name = "{}" , last_name = "{}", code = "{}", gender = "{}",work_Pposition = "{}" WHERE code="{}" '.format(name1,last1,code1,gender1,userworkposition1,id1)    
        cur.execute(command)    
        con.commit()
    def user_sql_search(self,id1):
        con = sql.connect('mydb.db')
        cur = con.cursor()
        row = cur.execute('SELECT * FROM user WHERE code="{}"'.format(id1))    
        return list(row)

    def user_search(self,event = None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.userId=self.user_search_ent.get()
        self.user_count=0
        if self.userId !='':
            for i in self.user_table.get_children():
                self.user_table.delete(i)
            self.row=self.cur.execute('SELECT * FROM user WHERE code="{}"'.format(self.userId))
            self.search_list=list(self.row)
            self.user_table.insert(parent='',index='end',iid=self.user_count,text='',
            values=(self.search_list[0][4],self.search_list[0][3],self.search_list[0][2],
            self.search_list[0][1],self.search_list[0][0],str(self.user_count+1)))
        else:
            for item in self.user_table.get_children():
                self.user_table.delete(item)
            self.user_data_to_table()

    def user_delete(self, event = None) :
        self.user_q = messagebox.askquestion("Confirm","آیا مطمئن هستید؟")  
        if self.user_q == "yes" :
            con = sql.connect('mydb.db')
            cur = con.cursor()

            def sql_delete(name):
                command = ' DELETE FROM user WHERE code="{}" '.format(name)    
                cur.execute(command)    
                con.commit()
            sql_delete(self.values[2])
            self.deletee = self.user_table.selection()[0]
            self.user_table.delete(self.deletee)   

            self.UserName_ent.delete(0,END)
            self.UserLast_ent.delete(0,END)
            self.UserCode_ent.delete(0,END)
            self.UserGender_combo.set("یک گزینه را انتخاب کنید")
            self.UserWorkPosition_combo.set("یک گزینه را انتخاب کنید")
            
            self.user_img = Image.open('img/empty.png')
            self.user_image = self.user_img.resize((220, 176))
            self.user_photo = ImageTk.PhotoImage(self.user_image)
            self.user_label = Label(User, image=self.user_photo, width=self.new_width, height=self.new_height)
            self.user_label.place(x = 197 , y = 148) 





    def warehouse_stock(self) :
        stock.state("withdrawn")
        stock.geometry("1200x700+350+200")
        stock.title('موجودی انبار')

        self.stock_image = PhotoImage(file = 'img/stock_back.png')
        self.stock_img = Label(stock,image = self.stock_image ,relief="flat")
        self.stock_img.place(x = 0 , y = 0)

        self.stock_table = ttk.Treeview(stock,show='headings',height=11)
        self.stock_table['columns']=('number','type','group','code','name','row')
        self.stock_table.column('#0',width=0,stretch=NO)
        self.stock_table.column('number',width=190,anchor=E)
        self.stock_table.column('type',width=190,anchor=E)
        self.stock_table.column('group',width=190,anchor=E)
        self.stock_table.column('code',width=190,anchor=E)
        self.stock_table.column('name',width=190,anchor=E)
        self.stock_table.column('row',width=100,anchor=E)
        self.stock_table.heading('#0',text='',anchor=E)
        self.stock_table.heading('number',text='تعداد',anchor=E)
        self.stock_table.heading('type',text='نوع کالا',anchor=E)
        self.stock_table.heading('group',text='گروه کالا',anchor=E)
        self.stock_table.heading('code',text='کد کالا',anchor=E)
        self.stock_table.heading('name',text='نام کالا',anchor=E)
        self.stock_table.heading('row',text='ردیف',anchor=E)
        ttk.Style().theme_use('clam')
        ttk.Style().configure("Treeview.Heading",font=('B koodak', 18),padding=[0, 5, 15, 5],background='#495057',foreground="white",bd=0,relief='flat')
        ttk.Style().map("Treeview.Heading",background=[('active','#495057')])
        ttk.Style().configure("Treeview", highlightthickness=0, height=150,bd=0, font=('AraFProgram', 16),background="white",foreground="black",rowheight = 35,fieldbackground="white")
        ttk.Style().map("Treeview",background=[('selected', '#DEE2E6')],foreground=[('selected', 'black')])
        
        self.stock_table.place(x = 75 , y = 135)

        self.serach_btn_img = PhotoImage(file = 'img/search_btn.png')
        self.stock_search_btn = Button(stock,bg = "#495057",activebackground="#495057" , image = self.serach_btn_img,width=150 ,relief="flat")
        self.stock_search_ent = Entry(stock, bg = '#FFFFFF', width = 25 , font = ('B Koodak' , 14) , relief = 'flat' , justify = 'right',fg='#495057')
        self.stock_search_btn.place(x = 63 , y = 32)
        self.stock_search_ent.place(x = 241 , y = 40)

        self.delete_img = PhotoImage(file = 'img/delete_btn.png')
        self.User_registration_delete = Button(stock,bg = "#FFFFFF",activebackground= "#FFFFFF", image = self.delete_img,font = ('B Koodak' , 14),width=197 ,relief="flat" , fg = "#FFFFFF") 
        self.home_img = PhotoImage(file = 'img/home_btn.png')
        self.stock_exit = Button(stock,bg = "#FFFFFF" , image = self.home_img,width=230 ,relief="flat") 

        self.User_registration_delete.place(x=50, y=625)    
        self.stock_exit.place(x=920, y=625) 

        self.stock_search_btn.bind('<Button-1>',self.stock_search)
        self.stock_exit.bind('<Button-1>',self.stock_to_home)
        self.User_registration_delete.bind('<Button-1>',self.stock_delete)
        self.stock_table.bind('<Button-1>',self.stock_select)
        self.stock_table.bind('<ButtonRelease-1>',self.stock_select)
    def data_to_stock(self) :
        self.stocklst = []
        self.stock_count=0
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        row=self.cur.execute('SELECT * FROM kala')
        for i in row :
            self.stocklst.append(i)
        for i in self.stocklst:
            self.stock_table.insert(parent='',index='end',iid=self.stock_count,text='',
            values=(i[6],i[4],i[5],i[0],i[1],str(self.stock_count+1)))
            self.stock_count += 1
    def stock_search(self,event = None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.stockID=self.stock_search_ent.get()
        self.stock_count=0
        if self.stockID !='':
            for i in self.stock_table.get_children():
                self.stock_table.delete(i)
            self.row=self.cur.execute('SELECT * FROM kala WHERE id="{}"'.format(self.stockID))
            self.search_list=list(self.row)
            self.stock_table.insert(parent='',index='end',iid=self.stock_count,text='',
            values=(self.search_list[0][5],self.search_list[0][4],self.search_list[0][2],
            self.search_list[0][0],self.search_list[0][1],str(self.stock_count+1)))
    def stock_select(self, event = None) :
        self.stock_selected = self.stock_table.focus()
        self.stock_values = self.stock_table.item(self.stock_selected , "values")
    def stock_delete(self, event = None) :
        con = sql.connect('mydb.db')
        cur = con.cursor()

        def sql_delete(name):
            command = ' DELETE FROM kala WHERE id="{}" '.format(name)    
            cur.execute(command)    
            con.commit()
        sql_delete(self.stock_values[3])
        self.deletee = self.stock_table.selection()[0]
        self.stock_table.delete(self.deletee) 





    def import_product(self):
        importt.state("withdrawn")
        importt.geometry("1400x900+250+50")
        importt.title('ورود کالا')

        self.import_image = PhotoImage(file = 'img/import_product_back.png')
        self.import_img = Label(importt,image = self.import_image ,relief="flat")
        self.import_img.place(x = 0 , y = 0)

        self.import_home_img = PhotoImage(file = 'img/import_home_btn.png')
        self.import_home_btn = Button(importt,bg = "#495057" , image = self.import_home_img,font = ('B Koodak' , 13),width=189 ,relief="flat" , fg = "#000000",activebackground="#495057")
        self.import_home_btn.place(x = 75 , y = 43)

        self.import_check_img = PhotoImage(file = 'img/check_btn.png')
        self.us_code_ent = Entry(importt, bg = '#FFFFFF', width = 23 , font = ('B Koodak' , 14) , relief = 'flat' , justify = 'right',fg='#495057')
        self.us_code_btn = Button(importt,bg = "#DEE2E6" , image = self.import_check_img,font = ('B Koodak' , 13),width=130 ,relief="flat" , fg = "#000000")
        self.us_code_ent.place(x = 1073 , y = 165)
        self.us_code_btn.place(x = 924 , y = 157)
        self.pr_code_ent = Entry(importt, bg = '#FFFFFF', width = 23 , font = ('B Koodak' , 14) , relief = 'flat' , justify = 'right',fg='#495057')
        self.pr_code_btn = Button(importt,bg = "#DEE2E6" , image = self.import_check_img,font = ('B Koodak' , 13),width=130 ,relief="flat" , fg = "#000000")
        self.pr_code_ent.place(x = 1073 , y = 278)
        self.pr_code_btn.place(x = 1128 , y = 333)
        
        self.us_name_lbl = Label(importt,text = ": نام و نام خانوادگی",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.us_gender_lbl = Label(importt,text = ": جنسیت",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.us_name_lbl.place(x = 738, y = 163)
        self.us_gender_lbl.place(x = 423, y = 163)
        self.us_name = Label(importt,text= "",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#000000')
        self.us_gender = Label(importt,text= "",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#000000')
        self.us_name.place(x = 550, y = 163)
        self.us_gender.place(x = 319, y = 163)

        self.pr_name_lbl = Label(importt,text = ": نام کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.pr_point_lbl = Label(importt,text = ": نقطه خرید",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.pr_type_lbl = Label(importt,text = ": نوع کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.pr_group_lbl = Label(importt,text = ": گروه کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.pr_name_lbl.place(x = 935, y = 262)
        self.pr_point_lbl.place(x = 935 , y = 333)
        self.pr_type_lbl.place(x = 600 , y = 262)
        self.pr_group_lbl.place(x = 600 , y = 333)
        self.pr_name = Label(importt,text= "",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#000000')
        self.pr_point = Label(importt,text= "",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#000000')
        self.pr_type = Label(importt,text= "",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#000000',width =15)
        self.pr_group = Label(importt,text= "",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#000000',width =15)
        self.pr_name.place(x = 804, y = 262)
        self.pr_point.place(x = 804 , y = 333)
        self.pr_type.place(x = 320 , y = 262)
        self.pr_group.place(x = 320 , y = 333)

        self.number_lbl = Label(importt,text = ": تعداد",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.number_ent = Entry(importt, bg = '#FFFFFF', width = 22 , font = ('B Koodak' , 13) , relief = 'flat' , justify = 'right',fg='#495057')
        self.number_lbl.place(x = 1245, y = 442)
        self.number_ent.place(x = 1018, y = 450)
        self.date_lbl = Label(importt,text = ": تاریخ",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.date_cal = DateEntry(importt, width=17,font = ('B Koodak' , 12), background='#495057',sforeground='#DEE2E6', borderwidth=2,justify = 'center',relief = 'flat')
        self.date_lbl.place(x = 885, y = 442)
        self.date_cal.place(x = 657, y = 450)
        self.import_order_code_lbl = Label(importt,text = ": کد سفارش",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.import_order_code_ent = Entry(importt, bg = '#FFFFFF', width = 22 , font = ('B Koodak' , 13) , relief = 'flat' , justify = 'right',fg='#495057')
        self.import_order_code_lbl.place(x = 521, y = 442)
        self.import_order_code_ent.place(x = 291, y = 450)
        self.import_submir_img = PhotoImage(file = 'img/import_submit.png')
        self.import_submir_btn = Button(importt,bg = "#DEE2E6" , image = self.import_submir_img,font = ('B Koodak' , 13),width=138 ,relief="flat" , fg = "#000000")
        self.import_submir_btn.place(x = 116, y = 437)

        self.import_table = ttk.Treeview(importt,show='headings',height=6)
        self.import_table['columns']=('date','number','type','group','user_name','product_name','order_code','row')
        self.import_table.column('#0',width=0,stretch=NO)
        self.import_table.column('date',width=160,anchor=E)
        self.import_table.column('number',width=160,anchor=E)
        self.import_table.column('type',width=160,anchor=E)
        self.import_table.column('group',width=160,anchor=E)
        self.import_table.column('user_name',width=160,anchor=E)
        self.import_table.column('product_name',width=160,anchor=E)
        self.import_table.column('order_code',width=160,anchor=E)
        self.import_table.column('row',width=130,anchor=E)
        self.import_table.heading('#0',text='',anchor=E)
        self.import_table.heading('date',text='تاریخ',anchor=E)
        self.import_table.heading('number',text='تعداد',anchor=E)
        self.import_table.heading('type',text='نوع کالا',anchor=E)
        self.import_table.heading('group',text='گروه کالا',anchor=E)
        self.import_table.heading('user_name',text='نام و نام خانوادگی',anchor=E)
        self.import_table.heading('product_name',text='نام کالا',anchor=E)
        self.import_table.heading('order_code',text='کد سفارش',anchor=E)
        self.import_table.heading('row',text='ردیف',anchor=E)
        ttk.Style().theme_use('clam')
        ttk.Style().configure("Treeview.Heading",font=('B koodak', 18),padding=[0, 5, 15, 5],background='#495057',foreground="white",bd=0,relief='flat')
        ttk.Style().map("Treeview.Heading",background=[('active','#495057')])
        ttk.Style().configure("Treeview", highlightthickness=0, height=150,bd=0, font=('AraFProgram', 16),background="white",foreground="black",rowheight = 35,fieldbackground="white")
        ttk.Style().map("Treeview",background=[('selected', '#DEE2E6')],foreground=[('selected', 'black')])
        
        self.import_table.place(x = 75 , y = 562)

        self.us_code_btn.bind('<Button-1>',self.import_user_fill)
        self.pr_code_btn.bind('<Button-1>',self.import_prduct_fill)
        self.import_submir_btn.bind('<Button-1>',self.import_submit)
        self.import_home_btn.bind('<Button-1>',self.import_to_home)

    def import_user_fill(self,event = None) :
        try :
            self.import_user_code = self.us_code_ent.get()
            con = sql.connect('mydb.db')
            cur = con.cursor()
            self.import_user_data = cur.execute('SELECT * FROM user WHERE code="{}"'.format(self.import_user_code))
            self.import_user_data = list(self.import_user_data)
            if self.import_user_data[0][4] == "فروشنده" :
                self.fullname = self.import_user_data[0][0] + " " + self.import_user_data[0][1]
                self.us_name['text']= '{: ^20}'.format(self.fullname)
                self.us_gender['text']='{: ^10}'.format(self.import_user_data[0][3])
            else :
                messagebox.showinfo("information","کاربر با این کد ملی قادر به ثبت ورود کالا نیست")  
        except :
            messagebox.showinfo("information","کاربری با این کد ملی وجود ندارد")
    def import_prduct_fill(self,event = None) :
        self.import_product_code = self.pr_code_ent.get()
        con = sql.connect('mydb.db')
        cur = con.cursor()
        self.import_product_data = cur.execute('SELECT * FROM kala WHERE id="{}"'.format(self.import_product_code))
        self.import_product_data = list(self.import_product_data)
        self.pr_name['text']= '{: ^10}'.format(self.import_product_data[0][1])
        self.pr_point['text']='{: ^10}'.format(self.import_product_data[0][2])
        self.pr_type['text']='{: ^20}'.format(self.import_product_data[0][4])
        self.pr_group['text']='{: ^20}'.format(self.import_product_data[0][5])

        con = sql.connect('mydb.db')
        cur = con.cursor()
        import_imh_cmd = "SELECT photoo FROM kala WHERE id = '{}'".format(self.import_product_code)
        cur.execute(import_imh_cmd)
        self.image_data = cur.fetchone()[0]
        self.procuct_img = Image.open(io.BytesIO(self.image_data))
        self.procuct_image = self.procuct_img.resize((175, 124))
        self.import_photo = ImageTk.PhotoImage(self.procuct_image)
        self.import_photo_label = Label(importt , image=self.import_photo)
        self.import_photo_label.place(x = 115 , y = 260)
    def import_submit(self,event =  None) :
        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        self.import_number = self.number_ent.get()
        self.import_date = self.date_cal.get()
        self.import_order = self.import_order_code_ent.get()
        self.import_table.insert(parent = '',index = 'end',text = 'parent',values = (self.import_date,self.import_number,self.pr_type['text'],self.pr_group['text'],self.us_name['text'],self.pr_name['text'],self.import_order,self.import_count+1))
        self.edit_stck = self.cur.execute('SELECT stock FROM kala WHERE id="{}"'.format(self.import_product_code))
        self.edit_stck = list(self.edit_stck)
        self.new_stock = int(self.edit_stck[0][0]) + int(self.import_number)
        command = ' UPDATE kala SET stock = {} WHERE id="{}" '.format(self.new_stock,self.import_product_code)    
                                        
        self.import_history_data=(self.import_order ,self.pr_name['text'],self.import_product_code,self.pr_group['text'],self.pr_type['text'],self.new_stock,self.us_name['text'],self.import_user_code,self.us_gender['text'],self.import_number,self.import_date,"کالا وارد شد")
        self.cur.execute('''CREATE TABLE IF NOT EXISTS history (order_code TEXT , product_name TEXT,product_code TEXT,groupp TEXT
        ,type TEXT,stock INTEGER,user_name TEXT,user_code TEXT,user_gender TEXT,number TEXT,date TEXT,situation TEXT)''')
        self.cur.execute('INSERT INTO history(order_code,product_name,product_code,groupp,type ,stock,user_name,user_code,user_gender,number,date,situation) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',self.import_history_data)
        self.cur.execute(command)    
        self.con.commit()
        self.us_name['text'] = ""
        self.us_gender['text'] = ""
        self.pr_name['text'] = ""
        self.pr_point['text'] = ""
        self.pr_type['text'] = ""
        self.pr_group['text'] = ""
        self.us_code_ent.delete(0,END)
        self.pr_code_ent.delete(0,END)
        self.number_ent.delete(0,END)
        self.date_cal.delete(0,END)
        self.import_order_code_ent.delete(0,END)

        self.impo_empty_img = Image.open('img/import_empty.png')
        self.impo_empty_image = self.impo_empty_img.resize((175, 124))
        self.impo_empty = ImageTk.PhotoImage(self.impo_empty_image)
        self.impo_empty_label = Label(importt, image=self.impo_empty)
        self.impo_empty_label.place(x = 115 , y = 260)
    def data_to_import_table(self):
        self.import_lst = []
        self.import_count=0
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.data_imoport_command = "SELECT * FROM history WHERE situation = '{}'".format("کالا وارد شد")
        self.row=self.cur.execute(self.data_imoport_command)
        for i in self.row :
            self.import_lst.append(i)
        for i in self.import_lst:
            self.import_table.insert(parent='',index='end',iid=self.import_count,text='',
            values=(i[10],i[9],i[4],i[3],i[6],i[1],i[0],str(self.import_count+1)))
            self.import_count += 1






    def purchase_request(self) :
        purchase.state("withdrawn")
        purchase.geometry("1200x800+360+140")
        purchase.title('درخواست کالا')

        self.purchase_image = PhotoImage(file = 'img/purchase_back.png')
        self.purchase_img = Label(purchase,image = self.purchase_image ,relief="flat")
        self.purchase_img.place(x = 0 , y = 0)

        self.purchase_table = ttk.Treeview(purchase,show='headings',height=13)
        self.purchase_table['columns']=('point','number','type','group','code','name','row')
        self.purchase_table.column('#0',width=0,stretch=NO)
        self.purchase_table.column('point',width=150,anchor=E)
        self.purchase_table.column('number',width=150,anchor=E)
        self.purchase_table.column('type',width=150,anchor=E)
        self.purchase_table.column('group',width=150,anchor=E)
        self.purchase_table.column('code',width=150,anchor=E)
        self.purchase_table.column('name',width=150,anchor=E)
        self.purchase_table.column('row',width=150,anchor=E)
        self.purchase_table.heading('#0',text='',anchor=E)
        self.purchase_table.heading('point',text='نقطه خرید',anchor=E)
        self.purchase_table.heading('number',text='تعداد',anchor=E)
        self.purchase_table.heading('type',text='نوع کالا',anchor=E)
        self.purchase_table.heading('group',text='گروه کالا',anchor=E)
        self.purchase_table.heading('code',text='کد کالا',anchor=E)
        self.purchase_table.heading('name',text='نام کالا',anchor=E)
        self.purchase_table.heading('row',text='ردیف',anchor=E)
        ttk.Style().theme_use('clam')
        ttk.Style().configure("Treeview.Heading",font=('B koodak', 18),padding=[0, 5, 15, 5],background='#495057',foreground="white",bd=0,relief='flat')
        ttk.Style().map("Treeview.Heading",background=[('active','#495057')])
        ttk.Style().configure("Treeview", highlightthickness=0, height=150,bd=0, font=('AraFProgram', 16),background="white",foreground="black",rowheight = 35,fieldbackground="white")
        ttk.Style().map("Treeview",background=[('selected', '#DEE2E6')],foreground=[('selected', 'black')])
        
        self.purchase_table.place(x = 75 , y = 155)

        self.purchase_home_img = PhotoImage(file = 'img/home_btn.png')
        self.purchase_home_btn = Button(purchase,bg = "#FFFFFF" , image = self.purchase_home_img,font = ('B Koodak' , 13),width=230 ,relief="flat" , fg = "#000000",activebackground="#FFFFFF")
        self.purchase_home_btn.place(x = 919 , y = 724)
        
        self.purchase_order_img = PhotoImage(file = 'img/order_btn.png')
        self.purchase_order_btn = Button(purchase,bg = "#FFFFFF" , image = self.purchase_order_img,font = ('B Koodak' , 13),width=187 ,relief="flat" , fg = "#000000",activebackground="#FFFFFF")
        self.purchase_order_btn.place(x = 50 , y = 722)

        self.purchase_home_btn.bind('<Button-1>',self.purchase_to_home)
        self.purchase_order_btn.bind('<Button-1>',self.purchase_order)
        self.purchase_table.bind('<Button-1>',self.purchase_select)
        self.purchase_table.bind('<ButtonRelease>',self.purchase_select)

    def data_to_purchase_table(self) :
        self.purchase_lst = []
        self.purchase_count=0
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.row=self.cur.execute('SELECT * FROM kala')
        for i in self.row :
            self.purchase_lst.append(i)
        for i in self.purchase_lst:
            if int(i[2]) > int(i[6]) :
                self.purchase_table.insert(parent='',index='end',iid=self.purchase_count,text='',
                values=(i[2],i[6],i[4],i[5],i[0],i[1],str(self.purchase_count+1)))
                self.purchase_count += 1
    def purchase_order(self,event = None) :
        purchase.state("withdrawn")
        importt.state("normal")
        for item in self.purchase_table.get_children():
            self.purchase_table.delete(item)
        con = sql.connect('mydb.db')
        cur = con.cursor()
        self.import_product_data = cur.execute('SELECT * FROM kala WHERE id="{}"'.format(self.purchase_values[4]))
        self.import_product_data = list(self.import_product_data)
        self.minimum_number = int(self.import_product_data[0][2]) - int(self.import_product_data[0][6])
        self.number_ent.insert(0,self.minimum_number)
        self.pr_code_ent.insert(0,self.purchase_values[4])
        self.import_prduct_fill()
        self.data_to_import_table()
    def purchase_select(self, event = None) :
        self.purchase_selected = self.purchase_table.focus()
        self.purchase_values = self.purchase_table.item(self.purchase_selected , "values")





    def departure_product(self) :
        departure.state("withdrawn")
        departure.geometry("1500x900+250+50")
        departure.title('خروج کالا')


        self.departure_image = PhotoImage(file = 'img/departure_back.png')
        self.departure_img = Label(departure,image = self.departure_image ,relief="flat")
        self.departure_img.place(x = 0 , y = 0)

        self.check_img = PhotoImage(file = 'img/check_btn.png')
        self.departure_us_code_ent = Entry(departure, bg = '#FFFFFF', width = 25 , font = ('B Koodak' , 14) , relief = 'flat' , justify = 'right',fg='#495057')
        self.departure_us_code_btn = Button(departure,bg = "#DEE2E6" , image = self.check_img,font = ('B Koodak' , 13),width=130 ,relief="flat" , fg = "#000000")
        self.departure_us_code_ent.place(x = 1125 , y = 147)
        self.departure_us_code_btn.place(x = 1186 , y = 195)
        self.departure_pr_code_ent = Entry(departure, bg = '#FFFFFF', width = 33 , font = ('B Koodak' , 14) , relief = 'flat' , justify = 'right',fg='#495057')
        self.departure_pr_code_btn = Button(departure,bg = "#DEE2E6" , image = self.check_img,font = ('B Koodak' , 13),width=130 ,relief="flat" , fg = "#000000")
        self.departure_pr_code_ent.place(x = 636 , y = 156)
        self.departure_pr_code_btn.place(x = 469 , y = 147)
        
        self.departure_us_name_lbl = Label(departure,text = ": نام",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.departure_us_last_lbl = Label(departure,text = ": نام خانوادگی",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.departure_us_gender_lbl = Label(departure,text = ": جنسیت",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.departure_us_name_lbl.place(x = 1299, y = 271)
        self.departure_us_last_lbl.place(x = 1299, y = 321)
        self.departure_us_gender_lbl.place(x = 1299, y = 373)
        self.departure_us_name = Label(departure,text= "",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#000000')
        self.departure_us_last = Label(departure,text= "",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#000000')
        self.departure_us_gender = Label(departure,text= "",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#000000')
        self.departure_us_name.place(x = 1197, y = 271)
        self.departure_us_last.place(x = 1197, y = 321)
        self.departure_us_gender.place(x = 1197, y = 373)

        self.departure_pr_name_lbl = Label(departure,text = ": نام کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.departure_pr_number_lbl = Label(departure,text = ": موجودی",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.departure_pr_type_lbl = Label(departure,text = ": نوع کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.departure_pr_group_lbl = Label(departure,text = ": گروه کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.departure_pr_name_lbl.place(x = 960, y = 248)
        self.departure_pr_number_lbl.place(x = 960 , y = 334)
        self.departure_pr_type_lbl.place(x = 770 , y = 248)
        self.departure_pr_group_lbl.place(x = 770 , y = 334)
        self.departure_pr_name = Label(departure,text= "",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#000000')
        self.departure_pr_number = Label(departure,text= "",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#000000')
        self.departure_pr_type = Label(departure,text= "",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#000000',width= 10)
        self.departure_pr_group = Label(departure,text= "",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#000000',width= 10)
        self.departure_pr_name.place(x = 874, y = 248)
        self.departure_pr_number.place(x = 874 , y = 334)
        self.departure_pr_type.place(x = 570, y = 248)
        self.departure_pr_group.place(x = 570 , y = 334)

        self.departure_number_lbl = Label(departure,text = "تعداد",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.departure_number_ent = Entry(departure, bg = '#FFFFFF', width = 20 , font = ('B Koodak' , 13) , relief = 'flat' , justify = 'right',fg='#495057')
        self.departure_number_lbl.place(x = 179, y = 145)
        self.departure_number_ent.place(x = 113, y = 181)
        self.departure_date_lbl = Label(departure,text = "تاریخ",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.departure_date_cal = DateEntry(departure, width=17,font = ('B Koodak' , 12), background='#495057',sforeground='#DEE2E6', borderwidth=2,justify = 'center',relief = 'flat')
        self.departure_date_lbl.place(x = 179, y = 220)
        self.departure_date_cal.place(x = 125, y = 259)
        self.departure_code_lbl = Label(departure,text = "کد سفارش",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#707070')
        self.departure_code_ent = Entry(departure, bg = '#FFFFFF', width = 20 , font = ('B Koodak' , 13) , relief = 'flat' , justify = 'right',fg='#495057')
        self.departure_code_lbl.place(x = 159, y = 298)
        self.departure_code_ent.place(x = 113, y = 337)
        self.departure_submit_img = PhotoImage(file = 'img/import_submit.png')
        self.departure_submit_btn = Button(departure,bg = "#DEE2E6" , image = self.import_submir_img,font = ('B Koodak' , 13),width=138 ,relief="flat" , fg = "#000000")
        self.departure_submit_btn.place(x = 134, y = 379)

        self.departure_table = ttk.Treeview(departure,show='headings',height=6)
        self.departure_table['columns']=('situation','date','number','type','group','user_name','product_name','departure_code','row')
        self.departure_table.column('#0',width=0,stretch=NO)
        self.departure_table.column('situation',width=160,anchor=E)
        self.departure_table.column('date',width=160,anchor=E)
        self.departure_table.column('number',width=160,anchor=E)
        self.departure_table.column('type',width=160,anchor=E)
        self.departure_table.column('group',width=160,anchor=E)
        self.departure_table.column('user_name',width=160,anchor=E)
        self.departure_table.column('product_name',width=160,anchor=E)
        self.departure_table.column('departure_code',width=160,anchor=E)
        self.departure_table.column('row',width=70,anchor=E)
        self.departure_table.heading('#0',text='',anchor=E)
        self.departure_table.heading('situation',text='وضعیت',anchor=E)
        self.departure_table.heading('date',text='تاریخ',anchor=E)
        self.departure_table.heading('number',text='تعداد',anchor=E)
        self.departure_table.heading('type',text='نوع کالا',anchor=E)
        self.departure_table.heading('group',text='گروه کالا',anchor=E)
        self.departure_table.heading('user_name',text='نام و نام خانوادگی',anchor=E)
        self.departure_table.heading('product_name',text='نام کالا',anchor=E)
        self.departure_table.heading('departure_code',text='کد',anchor=E)
        self.departure_table.heading('row',text='ردیف',anchor=E)
        ttk.Style().theme_use('clam')
        ttk.Style().configure("Treeview.Heading",font=('B koodak', 18),padding=[0, 5, 15, 5],background='#495057',foreground="white",bd=0,relief='flat')
        ttk.Style().map("Treeview.Heading",background=[('active','#495057')])
        ttk.Style().configure("Treeview", highlightthickness=0, height=150,bd=0, font=('AraFProgram', 16),background="white",foreground="black",rowheight = 35,fieldbackground="white")
        ttk.Style().map("Treeview",background=[('selected', '#DEE2E6')],foreground=[('selected', 'black')])
        
        self.departure_table.place(x = 75 , y = 500)

        self.departure_change_situation_image = PhotoImage(file = 'img/change_situation_btn.png')
        self.departure_change_situation_btn = Button(departure,bg = "#FFFFFF" , image = self.departure_change_situation_image,font = ('B Koodak' , 13),width=230 ,relief="flat" , fg = "#000000")
        self.departure_change_situation_btn.place(x = 51 , y = 815)

        self.departure_home_image = PhotoImage(file = 'img/home_btn.png')
        self.departure_home_btn = Button(departure,bg = "#FFFFFF" , image = self.departure_home_image,font = ('B Koodak' , 13),width=230 ,relief="flat" , fg = "#000000")
        self.departure_home_btn.place(x = 1219 , y = 815)

        self.departure_us_code_btn.bind('<Button-1>',self.departure_user_fill)
        self.departure_pr_code_btn.bind('<Button-1>',self.departure_prduct_fill)
        self.departure_submit_btn.bind('<Button-1>',self.departure_submit)
        self.departure_table.bind('<Button-1>',self.departure_select)
        self.departure_table.bind('<ButtonRelease>',self.departure_select)
        self.departure_change_situation_btn.bind('<Button-1>',self.change_situation)
        self.departure_home_btn.bind('<Button-1>',self.departure_to_home)

    def departure_user_fill(self,event = None) :
        try :
            self.departure_user_code = self.departure_us_code_ent.get()
            con = sql.connect('mydb.db')
            cur = con.cursor()
            self.departure_user_data = cur.execute('SELECT * FROM user WHERE code="{}"'.format(self.departure_user_code))
            self.departure_user_data = list(self.departure_user_data)
            if self.departure_user_data[0][4] == "کارمند" :
                self.departure_us_name['text']= '{: ^10}'.format(self.departure_user_data[0][0])
                self.departure_us_last['text']= '{: ^10}'.format(self.departure_user_data[0][1])
                self.departure_us_gender['text']='{: ^10}'.format(self.departure_user_data[0][3])
            else :
                messagebox.showinfo("information","کاربر با این کد ملی قادر به ثبت ورود کالا نیست")  
        except :
            messagebox.showinfo("information","کاربری با این کد ملی وجود ندارد")
    def departure_prduct_fill(self,event = None) :
        self.departure_product_code = self.departure_pr_code_ent.get()
        con = sql.connect('mydb.db')
        cur = con.cursor()
        self.departure_product_data = cur.execute('SELECT * FROM kala WHERE id="{}"'.format(self.departure_product_code))
        self.departure_product_data = list(self.departure_product_data)
        self.departure_pr_name['text']= '{: ^10}'.format(self.departure_product_data[0][1])
        self.departure_pr_number['text']='{: ^10}'.format(self.departure_product_data[0][6])
        self.departure_pr_type['text']='{: ^20}'.format(self.departure_product_data[0][4])
        self.departure_pr_group['text']='{: ^20}'.format(self.departure_product_data[0][5])

        con = sql.connect('mydb.db')
        cur = con.cursor()
        departure_imh_cmd = "SELECT photoo FROM kala WHERE id = '{}'".format(self.departure_product_code)
        cur.execute(departure_imh_cmd)
        self.image_data = cur.fetchone()[0]
        self.procuct_img = Image.open(io.BytesIO(self.image_data))
        self.procuct_image = self.procuct_img.resize((170, 160))
        self.departure_photo = ImageTk.PhotoImage(self.procuct_image)
        self.departure_photo_label = Label(departure , image=self.departure_photo)
        self.departure_photo_label.place(x = 367 , y = 239)
        
    def departure_submit(self,event = None) :
        self.departure_number = self.departure_number_ent.get()
        self.departure_date = self.departure_date_cal.get()
        self.departure_code = self.departure_code_ent.get()
        # self.import_count = 0
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.departure_fullname = self.departure_user_data[0][0] + " " + self.departure_user_data[0][1]

        self.departure_table.insert(parent = '',index = 'end',text = 'parent',values = ("در حال بررسی",self.departure_date,self.departure_number,self.departure_pr_type['text'],self.departure_pr_group['text'],self.departure_fullname,self.departure_pr_name['text'],self.departure_code,self.departure_count+1))
        self.departure_product_data = self.cur.execute('SELECT * FROM kala WHERE id="{}"'.format(self.departure_product_code))
        self.departure_product_data = list(self.departure_product_data)
        self.history_data=(self.departure_code ,self.departure_pr_name['text'],self.departure_product_code,self.departure_pr_group['text'],self.departure_pr_type['text'],self.departure_product_data[0][6],self.departure_fullname,self.departure_user_code,self.departure_us_gender['text'],self.departure_number,self.departure_date,"در حال بررسی")
        self.cur.execute('''CREATE TABLE IF NOT EXISTS history (order_code TEXT , product_name TEXT,product_code TEXT,groupp TEXT
        ,type TEXT,stock INTEGER,user_name TEXT,user_code TEXT,user_gender TEXT,number TEXT,date TEXT,situation TEXT)''')
        self.cur.execute('INSERT INTO history(order_code,product_name,product_code,groupp,type ,stock,user_name,user_code,user_gender,number,date,situation) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',self.history_data)
        self.con.commit()
        self.departure_us_name['text'] = ""
        self.departure_us_last['text'] = ""
        self.departure_us_gender['text'] = ""
        self.departure_pr_name['text'] = ""
        self.departure_pr_number['text'] = ""
        self.departure_pr_type['text'] = ""
        self.departure_pr_group['text'] = ""
        self.departure_us_code_ent.delete(0,END)
        self.departure_pr_code_ent.delete(0,END)
        self.departure_number_ent.delete(0,END)
        self.departure_code_ent.delete(0,END)
        self.departure_date_cal.delete(0,END)

        self.departure_empty_img = Image.open('img/import_empty.png')
        self.departure_empty_image = self.departure_empty_img.resize((170, 160))
        self.departure_empty = ImageTk.PhotoImage(self.departure_empty_image)
        self.departure_empty_label = Label(departure, image=self.departure_empty)
        self.departure_empty_label.place(x = 367 , y = 239)
    def data_to_departure_table(self):
        self.departure_lst = []
        self.departure_count=0
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.data_departuret_command = "SELECT * FROM history WHERE situation = 'در حال بررسی' OR situation = 'آماده تحویل' OR situation = 'تحویل داده شده'"

        self.row=self.cur.execute(self.data_departuret_command)

        for i in self.row :
            self.departure_lst.append(i)
        for i in self.departure_lst:
            self.departure_table.insert(parent='',index='end',iid=self.departure_count,text='',
            values=(i[11],i[10],i[9],i[4],i[3],i[6],i[1],i[0],str(self.departure_count+1)))
            self.departure_count += 1
    def departure_select(self, event = None) :
        self.departure_selected = self.departure_table.focus()
        self.departure_values = self.departure_table.item(self.departure_selected , "values")
        # self.departure_values = list(self.departure_values)
        con = sql.connect('mydb.db')
        cur = con.cursor()        
        self.departure_select_data = cur.execute('SELECT * FROM history WHERE order_code="{}"'.format(self.departure_values[7]))
        self.departure_select_data = list(self.departure_select_data)
        self.departure_user_data = cur.execute('SELECT * FROM user WHERE code="{}"'.format(self.departure_select_data[0][7]))
        self.departure_user_data = list(self.departure_user_data)
        self.departure_pr_name['text']= '{: ^10}'.format(self.departure_select_data[0][1])
        self.departure_pr_number['text']='{: ^10}'.format(self.departure_select_data[0][5])
        self.departure_pr_group['text']='{: ^20}'.format(self.departure_select_data[0][3])
        self.departure_pr_type['text']='{: ^20}'.format(self.departure_select_data[0][4])
        self.departure_us_name['text']= '{: ^10}'.format(self.departure_user_data[0][0])
        self.departure_us_last['text']= '{: ^10}'.format(self.departure_user_data[0][1])
        self.departure_us_gender['text']='{: ^10}'.format(self.departure_user_data[0][3])
        self.departure_number_ent.delete(0,END)
        self.departure_number_ent.insert(0,self.departure_select_data[0][9])
        self.departure_date_cal.delete(0,END)
        self.departure_date_cal.insert(0,self.departure_select_data[0][10])
        self.departure_code_ent.delete(0,END)
        self.departure_code_ent.insert(0,self.departure_select_data[0][0])
        self.departure_pr_code_ent.delete(0,END)
        self.departure_pr_code_ent.insert(0,self.departure_select_data[0][2])
        self.departure_us_code_ent.delete(0,END)
        print(self.departure_pr_code_ent.get())
        self.departure_us_code_ent.insert(0,self.departure_select_data[0][7])
        departure_imh_cmd = "SELECT photoo FROM kala WHERE id = '{}'".format(self.departure_pr_code_ent.get())
        cur.execute(departure_imh_cmd)
        self.image_data = cur.fetchone()[0]
        self.procuct_img = Image.open(io.BytesIO(self.image_data))
        self.procuct_image = self.procuct_img.resize((170, 160))
        self.departure_photo = ImageTk.PhotoImage(self.procuct_image)
        self.departure_photo_label = Label(departure , image=self.departure_photo)
        self.departure_photo_label.place(x = 367 , y = 239)
    def change_situation(self, event = None) :
        con = sql.connect('mydb.db')
        cur = con.cursor()
        self.departure_situation_data = cur.execute('SELECT * FROM history WHERE order_code="{}"'.format(self.departure_values[7]))
        self.departure_situation_data = list(self.departure_situation_data)

        if self.departure_situation_data[0][11] == "در حال بررسی" :
            self.departure_situation = "آماده تحویل"
        elif self.departure_situation_data[0][11] == "آماده تحویل" :
            print("asd")
            self.departure_situation = "تحویل داده شده"
            self.departure_edit_stock = cur.execute('SELECT stock FROM kala WHERE id="{}"'.format(self.departure_situation_data[0][2]))
            self.departure_edit_stock = list(self.departure_edit_stock)
            self.departure_new_stock = int(self.departure_edit_stock[0][0]) - int((self.departure_situation_data[0][9]))
            cur.execute(' UPDATE kala SET stock = {} WHERE id="{}" '.format(self.departure_new_stock,self.departure_situation_data[0][2]))  
            cur.execute(' UPDATE history SET stock = {} WHERE order_code="{}" '.format(self.departure_new_stock,self.departure_situation_data[0][0]))  
        command_upadate_situation = ' UPDATE history SET situation = "{}"  WHERE order_code="{}" '.format(self.departure_situation,self.departure_values[7])    
        cur.execute(command_upadate_situation)    
        con.commit()
        self.departure_table.item(self.departure_selected ,values = (self.departure_situation,self.departure_values[1],self.departure_values[2],self.departure_values[3],self.departure_values[4],self.departure_values[5],self.departure_values[6],self.departure_values[7],self.departure_values[8])) 
        self.departure_us_name['text'] = ""
        self.departure_us_last['text'] = ""
        self.departure_us_gender['text'] = ""
        self.departure_pr_name['text'] = ""
        self.departure_pr_number['text'] = ""
        self.departure_pr_type['text'] = ""
        self.departure_pr_group['text'] = ""
        self.departure_us_code_ent.delete(0,END)
        self.departure_pr_code_ent.delete(0,END)
        self.departure_number_ent.delete(0,END)
        self.departure_code_ent.delete(0,END)
        self.departure_date_cal.delete(0,END)

        self.departure_empty_img = Image.open('img/import_empty.png')
        self.departure_empty_image = self.departure_empty_img.resize((170, 160))
        self.departure_empty = ImageTk.PhotoImage(self.departure_empty_image)
        self.departure_empty_label = Label(departure, image=self.departure_empty)
        self.departure_empty_label.place(x = 367 , y = 239)





    def order_history(self) :
        history.state("withdraw")
        history.geometry("1200x800+360+100")
        history.title('تاریخچه سفارشات')

        self.history_image = PhotoImage(file = 'img/history_back.png')
        self.history_img = Label(history,image = self.history_image ,relief="flat")
        self.history_img.place(x = 0 , y = 0)

        self.history_table = ttk.Treeview(history,show='headings',height=13)
        self.history_table['columns']=('point','type','group','code','name','row')
        self.history_table.column('#0',width=0,stretch=NO)
        self.history_table.column('point',width=175,anchor=E)
        # self.history_table.column('number',width=150,anchor=E)
        self.history_table.column('type',width=175,anchor=E)
        self.history_table.column('group',width=175,anchor=E)
        self.history_table.column('code',width=175,anchor=E)
        self.history_table.column('name',width=175,anchor=E)
        self.history_table.column('row',width=175,anchor=E)
        self.history_table.heading('#0',text='',anchor=E)
        self.history_table.heading('point',text='نقطه خرید',anchor=E)

        self.history_table.heading('type',text='نوع کالا',anchor=E)
        self.history_table.heading('group',text='گروه کالا',anchor=E)
        self.history_table.heading('code',text='کد کالا',anchor=E)
        self.history_table.heading('name',text='نام کالا',anchor=E)
        self.history_table.heading('row',text='ردیف',anchor=E)
        ttk.Style().theme_use('clam')
        ttk.Style().configure("Treeview.Heading",font=('B koodak', 18),padding=[0, 5, 15, 5],background='#495057',foreground="white",bd=0,relief='flat')
        ttk.Style().map("Treeview.Heading",background=[('active','#495057')])
        ttk.Style().configure("Treeview", highlightthickness=0, height=150,bd=0, font=('AraFProgram', 16),background="white",foreground="black",rowheight = 35,fieldbackground="white")
        ttk.Style().map("Treeview",background=[('selected', '#DEE2E6')],foreground=[('selected', 'black')])
        
        self.history_table.place(x = 75 , y = 155)

        self.history_show_image = PhotoImage(file = 'img/show_btn.png')
        self.history_show_btn = Button(history,bg = "#FFFFFF" , image = self.history_show_image,font = ('B Koodak' , 13),width=200 ,relief="flat" , fg = "#000000")
        self.history_show_btn.place(x = 50 , y = 722)

        self.history_home_img = PhotoImage(file = 'img/home_btn.png')
        self.history_home_btn = Button(history,bg = "#FFFFFF" , image = self.history_home_img,font = ('B Koodak' , 13),width=230 ,relief="flat" , fg = "#000000",activebackground="#FFFFFF")
        self.history_home_btn.place(x = 919 , y = 724)
        
        self.history_table.bind('<Button-1>',self.history_select)
        self.history_table.bind('<ButtonRelease>',self.history_select)
        self.history_show_btn.bind('<Button-1>',self.history_show)
        self.history_home_btn.bind('<Button-1>',self.history_to_home)
    def history_table_by_Date(self) :
        self.history_count = 0
        con = sql.connect('mydb.db')
        cur = con.cursor() 

        row =cur.execute('SELECT * FROM kala')
        self.his_lst = []
        for i in row :
            self.his_lst.append(i)
        for i in self.his_lst:
            self.history_table.insert(parent='',index='end',iid=self.history_count,text='',
            values=(i[2],i[4],i[5],i[0],i[1],str(self.history_count+1)))
            self.history_count += 1
        self.history_df = pd.read_sql_query("SELECT * FROM history",con)
        
    def history_select(self,event = None) :
        self.history_selected = self.history_table.focus()
        self.history_values = self.history_table.item(self.history_selected , "values")
    def history_show(self,event = None) :
        print(self.history_values[3])
        self.plot_df = self.history_df[((self.history_df['situation'] == "تحویل داده شده") | (self.history_df['situation'] == "کالا وارد شد")) & (self.history_df['product_code'] == self.history_values[3])] 
        self.plot_df = self.plot_df.filter(items = ["stock","date"])
        self.plot_df['date'] = pd.to_datetime(self.plot_df['date'])
        self.plot_df = self.plot_df.sort_values('date')
        self.x = self.plot_df["date"].tolist()
        self.y = self.plot_df["stock"].tolist()

        fig = plt.figure(figsize  = (12,7))
        plt.plot(self.x,self.y , color = 'b' ,
            linewidth = 1 , 
            linestyle = '--' , 
            marker = 'o',
            markersize = 8 , 
            markerfacecolor = 'lightblue',
            markeredgecolor = 'brown',
            markeredgewidth = 1   
        )

        plt.grid(which = 'both' ,color = 'grey' ,linestyle = '-.' ,linewidth = 0.5)

        plt.show()

        self.frm  = LabelFrame(self , text = 'Plot' , padx = 5 , pady = 10)
        self.frm.place(x = 50 , y = 0)
        bar = FigureCanvasTkAgg(fig,self.frm)
        bar.get_tk_widget().pack(side = LEFT , fill = BOTH)





    def billing(self) :
        bill_main.state("withdrawn")
        bill_main.geometry("1200x800+360+100")
        bill_main.title("صدور قبض")
        self.bill_image = PhotoImage(file = 'img/bill_back.png')
        self.bill_img = Label(bill_main,image = self.bill_image ,relief="flat")
        self.bill_img.place(x = 0 , y = 0)

        self.bill_table = ttk.Treeview(bill_main,show='headings',height=13)
        self.bill_table['columns']=('point','type','group','code','name','row')
        self.bill_table.column('#0',width=0,stretch=NO)
        self.bill_table.column('point',width=175,anchor=E)
        self.bill_table.column('type',width=175,anchor=E)
        self.bill_table.column('group',width=175,anchor=E)
        self.bill_table.column('code',width=175,anchor=E)
        self.bill_table.column('name',width=175,anchor=E)
        self.bill_table.column('row',width=175,anchor=E)
        self.bill_table.heading('#0',text='',anchor=E)
        self.bill_table.heading('point',text='نقطه خرید',anchor=E)
        self.bill_table.heading('type',text='نوع کالا',anchor=E)
        self.bill_table.heading('group',text='گروه کالا',anchor=E)
        self.bill_table.heading('code',text='کد کالا',anchor=E)
        self.bill_table.heading('name',text='نام کالا',anchor=E)
        self.bill_table.heading('row',text='ردیف',anchor=E)
        ttk.Style().theme_use('clam')
        ttk.Style().configure("Treeview.Heading",font=('B koodak', 18),padding=[0, 5, 15, 5],background='#495057',foreground="white",bd=0,relief='flat')
        ttk.Style().map("Treeview.Heading",background=[('active','#495057')])
        ttk.Style().configure("Treeview", highlightthickness=0, height=150,bd=0, font=('AraFProgram', 16),background="white",foreground="black",rowheight = 35,fieldbackground="white")
        ttk.Style().map("Treeview",background=[('selected', '#DEE2E6')],foreground=[('selected', 'black')])
        
        self.bill_table.place(x = 75 , y = 155)

        self.bill_show_image = PhotoImage(file = 'img/bill_show_btn.png')
        self.bill_show_btn = Button(bill_main,bg = "#FFFFFF" , image = self.bill_show_image,font = ('B Koodak' , 13),width=200 ,relief="flat" , fg = "#000000")
        self.bill_show_btn.place(x = 50 , y = 722)
        
        self.Mbill_home_img = PhotoImage(file = 'img/home_btn.png')
        self.Mbill_home_btn = Button(bill_main,bg = "#FFFFFF" , image = self.Mbill_home_img,font = ('B Koodak' , 13),width=230 ,relief="flat" , fg = "#000000",activebackground="#FFFFFF")
        self.Mbill_home_btn.place(x = 919 , y = 724)

        self.bill_table.bind('<Button-1>',self.bill_main_select)
        self.bill_table.bind('<ButtonRelease>',self.bill_main_select)
        self.bill_show_btn.bind('<Button-1>',self.Mbill_to_Dbill)
        self.Mbill_home_btn.bind('<Button-1>',self.bill_to_home)
    def data_to_bill_main(self) :
        self.bill_count = 0
        con = sql.connect('mydb.db')
        cur = con.cursor() 

        row =cur.execute('SELECT * FROM kala')
        self.Mbill_lst = []
        for i in row :
            self.Mbill_lst.append(i)
        for i in self.Mbill_lst:
            self.bill_table.insert(parent='',index='end',iid=self.bill_count,text='',
            values=(i[2],i[4],i[5],i[0],i[1],str(self.bill_count+1)))
            self.bill_count += 1
    def bill_main_select(self,event = None) :
        self.bill_selected = self.bill_table.focus()
        self.bill_values = self.bill_table.item(self.bill_selected , "values")

    def Mbill_to_Dbill(self,event = None) :
        bill_detail.state("normal")
        bill_main.state("withdrawn")
        self.data_to_detail_bill()



    def bill_detaill(self) :
        bill_detail.state("withdrawn")
        bill_detail.geometry("1200x800+360+100")
        bill_detail.title("صدور قبض")

        self.bill_detail_image = PhotoImage(file = 'img/bill_back.png')
        self.bill_detail_img = Label(bill_detail,image = self.bill_detail_image ,relief="flat")
        self.bill_detail_img.place(x = 0 , y = 0)

        self.bill_detail_table = ttk.Treeview(bill_detail,show='headings',height=13)
        self.bill_detail_table['columns']=('situation','number','user_name','prodoct_name','date','order_code','row')
        self.bill_detail_table.column('#0',width=0,stretch=NO)
        self.bill_detail_table.column('situation',width=160,anchor=E)
        self.bill_detail_table.column('number',width=160,anchor=E)
        self.bill_detail_table.column('user_name',width=160,anchor=E)
        self.bill_detail_table.column('prodoct_name',width=160,anchor=E)
        self.bill_detail_table.column('date',width=160,anchor=E)
        self.bill_detail_table.column('order_code',width=160,anchor=E)
        self.bill_detail_table.column('row',width=90,anchor=E)
        self.bill_detail_table.heading('#0',text='',anchor=E)
        self.bill_detail_table.heading('situation',text='وضعیت',anchor=E)
        self.bill_detail_table.heading('number',text='تعداد',anchor=E)
        self.bill_detail_table.heading('user_name',text='نام شخص',anchor=E)
        self.bill_detail_table.heading('prodoct_name',text='نام کالا',anchor=E)
        self.bill_detail_table.heading('date',text='تاریخ',anchor=E)
        self.bill_detail_table.heading('order_code',text='شماره سفارش',anchor=E)
        self.bill_detail_table.heading('row',text='ردیف',anchor=E)
        ttk.Style().theme_use('clam')
        ttk.Style().configure("Treeview.Heading",font=('B koodak', 18),padding=[0, 5, 15, 5],background='#495057',foreground="white",bd=0,relief='flat')
        ttk.Style().map("Treeview.Heading",background=[('active','#495057')])
        ttk.Style().configure("Treeview", highlightthickness=0, height=150,bd=0, font=('AraFProgram', 16),background="white",foreground="black",rowheight = 35,fieldbackground="white")
        ttk.Style().map("Treeview",background=[('selected', '#DEE2E6')],foreground=[('selected', 'black')])
        
        self.bill_detail_table.place(x = 75 , y = 155)
        
        self.Dbill_home_img = PhotoImage(file = 'img/back_btn.png')
        self.Dbill_home_btn = Button(bill_detail,bg = "#FFFFFF" , image = self.Dbill_home_img,font = ('B Koodak' , 13),width=230 ,relief="flat" , fg = "#000000",activebackground="#FFFFFF")
        self.Dbill_home_btn.place(x = 919 , y = 724)

        self.Dbill_show_image = PhotoImage(file = 'img/bill_show_btn.png')
        self.Dbill_show_btn = Button(bill_detail,bg = "#FFFFFF" , image = self.Dbill_show_image,font = ('B Koodak' , 13),width=200 ,relief="flat" , fg = "#000000")
        self.Dbill_show_btn.place(x = 35 , y = 722)

        self.bill_detail_table.bind('<Button-1>',self.bill_detail_select)
        self.bill_detail_table.bind('<ButtonRelease>',self.bill_detail_select)
        self.Dbill_show_btn.bind('<Button-1>',self.fill_bill)
        self.Dbill_home_btn.bind('<Button-1>',self.Dbill_to_Mbill)
    def data_to_detail_bill(self) :
        self.bill_count = 0
        con = sql.connect('mydb.db')
        cur = con.cursor() 
        query = "SELECT * FROM history WHERE product_code = '{}'".format(self.bill_values[3])
        result = cur.execute(query).fetchall()
        for i in result:
            self.bill_detail_table.insert(parent='',index='end',iid=self.bill_count,text='',
            values=(i[11],i[9],i[6],i[1],i[10],i[0],str(self.bill_count+1)))
            self.bill_count += 1
    def bill_detail_select(self,event = None) :
        self.bill_detail_selected = self.bill_detail_table.focus()
        self.bill_detail_values = self.bill_detail_table.item(self.bill_detail_selected , "values")
    def show_bill(self,event = None) :
        bill.state("withdrawn")
        bill.geometry("1200x800+360+140") 

        self.bill_main_image = PhotoImage(file = 'img/billl_back.png')
        self.bill_main_img = Label(bill,image = self.bill_main_image ,relief="flat")
        self.bill_main_img.place(x = 0 , y = 0)

        self.bill_order_code_lbl = Label(bill,text = ": کد سفارش",font = ('B Koodak' , 20),bg = '#495057',fg = '#DEE2E6')
        self.bill_product_code_lbl = Label(bill,text = ": کد محصول",font = ('B Koodak' , 20),bg = '#495057',fg = '#DEE2E6')
        self.bill_product_name_lbl = Label(bill,text = ": نام محصول",font = ('B Koodak' , 20),bg = '#495057',fg = '#DEE2E6')
        self.bill_situation_lbl = Label(bill,text = ": وضعیت",font = ('B Koodak' , 20),bg = '#495057',fg = '#DEE2E6')
        self.bill_user_name_lbl = Label(bill,text = ": نام",font = ('B Koodak' , 20),bg = '#495057',fg = '#DEE2E6')
        self.bill_user_code_lbl = Label(bill,text = ": کد ملی",font = ('B Koodak' , 20),bg = '#495057',fg = '#DEE2E6')
        self.bill_order_code_lbl.place(x = 969, y = 170)
        self.bill_product_code_lbl.place(x = 969, y = 258)
        self.bill_product_name_lbl.place(x = 969, y = 346)
        self.bill_situation_lbl.place(x = 519, y = 170)
        self.bill_user_name_lbl.place(x = 519, y = 258)
        self.bill_user_code_lbl.place(x = 519, y = 346)
        self.bill_date_lbl = Label(bill,text = ": تاریخ",font = ('B Koodak' , 15),bg = '#DEE2E6',fg = '#495057')
        self.bill_number_lbl = Label(bill,text = ": تعداد",font = ('B Koodak' , 15),bg = '#DEE2E6',fg = '#495057')
        self.bill_stock_lbl = Label(bill,text = ": موجودی",font = ('B Koodak' , 25),bg = '#DEE2E6',fg = '#495057')
        self.bill_date_lbl.place(x = 913, y = 530)
        self.bill_number_lbl.place(x = 491, y = 530)
        self.bill_stock_lbl.place(x = 657, y = 590)

        self.bill_order_code = Label(bill,font = ('B Koodak' , 20),bg = '#495057',fg = '#FFFFFF',width = 12)
        self.bill_product_code = Label(bill,font = ('B Koodak' , 20),bg = '#495057',fg = '#FFFFFF',width = 12)
        self.bill_product_name = Label(bill,font = ('B Koodak' , 20),bg = '#495057',fg = '#FFFFFF',width = 12)
        self.bill_situation = Label(bill,font = ('B Koodak' , 20),bg = '#495057',fg = '#FFFFFF',width = 15)
        self.bill_user_name = Label(bill,font = ('B Koodak' , 20),bg = '#495057',fg = '#FFFFFF',width = 15)
        self.bill_user_code = Label(bill,font = ('B Koodak' , 20),bg = '#495057',fg = '#FFFFFF',width = 15)
        self.bill_order_code.place(x = 720, y = 170)
        self.bill_product_code.place(x = 720, y = 258)
        self.bill_product_name.place(x = 720, y = 346)
        self.bill_situation.place(x = 245, y = 170)
        self.bill_user_name.place(x = 245, y = 258)
        self.bill_user_code.place(x = 245, y = 346)
        self.bill_date = Label(bill,font = ('B Koodak' , 15),bg = '#DEE2E6',fg = '#000000')
        self.bill_number = Label(bill,font = ('B Koodak' , 15),bg = '#DEE2E6',fg = '#000000')
        self.bill_stock = Label(bill,font = ('B Koodak' , 25),bg = '#DEE2E6',fg = '#000000')
        self.bill_date.place(x = 773, y = 530)
        self.bill_number.place(x = 400, y = 530)
        self.bill_stock.place(x = 547, y = 590)

        self.bill_back_img = PhotoImage(file = 'img/back_btn.png')
        self.bill_back = Button(bill,bg = "#FFFFFF",activebackground= "#FFFFFF", image = self.bill_back_img,width=230 ,relief="flat") 
        self.bill_home_img = PhotoImage(file = 'img/home_btn.png')
        self.bill_exit = Button(bill,bg = "#FFFFFF" , image = self.bill_home_img,width=230 ,relief="flat") 

        self.bill_back.place(x=50, y=715)    
        self.bill_exit.place(x=920, y=715) 

        self.bill_back.bind('<Button-1>',self.bill_to_Dbill)
        self.bill_exit.bind('<Button-1>',self.bill_to_main)

    def fill_bill(self,event = None) :
        bill_detail.state("withdrawn")
        bill.state("normal")
        bill.title("صدور قبض")

        con = sql.connect('mydb.db')
        cur = con.cursor()        
        self.bill_select_data = cur.execute('SELECT * FROM history WHERE order_code="{}"'.format(self.bill_detail_values[5]))
        self.bill_select_data = list(self.bill_select_data)        
        self.bill_order_code['text']='{: ^20}'.format(self.bill_select_data[0][0])
        self.bill_product_code['text']='{: ^20}'.format(self.bill_select_data[0][2])
        self.bill_product_name['text']='{: ^20}'.format(self.bill_select_data[0][1])
        self.bill_situation['text']='{: ^20}'.format(self.bill_select_data[0][11])
        self.bill_user_name['text']='{: ^20}'.format(self.bill_select_data[0][6])
        self.bill_user_code['text']='{: ^20}'.format(self.bill_select_data[0][7])
        self.bill_date['text']='{: ^10}'.format(self.bill_select_data[0][10])
        self.bill_number['text']='{: ^10}'.format(self.bill_select_data[0][9])
        self.bill_stock['text']='{: ^10}'.format(self.bill_select_data[0][5])


program = home(main)
main.mainloop()

