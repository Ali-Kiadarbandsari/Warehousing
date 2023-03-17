import sqlite3 as sql
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
class main(Tk):
    def __init__(self) :
        Tk.__init__(self)
        # self.check()
        # self.register()
        # self.login()
        # self.main()
        self.Product_registration()
#----------------------------------------------------------------------------------------------------------


    # def main(self) :
    #     self.geometry('1200x680+550+150')
    #     self.title('main')

    #     self.main_image = PhotoImage(file = 'D:/123/!python/Projects/anbardari/img/main_back.png')
    #     self.main_img = Label(self,image = self.main_image ,relief="flat")
    #     self.main_img.place(x = 0 , y = 0)

    #     self.btn1 = Button(self,text = "ورود به صفحه" ,relief="flat" ,font = ('B Koodak' , 12),width = 15,fg = "#DEE2E6", bg = "#495057",activebackground = '#495057')
    #     self.btn2 = Button(self,text = "ورود به صفحه" ,relief="flat" ,font = ('B Koodak' , 12),width = 15,fg = "#DEE2E6", bg = "#495057",activebackground = '#495057')
    #     self.btn3 = Button(self,text = "ورود به صفحه" ,relief="flat" ,font = ('B Koodak' , 12),width = 15,fg = "#DEE2E6", bg = "#495057",activebackground = '#495057')
    #     self.btn4 = Button(self,text = "ورود به صفحه" ,relief="flat" ,font = ('B Koodak' , 12),width = 15,fg = "#DEE2E6", bg = "#495057",activebackground = '#495057')
    #     self.btn5 = Button(self,text = "ورود به صفحه" ,relief="flat" ,font = ('B Koodak' , 12),width = 15,fg = "#DEE2E6", bg = "#495057",activebackground = '#495057')
    #     self.btn6 = Button(self,text = "ورود به صفحه" ,relief="flat" ,font = ('B Koodak' , 12),width = 15,fg = "#DEE2E6", bg = "#495057",activebackground = '#495057')
    #     self.btn7 = Button(self,text = "ورود به صفحه" ,relief="flat" ,font = ('B Koodak' , 12),width = 15,fg = "#DEE2E6", bg = "#495057",activebackground = '#495057')
    #     self.btn8 = Button(self,text = "ورود به صفحه" ,relief="flat" ,font = ('B Koodak' , 12),width = 15,fg = "#DEE2E6", bg = "#495057",activebackground = '#495057')
        
    #     self.btn1.place(x = 87 , y = 248)
    #     self.btn2.place(x = 381 , y = 248)
    #     self.btn3.place(x = 671 , y = 248)
    #     self.btn4.place(x = 961 , y = 248)
    #     self.btn5.place(x = 87 , y = 558)
    #     self.btn6.place(x = 381 , y = 558)
    #     self.btn7.place(x = 671 , y = 558)
    #     self.btn8.place(x = 961 , y = 558)


