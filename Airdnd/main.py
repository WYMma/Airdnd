from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import sqlite3

conn = sqlite3.connect('hotels.db')
c = conn.cursor()
# functions
def menu_window():
    hotelsmenu = root
    hotelsmenu.geometry("600x800")
    hotelsmenu.title("airdnd")
    hotelsmenu.iconphoto(False, ImageTk.PhotoImage(Image.open("logo.ico")))
    hotelsmenu.config(bg="#efefef")
    panel2 = Label(hotelsmenu, image=img2)
    panel2.place(x=-2, y=0)
    button1 = Button(hotelsmenu, command=bookingh1, relief=RAISED, padx=10, pady=10, highlightthickness=0, bd=0)
    button1.config(image=img3)
    button2 = Button(hotelsmenu, command=bookingh2, relief=RAISED, padx=10, pady=10, highlightthickness=0, bd=0)
    button2.config(image=img4)
    button3 = Button(hotelsmenu, command=bookingh3, relief=RAISED, padx=10, pady=10, highlightthickness=0, bd=0)
    button3.config(image=img5)
    button4 = Button(hotelsmenu, command=bookingh4, relief=RAISED, padx=10, pady=10, highlightthickness=0, bd=0)
    button4.config(image=img6)
    button1.place(relx=0.05, rely=0.32)
    button2.place(relx=0.53, rely=0.32)
    button3.place(relx=0.05, rely=0.65)
    button4.place(relx=0.53, rely=0.65)
def move():
    global x
    if x == 5:
        x = 1
    if x == 1:
        l.config(image=hp1)
    elif x == 2:
        l.config(image=hp2)
    elif x == 3:
        l.config(image=hp3)
    elif x == 4:
        l.config(image=hp4)
    elif x == 5:
        l.config(image=hp5)
    x += 1
    root.after(4000, move)
def confirmh():
    confirm_win1 = root
    confirm_win1.geometry("600x800")
    confirm_win1.title("Confirm Reservation")
    confirm_win1.iconphoto(False, ImageTk.PhotoImage(Image.open("logo.ico")))
    confirm_win1.config(bg="#fff")
    cbanner = Label(confirm_win1, image=banner)
    cbanner.place(x=-2, y=0)
    nb = Label(confirm_win1, text=receipt, font=('nexa bold', 15, 'bold'), bg="#fff")
    nb.place(x=285.46, y=405.36)
    mode = Label(confirm_win1, text=accom, font=('nexa bold', 15, 'bold'), bg="#fff")
    mode.place(x=300.46, y=430.36)
    price = Label(confirm_win1, text=pr, font=('nexa bold', 15, 'bold'), bg="#fff")
    price.place(x=215.46, y=458.36)
    gohome = Button(confirm_win1, command=menu_window, highlightthickness=0, bd=0, bg="#fff")
    gohome.config(image=home, padx=30)
    gohome.place(x=257, y=631)
