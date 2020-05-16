from tkinter import *
from tkinter import messagebox


class UserService:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.data = {
            "Murid1": {
                "username": "Arief",
                "password": "12345",
            },
            "Murid2": {
                "username": "Admin",
                "password": "12345",
            }
        }

    def login(self):
        get_data = self.checkCredentials()
        if get_data:
            messagebox.showinfo("Login Sukses!", f"Selamat datang {get_data['username']}!")
            return True
        else:
            messagebox.showinfo("Peringatan!", "Login Gagal!")
            return False

    def checkCredentials(self):
        for murid in self.data:
            get_data_user = self.data[murid]
            if self.username == get_data_user['username']:
                if self.password == get_data_user['password']:
                    return get_data_user
                else:
                    return False


class BelajarFisikaSMP:
    def __init__(self, window_tk):
        self.windowTk = window_tk
        self.stack_history = []
        self.widget_list = []

    def loginForm(self):
        self.displayPhoto('orang.png')
        psn_awal = Label(self.windowTk, text="Silakan login terlebih dahulu", font=("Arial Bold", 18), bg='white')
        psn_awal.pack()
        self.widget_list.append(psn_awal)

        form_frame = Frame(self.windowTk, bg='white')
        form_frame.pack()
        self.widget_list.append(form_frame)

        Label(form_frame, text="Username", font=("Arial", 18), bg='white').grid(row=0)
        Label(form_frame, text="Password", font=("Arial", 18), bg='white').grid(row=1)

        user_entry = Entry(form_frame, font=("Arial", 15))
        pass_entry = Entry(form_frame, show="*", font=("Arial", 15))

        user_entry.grid(row=0, column=1)
        pass_entry.grid(row=1, column=1)

        def performLogin():
            username = user_entry.get()
            password = pass_entry.get()
            if username == "" or password == "":
                messagebox.showinfo("Peringatan!", "Mohon lengkapi form yang kosong!")
            else:
                user_udah_ngisi = UserService(username, password)
                login_success = user_udah_ngisi.login()
                if login_success:
                    self.destroyWidget()
                    self.tampilanHome()

        btn_login = Button(mywindow, text="Login", command=performLogin, width=35, font=("Arial", 12))
        btn_login.pack()
        self.widget_list.append(btn_login)

    def destroyWidget(self):
        for _ in reversed(self.widget_list):
            self.widget_list.pop().destroy()

    def displayPhoto(self, filename):
        photo = PhotoImage(file=filename)
        label = Label(self.windowTk, image=photo)
        label.image = photo
        label.pack()
        self.widget_list.append(label)

    def historyLog(self, text):
        if len(self.stack_history) > 0:
            self.stack_history.pop().destroy()
        history = Label(self.windowTk, text=f"History: {text}", bd=1, relief=SUNKEN, anchor=W)
        self.stack_history.append(history)
        history.pack(side=BOTTOM, fill=X)

    def tampilanHome(self):
        well_msg = Label(mywindow, text="\n\nSelamat datang!!!\nSilakan buka materi di pojok kiri atas\n\n\"Hidup itu "
                                        "seperti bersepeda.\nKalau kamu ingin menjaga\nkeseimbanganmu,\nkamu harus "
                                        "terus bergerak maju.\"\n-Albert Einstein")
        well_msg.config(font=("Arial Bold", 24), bg='white')
        well_msg.pack()
        self.widget_list.append(well_msg)

        def glbklik():
            self.destroyWidget()

            self.displayPhoto("glb.png")
            vst_frame = Frame(self.windowTk, bg='white')
            vst_frame.pack()
            self.widget_list.append(vst_frame)

            labelMateri(vst_frame, 0, 'Kecepatan', 'Jarak', 'Waktu')
            labelMateri(vst_frame, 2, 'm/s', 'meter', 'sekon')

            veloc_ent = Entry(vst_frame)
            space_ent = Entry(vst_frame)
            time_ent = Entry(vst_frame)

            veloc_ent.grid(row=0, column=1)
            space_ent.grid(row=1, column=1)
            time_ent.grid(row=2, column=1)

            def calcVST():
                v = veloc_ent.get()
                s = space_ent.get()
                t = time_ent.get()

                if len(v) == 0 and len(s) > 0 and len(t) > 0:
                    v = float(s) / float(t)
                    veloc_ent.delete(0, "end")
                    veloc_ent.insert(0, v)
                    self.historyLog(f"Kecepatan = {v}, Jarak = {s}, Waktu = {t}")
                elif len(s) == 0 and len(v) > 0 and len(t) > 0:
                    s = float(t) * float(v)
                    space_ent.delete(0, "end")
                    space_ent.insert(0, s)
                    self.historyLog(f"Kecepatan = {v}, Jarak = {s}, Waktu = {t}")
                elif len(t) == 0 and len(s) > 0 and len(v) > 0:
                    t = float(s) / float(v)
                    time_ent.delete(0, "end")
                    time_ent.insert(0, t)
                    self.historyLog(f"Kecepatan = {v}, Jarak = {s}, Waktu = {t}")
                else:
                    messagebox.showinfo("Peringatan!", "Kosongi salah satu!")

            btn_calcvst = Button(mywindow, text="Hitung", command=calcVST)
            btn_calcvst.pack()
            self.widget_list.append(btn_calcvst)

        def glbbklik():
            self.destroyWidget()
            self.displayPhoto("glbb.png")
            frame1 = Frame(self.windowTk, bg='white')
            frame1.pack()
            self.widget_list.append(frame1)

            def operation1():
                labelMateri(frame1, 0, 'vt', 'vo', 'a', 't')
                labelMateri(frame1, 2, 'm/s', 'm/s', 'm/s^2', 's')

                entry1 = Entry(frame1)
                entry2 = Entry(frame1)
                entry3 = Entry(frame1)
                entry4 = Entry(frame1)

                entry1.grid(row=0, column=1)
                entry2.grid(row=1, column=1)
                entry3.grid(row=2, column=1)
                entry4.grid(row=3, column=1)

                def calc1():
                    vt = entry1.get()
                    vo = entry2.get()
                    a = entry3.get()
                    t = entry4.get()

                    if len(vt) == 0 and len(vo) > 0 and len(a) > 0 and len(t) > 0:
                        vt = float(vo) + float(a) * float(t)
                        entry1.delete(0, "end")
                        entry1.insert(0, vt)
                        self.historyLog(f"vt = {vt}, vo = {vo}, a = {a}, t = {t}")
                    elif len(vo) == 0 and len(vt) > 0 and len(a) > 0 and len(t) > 0:
                        vo = float(vt) - float(a) * float(t)
                        entry2.delete(0, "end")
                        entry2.insert(0, vo)
                        self.historyLog(f"vt = {vt}, vo = {vo}, a = {a}, t = {t}")
                    elif len(a) == 0 and len(vo) > 0 and len(vt) > 0 and len(t) > 0:
                        a = (float(vt) - float(vo)) / float(t)
                        entry3.delete(0, "end")
                        entry3.insert(0, a)
                        self.historyLog(f"vt = {vt}, vo = {vo}, a = {a}, t = {t}")
                    elif len(t) == 0 and len(vo) > 0 and len(a) > 0 and len(vt) > 0:
                        t = (float(vt) - float(vo)) / float(a)
                        entry4.delete(0, "end")
                        entry4.insert(0, t)
                        self.historyLog(f"vt = {vt}, vo = {vo}, a = {a}, t = {t}")
                    else:
                        messagebox.showinfo("Peringatan!", "Kosongi salah satu!")

                btn_calc1 = Button(frame1, text="Hitung", command=calc1)
                btn_calc1.grid(row=4, column=1)
                self.widget_list.append(btn_calc1)

            def operation2():
                labelMateri(frame1, 3, 'vt', 'vo', 'a', 'S')
                labelMateri(frame1, 5, 'm/s', 'm/s', 'm/s^2', 'm')

                entry1 = Entry(frame1)
                entry2 = Entry(frame1)
                entry3 = Entry(frame1)
                entry4 = Entry(frame1)

                entry1.grid(row=0, column=4)
                entry2.grid(row=1, column=4)
                entry3.grid(row=2, column=4)
                entry4.grid(row=3, column=4)

                def calc1():
                    vt = entry1.get()
                    vo = entry2.get()
                    a = entry3.get()
                    t = entry4.get()

                    if len(vt) == 0 and len(vo) > 0 and len(a) > 0 and len(t) > 0:
                        vt = (float(vo) ** 2 + (float(a) * float(t) * 2)) ** 0.5
                        entry1.delete(0, "end")
                        entry1.insert(0, vt)
                        self.historyLog(f"vt = {vt}, vo = {vo}, a = {a}, t = {t}")
                    elif len(vo) == 0 and len(vt) > 0 and len(a) > 0 and len(t) > 0:
                        vo = (float(vt) ** 2 - float(a) * float(t) * 2) * 0.5
                        entry2.delete(0, "end")
                        entry2.insert(0, vo)
                        self.historyLog(f"vt = {vt}, vo = {vo}, a = {a}, t = {t}")
                    elif len(a) == 0 and len(vo) > 0 and len(vt) > 0 and len(t) > 0:
                        a = (float(vt) ** 2 - float(vo) ** 2) / float(t) / 2
                        entry3.delete(0, "end")
                        entry3.insert(0, a)
                        self.historyLog(f"vt = {vt}, vo = {vo}, a = {a}, t = {t}")
                    elif len(t) == 0 and len(vo) > 0 and len(a) > 0 and len(vt) > 0:
                        t = (float(vt) ** 2 - float(vo) ** 2) / float(a) / 2
                        entry4.delete(0, "end")
                        entry4.insert(0, t)
                        self.historyLog(f"vt = {vt}, vo = {vo}, a = {a}, t = {t}")
                    else:
                        messagebox.showinfo("Peringatan!", "Kosongi salah satu!")

                btn_calc2 = Button(frame1, text="Hitung", command=calc1)
                btn_calc2.grid(row=4, column=4)
                self.widget_list.append(btn_calc2)

            operation1()
            operation2()

        def gayaklik():
            self.destroyWidget()
            self.displayPhoto("gaya.png")
            frame_gaya = Frame(self.windowTk, bg='white')
            frame_gaya.pack()
            self.widget_list.append(frame_gaya)

            labelMateri(frame_gaya, 0, 'F', 'm', 'a')
            labelMateri(frame_gaya, 2, 'N', 'Kg', 'm/s^2')

            val_f = Entry(frame_gaya)
            valm = Entry(frame_gaya)
            vala = Entry(frame_gaya)

            val_f.grid(row=0, column=1)
            valm.grid(row=1, column=1)
            vala.grid(row=2, column=1)

            def calcVST():
                f = val_f.get()
                m = valm.get()
                a = vala.get()

                if len(f) == 0 and len(m) > 0 and len(a) > 0:
                    f = float(m) * float(a)
                    val_f.delete(0, "end")
                    val_f.insert(0, f)
                    self.historyLog(f"F = {f}, m = {m}, a = {a}")
                elif len(m) == 0 and len(f) > 0 and len(a) > 0:
                    m = float(f) / float(a)
                    valm.delete(0, "end")
                    valm.insert(0, m)
                    self.historyLog(f"F = {f}, m = {m}, a = {a}")
                elif len(a) == 0 and len(m) > 0 and len(f) > 0:
                    a = float(f) / float(m)
                    vala.delete(0, "end")
                    vala.insert(0, a)
                    self.historyLog(f"F = {f}, m = {m}, a = {a}")

                else:
                    messagebox.showinfo("Peringatan!", "Kosongi salah satu!")

            btn_calcvst = Button(self.windowTk, text="Hitung", command=calcVST)
            btn_calcvst.pack()
            self.widget_list.append(btn_calcvst)

        menu = Menu(self.windowTk)
        self.windowTk.config(menu=menu)
        submenu = Menu(menu)
        menu.add_cascade(label="Materi", menu=submenu)
        submenu.add_command(label="Gerak Lurus Beraturan", command=glbklik)
        submenu.add_command(label="Gerak Lurus Berubah Beraturan", command=glbbklik)
        submenu.add_command(label="Gaya dan Hukum Newton II", command=gayaklik)


def labelMateri(frame, column, *args):
    for i in range(len(args)):
        Label(frame, text=args[i], bg='white').grid(row=i, column=column)


def startSplashScreen():
    splash = Tk()
    splash.wm_overrideredirect(True)
    splash.geometry(f"{splash.winfo_screenwidth()}x{splash.winfo_screenheight()}")

    pict = PhotoImage(file="fis.png")
    background_label = Label(splash, image=pict)
    background_label.pack()

    splash.after(5000, splash.destroy)
    splash.mainloop()


startSplashScreen()

mywindow = Tk()
mywindow.wm_title("Belajar Fisika SMP")
mywindow.geometry('640x480')
mywindow.configure(background='white')

winTk = BelajarFisikaSMP(mywindow)
winTk.loginForm()

mywindow.mainloop()