#----------------------------------------------------------------------------------------------------------

    # def register(self) :
    #     self.geometry('900x500+150+150')
    #     self.title('register')
    #     self.state('withdrawn')
    #     self.register_image = PhotoImage(file = 'D:/123/!python/Projects/anbardari/img/register_back.png')
    #     self.register_img = Label(self,image = self.register_image )
    #     self.register_img.place(x = 0 , y = 0)

    #     self.name = Label(self,text = ": نام",font = ('B Koodak' , 18),bg = '#F8F9FA',fg = '#707070')
    #     self.last = Label(self,text = ": نام خانوادگی",font = ('B Koodak' , 18),bg = '#F8F9FA',fg = '#707070')
    #     self.user = Label(self,text = ": نام کابری",font = ('B Koodak' , 18),bg = '#F8F9FA',fg = '#707070')
    #     self.passw = Label(self,text = ": کلمه کاربری",font = ('B Koodak' , 18),bg = '#F8F9FA',fg = '#707070')

    #     self.name_ent = Entry(self, bg = '#adb5bd', width = 25 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#FFFFFF')
    #     self.last_ent = Entry(self, bg = '#adb5bd', width = 25 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#FFFFFF')
    #     self.user_ent = Entry(self, bg = '#adb5bd', width = 25 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#FFFFFF')
    #     self.passw_ent = Entry(self, bg = '#adb5bd', width = 25 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#FFFFFF')

    #     self.name.place(x =750 , y = 90 )
    #     self.last.place(x =750 , y = 155 )
    #     self.user.place(x =750 , y = 220 )
    #     self.passw.place(x =750 , y = 283 )

    #     self.name_ent.place(x =500 , y = 100 )
    #     self.last_ent.place(x =500 , y = 165 )
    #     self.user_ent.place(x =500 , y = 230 )
    #     self.passw_ent.place(x =500, y = 293 )

    #     self.submit_btn = Button(self,bg = "#495057" , text = "ثبت",font = ('B Koodak' , 14),width=10 ,relief="flat" , fg = "#FFFFFF")
    #     self.exit_btn = Button(self,bg = "#495057" , text = "خروج",font = ('B Koodak' , 14),width=10 ,relief="flat" , fg = "#FFFFFF")

    #     self.submit_btn.place(x = 544 ,y = 382)
    #     self.exit_btn.place(x = 704 , y = 382)




    # def login(self):
    #     self.geometry('450x550+550+150')
    #     self.title('login')

    #     self.login_image = PhotoImage(file = 'D:/123/!python/Projects/anbardari/img/login_back.png')
    #     self.login_img = Label(self,image = self.login_image ,relief="flat")
    #     self.login_img.place(x = 0 , y = 0)

    #     self.user = Label(self,text = ": نام کاربری",font = ('B Koodak' , 18),bg = '#495057',fg = '#F8F9FA')
    #     self.passw = Label(self,text = ": رمز عبور",font = ('B Koodak' , 18),bg = '#495057',fg = '#F8F9FA')
    #     self.user.place(x = 310 , y = 141)
    #     self.passw.place(x = 310 , y = 209)
        
    #     self.user_ent = Entry(self, bg = '#ced4da', width = 23 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
    #     self.passw_ent = Entry(self, bg = '#ced4da', width = 23 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057',show = "")
    #     self.user_ent.place(x = 80 , y = 151)
    #     self.passw_ent.place(x = 80 , y = 219)

    #     # self.baz_image = PhotoImage(file = 'img/login_back.png')
    #     self.baste_image = PhotoImage(file = 'D:/123/!python/Projects/anbardari/img/baste.png')
    #     self.eye = Button(self,image = self.baste_image ,relief="flat" , bg = "#495057",activebackground = '#495057')
    #     self.eye.place(x = 35 , y = 219)

    #     self.submit_btn = Button(self,bg = "#6C757D" , text = "ثبت",font = ('B Koodak' , 14),width=13 ,relief="flat" , fg = "#FFFFFF")
    #     self.submit_btn.place(x = 148 , y = 336)

    #     self.eye.bind('<Button-1>',self.hide)
    #     self.eye.bind('<ButtonRelease>',self.hide)

    # def check(self) :
    #     conn = sql.connect('mydb.db')
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    #     tables = cursor.fetchall()
    #     if len(tables) == 0:
    #         pass
    #     else:
    #         pass
    #     cursor.close()
    #     conn.close()

    # def hide(self,event = None):
    #     if self.passw_ent['show'] == '*' :
    #         self.passw_ent['show'] = ""
    #         self.baste_image['file'] = 'D:/123/!python/Projects/anbardari/img/baz.png'
    #     elif self.passw_ent['show'] == "" :
    #         self.passw_ent['show'] = '*'
    #         self.baste_image['file'] = 'D:/123/!python/Projects/anbardari/img/baste.png'
