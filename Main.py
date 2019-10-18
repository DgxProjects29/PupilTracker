from tkinter import *
from frames import EyeFrame, SettingsFrame


class Main:

    def __init__(self, vt):
        self.main_frame = vt

        self.settings()

        self.up_toolbar = Frame(self.main_frame, width=1050, height=15, bg="#000a12")  # 80 star
        self.toolbar = Frame(self.main_frame, width=1050, height=65, bg="#263238")
        self.put_toolbar()

        self.sett_frame = SettingsFrame.SettingsFrame(self.main_frame)
        self.eye_frame = EyeFrame.EyeFrame(self.main_frame)

        self.frame_id_place = 0

        self.settings_but = None
        self.eye_image_but = None
        self.create_toolbar_buttons()
        self.button_id = None
        self.create_id_button()

        self.put_eye_frame()

    def settings(self):
        self.main_frame.config(bg="#f1f1f1")
        self.main_frame.title("")
        self.main_frame.resizable(0, 0)

        winx = self.main_frame.winfo_screenwidth()
        winy = self.main_frame.winfo_screenheight()
        # screen center
        cx = int((winx - 1050) / 2)
        cy = int((winy - 640) / 2) - 28
        self.main_frame.geometry(f"1050x640+{cx}+{cy}")

    def put_toolbar(self):
        Label(self.toolbar, text="Pupil Tracker", bg="#263238", fg="#ffffff", font=("Roboto", 21)).place(x=20, y=10)
        self.up_toolbar.pack()
        self.toolbar.pack()

    def put_eye_frame(self):
        self.frame_id_place = 0

        self.sett_frame.forget_place()
        self.eye_frame.forget_place()

        self.eye_frame.place_frame()

        play_image = PhotoImage(file="images/play.png")
        self.button_id.config(image=play_image)
        self.button_id.image = play_image

    def put_settings_frame(self):
        self.frame_id_place = 1

        self.sett_frame.forget_place()
        self.eye_frame.forget_place()

        self.sett_frame.place_frame()

        save_image = PhotoImage(file="images/save.png")
        self.button_id.config(image=save_image)
        self.button_id.image = save_image

    def create_toolbar_buttons(self):

        settings_but_image = PhotoImage(file="images/settings.png")
        self.settings_but = Button(self.toolbar, bg="#263238", image=settings_but_image, relief="flat",
                                   activebackground="#263238", overrelief="ridge", command=self.put_settings_frame)

        self.settings_but.place(x=980, y=6)
        self.settings_but.image = settings_but_image

        eye_image_but_image = PhotoImage(file="images/eyeimg.png")
        self.eye_image_but = Button(self.toolbar, bg="#263238", image=eye_image_but_image, relief="flat",
                                  activebackground="#263238", overrelief="ridge", command=self.put_eye_frame)

        self.eye_image_but.place(x=910, y=6)
        self.eye_image_but.image = eye_image_but_image

    def create_id_button(self):
        image_but_id = PhotoImage(file="images/play.png")
        self.button_id = Button(self.toolbar, bg="#263238", image=image_but_id, relief="flat",
                                activebackground="#263238", overrelief="ridge", command=self.command_for_id_button)

        self.button_id.place(x=800, y=6)
        self.button_id.image = image_but_id

    def command_for_id_button(self):
        if self.frame_id_place == 0:
            self.eye_frame.start_loop()
        elif self.frame_id_place == 1:
            self.sett_frame.save_settings()


Vt = Tk()
v = Main(Vt)
Vt.mainloop()