# mainwindow
root = Tk()
root['bg'] = '#fff'
root.title('airdnd')
root.iconphoto(False, ImageTk.PhotoImage(Image.open("logo.ico")))
root.geometry("600x720")
# hotel1
def bookingh1():
    def submit():
        conn = sqlite3.connect('hotels.db')
        c = conn.cursor()
        global receipt
        global accom
        global pr
        global banner
        receipt = box.get()
        if rb.get() == choiceh1[0]:
            accom = "Single"
        else:
            accom = "Double"

        c.execute("SELECT * FROM (SELECT * FROM hotel1 WHERE type =?) WHERE stat = 'free'",(accom,))
        result = c.fetchall()
        test = len(result) > 0
        if test:
            if accom == "Single":
                try:
                    messagebox.showinfo(title='Receipt',
                                        message='You"ve successfully booked a room! \n your bill is '+ str(280 * int(receipt)) + 'DT.')
                    id= 101 - len(result)
                    stat = "busy"
                    c.execute("UPDATE hotel1 SET stat =? WHERE roomid =?", (stat,id))
                    conn.commit()
                    conn.close()
                    pr = str(280 * int(receipt)) + 'DT.'
                    banner = c1
                    confirmh()
                except:
                    messagebox.showwarning(title='Error!', message='Please enter a valid number.')
                    box.delete(0, END)
            else:
                try:
                    messagebox.showinfo(title='Receipt',
                                        message='You"ve successfully booked a room! \n your bill is '+ str(409 * int(receipt)) + 'DT.')
                    id= 51 - len(result)
                    stat = "busy"
                    c.execute("UPDATE hotel1 SET stat =? WHERE roomid =?", (stat, id))
                    conn.commit()
                    conn.close()
                    pr = str(409 * int(receipt)) + 'DT'
                    banner = c1
                    confirmh()
                except:
                    messagebox.showwarning(title='Error!', message='Please enter a valid number.')
                    box.delete(0, END)
        else:
            messagebox.showwarning(title='Sorry', message='Sorry dear customer there are no available rooms of this '
                                                          'type.')
    booking_win1 = root
    booking_win1.geometry("600x800")
    booking_win1.title("Hotel Booking")
    booking_win1.iconphoto(False, ImageTk.PhotoImage(Image.open("logo.ico")))
    booking_win1.config(bg="#fff")
    hotelbanner = Label(booking_win1, image=h1)
    hotelbanner.place(x=-2, y=0)
    box = Entry(booking_win1, font=('nexa bold', 15, 'bold'), width=5)
    box.place(x=413, y=279)
    rb = ttk.Combobox(booking_win1, values=choiceh1)
    rb.current(0)
    rb.place(x=413, y=354)

    button5 = Button(booking_win1, command=submit, highlightthickness=0, bd=0, bg="#fff")
    button5.config(image=sub, padx=30)
    button5.place(x=440.5, y=405.5)
    goback = Button(booking_win1, command=menu_window, highlightthickness=0, bd=0, bg="#fff")
    goback.config(image=back, padx=30)
    goback.place(x=36, y=220)
choiceh1 = ["Single (280DT/n)", "Double (409DT/n)"]
img3 = ImageTk.PhotoImage(Image.open("img/Group 1.png"))
h1 = ImageTk.PhotoImage(Image.open("img/hotels/hotel1.png"))
c1 = ImageTk.PhotoImage(Image.open("img/hotels/c1.png"))
# hotel2
def bookingh2():
    def submit():
        conn = sqlite3.connect('hotels.db')
        c = conn.cursor()
        global receipt
        global accom
        global pr
        global banner
        receipt = box.get()
        if rb.get() == choiceh2[0]:
            accom = "Single"
        else:
            accom = "Double"
        c.execute("SELECT * FROM (SELECT * FROM hotel2 WHERE type =?) WHERE stat = 'free'", (accom,))
        result = c.fetchall()
        test = len(result) > 0
        if test:
            if accom == "Single":
                try:
                    messagebox.showinfo(title='Receipt',
                                        message='You"ve successfully booked a room \nYour bill is ' + str(
                                            92 * int(receipt)) + 'DT')
                    id = 101 - len(result)
                    stat = "busy"
                    c.execute("UPDATE hotel2 SET stat =? WHERE roomid =?", (stat, id))
                    conn.commit()
                    conn.close()
                    pr = str(92 * int(receipt)) + 'DT.'
                    banner = c2
                    confirmh()
                except:
                    messagebox.showwarning(title='Error!', message='Please enter a valid number.')
                    box.delete(0, END)
            else:
                try:
                    messagebox.showinfo(title='Receipt',
                                        message='You"ve successfully booked a room \nYour bill is ' + str(
                                            190 * int(receipt)) + 'DT')
                    id = 51 - len(result)
                    stat = "busy"
                    c.execute("UPDATE hotel2 SET stat =? WHERE roomid =?", (stat, id))
                    conn.commit()
                    conn.close()
                    pr = str(190 * int(receipt)) + 'DT'
                    banner = c2
                    confirmh()
                except:
                    messagebox.showwarning(title='Error!', message='Please enter a valid number.')
                    box.delete(0, END)
        else:
            messagebox.showwarning(title='Sorry', message='Sorry dear customer there are no available rooms of this '
                                                          'type.')

    booking_win2 = root
    booking_win2.geometry("600x800")
    booking_win2.title("Hotel Booking")
    booking_win2.iconphoto(False, ImageTk.PhotoImage(Image.open("logo.ico")))
    booking_win2.config(bg="#fff")
    hotelbanner2 = Label(booking_win2, image=h2)
    hotelbanner2.place(x=-2, y=0)
    box = Entry(booking_win2, font=('nexa bold', 15, 'bold'), width=5)
    box.place(x=413, y=279)
    rb = ttk.Combobox(booking_win2, values=choiceh2)
    rb.current(0)
    rb.place(x=413, y=354)
    button5 = Button(booking_win2, command=submit, highlightthickness=0, bd=0, bg="#fff")
    button5.config(image=sub, padx=30)
    button5.place(x=440.5, y=405.5)
    goback = Button(booking_win2, command=menu_window, highlightthickness=0, bd=0, bg="#fff")
    goback.config(image=back, padx=30)
    goback.place(x=36, y=220)