#----------------------------------------------------------------------------------------------------------

    def Product_registration(self) :
        self.geometry('1400x850+300+50')
        self.title('Product registration')

        self.Product_registration_image = PhotoImage(file = 'D:/123/!python/Projects/anbardari/img/Product-registration_back.png')
        self.Product_registration_img = Label(self,image = self.Product_registration_image ,relief="flat")
        self.Product_registration_img.place(x = 0 , y = 0)
        
        self.product_name = Label(self,text = ": نام کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.product_code = Label(self,text = ": کد کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.point_purchase = Label(self,text = ": نقطه خرید",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.Description = Label(self,text = ": توضیحات کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.product_name.place(x = 1169 , y = 137)
        self.product_code.place(x = 1169 , y = 189)
        self.point_purchase.place(x = 1169 , y = 241)
        self.Description.place(x = 1169 , y = 293)

        self.product_name_ent = Entry(self, bg = '#FFFFFF', width = 35 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
        self.product_code_ent = Entry(self, bg = '#FFFFFF', width = 35 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
        self.point_purchase_ent = Entry(self, bg = '#FFFFFF', width = 35 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
        self.Description_ent = Entry(self, bg = '#FFFFFF', width = 35 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
        self.product_name_ent.place(x = 824 , y = 141)
        self.product_code_ent.place(x = 824 , y = 193)
        self.point_purchase_ent.place(x = 824 , y = 245)
        self.Description_ent.place(x = 824 , y = 297)

        self.photo_submit = Button(self,bg = "#6C757D" , text = "بارگذاری عکس",font = ('B Koodak' , 12),width=13 ,relief="flat" , fg = "#FFFFFF")
        self.photo_submit.place(x = 168 , y = 298)

        self.product_type = Label(self,text = ": نوع کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.product_group = Label(self,text = ": نام گروه کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.product_type.place(x = 607 , y = 145)
        self.product_group.place(x = 607 , y = 245)

        self.product_type_combo = ttk.Combobox(self,width = 20 , font = ('B Koodak' , 12),justify = 'right',values=["مواد خام", "کالای خریداری شده", "کالای توید شده اولیه", "کالای تولید شده برای فروش"])
        self.product_group_combo = ttk.Combobox(self,width = 20 , font = ('B Koodak' , 12),justify = 'right',values=["فلزات", "مواد غذایی"])
        self.product_type_combo.set("یک گزینه را انتخاب کنید")
        self.product_group_combo.set("یک گزینه را انتخاب کنید")
        self.product_type_combo.place(x=378, y=148)
        self.product_group_combo.place(x=378, y=248)

        self.Product_registration_submit = Button(self,bg = "#495057" , text = "ثبت",font = ('B Koodak' , 14),width=17 ,relief="flat" , fg = "#FFFFFF") 
        self.Product_registration_exit = Button(self,bg = "#495057" , text = "صفحه اصلی",font = ('B Koodak' , 14),width=17 ,relief="flat" , fg = "#FFFFFF") 
        self.Product_registration_submit.place(x=460, y=775)
        self.Product_registration_exit.place(x=710, y=775)    

        self.photo_submit.bind('<Button-1>',self.change_image)
        self.Product_registration_submit.bind('<Button-1>',self.Product_registration_info)
    def change_image(self,event = None) :
        self.filename = filedialog.askopenfilename()
        self.pr_image = Image.open(self.filename)
        self.pr_image.thumbnail((220, 176))  
        self.photo = ImageTk.PhotoImage(self.pr_image)
        self.pr_image = Label(self,image = self.photo ,relief="flat")
        self.pr_image.place(x=130, y=109)  
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
        self.data=(self.code,self.name,self.point,self.desc,self.type,self.group,self.photo)
        self.cur.execute('''CREATE TABLE IF NOT EXISTS kala (id   ,name TEXT ,point INTEGER,Description TEXT
        ,type TEXT,groupp TEXT,photoo BLOB)''')
        self.cur.execute('INSERT INTO kala(id,name,point,Description,type,groupp,photoo) VALUES(?,?,?,?,?,?,?)',self.data)
        self.con.commit()

        self.product_type_combo.set("یک گزینه را انتخاب کنید")
        self.product_group_combo.set("یک گزینه را انتخاب کنید")
        self.product_code_ent.delete(0,END)
        self.product_name_ent.delete(0,END)
        self.point_purchase_ent.delete(0,END)
        self.Description_ent.delete(0,END)

    def covert_to_binary_data(self,filename):
        with open (filename , 'rb') as f:
            blobdata = f.read()
        return blobdata
        
        







o = main()
o.mainloop()