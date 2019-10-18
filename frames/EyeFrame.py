from tkinter import *
import pickle
import os

import PIL.Image
import PIL.ImageTk

from classes import CameraView, PupilScan2, BluePy


class EyeFrame:

    def __init__(self, mf):
        self.main_frame = mf

        self.frame = Frame(self.main_frame, width=1050, height=560, bg="#f1f1f1")

        parent = os.path.abspath(os.path.join('frames', os.pardir))
        self.data_settings = pickle.loads(open(parent + "/data/settings.pickle", "rb").read())

        self.Cview = CameraView.CameraView()
        self.Cview.start()  # it does nothing

        self.pupil = PupilScan2.PupilScan()

        # Labels of information
        self.command_label = None
        self.pos_label = None
        self.ratio_label = None
        self.blink_label = None

        # Variables of information
        self.command = None
        self.pos = None
        self.ratio = None
        self.blink = None

        self.thresh_bar_value = IntVar()

        self.create_frame_data()

        self.canvas = None
        self.canvas_camera()

        # Delay of the camera loop
        self.delay = 15

        self.bluepy = None

    def start_loop(self):
        if self.data_settings['blue_mode'] == 1:
            self.start_blue()
            # self.start_blue()
        self.camera_loop()

    def canvas_camera(self):
        self.canvas = Canvas(self.frame, width=640, height=480, bg="#FAFAFA", bd=0, highlightthickness=0,
                             relief='ridge')
        self.canvas.place(x=40, y=40)  # 640 y 480

    def start_blue(self):
        self.bluepy = BluePy.BluePy()
        self.bluepy.start()

    def camera_loop(self):
        ret, frame = self.Cview.get_frame()
        if ret:

            # Use the Thresh Slider instead of the static value
            if self.data_settings['thresh_slider'] == 1:
                self.pupil.change_thresh_type(self.thresh_bar_value.get())

            if self.data_settings['blue_mode'] == 1:
                new_frame, self.ratio, self.blink, self.command, self.pos = self.pupil.scanning(frame)
                self.put_label_data()
                self.blue_option()
            else:
                new_frame, self.ratio, self.blink, self.command, self.pos = self.pupil.scanning(frame)
                self.put_label_data()

            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(new_frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        self.frame.after(self.delay, self.camera_loop)

    def blue_option(self):
        # According to the command it sends a different byte to the arduino
        if self.bluepy.is_connected():
            if self.command != "NoFace":
                if self.blink == "True":
                    self.bluepy.send_blink_command()
                    print("blink")
                elif self.command == "ERROR" and self.blink == "False":
                    self.bluepy.send_turn_off_command()
                    print("nothing")
                elif self.command == "Left":
                    self.bluepy.send_left_command()
                    print("left")
                elif self.command == "Slight Right":
                    self.bluepy.send_right_command()
                    print("Right")
                elif self.command == "Strong Right":
                    self.bluepy.send_right_command()
                    print("Right")
                elif self.command == "Neutro":
                    self.bluepy.send_neutro_command()
                    print("neutro")
            else:
                self.bluepy.send_turn_off_command()

    def create_frame_data(self):
        frame_data = Frame(self.frame, width=310, height=480, bg="#FAFAFA")

        frame_title = Frame(frame_data, width=310, height=50, bg="#102027")
        frame_title.place(x=0, y=0)

        Label(frame_data, text="Info", bg="#102027", fg="#ffffff", font=("Roboto", 16)).place(x=20, y=10)

        Label(frame_data, text="Command :", bg="#FAFAFA", fg="#000000", font=("Roboto Lt", 15)).place(x=20, y=80)
        Label(frame_data, text="Position :", bg="#FAFAFA", fg="#000000", font=("Roboto Lt", 15)).place(x=20, y=160)
        Label(frame_data, text="Ratio :", bg="#FAFAFA", fg="#000000", font=("Roboto Lt", 15)).place(x=20, y=240)
        Label(frame_data, text="Blink :", bg="#FAFAFA", fg="#000000", font=("Roboto Lt", 15)).place(x=20, y=320)

        self.command_label = Label(frame_data, text="", bg="#FAFAFA", fg="#000000", font=("Roboto Lt", 13))
        self.pos_label = Label(frame_data, text="", bg="#FAFAFA", fg="#000000", font=("Roboto Lt", 13))
        self.ratio_label = Label(frame_data, text="", bg="#FAFAFA", fg="#000000", font=("Roboto Lt", 13))
        self.blink_label = Label(frame_data, text="", bg="#FAFAFA", fg="#000000", font=("Roboto Lt", 13))

        self.command_label.place(x=20, y=115)
        self.pos_label.place(x=20, y=195)
        self.ratio_label.place(x=20, y=275)
        self.blink_label.place(x=20, y=355)

        Label(frame_data, text="Thresh Slider", bg="#FAFAFA", fg="#000000", font=("Roboto Lt", 10)).place(x=110, y=407)
        sclbar = Scale(frame_data, orient=HORIZONTAL, from_=0, to=120, length=280,
                       activebackground="#939393",  bg="#F8F8F8",
                       troughcolor="#DADADA", variable=self.thresh_bar_value, font=("Roboto Lt", 10))
        sclbar.place(x=15, y=430)

        frame_data.place(x=700, y=40)

    def put_label_data(self):
        if self.command != "NoFace":
            self.command_label.config(text=self.command)
            self.pos_label.config(text=self.pos)
            self.ratio_label.config(text=self.ratio)
            self.blink_label.config(text=self.blink)
        else:
            self.command_label.config(text="")
            self.pos_label.config(text="")
            self.ratio_label.config(text="")
            self.blink_label.config(text="")

    def place_frame(self):
        self.frame.place(x=0, y=80)

    def forget_place(self):
        self.frame.place_forget()