choiceh2 = ["Single (92DT/n)", "Double (190DT/n)"]
img4 = ImageTk.PhotoImage(Image.open("img/Group 2.png"))
h2 = ImageTk.PhotoImage(Image.open("img/hotels/hotel2.png"))
c2 = ImageTk.PhotoImage(Image.open("img/hotels/c2.png"))
# hotel3
def bookingh3():
    def submit():
        conn = sqlite3.connect('hotels.db')
        c = conn.cursor()
        global receipt
        global accom
        global pr
        global banner
        receipt = box.get()
        if rb.get() == choiceh3[0]:
            accom = "Single"
        else:
            accom = "Double"
        c.execute("SELECT * FROM (SELECT * FROM hotel3 WHERE type =?) WHERE stat = 'free'", (accom,))
        result = c.fetchall()
        test = len(result) > 0
        if test:
            if accom == "Single":
                try:
                    messagebox.showinfo(title='Receipt',
                                        message='You"ve successfully booked a room \nYour bill is ' + str(
                                            95 * int(receipt)) + 'DT')
                    id = 101 - len(result)
                    stat = "busy"
                    c.execute("UPDATE hotel3 SET stat =? WHERE roomid =?", (stat, id))
                    conn.commit()
                    pr = str(95 * int(receipt)) + 'DT'
                    banner = c3
                    confirmh()
                except:
                    messagebox.showwarning(title='Error!', message='Please enter a valid number.')
                    box.delete(0, END)
            else:
                try:
                    messagebox.showinfo(title='Receipt',
                                        message='You"ve successfully booked a room \nYour bill is ' + str(
                                            173 * int(receipt)) + 'DT')
                    id = 51 - len(result)
                    stat = "busy"
                    c.execute("UPDATE hotel3 SET stat =? WHERE roomid =?", (stat, id))
                    conn.commit()
                    pr = str(173 * int(receipt)) + 'DT'
                    banner = c3
                    confirmh()
                except:
                    messagebox.showwarning(title='Error!', message='Please enter a valid number.')
                    box.delete(0, END)
        else:
            messagebox.showwarning(title='Sorry', message='Sorry dear customer there are no available rooms of this '
                                                          'type.')

    booking_win3 = root
    booking_win3.geometry("600x800")
    booking_win3.title("Hotel Booking")
    booking_win3.iconphoto(False, ImageTk.PhotoImage(Image.open("logo.ico")))
    booking_win3.config(bg="#fff")
    hotelbanner3 = Label(booking_win3, image=h3)
    hotelbanner3.place(x=-2, y=0)
    box = Entry(booking_win3, font=('nexa bold', 15, 'bold'), width=5)
    box.place(x=413, y=279)
    rb = ttk.Combobox(booking_win3, values=choiceh3)
    rb.current(0)
    rb.place(x=413, y=354)
    button5 = Button(booking_win3, command=submit, highlightthickness=0, bd=0, bg="#fff")
    button5.config(image=sub, padx=30)
    button5.place(x=440.5, y=405.5)
    goback = Button(booking_win3, command=menu_window, highlightthickness=0, bd=0, bg="#fff")
    goback.config(image=back, padx=30)
    goback.place(x=36, y=220)
