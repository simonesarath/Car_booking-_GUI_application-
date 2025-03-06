import tkinter 
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3
#import hashlib

def book_car(car_id, Username,home_window):
    conn=sqlite3.connect('showcar.db')
    cursor=conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                  Id INTEGER PRIMARY KEY AUTOINCREMENT,
                  Username TEXT NOT NULL,
                  car_id INTEGER NOT NULL,
                  FOREIGN KEY(Username) REFERENCES users(Username))''')

    cursor.execute("INSERT INTO bookings(Username,car_id) VALUES (?, ?)", (Username,car_id))
    conn.commit()
    conn.close()

    messagebox.showinfo("Booking Confirmation", "Your Car Is Booked On Our Website",parent=home_window)

    open_car_specifications(car_id,Username)

def open_car_specifications(car_id, Username):
    spec_window = Toplevel()
    spec_window.geometry("600x400")
    spec_window.title(f"Car Specifications for Car ID: {car_id}")

    car_specs = {
        1: {"Make": "Tesla", "Model": "Model S", "Year": 2022, "Engine": "Electric", "Price": "₹ 85,000"},
        2: {"Make": "Ford", "Model": "Mustang", "Year": 2023, "Engine": "Internal combustion", "Price": "₹ 95,000"},
        3: {"Make": "Chevrolet", "Model": "Camaro", "Year": 2023, "Engine": "Internal combustion", "Price": "₹ 85,000"},
        4: {"Make": "Lamborghini", "Model": "Aventador", "Year": 2024, "Engine": "Internal combustion", "Price": "₹ 99,000"},
        5: {"Make": "BMW", "Model": "X7", "Year": 2023, "Engine": "Hybrid electric", "Price": "₹ 90,000"},
        6: {"Make": "Bugatti", "Model": "Chiron", "Year": 2024, "Engine": "Hybrid electric", "Price": "₹ 95,000"},
        7: {"Make": "Mahindra", "Model": "XUV700", "Year": 2024, "Engine": "Plug-in hybrid", "Price": "₹ 99,000"},
        # Add more car specifications as needed
    }

    specs = car_specs.get(car_id, {})

    # Display the car specifications in the new window
    if specs:
        Label(spec_window, text=f"Specifications for Car ID: {car_id}", font=("Helvetica", 16, "bold"),fg="darkgoldenrod1").pack(pady=10)
        for key, value in specs.items():
            Label(spec_window, text=f"{key}: {value}", font=("Helvetica", 14)).pack(pady=5)
    else:
        Label(spec_window, text="No specifications available for this car.", font=("Helvetica", 14)).pack(pady=20)

    Button(spec_window,text="Close",font=("times new roman",18,"italic"),fg="cadetblue1",bg="blue4",activebackground="aquamarine4",relief=RAISED,command=spec_window.destroy).pack(pady=50)

def open_home_page(Username):
    
    '''for widget in win.winfo.children():
        widget.destroy()'''
        
    home_window =Toplevel() #win
    home_window.geometry("1000x800")
    home_window.title("Home Page")
    messagebox.showinfo("Success","Here We Go To Home Page !",parent=home_window)

    '''label=Label(home_window,text="CHARIOT CRUISERS ☠",font=("sans serif",19,"italic"),fg="magenta")
    label.place(x=5,y=20)'''

    welcome_label = Label(home_window, text="Welcome to the Online Car Showroom!", font=("sans serif",19,"italic"),fg="magenta")
    welcome_label.grid(row=0, column=0, columnspan=3, pady=20)

    image_paths = [
        ("car1.jpg",1),
        ("car2.jpg",2),
        ("car3.jpg",3),
        ("car4.jpg",4),
        ("car5.jpg",5),
        ("car6.jpg",6),
        ("car7.jpg",7),
        ("car8.jpg",8),
        ("car9.jpg",9),
    ]

    max_per_row=3
    row = 1
    col = 0
    
    for idx, (img_path, car_id) in enumerate(image_paths):
        img = Image.open(img_path)
        img = img.resize((200, 150))  
        photo = ImageTk.PhotoImage(img)

        label = Label(home_window, image=photo)
        label.image = photo
        label.grid(row=row, column=col, padx=20, pady=20) 
        
        btn = Button(home_window, text=f"Book Car {car_id}" ,bd=1, fg="deepskyblue1",bg="firebrick1",activebackground="darkgoldenrod3", command=lambda id=car_id: book_car(id, Username,home_window))
        btn.grid(row=row+1, column=col, pady=5)
        
        if (idx + 1) % max_per_row == 0:
            row += 2
            col = 0
        else:
            col += 1

    logout_button =Button(home_window, text="Logout",font=("times new roman",18,"italic"),fg="cadetblue1",bg="blue4",activebackground="aquamarine4",relief=RAISED,command=home_window.destroy)
    logout_button.place(x=800,y=400)

    home_window.mainloop()

   
def signin_page():#sign in second page

    def signin_database():
        Username=username_var.get()
        Address=address_var.get()
        Phonenumber=number_var.get()
        Password=pass_var.get()

        if e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="":
            messagebox.showerror("Error","All Fields Are Must Required",parent=win)
        else:
            try:
                conn=sqlite3.connect("showcar.db")
                mycursor=conn.cursor()
                
                mycursor.execute('SELECT * FROM Usersdata WHERE UserName =? AND UserPassword =?', (Username,Password))
                user=mycursor.fetchall()

                if user:
                    messagebox.showinfo("Login Successfully","Welcome, "+ Username + "!",parent=win)
                    
                    open_home_page(Username)
                    win.destroy()
                else:
                    messagebox.showerror("Login Failed","Invalid username or password",parent=win)

            except sqlite3.Error as e:
                messagebox.showerror("Database Error","An error occurred:{e}",parent=win)

            finally:
                if conn:
                    conn.close()
        
    def sign_password():
        if e4.cget("show") == "*":
            e4.config(show="")
        else:
            e4.config(show="*")

    def cleartext():
        if e1.get()=="" and e2.get()=="" and e3.get()=="" and e4.get()=="":
            messagebox.showerror("Error","Field Is Empty",parent=win)
        else:
            username_var.set("")
            address_var.set("")
            number_var.set("")
            pass_var.set("")
            
    def forgot_passpage():
        
        def change_password():
            Email=email_var.get()
            Newpassword=new_password_var.get()
            Confirmpassword=confirm_password_var.get()
            
            if e1.get()=="" or e2.get()=="" or e3.get()=="":
                messagebox.showerror("Error","All Fileds Are Required",parent=window)

            #hashed_password = hashlib.sha256(Newpassword.encode()).hexdigest() 

            try:
                conn=sqlite3.connect("showcar.db")
                mycursor=conn.cursor()

                mycursor.execute('UPDATE Usersdata SET UserPassword =?,ConfirmPassword=? WHERE EmailId=?',(Newpassword, Confirmpassword, Email))
                conn.commit()
                
                if mycursor.rowcount==0:
                    messagebox.showerror("Error","Email not found",parent=window)
                else:
                    messagebox.showinfo("Success","Newpassword Reset Successfully",parent=window)
                    
                    forgot_passpage.destroy()
                    signin_page()
                    
            except sqlite3.Error as e:
                messagebox.showerror("Database Error","An Error Occured:{e}",parent=window)
            finally:
                if conn:
                    conn.close()
                                   
        window=Toplevel() #win
        window.title("Change Password")
        image=Image.open("forgotpass.jpg")
        resize_image = image.resize((900, 800))
        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(window,image=img)
        label1.image = img
        label1.pack()
        
        email_var=StringVar()
        new_password_var=StringVar()
        confirm_password_var=StringVar()
            
        def new_pass():
            if e2.cget("show") == "*" or e3.cget("show") == "*":
                e2.config(show=""),e3.config(show="")
            else:
                e2.config(show="*"),e3.config(show="*")

        def clear_text():
            if e1.get()=="" and e2.get()=="" and e3.get()=="":
                messagebox.showerror("Error","Field Is Empty",parent=window)
            else:
                email_var.set("")
                new_password_var.set("")
                confirm_password_var.set("")
                    

        l1=Label(window,text="CHARIOT CRUISERS",font=("algerian",27,"italic"),fg="darkgoldenrod1",bg="white")
        l1.place(x=300,y=30)
        l2=Label(window,text="Reset Password",font=("Poppins",25,"italic"),fg="firebrick",bg="white")
        l2.place(x=335,y=80)

        l3=Label(window,text="EmailId",font=("times new roman",20,"italic"),fg="gold",bg="white")
        l3.place(x=400,y=200)
        e1=Entry(window,textvariable=email_var,font=("times new roman",18),bd=6,fg="white",bg="lavenderblush4",width=30)
        e1.place(x=285,y=240)

        l4=Label(window,text="NewPassword",font=("times new roman",20,"italic"),fg="gold",bg="white")
        l4.place(x=380,y=320)
        e2=Entry(window,textvariable=new_password_var,font=("times new roman",18),bd=6,fg="white",show="*",bg="lavenderblush4",width=30)
        e2.place(x=285,y=360)

        l5=Label(window,text="ConfirmPassword",font=("times new roman",20,"italic"),fg="gold",bg="white")
        l5.place(x=370,y=440)
        e3=Entry(window,textvariable=confirm_password_var,font=("times new roman",18),bd=6,fg="white",show="*",bg="lavenderblush4",width=30)
        e3.place(x=285,y=480)

        checkbutt1=Checkbutton(window,text="Show Password",font=("times new roman",16),fg="blueviolet",bg="white",relief=FLAT,command=new_pass)
        checkbutt1.place(x=500,y=530)  

        sumbit_butt=Button(window,text="Sumbit",font=("times new roman",20,"italic"),fg="pink",bg="blue4",activebackground="aquamarine4",relief=RAISED,command=change_password)
        sumbit_butt.place(x=400,y=610)

        clear_butt=Button(window,text="Clear",font=("times",16,"italic"),fg="deeppink1",bg="deepskyblue2",activebackground="beige",relief=RAISED,command=clear_text)
        clear_butt.place(x=660,y=610)

        #window.mainloop()
        
            
    win=Toplevel()#main 
    win.geometry("700x900")
    win.title("Sign in form")

    username_var=StringVar()
    address_var=StringVar()
    number_var=StringVar()
    pass_var=StringVar()
    
    l1=Label(win,text="HELLO!,WELCOME BACK 👤",font=("algerian",22,"italic"),fg="purple")
    l1.place(x=180,y=20)
    l2=Label(win,text="CHARIOT CRUISERS \n SIGN IN",font=("algerian",25,"italic"),fg="orange")
    l2.place(x=190,y=70)
    
    l3=Label(win,text="UserName",font=("times new roman",20,"italic"),fg="gold")
    l3.place(x=150,y=180)
    e1=Entry(win,textvariable=username_var,font=("times new roman",18),bd=6,fg="white",bg="lavenderblush4",width=34)
    e1.place(x=150,y=220)

    l4=Label(win,text="YourAddress",font=("times new roman",20,"italic"),fg="gold")
    l4.place(x=150,y=280)
    e2=Entry(win,textvariable=address_var,font=("times new roman",18),bd=6,fg="white",bg="lavenderblush4",width=34)
    e2.place(x=150,y=320)

    l5=Label(win,text="Phonenumber",font=("times new roman",20,"italic"),fg="gold")
    l5.place(x=150,y=380)
    e3=Entry(win,textvariable=number_var,font=("times new roman",18),bd=6,fg="white",bg="lavenderblush4",width=34)
    e3.place(x=150,y=420)

    l6=Label(win,text="UserPassword",font=("times new roman",20,"italic"),fg="gold")
    l6.place(x=150,y=480)
    e4=Entry(win,textvariable=pass_var,font=("times new roman",18),bd=6,fg="white",show="*",bg="lavenderblush4",width=34)
    e4.place(x=150,y=520)

    c_butt1=Checkbutton(win,text="Show Password",font=("times new roman",16),fg="blueviolet",relief=FLAT,command=sign_password)
    c_butt1.place(x=415,y=560)

    '''c_butt2=Checkbutton(win,text="Remember Me",font=("times new roman",16,"italic"),bd=3,fg="darkgray")
    c_butt2.place(x=150,y=560)'''

    log=Button(win,text="SIGNIN",font=("times new roman",20,"italic"),fg="pink",bg="blue4",activebackground="aquamarine4",relief=RAISED,command=signin_database)
    log.place(x=300,y=615)

    clear_butt=Button(win,text="Clear",font=("times",16,"italic"),fg="deeppink1",bg="deepskyblue2",activebackground="beige",relief=RAISED,command=cleartext)
    clear_butt.place(x=600,y=630)

    l6=Label(win,text="You Don't Have An Account? Please",font=("times new roman",16,"italic"),fg="mediumpurple1")
    l6.place(x=50,y=680)

    Button(win,text="SignUpHere",font=("times",14,"italic"),fg="blue",relief=FLAT,command=signup_database).place(x=370,y=677)

    fo_butt3=Button(win,text="Forgot Password",font=("times new roman",16,"italic"),fg="blueviolet",relief=FLAT,command=forgot_passpage)
    fo_butt3.place(x=270,y=730)

    #win.mainloop()

#signup first page::
def signup_database():
    
    name=username_var.get()
    Email=email_var.get()
    userpassword=pass_var.get()
    confirmpassword=conf_pass_var.get()
    city=c_var.get()
    condition1=check_var1.get()
    condition2=check_var2.get()
    
    if e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="":
        messagebox.showerror("Error","All Fields Are Required",parent=main)
    elif e3.get() != e4.get():
        messagebox.showerror("Error","Passwords Mismatch",parent=main)
    elif check_var1.get()==0:
        messagebox.showerror("Error","Please Accept The Terms & Conditions",parent=main)
    elif check_var2.get()==0:
        messagebox.showerror("Error","Please Accept The News Notified Our Website",parent=main)

        try:
            conn=sqlite3.connect("showcar.db")
            mycursor=conn.cursor()
            print(" Signup Database created succesfully ")
            
            mycursor.execute(''' CREATE TABLE IF NOT EXISTS Usersdata (
                Id INTEGER PRIMARY KEY,
                UserName TEXT,
                EmailId TEXT,
                UserPassword TEXT,
                ConfirmPassword TEXT,
                Chooseyourcity TEXT )''')
            
            mycursor.execute('SELECT UserName FROM Usersdata WHERE UserName=?',(name,))
            result=mycursor.fetchone()
            
            if result:
                messagebox.showwarning("Warning","Username Already Exists",parent=main)
            else:
                mycursor.execute('INSERT INTO Usersdata (UserName, EmailId, UserPassword, ConfirmPassword, Chooseyourcity) VALUES (?, ?, ?, ?, ?)',(name, Email, userpassword, confirmpassword, city))
                conn.commit()
                messagebox.showinfo("Signup Successful", "Account Created Successfully!",parent=main)
                
                main.destroy()
                signin_page()
                
        except sqlite3.Error as e:
            messagebox.showinfo("Database Error","An Error Occurred:{e}",parent=main)
        finally:
            if conn:
                conn.close()

def show_password():
   if e3.cget("show") == "*":
       e3.config(show="")
   else:
       e3.config(show="*")
def confirm_password():
    if e4.cget("show") == "*":
        e4.config(show="")
    else:
        e4.config(show="*")
        
def clear_text():
    if e1.get()=="" and e2.get()=="" and e3.get()=="" and e4.get()=="":
        messagebox.showerror("Error","Empty Field",parent=main)
    else:
        username_var.set("")
        email_var.set("")
        pass_var.set("")
        conf_pass_var.set("")
        c_var.set("")
       
def terms_privacy(): #terms and conditions page for signup page
    term=Toplevel(main)
    term.geometry("1900x1400")
    term.title("Terms And Conditions And Privacy Policy")
    l1=Label(term,text="WELCOME TO CHARIOT CRUISERS",font=("sans serif",30,"italic"),fg="cornflowerblue")
    l1.place(x=420,y=30)
    l2=Label(term,text="TERMS AND CONDITIONS",font=("sans serif",30,"italic"),fg="darkolivegreen")
    l2.place(x=510,y=100)
    
    
main=Tk()
main.geometry("700x900")
main.title("SIGNUP FORM")

username_var=StringVar()
email_var=StringVar()
pass_var=StringVar()
conf_pass_var=StringVar()
c_var=StringVar()
check_var1=IntVar()
check_var2=IntVar()

l1=Label(main,text="CREATE YOUR ACCOUNT 👤",font=("sans serif",20,"italic"),fg="purple")
l1.place(x=170,y=20)
Label(main,text="WELCOME TO SIGNUP PAGE",font=("sans serif",20,"italic"),fg="magenta").place(x=150,y=70)

l2=Label(main,text="UserName",font=("arial",18,"bold"),fg="gold")
l2.place(x=280,y=130)
e1=Entry(main,textvariable=username_var,font=("arial",18),bd=6,fg="white",bg="lavenderblush4",width=28)
e1.place(x=160,y=170)

l3=Label(main,text="EmailId" ,font=("arial",18),fg="gold")
l3.place(x=295,y=220)
e2=Entry(main,textvariable=email_var,font=("arial",18),bd=6,fg="white",bg="lavenderblush4",width=28)
e2.place(x=160,y=260)

l4=Label(main,text="UserPassword",font=("arial",18),fg="gold")
l4.place(x=260,y=310)
e3=Entry(main,textvariable=pass_var,font=("arial",18),bd=6,fg="white",show="*",bg="lavenderblush4",width=28)
e3.place(x=160,y=350)
c_butt=Checkbutton(main,text="show password",font=("times new roman",13),fg="blueviolet",relief=FLAT,command=show_password)
c_butt.place(x=545,y=355)

l5=Label(main,text="ConfirmPassword",font=("arial",18),fg="gold")
l5.place(x=245,y=400)
e4=Entry(main,textvariable=conf_pass_var,font=("arial",18),bd=6,fg="white",show="*",bg="lavenderblush4",width=28)
e4.place(x=160,y=440)
c_butt=Checkbutton(main,text="show password",font=("times new roman",13),fg="blueviolet",relief=FLAT,command=confirm_password)
c_butt.place(x=545,y=445)

l6=Label(main,text="Chooseyourcity",font=("arial",18),fg="gold")
l6.place(x=40,y=520)

List_of_city=['Nagercoil','Chennai','Kanchipuram','Erode','Coimbatore','Trichy'] 
drop=OptionMenu(main,c_var,*List_of_city)
drop.config(width=35,height=2)
c_var.set("Chooseyourcity")
drop.config(bg="green",fg="white")
drop['menu'].config(bg="Lavender",font=1)
drop.place(x=270,y=510)

c_butt1=Checkbutton(main,text="Yes,I agree to the",font=('arial',14,'italic'),onvalue=1,bd=0.3,variable=check_var1)
c_butt1.place(x=50,y=570)

terms=Button(main,text="Terms And Conditions And Privacy Policy",font=("times",14,"italic"),fg="blue",relief=FLAT,command=terms_privacy)
terms.place(x=225,y=568)

c_butt2=Checkbutton(main,text="Yes,I want to be notified of exclusive offers,new products,upcoming\ncars model and the latest news from this website",font=('arial',14,'italic'),onvalue=1,bd=0.3,variable=check_var2)
c_butt2.place(x=50,y=600)

Button(main,text="SIGNUP",font=("times",20,"italic"),fg="pink",bg="coral",activebackground="firebrick1",width=9,relief=GROOVE,command=signup_database).place(x=280,y=680)

clear_butt=Button(main,text="Clear",font=("times",16,"italic"),fg="deeppink1",bg="deepskyblue2",activebackground="beige",relief=RAISED,command=clear_text)
clear_butt.place(x=590,y=693)

l7=Label(main,text="Already You Have An Account? Please",font=("times",14,"italic"),fg="mediumpurple1")
l7.place(x=90,y=750)

Button(main,text="SignInHere",font=("times",14,"italic"),fg="blue",relief=FLAT,command=signin_page).place(x=390,y=745)

main.mainloop()
