import pickle

# blue_mode: 0 = not use bluetooth mode, 1 = use bluetooth mode

# Thresh Value is used to identify which intensity of the gray scale is going to be used in the mask for the eye
# A lower value means is going to absorb darkest colors. 0-255

# Thresh_Slider 1 = allows to use the slider to adjust the thresh in live
# 0 = it does not allow

# eye value, which Eye is going to be scanned 0 = left, 1 = Right

# bk_time_eye, how much time the eye has to be closed to detect it as a 'blink', the number depends on the speed of
# your CPU

# eye_ratio_value, (This setting depends on the distance between the face and the camera) if you are far from the camera
# ,eye_ratio_value has to be a lower value due to the size of the face


action = int(input("input action: "))

settings = {'blue_mode': 0,
            'thresh_slider': 0,
            'blue_com': "COM11",
            'blue_bauds': 9600,
            'thresh_value': 15,
            'eye_value': 0,
            'bk_time_eye': 8,
            'eye_ratio_value': 3.9}

if action == 1:
    f = open("settings.pickle", "wb")
    f.write(pickle.dumps(settings))
    f.close()
else:
    load_settings = pickle.loads(open("settings.pickle", "rb").read())
    print(load_settings)
