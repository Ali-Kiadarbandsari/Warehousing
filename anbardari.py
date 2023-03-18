import sqlite3 as sql
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

class home(Tk):

    def __init__(self) :
        Tk.__init__(self)
        self.main()
        # self.Product_registration()
# ----------------------------------------------------------------------------------------------------------


    def main(self) :
        self.geometry('1200x680+550+150')
        self.title('main')

        self.main_image = PhotoImage(file = 'D:/123/!python/Projects/anbardari/img/main_back.png')
        self.main_img = Label(self,image = self.main_image ,relief="flat")
        self.main_img.place(x = 0 , y = 0)

        self.btn1 = Button(self,text = "ورود به صفحه" ,relief="flat" ,font = ('B Koodak' , 12),width = 15,fg = "#DEE2E6", bg = "#495057",activebackground = '#495057')
        self.btn2 = Button(self,text = "ورود به صفحه" ,relief="flat" ,font = ('B Koodak' , 12),width = 15,fg = "#DEE2E6", bg = "#495057",activebackground = '#495057')
        self.btn3 = Button(self,text = "ورود به صفحه" ,relief="flat" ,font = ('B Koodak' , 12),width = 15,fg = "#DEE2E6", bg = "#495057",activebackground = '#495057')
        self.btn4 = Button(self,text = "ورود به صفحه" ,relief="flat" ,font = ('B Koodak' , 12),width = 15,fg = "#DEE2E6", bg = "#495057",activebackground = '#495057')
        self.btn5 = Button(self,text = "ورود به صفحه" ,relief="flat" ,font = ('B Koodak' , 12),width = 15,fg = "#DEE2E6", bg = "#495057",activebackground = '#495057')
        self.btn6 = Button(self,text = "ورود به صفحه" ,relief="flat" ,font = ('B Koodak' , 12),width = 15,fg = "#DEE2E6", bg = "#495057",activebackground = '#495057')
        self.btn7 = Button(self,text = "ورود به صفحه" ,relief="flat" ,font = ('B Koodak' , 12),width = 15,fg = "#DEE2E6", bg = "#495057",activebackground = '#495057')
        self.btn8 = Button(self,text = "ورود به صفحه" ,relief="flat" ,font = ('B Koodak' , 12),width = 15,fg = "#DEE2E6", bg = "#495057",activebackground = '#495057')
        
        self.btn1.place(x = 87 , y = 248)
        self.btn2.place(x = 381 , y = 248)
        self.btn3.place(x = 671 , y = 248)
        self.btn4.place(x = 961 , y = 248)
        self.btn5.place(x = 87 , y = 558)
        self.btn6.place(x = 381 , y = 558)
        self.btn7.place(x = 671 , y = 558)
        self.btn8.place(x = 961 , y = 558)
        self.btn1.bind('<Button-1>',self.main_to_Pregistration)

    def main_to_Pregistration(self,event = None) :
        p = Pregistration()
        p.mainloop()

