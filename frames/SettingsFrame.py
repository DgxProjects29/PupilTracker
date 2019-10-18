from tkinter import *
import pickle
import os
from classes import PupilScan2

class SettingsFrame:
    def __init__(self, mf):
        self.main_frame = mf

        self.frame = Frame(self.main_frame, width=1050, height=560, bg="#f1f1f1")

        parent = os.path.abspath(os.path.join('frames', os.pardir))
        self.settings_data = pickle.loads(open(parent + "/data/settings.pickle", "rb").read())

        self.blue_mode = IntVar()
        self.thresh_slider_mode = IntVar()
        self.create_mode_settings()

        self.blue_com = StringVar()
        self.blue_bauds = StringVar()
        self.create_bt_settings()

        self.thresh = IntVar()
        self.eye_type = IntVar()
        self.blink_time_eye = IntVar()
        self.eye_ratio_value = DoubleVar()
        self.create_general_settings()

    def create_mode_settings(self):

        frame_mode = Frame(self.frame, width=310, height=480, bg="#FAFAFA")

        frame_title = Frame(frame_mode, width=310, height=50, bg="#102027")
        Label(frame_title, text="Mode", bg="#102027", fg="#ffffff", font=("Roboto", 16)).place(x=20, y=10)
        frame_title.place(x=0, y=0)

        bt = Radiobutton(frame_mode, text="Use Bluetooth", bg="#FAFAFA",
                         borderwidth=4, font=("Roboto", 15), value=1, variable=self.blue_mode)

        no_bt = Radiobutton(frame_mode, text="Not use Bluetooth", bg="#FAFAFA",
                            borderwidth=4, font=("Roboto", 15), value=0, variable=self.blue_mode)

        if self.settings_data['blue_mode'] == 0:
            no_bt.select()
        else:
            bt.select()

        bt.place(x=20, y=80)
        no_bt.place(x=20, y=130)

        thresh_slider = Radiobutton(frame_mode, text="Use Thresh Slider", bg="#FAFAFA",
                         borderwidth=4, font=("Roboto", 15), value=1, variable=self.thresh_slider_mode)

        no_thresh_slider = Radiobutton(frame_mode, text="Not use Thresh Slider", bg="#FAFAFA",
                            borderwidth=4, font=("Roboto", 15), value=0, variable=self.thresh_slider_mode)

        if self.settings_data['thresh_slider'] == 0:
            no_thresh_slider.select()
        else:
            thresh_slider.select()

        thresh_slider.place(x=20, y=200)
        no_thresh_slider.place(x=20, y=250)

        frame_mode.place(x=40, y=30)

    def create_bt_settings(self):

        frame_bt = Frame(self.frame, width=310, height=480, bg="#FAFAFA")

        frame_title = Frame(frame_bt, width=310, height=50, bg="#102027")
        Label(frame_title, text="Bluetooth", bg="#102027", fg="#ffffff", font=("Roboto", 16)).place(x=20, y=10)
        frame_title.place(x=0, y=0)

        Label(frame_bt, text="Puerto: ", bg="#FAFAFA", fg="#000000", font=("Roboto", 15)).place(x=20, y=80)
        com_entry = Entry(frame_bt, bg="#FAFAFA", width=8, font=("Roboto", 14), textvariable=self.blue_com)

        Label(frame_bt, text="Bauds: ", bg="#FAFAFA", fg="#000000", font=("Roboto", 15)).place(x=20, y=140)
        baud_entry = Entry(frame_bt, bg="#FAFAFA", width=8, font=("Roboto", 14), textvariable=self.blue_bauds)

        com_entry.insert(0, self.settings_data['blue_com'])
        baud_entry.insert(0, self.settings_data['blue_bauds'])

        com_entry.place(x=110, y=80)
        baud_entry.place(x=110, y=140)

        frame_bt.place(x=370, y=30)

    def create_general_settings(self):

        frame_general = Frame(self.frame, width=310, height=480, bg="#FAFAFA")

        frame_title = Frame(frame_general, width=310, height=50, bg="#102027")
        Label(frame_title, text="General", bg="#102027", fg="#ffffff", font=("Roboto", 16)).place(x=20, y=10)
        frame_title.place(x=0, y=0)

        eye_left = Radiobutton(frame_general, text="Left Eye", bg="#FAFAFA",
                         borderwidth=4, font=("Roboto", 15), value=0, variable=self.eye_type)

        right_left = Radiobutton(frame_general, text="Right Eye", bg="#FAFAFA",
                            borderwidth=4, font=("Roboto", 15), value=1, variable=self.eye_type)

        if self.settings_data['eye_value'] == 0:
            eye_left.select()
        else:
            right_left.select()

        eye_left.place(x=20, y=120)
        right_left.place(x=20, y=170)

        Label(frame_general, text="Thresh: ", bg="#FAFAFA", fg="#000000", font=("Roboto", 15)).place(x=20, y=80)
        thresh_entry = Entry(frame_general, bg="#FAFAFA", width=8, font=("Roboto", 14), textvariable=self.thresh)
        Label(frame_general, text="Eye Time: ", bg="#FAFAFA", fg="#000000", font=("Roboto", 15)).place(x=20, y=225)
        eye_time_entry = Entry(frame_general, bg="#FAFAFA", width=8, font=("Roboto", 14),
                               textvariable=self.blink_time_eye)
        Label(frame_general, text="Ratio Value: ", bg="#FAFAFA", fg="#000000", font=("Roboto", 15)).place(x=20, y=275)
        eye_ratio_entry = Entry(frame_general, bg="#FAFAFA", width=8, font=("Roboto", 14),
                               textvariable=self.eye_ratio_value)

        thresh_entry.delete(0, END)
        thresh_entry.insert(0, self.settings_data['thresh_value'])

        eye_time_entry.delete(0, END)
        eye_time_entry.insert(0, self.settings_data['bk_time_eye'])

        eye_ratio_entry.delete(0, END)
        eye_ratio_entry.insert(0, self.settings_data['eye_ratio_value'])

        thresh_entry.place(x=110, y=80)
        eye_time_entry.place(x=140, y=225)
        eye_ratio_entry.place(x=140, y=275)

        frame_general.place(x=700, y=30)

    def place_frame(self):
        self.frame.place(x=0, y=80)

    def forget_place(self):
        self.frame.place_forget()

    def save_settings(self):
        try:
            new_settings = {'blue_mode': self.blue_mode.get(),
                            'thresh_slider': self.thresh_slider_mode.get(),
                            'blue_com': self.blue_com.get(),
                            'blue_bauds': self.blue_bauds.get(),
                            'thresh_value': self.thresh.get(),
                            'eye_value': self.eye_type.get(),
                            'bk_time_eye': self.blink_time_eye.get(),
                            'eye_ratio_value': self.eye_ratio_value.get()}

            print(new_settings)
            f = open("data/settings.pickle", "wb")
            f.write(pickle.dumps(new_settings))
            f.close()

            PupilScan2.PupilScan().refresh_data()
        except:
            print("ERROR")