choiceh3 = ["Single (95DT/n)", "Double (173DT/n)"]
img5 = ImageTk.PhotoImage(Image.open("img/Group 3.png"))
h3 = ImageTk.PhotoImage(Image.open("img/hotels/hotel3.png"))
c3 = ImageTk.PhotoImage(Image.open("img/hotels/c3.png"))
# hotel4
def bookingh4():
    def submit():
        conn = sqlite3.connect('hotels.db')
        c = conn.cursor()
        global receipt
        global accom
        global pr
        global banner
        receipt = box.get()
        if rb.get() == choiceh4[0]:
            accom = "Single"
        else:
            accom = "Double"
        c.execute("SELECT * FROM (SELECT * FROM hotel4 WHERE type =?) WHERE stat = 'free'", (accom,))
        result = c.fetchall()
        test = len(result) > 0
        if test:
            if accom == "Single":
                try:
                    messagebox.showinfo(title='Receipt',
                                        message='You"ve successfully booked a room \nYour bill is ' + str(
                                            67 * int(receipt)) + 'DT')
                    id = 101 - len(result)
                    stat = "busy"
                    c.execute("UPDATE hotel4 SET stat =? WHERE roomid =?", (stat, id))
                    conn.commit()
                    pr = str(67 * int(receipt)) + 'DT'
                    banner = c4
                    confirmh()
                except:
                    messagebox.showwarning(title='Error!', message='Please enter a valid number.')
                    box.delete(0, END)
            else:
                try:
                    messagebox.showinfo(title='Receipt',
                                        message='You"ve successfully booked a room \nYour bill is ' + str(
                                            127 * int(receipt)) + 'DT')
                    id = 51 - len(result)
                    stat = "busy"
                    c.execute("UPDATE hotel4 SET stat =? WHERE roomid =?", (stat, id))
                    conn.commit()
                    pr = str(127 * int(receipt)) + 'DT'
                    banner = c4
                    confirmh()
                except:
                    messagebox.showwarning(title='Error!', message='Please enter a valid number.')
                    box.delete(0, END)
        else:
            messagebox.showwarning(title='Sorry', message='Sorry dear customer there are no available rooms of this '
                                                          'type.')

    booking_win4 = root
    booking_win4.geometry("600x800")
    booking_win4.title("Hotel Booking")
    booking_win4.iconphoto(False, ImageTk.PhotoImage(Image.open("logo.ico")))
    booking_win4.config(bg="#fff")
    hotelbanner4 = Label(booking_win4, image=h4)
    hotelbanner4.place(x=-2, y=0)
    box = Entry(booking_win4, font=('nexa bold', 15, 'bold'), width=5)
    box.place(x=413, y=279)
    rb = ttk.Combobox(booking_win4, values=choiceh4)
    rb.current(0)
    rb.place(x=413, y=354)
    button5 = Button(booking_win4, command=submit, highlightthickness=0, bd=0, bg="#fff")
    button5.config(image=sub, padx=30)
    button5.place(x=440.5, y=405.5)
    goback = Button(booking_win4, command=menu_window, highlightthickness=0, bd=0, bg="#fff")
    goback.config(image=back, padx=30)
    goback.place(x=36, y=220)
choiceh4 = ["Single (67DT/n)", "Double (127DT/n)"]
img6 = ImageTk.PhotoImage(Image.open("img/Group 4.png"))
h4 = ImageTk.PhotoImage(Image.open("img/hotels/hotel4.png"))
c4 = ImageTk.PhotoImage(Image.open("img/hotels/c4.png"))
# images
img = ImageTk.PhotoImage(Image.open("img/banner.png"))
img2 = ImageTk.PhotoImage(Image.open("img/banner2.png"))
sub = ImageTk.PhotoImage(Image.open("img/sub.png"))
back = ImageTk.PhotoImage(Image.open("img/back.png"))
exp = ImageTk.PhotoImage(Image.open("img/exp.png"))
home = ImageTk.PhotoImage(Image.open("img/home.png"))
hp1 = ImageTk.PhotoImage(Image.open("img/homepage/Layer 2.png"))
hp2 = ImageTk.PhotoImage(Image.open("img/homepage/Layer 3.png"))
hp3 = ImageTk.PhotoImage(Image.open("img/homepage/Layer 4.png"))
hp4 = ImageTk.PhotoImage(Image.open("img/homepage/Layer 5.png"))
hp5 = ImageTk.PhotoImage(Image.open("img/homepage/Layer 6.png"))
# code
panel = Label(root, image=img)
panel.pack()
l = Label(root, font="bold")
l.pack()
x = 1
move()
button0 = Button(root, command=menu_window, highlightthickness=0, bd=0)
button0.config(image=exp)
button0.place(relx=0.39, rely=0.6)
root.mainloop()