class Pregistration(Tk) :
    def __init__(self) :
        Tk.__init__(self)
        self.Product_registration()
        self.data_to_treeview()
        # self.style = ttk.Style()
        self.kalalst = []
        self.kalaid = ""
        self.lst = []
    def Product_registration(self) :
        self.geometry('1400x900+300+50')
        self.title('Product registration')

        self.Product_registration_image = PhotoImage(file = 'D:/123/!python/Projects/anbardari/img/Product-registration_back.png')
        self.Product_registration_img = Label(self,image = self.Product_registration_image ,relief="flat")
        self.Product_registration_img.place(x = 0 , y = 0)

        self.search_btn = Button(self,bg = "#DEE2E6" , text = "جستجو",font = ('B Koodak' , 13),width=12 ,relief="flat" , fg = "#000000")
        self.search_ent = Entry(self, bg = '#FFFFFF', width = 35 , font = ('B Koodak' , 14) , relief = 'flat' , justify = 'right',fg='#495057')
        self.search_btn.place(x = 85 , y = 33)
        # self.search_btn.place(x = 0 , y = 0)
        self.search_ent.place(x = 266 , y = 40)
        # self.search_ent.place(x = 0 , y = 0)
        
        self.product_name = Label(self,text = ": نام کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.product_code = Label(self,text = ": کد کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.point_purchase = Label(self,text = ": نقطه خرید",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.Description = Label(self,text = ": توضیحات کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.product_name.place(x = 1169 , y = 181)
        self.product_code.place(x = 1169 , y = 233)
        self.point_purchase.place(x = 1169 , y = 285)
        self.Description.place(x = 1169 , y = 337)

        self.product_name_ent = Entry(self, bg = '#FFFFFF', width = 35 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
        self.product_code_ent = Entry(self, bg = '#FFFFFF', width = 35 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
        self.point_purchase_ent = Entry(self, bg = '#FFFFFF', width = 35 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
        self.Description_ent = Entry(self, bg = '#FFFFFF', width = 35 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
        self.product_name_ent.place(x = 824 , y = 185)
        self.product_code_ent.place(x = 824 , y = 237)
        self.point_purchase_ent.place(x = 824 , y = 289)
        self.Description_ent.place(x = 824 , y = 341)

        self.photo_submit = Button(self,bg = "#6C757D" , text = "بارگذاری عکس",font = ('B Koodak' , 12),width=13 ,relief="flat" , fg = "#FFFFFF")
        self.photo_submit.place(x = 168 , y = 342)

        self.product_type = Label(self,text = ": نوع کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.product_group = Label(self,text = ": نام گروه کالا",font = ('B Koodak' , 18),bg = '#DEE2E6',fg = '#495057')
        self.product_type.place(x = 607 , y = 189)
        self.product_group.place(x = 607 , y = 289)

        self.product_type_combo = ttk.Combobox(self,width = 20 , font = ('B Koodak' , 12),justify = 'right',values=["مواد خام", "کالای خریداری شده", "کالای توید شده اولیه", "کالای تولید شده برای فروش"])
        self.product_group_combo = ttk.Combobox(self,width = 20 , font = ('B Koodak' , 12),justify = 'right',values=["فلزات", "مواد غذایی"])
        self.product_type_combo.set("یک گزینه را انتخاب کنید")
        self.product_group_combo.set("یک گزینه را انتخاب کنید")
        self.product_type_combo.place(x=378, y=195)
        self.product_group_combo.place(x=378, y=295)

        self.Product_registration_submit = Button(self,bg = "#495057" , text = "ثبت",font = ('B Koodak' , 14),width=15 ,relief="flat" , fg = "#FFFFFF") 
        self.Product_registration_edit = Button(self,bg = "#495057" , text = "ویرایش",font = ('B Koodak' , 14),width=15 ,relief="flat" , fg = "#FFFFFF") 
        self.Product_registration_delete = Button(self,bg = "#495057" , text = "حذف",font = ('B Koodak' , 14),width=15 ,relief="flat" , fg = "#FFFFFF") 
        self.Product_registration_exit = Button(self,bg = "#495057" , text = "صفحه اصلی",font = ('B Koodak' , 14),width=17 ,relief="flat" , fg = "#FFFFFF") 
        self.Product_registration_submit.place(x=50, y=815)
        self.Product_registration_edit.place(x=250, y=815)    
        self.Product_registration_delete.place(x=450, y=815)    
        self.Product_registration_exit.place(x=1140, y=815)    

        self.kala      = ttk.Treeview(self,show='headings',height=7)
        self.kala['columns']=('group','Type','point','id','Name','row')
        self.kala.column('#0',width=0,stretch=NO)
        self.kala.column('group',width=220,anchor=E)
        self.kala.column('Type',width=220,anchor=E)
        self.kala.column('point',width=220,anchor=E)
        self.kala.column('id',width=200,anchor=E)
        self.kala.column('Name',width=220,anchor=E)
        self.kala.column('row',width=150,anchor=E)
        self.kala.heading('#0',text='',anchor=E)
        self.kala.heading('group',text=' : گروه کالا',anchor=E)
        self.kala.heading('Type',text=' : نوع کالا',anchor=E)
        self.kala.heading('point',text=' : نقطه خرید',anchor=E)
        self.kala.heading('id',text=' : کد کالا',anchor=E)
        self.kala.heading('Name',text=' : نام کالا',anchor=E)
        self.kala.heading('row',text=' : ردیف',anchor=E)
        ttk.Style().theme_use('clam')
        ttk.Style().configure("Treeview.Heading",font=('Lalezar', 18),padding=[0, 5, 15, 5],background='#474A56',foreground="white",bd=0,relief='raised')
        ttk.Style().map("Treeview.Heading",
            background=[('active','#686A75')])
        ttk.Style().configure("Treeview", highlightthickness=0, height=150,bd=0, font=('AraFProgram', 16),background="white",foreground="black",rowheight = 35,fieldbackground="white")
        ttk.Style().map("Treeview",background=[('selected', '#7A8BA7')],foreground=[('selected', 'white')])
        
        self.kala.place(x = 75 , y = 477)

        self.photo_submit.bind('<Button-1>',self.change_image)
        self.Product_registration_submit.bind('<Button-1>',self.Product_registration_info)
        self.kala.bind('<Button-1>',self.show_info)
        self.kala.bind('<ButtonRelease-1>',self.show_info)
        self.Product_registration_edit.bind('<Button-1>',self.edit)
        self.Product_registration_delete.bind('<Button-1>',self.delete)
        self.search_btn.bind('<Button-1>',self.search)


    def show_info(self,event = None) :
        self.product_type_combo.set("یک گزینه را انتخاب کنید")
        self.product_group_combo.set("یک گزینه را انتخاب کنید")
        self.product_code_ent.delete(0,END)
        self.product_name_ent.delete(0,END)
        self.point_purchase_ent.delete(0,END)
        self.Description_ent.delete(0,END)

        self.selected = self.kala.focus()
        self.values = self.kala.item(self.selected , "values")
        # print(self.values)
        self.lst = self.sql_search(self.values[3])
        self.product_name_ent.insert(0,self.lst[0][1])
        self.product_code_ent.insert(0,self.lst[0][0])
        self.point_purchase_ent.insert(0,self.lst[0][2])
        self.Description_ent.insert(0,self.lst[0][3])
        self.product_type_combo.set(self.lst[0][4])
        self.product_group_combo.set(self.lst[0][5])
    def edit(self,event = None):
        self.code = self.product_code_ent.get()
        self.name = self.product_name_ent.get()
        self.point = self.point_purchase_ent.get()
        self.desc = self.Description_ent.get()
        self.type = self.product_type_combo.get()
        self.group = self.product_group_combo.get()
        self.sql_update(self.values[3],self.code,self.name,self.point,self.desc,self.type,self.group)
        self.kala.item(self.selected ,values = (self.group,self.type,self.point,self.code,self.name,self.values[5])) 
    def delete(self, event = None) :
        con = sql.connect('mydb.db')
        cur = con.cursor()

        def sql_delete(name):
            command = ' DELETE FROM kala WHERE id="{}" '.format(name)    
            cur.execute(command)    
            con.commit()
        sql_delete(self.values[3])
        self.kala.delete(int(self.values[5])-1)
        
    def sql_update(self,id1,code1,name1,point1,Description1,type1,group1):
        con = sql.connect('mydb.db')
        cur = con.cursor()
        command = ' UPDATE kala SET id = "{}" , name = "{}", point = "{}", Description = "{}", type = "{}",groupp = "{}" WHERE id="{}" '.format(code1,name1,point1,Description1,type1,group1,id1)    
        cur.execute(command)    
        con.commit()

    def search(self,event = None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.idK=self.search_ent.get()
        self.count=0
        if self.idK !='':
            for i in self.kala.get_children():
                self.kala.delete(i)
            self.row=self.cur.execute('SELECT * FROM kala WHERE id="{}"'.format(self.idK))
            self.search_list=list(self.row)
            self.kala.insert(parent='',index='end',iid=self.count,text='',
                                    values=(self.search_list[0][4],self.search_list[0][3],self.search_list[0][2],
                                            self.search_list[0][1],self.search_list[0][0],str(self.count+1)))
        else:
            self.lst=[]
            self.listKala.delete('0')
            self.data_to_list()
    
    def data_to_treeview(self):
        self.kalalst = []
        self.count=0
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        row=self.cur.execute('SELECT * FROM kala')
        for i in row :
            self.kalalst.append(i)
        for i in self.kalalst:
            self.kala.insert(parent='',index='end',iid=self.count,text='',
                                 values=(i[5],i[4],i[2],i[0],i[1],str(self.count+1)))
            self.count += 1

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

        self.kala.insert(parent = '',index = 'end',text = 'parent',values = (self.group,self.type,self.point,self.code,self.name,self.count+1))

        # self.data_to_treeview()
    def covert_to_binary_data(self,filename):
        with open (filename , 'rb') as f:
            blobdata = f.read()
        return blobdata
    
class signup(Tk) :
    def __init__(self) :
        Tk.__init__(self)
        self.check()

    def register(self) :
        self.geometry('900x500+450+150')
        self.title('register')
        self.register_image = PhotoImage(file = 'D:/123/!python/Projects/anbardari/img/register_back.png')
        self.register_img = Label(self,image = self.register_image )
        self.register_img.place(x = 0 , y = 0)

        self.name = Label(self,text = ": نام",font = ('B Koodak' , 18),bg = '#F8F9FA',fg = '#707070')
        self.last = Label(self,text = ": نام خانوادگی",font = ('B Koodak' , 18),bg = '#F8F9FA',fg = '#707070')
        self.user = Label(self,text = ": نام کابری",font = ('B Koodak' , 18),bg = '#F8F9FA',fg = '#707070')
        self.passw = Label(self,text = ": کلمه کاربری",font = ('B Koodak' , 18),bg = '#F8F9FA',fg = '#707070')

        self.name_ent = Entry(self, bg = '#adb5bd', width = 25 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#FFFFFF')
        self.last_ent = Entry(self, bg = '#adb5bd', width = 25 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#FFFFFF')
        self.user_ent = Entry(self, bg = '#adb5bd', width = 25 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#FFFFFF')
        self.passw_ent = Entry(self, bg = '#adb5bd', width = 25 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#FFFFFF')

        self.name.place(x =750 , y = 90 )
        self.last.place(x =750 , y = 155 )
        self.user.place(x =750 , y = 220 )
        self.passw.place(x =750 , y = 283 )

        self.name_ent.place(x =500 , y = 100 )
        self.last_ent.place(x =500 , y = 165 )
        self.user_ent.place(x =500 , y = 230 )
        self.passw_ent.place(x =500, y = 293 )

        self.submit_btn = Button(self,bg = "#495057" , text = "ثبت",font = ('B Koodak' , 14),width=10 ,relief="flat" , fg = "#FFFFFF")
        self.exit_btn = Button(self,bg = "#495057" , text = "خروج",font = ('B Koodak' , 14),width=10 ,relief="flat" , fg = "#FFFFFF")

        self.submit_btn.place(x = 544 ,y = 382)
        self.exit_btn.place(x = 704 , y = 382)

        self.submit_btn.bind('<Button-1>',self.register_check)



    def login(self):
        self.geometry('450x550+550+150')
        self.title('login')

        self.login_image = PhotoImage(file = 'D:/123/!python/Projects/anbardari/img/login_back.png')
        self.login_img = Label(self,image = self.login_image ,relief="flat")
        self.login_img.place(x = 0 , y = 0)

        self.user = Label(self,text = ": نام کاربری",font = ('B Koodak' , 18),bg = '#495057',fg = '#F8F9FA')
        self.passw = Label(self,text = ": رمز عبور",font = ('B Koodak' , 18),bg = '#495057',fg = '#F8F9FA')
        self.user.place(x = 310 , y = 141)
        self.passw.place(x = 310 , y = 209)
        
        self.user_entt = Entry(self, bg = '#ced4da', width = 23 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057')
        self.passw_entt = Entry(self, bg = '#ced4da', width = 23 , font = ('B Koodak' , 12) , relief = 'flat' , justify = 'right',fg='#495057',show = "")
        self.user_entt.place(x = 80 , y = 151)
        self.passw_entt.place(x = 80 , y = 219)

        # self.baz_image = PhotoImage(file = 'img/login_back.png')
        self.baste_image = PhotoImage(file = 'D:/123/!python/Projects/anbardari/img/baste.png')
        self.eye = Button(self,image = self.baste_image ,relief="flat" , bg = "#495057",activebackground = '#495057')
        self.eye.place(x = 35 , y = 219)

        self.submit_btn = Button(self,bg = "#6C757D" , text = "ثبت",font = ('B Koodak' , 14),width=13 ,relief="flat" , fg = "#FFFFFF")
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
            self.register()
        else:
            self.login()
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

        self.state('withdrawn')
        self.mainnn()
    def mainnn(self) :
        mm = home()
        mm.mainloop()
    def login_check(self,event = None) :
        con = sql.connect('mydb.db')
        cur = con.cursor()
        def sql_show():
            
            row = cur.execute('SELECT * FROM login')
            lst = list(row)
            return lst       
                
        lst = sql_show()
        print(lst[0][3])
        if self.user_entt.get() == lst[0][2] and self.passw_entt.get() == lst[0][3] :
            print("asd")
            # m = main()
            # m.mainloop()
    def hide(self,event = None):
        if self.passw_ent['show'] == '*' :
            self.passw_ent['show'] = ""
            self.baste_image['file'] = 'D:/123/!python/Projects/anbardari/img/baz.png'
        elif self.passw_ent['show'] == "" :
            self.passw_ent['show'] = '*'
            self.baste_image['file'] = 'D:/123/!python/Projects/anbardari/img/baste.png'





p = Pregistration()
p.mainloop()

